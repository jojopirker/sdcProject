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
        <h2>Dashboard</h2>
        {loading &&
            <>Loading may take time...
                <Spinner animation="border" />
            </>}
        <Container>
            <iframe src={`:8050/${route}`}
                style={{ width: "100%", height: "75vh" }}
                onLoad={() => { setLoading(false) }} /> {/**todo change url**/}
        </Container>

    </>)
}

export default DashIntegration;