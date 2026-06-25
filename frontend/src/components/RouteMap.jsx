import { MapContainer, TileLayer, Polyline, Marker } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import polyline from "@mapbox/polyline";

export default function RouteMap({ encodedRoute }) {
    if (!encodedRoute) return null;

    const coords = polyline.decode(encodedRoute);

    const latlngs = coords.map(([lat, lng]) => [lat, lng]);

    return (
        <MapContainer center={latlngs[0]} zoom={5} style={{ height: "400px", width: "100%" }}>

            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {/* Route line */}
            <Polyline positions={latlngs} color="blue" />

            {/* Start marker */}
            <Marker position={latlngs[0]} />

            {/* End marker */}
            <Marker position={latlngs[latlngs.length - 1]} />

        </MapContainer>
    );
}