#!/bin/bash

################################################################################
# Variables                                                                         #
################################################################################
keep_db=false
tests_only=false
container_name=postgres
################################################################################
# Help                                                                         #
################################################################################
Help() {
  # Display Help
  echo "Test script for run integration tests with postgres."
  echo
  echo "Syntax: ./run_test.sh [--help|tests-only|keep-db]"
  echo "options:"
  echo "--help, -h           Print this Help."
  echo "--tests-only, -t     Start only tests need to be runned db"
  echo "--keep-db, -k        Not killed postgres container"
  echo
}

################################################################################
################################################################################
# Process the input options. Add options as needed.                            #
################################################################################
# Get the options
while [[ "$#" -gt 0 ]]; do
  case $1 in
  -h | --help)
    Help
    exit 0
    shift
    ;;
  -t | --tests-only) tests_only=true ;;
  -k | --keep-db) keep_db=true ;;
  *)
    echo "Unknown parameter passed: $1"
    exit 1
    ;;
  esac
  shift
done
# Main program                                                                 #
################################################################################
################################################################################

cat <<EOF
Start testing!

Provided variabels:
--> Created container: $container_name
--> Keep container: $keep_db
--> Test only: $tests_only

EOF

check() {
  if [[ $? -ne 0 ]]; then
    echo "$1 ended with error"
    exit $?
  fi
}

if [[ $tests_only = false ]]; then
  docker run -p 5432:5432 --name $container_name -e POSTGRES_PASSWORD=postgres -d postgres:16-alpine
  check "start docker container"
  until nc -z $(docker inspect --format='{{.NetworkSettings.IPAddress}}' $container_name) 5432; do
    echo "waiting for postgres container..."
    sleep 0.5
  done
fi

poetry run pytest -k old_aproach

if [[ $tests_only = false && $keep_db = false ]]; then
  docker kill $container_name
  check "kill docker container"
  docker rm $container_name
  check "remove docker container"
fi
