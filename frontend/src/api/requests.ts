import axios from "axios";

export type LargeDataType = {
  big_data: string;
  hash: string;
  id: string;
};

export default class LargeData {
  private readonly url: string;
  constructor(url: string, redisHost: string, redisPort: number) {
    this.url = url;
  }

  async getAll(): Promise<Array<LargeDataType>> {
    const response = await axios.get(`${this.url}/large_data/`);

    return response.data;
  }

  async getOneLargeData(id: number): Promise<LargeDataType> {
    return await axios.get(`${this.url}/large_data/${id}`);
  }

  async postLargeData(largeData: string): Promise<string> {
    const large_data = { big_data: largeData };
    // clear cache if we are post
    return await axios.post(`${this.url}/large_data/`, large_data);
  }

  async updateLargeData(largeData: string, id: string): Promise<string> {
    const data = { big_data: largeData };
    // clear cache if we are post
    return await axios.put(`${this.url}/large_data/${id}`, data);
  }
}
