import { useState } from 'react';
import './App.css';


function Sale(props) {
  const [count, setCount] = useState(0);  

  const handleClick = () => {
    setCount((c) => c + 1);
    props.onAdd();                        
  };

  return (
    <div className="item1">
      <h1>{props.name}</h1>
      {props.image && <img src={props.image} alt={props.name} />}
      <b className="title1">Цена: {props.cost}</b>
      <button className="SaleButton" onClick={handleClick}>
        Добавить в корзину
      </button>
      <p className="V">Выбрано товара: {count}</p>
    </div>
  );
}

function App() {
  const [allCount, setAllCount] = useState(0);

  function handleClick() {
    setAllCount((c) => c + 1);              
  }

  return (
    <div>
      <table>
        <tbody>
          <tr>
            <td><Sale name="Хлеб"    image="https://static.vecteezy.com/system/resources/previews/004/141/669/non_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg" cost="65"  onAdd={handleClick} /></td>
            <td><Sale name="Молоко"  image="https://static.vecteezy.com/system/resources/previews/004/141/669/non_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg" cost="90"  onAdd={handleClick} /></td>
          </tr>
          <tr>
            <td><Sale name="Чай"     image="https://static.vecteezy.com/system/resources/previews/004/141/669/non_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg" cost="400" onAdd={handleClick} /></td>
            <td><Sale name="Колбаса" image="https://static.vecteezy.com/system/resources/previews/004/141/669/non_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg" cost="150" onAdd={handleClick} /></td>
          </tr>
          <tr>
            <td colSpan={2}>
              <h3>Выбрано товаров: {allCount}</h3>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default App;