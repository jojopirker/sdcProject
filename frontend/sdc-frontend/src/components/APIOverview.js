import Container from 'react-bootstrap/Container';
import React from 'react';
/**
 * 
 * @returns APIOverview
 */
const APIOverview = () => {
    return(
    <>
        <Container>
            <h1>API Overview</h1>
            <iframe src={`${process.env.REACT_APP_API}/docs`}
                style={{ width: "100%", height: "75vh" }}
                title="This is the frame for the dashoard" 
                />
        </Container>
    </>)
}

export default APIOverview;