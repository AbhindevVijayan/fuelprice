import { useState } from "react";
import { getFuelPlan } from "../api/fuelApi";

function RouteForm({ setResult }) {
    const [start, setStart] = useState("");
    const [end, setEnd] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const data = await getFuelPlan(start, end);

            console.log("API RAW RESPONSE:", data);

            // 🔥 handle both possible response formats
            const cleanData = data?.data ? data.data : data;

            console.log("CLEAN DATA SENT TO STATE:", cleanData);

            setResult(cleanData);

        } catch (error) {
            console.error("API ERROR:", error);
            alert("Failed to get fuel plan");
            setResult(null);
        }

        setLoading(false);
    };

    return (
        <div>
            <h2>Fuel Planner</h2>

            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Start location"
                    value={start}
                    onChange={(e) => setStart(e.target.value)}
                />

                <input
                    type="text"
                    placeholder="Destination"
                    value={end}
                    onChange={(e) => setEnd(e.target.value)}
                />

                <button type="submit">
                    {loading ? "Calculating..." : "Plan Route"}
                </button>
            </form>
        </div>
    );
}

export default RouteForm;