import React, { useState, useMemo, useRef } from 'react';
import { MapContainer as Map, TileLayer, Marker } from 'react-leaflet';
import { Container, Row, Col, Button,Spinner } from 'react-bootstrap';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

export const MLPrediction = () => {
    // Map variables
    const [currentPos, setCurrentPos] = useState([55.4, -3.5]);
    const markerRef = useRef([55.4, -3.5])
    const center = [55.4, -3.5]
    const zoom = 5
    const eventHandlers = useMemo(
        () => ({
            dragend() {
                const marker = markerRef.current
                if (marker != null) {
                    const tmpPos = marker.getLatLng();
                    setCurrentPos([tmpPos.lat,tmpPos.lng])
                }
            },
        }),
        [],
    )

    const myIcon = L.icon({
        iconUrl: '/car.png',
        iconSize: [64, 64],
        iconAnchor: [32, 64],
        popupAnchor: null,
        shadowUrl: null,
        shadowSize: null,
        shadowAnchor: null
    });

    // prediction vars
    const [first_road_class, setFirst_road_class] = useState("A");
    const [weather_conditions, setWeather_conditions] = useState("Fine no high winds");
    const [surface_condition, setSurface_condition] = useState("Dry");
    const [urbanOrRural, setUrbanOrRural] = useState("Urban");
    const [vehicle_Type, setVehicle_Type] = useState("Ridden horse");
    const [date, setDate] = useState(null);
    const [loading, setLoading] = useState(false);
    const [answer, setAnswer] = useState("");

    const canSubmit = () => date && first_road_class && weather_conditions && surface_condition && urbanOrRural && vehicle_Type;

    const handleSubmit = async () => {
        var data = {
            "first_road_class": first_road_class,
            "weather_conditions": weather_conditions,
            "road_surface_conditions": surface_condition,
            "urban_or_rural_area": urbanOrRural,
            "vehicle_type": vehicle_Type,
            "longitude": currentPos[1],
            "latitude": currentPos[0],
            "picked_date": date.toString()}
        console.log(data);
        setLoading(true);
        await fetch(`${process.env.REACT_APP_API}/predict`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) 
          }).then((response)=>response.json()).then((data)=>{
            setLoading(false);
            console.log(data);
            setAnswer(data.accident_severty);
          });
    }

    return (
        <>
            <Container>
                <h1>Test the ML model</h1>
                <Row>
                    <Col xs={12} md={6}>
                        <Map center={center} zoom={zoom} style={{ height: '75vh'}}>
                            <TileLayer
                                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <Marker
                                draggable={true}
                                icon={myIcon}
                                eventHandlers={eventHandlers}
                                position={currentPos}
                                ref={markerRef}>
                            </Marker>
                        </Map>
                    </Col>
                    <Col xs={12} md={6}>
                        <Row>
                            <label htmlFor="1st_Road_Class">Choose a value for "1st_Road_Class":</label>
                            <select name="1st_Road_Class" id="1st_Road_Class" 
                            onChange={e => setFirst_road_class(e.target.value)} 
                            value={first_road_class}>
                                <option value="A">A</option>
                                <option value="B">B</option>
                                <option value="C">C</option>
                                <option value="Motorway">Motorway</option>
                                <option value="A(M)">A(M)</option>
                            </select>
                        </Row>
                        <Row>
                            <label htmlFor="weather_condition">Choose a weather condition:</label>
                            <select name="weather_condition" id="weather_condition" 
                            onChange={e => setWeather_conditions(e.target.value)}
                            value={weather_conditions}>
                                <option value="Fine no high winds">Fine no high winds</option>
                                <option value="Raining no high winds">Raining no high winds</option>
                                <option value="Snowing no high winds">Snowing no high winds</option>
                                <option value="Raining + high winds">Raining + high winds</option>
                                <option value="Fog or mist">Fog or mist</option>
                                <option value="Fine + high winds">Fine + high winds</option>
                                <option value="Fog or mist">Snowing + high winds</option>
                                <option value="Data missing or out of range">Data missing or out of range</option>
                                <option value="Other">Other</option>
                                <option value="Unknown">Unknown</option>
                            </select>
                        </Row>
                        <Row>
                            <label htmlFor="surface_condition">Choose road surface conditions:</label>
                            <select name="surface_condition" id="surface_condition" 
                            onChange={e => setSurface_condition(e.target.value)}
                            value={surface_condition}>
                                <option value="Dry">Dry</option>
                                <option value="Wet or damp">Wet or damp</option>
                                <option value="Frost or ice">Frost or ice</option>
                                <option value="Snow">Snow</option>
                                <option value="Flood over 3cm. deep'">Flood over 3cm. deep'</option>
                                <option value="Data missing or out of range">Data missing or out of range</option>
                            </select>
                        </Row>
                        <Row>
                            <label htmlFor="urban_or_rural">Choose urban or rural area:</label>
                            <select name="urban_or_rural" id="urban_or_rural" 
                            onChange={e => setUrbanOrRural(e.target.value)}
                            value={urbanOrRural}>
                                <option value="Urban">Urban</option>
                                <option value="Rural">Rural</option>
                                <option value="Unallocated">Unallocated</option>
                            </select>
                        </Row>
                        <Row>
                            <label htmlFor="Vehicle_Type">Choose a Vehicle Type:</label>
                            <select name="Vehicle_Type" id="Vehicle_Type" 
                            onChange={e => setVehicle_Type(e.target.value)}
                            value={vehicle_Type}>
                                <option value="Car">Car</option>
                                <option value="Ridden horse">Ridden horse</option>
                                <option value="Pedal cycle">Pedal cycle</option>
                                <option value="Agricultural vehicle">Agricultural vehicle</option>
                                <option value="Tram">Tram</option>
                                <option value="Mobility scooter">Mobility scooter</option>


                                <option value="Bus or coach (17 or more pass seats)">Bus or coach (17 or more pass seats)</option>
                                <option value="Motorcycle 125cc and under">Motorcycle 125cc and under</option>
                                <option value="Motorcycle over 125cc">Motorcycle over 125cc</option>
  
                                <option value="Van / Goods 3.5 tonnes mgw or under">Van / Goods 3.5 tonnes mgw or under</option>
                                <option value="Minibus (8 - 16 passenger seats)">Minibus (8 - 16 passenger seats)</option>
                                <option value="Goods over 3.5t. and under 7.5t">Goods over 3.5t. and under 7.5t</option>
                                <option value="Goods 7.5 tonnes mgw and over">Goods 7.5 tonnes mgw and over</option>
                                <option value="Data missing or out of range">Data missing or out of range</option>
                                <option value="Goods vehicle - unknown weight">Goods vehicle - unknown weight</option>
                                <option value="Motorcycle - unknown cc">Motorcycle - unknown cc</option>
                                <option value="Other vehicle">Other vehicle</option>
                                <option value="Electric motorcycle">Electric motorcycle</option>
                            </select>
                        </Row>
                        <Row>
                            <label htmlFor="dateTime">Choose a time and day:</label>
                            <input name="dateTime" id="dateTime" type="datetime-local" 
                            onChange={e => setDate(e.target.value)}>
                            </input>
                        </Row>
                        <Row style={{ marginTop: "5px" }}>
                            <Button onClick={handleSubmit} disabled={!canSubmit()}>Ask omniscient model</Button>
                        </Row>
                        <Row style={{ marginTop: "5px" }}>
                        {loading && <h2 className='text-center'><Spinner animation="border" /></h2>}
                        {!loading && answer && <h3>Predicted Severity is: <b>{answer}</b></h3>}
                        </Row>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default MLPrediction;