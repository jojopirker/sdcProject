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
        <Navbar bg="dark" expand="lg">
          <Container>
            <Navbar.Brand href="/">SDC - UK Accidents</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link href="dash-1">Dashboard 1</Nav.Link>
                <Nav.Link href="dash-2">Dashboard 2</Nav.Link>
                <NavDropdown title="Dashboards" id="basic-nav-dropdown">
                  <NavDropdown.Item href="dash-1">Dashboard</NavDropdown.Item>
                  <NavDropdown.Item href="dash-2">Dashboard 2</NavDropdown.Item>
                </NavDropdown>
                <Nav.Link href="apiOverview">ML API</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
    )
}

export default Navigation;