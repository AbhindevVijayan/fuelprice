import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
});

export const getFuelPlan = async (start, end) => {
    const response = await API.post("/route-fuel-plan/", {
        start: start,
        end: end,
    });

    return response.data;
};