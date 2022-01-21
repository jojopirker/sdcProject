import React from 'react'
import { Nav, NavDropdown } from 'react-bootstrap'
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'

/**
 * 
 * @returns Navigation Component
 */
const Navigation = ()=> {

    return(
        <Navbar bg="dark" variant="dark" expand="lg">
          <Container>
            <Navbar.Brand href="/">SDC - UK Accidents</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <NavDropdown title="Dashboards" id="basic-nav-dropdown">
                  <NavDropdown.Item href="dash-2">Accidents Dashoard</NavDropdown.Item>
                  <NavDropdown.Item href="dash-1">Vehicles Dashboard</NavDropdown.Item>
                </NavDropdown>
                <Nav.Link href="apiOverview">ML API</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
    )
}

export default Navigation;