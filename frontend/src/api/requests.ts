import axios from "axios";
import { Redis } from "ioredis";

export type LargeDataType = {
  big_data: string;
  hash: string;
  id: string;
};

export default class LargeData {
  private readonly url: string;
  private readonly redisClient: Redis;
  constructor(url: string, redisHost: string, redisPort: number) {
    this.url = url;
    this.redisClient = new Redis({ host: redisHost, port: redisPort });
  }

  async getAll(): Promise<Array<LargeDataType>> {
    const cachedData = await this.redisClient.get("large_data");

    if (cachedData) {
      return JSON.parse(cachedData);
    } else {
      const response = await axios.get(`${this.url}/large_data/`);
      await this.redisClient.set(
        "large_data",
        JSON.stringify(response.data),
        "EX",
        3600,
      );

      return response.data;
    }
  }

  async getOneLargeData(id: number): Promise<LargeDataType> {
    return await axios.get(`${this.url}/large_data/${id}`);
  }

  async postLargeData(largeData: string): Promise<string> {
    const large_data = { big_data: largeData };
    // clear cache if we are post
    await this.redisClient.flushall();
    return await axios.post(`${this.url}/large_data/`, large_data);
  }

  async updateLargeData(largeData: string, id: string): Promise<string> {
    const data = { big_data: largeData };
    // clear cache if we are post
    await this.redisClient.flushall();
    return await axios.put(`${this.url}/large_data/${id}`, data);
  }
}
