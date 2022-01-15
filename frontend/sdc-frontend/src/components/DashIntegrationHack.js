import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Spinner from 'react-bootstrap/Spinner';

/**
 * DashIntegration is a hack to present an iframe for the Dash
 * @returns The iframe with the dash app
 */
export const DashIntegration = ({ route }) => {
    const [loading, setLoading] = useState(true);

    return (<>
        <Container>
        {loading &&
            <>
                <h1 className='text-center'>Loading may take time...</h1>
                <h2 className='text-center'><Spinner animation="border" /></h2>
            </>}
            <iframe src={`${process.env.REACT_APP_DASH_APP}/${route}`}
                style={{ width: "100%", height: "85vh" }}
                title="This is the frame for the dashoard" 
                onLoad={() => { setLoading(false) }} /> {/**todo change url**/}
        </Container>
    </>)
}

export default DashIntegration;