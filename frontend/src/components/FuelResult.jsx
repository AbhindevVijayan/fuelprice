function FuelResult({ result }) {
    console.log("FUEL RESULT DATA:", result);

    if (!result) {
        return null;
    }

    const stops = result.fuel_stops || [];

    return (
        <div className="result">
            <h2>Route Details</h2>

            <p>
                <strong>From:</strong> {result.start}
            </p>

            <p>
                <strong>To:</strong> {result.end}
            </p>

            <p>
                <strong>Distance:</strong>{" "}
                {result.distance_miles
                    ? Number(result.distance_miles).toFixed(2)
                    : "0"} miles
            </p>

            <h3>Fuel Stops</h3>

            {stops.length > 0 ? (
                stops.map((stop, index) => (
                    <div key={index} className="fuel-stop">
                        <p>
                            <strong>Location:</strong> {stop.location}
                        </p>

                        <p>
                            <strong>Station:</strong> {stop.station}
                        </p>

                        <p>
                            <strong>Price:</strong> ${stop.price_per_gallon}
                        </p>

                        <p>
                            <strong>Gallons:</strong> {stop.gallons}
                        </p>

                        <p>
                            <strong>Cost:</strong> ${stop.cost}
                        </p>

                        <hr />
                    </div>
                ))
            ) : (
                <p>No fuel stops available</p>
            )}

            <h3>
                Total Fuel Cost: ${result.total_fuel_cost || 0}
            </h3>
        </div>
    );
}

export default FuelResult;