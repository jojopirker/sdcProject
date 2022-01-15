import React from 'react'
import { Table } from 'react-bootstrap'
import Container from 'react-bootstrap/Container'

/**
 * 
 * @returns GeneralInformation Component
 */
const GeneralInformation = () => {

    return(
        <Container>
          <h1>General Project Information</h1>
          <h2>Data</h2>
          <p>
            The Dataset is from Kaggle (Link: <a href='https://www.kaggle.com/benoit72/uk-accidents-10-years-history-with-many-variables'>UK-Accidents</a>). 
            These files provide detailed road safety data about the circumstances of personal injury road accidents in GB from 2005 to 2014. 
          </p>
          <Table striped bordered hover size="sm">
            <thead>
              <tr>
                <th>Dataset</th>
                <th>Information</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Accidents</td>
                <td>This is the main dataset, which contains information for example about the severity, weather, location, timestamp and road type</td>
              </tr>
              <tr>
                <td>Vehicles</td>
                <td>The dataset contains information mainly about the vehicle type/model, engine size, driver sex, driver age and car age</td>
              </tr>
              <tr>
                <td>Casualties</td>
                <td>The information is mostly about casualty severity, age, sex social class, casualty type, pedestrian or car passenger</td>
              </tr>
            </tbody>
          </Table>
          <h2>Structure</h2>
          <p>
            Through the Navigation the Dashboard and the severity accident prediction API can be reached.
          </p>
          <h2>Deployment</h2>
          <img src='infrastructure.jpeg' alt='Deployment Diagram'/>
          <br></br>
        </Container>
    )
}

export default GeneralInformation;