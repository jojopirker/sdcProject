import React from 'react'
import { Table, Container } from 'react-bootstrap'
/**
 * 
 * @returns GeneralInformation Component
 */
const GeneralInformation = () => {

    return(
        <Container>
          <h1>General Project Information</h1>
          The project insights can be found in the github repository under the following Link: 
          <a href="https://github.com/ds20m007/sdcProject">https://github.com/ds20m007/sdcProject</a>
          
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
          <h2>Deployment</h2>
          Below is a schematic of our pipline for deployment:<br />
          <img src='actions.png' alt='Deployment Diagram' style={{maxWidth:"100%"}} /><br />
          And here a little overview of the infrastructure used in deployment:<br />
          <img src='infrastructure.jpeg' alt='Deployment Diagram' style={{maxWidth:"100%"}} />

          <h2>Structure</h2>
          <p>
            Through the Navigation the Dashboards and the severity accident prediction API can be reached.
            The Dashboards are divided into an Accidents Dashboard and an Vehicle Dashboard. So there are two different viewing points on the dataset. 
          </p>

        </Container>
    )
}

export default GeneralInformation;