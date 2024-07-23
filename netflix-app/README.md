## React Router Dom
Libray used for implementing rounting in web applications built with React.It allows to create single page application that feature dynamic routes, enabling navigation between components without reloading the entire page.

```
import Login from './pages/Login';
import Signup from './pages/Signup';
import Netflix from './pages/Netflix';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path='/login' element={<Login />}/>
        <Route exact path='/signup' element={<Signup />}/>
        <Route exact path='/' element={<Netflix />}/>
      </Routes>
    </BrowserRouter>
  )
}
```

## Firebase
Firebase is an app development plateform by Google. It uses for building web and mobile apps and offers backend services , real-time databases, analytics, authentication, cloud storage.

## Styled-components
It's a popular library for styling React applications. It allows to crite CSS within Javascript.

```
const Container = styled.div`
    height: 100vh;
    width : 100vw;
    img{
        height: 100vh;
        width: 100vw; 
    }
`;
```

19'35