import React from 'react';
import styled from 'styled-components';
import BackgroundImage from '../components/BackgroundImage';
import Header from '../components/Header';

export default function Signup() {
  return (
    <Container>
        <BackgroundImage/>
        <Header/>
        <div className="content">
            <div className="body flex column a-center j-center">
                <div className="text column flex"> 
                    <h1>Unlimited movies, TV shows and more.</h1>
                    <h4>Watch anywhere. Cancel anytime.</h4>
                    <h5>Ready to watch? Enter your email to create or restart membership</h5>
                </div>
                <div className="form">
                    <input type="email" name='email' placeholder='Email Address' />
                    <input type="password" name='password' placeholder='Password' />
                    <button>Get Started</button>
                </div>
                <button>Log in </button>
            </div>
        </div>
    </Container>
  )
}

const Container = styled.div`
    position:relative;
    .content {
    position: absolute ;
        top: 0;
        left: 0;
        background-color : rgba(0,0,0,0.5);
        height : 100vh;
        width: 100vw;
        display : grid;
        grid-template-rows : 15vh 85vh;
    }
`;