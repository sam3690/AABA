import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // backend FastAPI
});

export const getJobs = async () => {
  const res = await API.get("/jobs");
  return res.data;
};

export const getMonitoringData = async () => {
  const res = await API.get("/monitoring/health");
  return res.data;
};
