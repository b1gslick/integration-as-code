from testcontainers.core.container import Optional, wait_container_is_ready
from testcontainers.core.generic import DockerContainer
from testcontainers.core.utils import logging


class HashService(DockerContainer):
    def __init__(
        self,
        image: str = "",
        host: str = "localhost",
        port: int = 8080,
        **kwargs,
    ) -> None:
        super().__init__(image=image, **kwargs)
        self.host = host
        self.port = port

        self.with_exposed_ports(self.port)

    def _configure(self) -> None:
        self.with_env("host", self.host)
        self.with_env("port", str(self.port))
