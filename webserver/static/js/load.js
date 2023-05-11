// Create a class for the element
class PopUpInfo extends HTMLElement {
  constructor() {
    // Always call super first in constructor
    super();

    // Create a shadow root
    const shadow = this.attachShadow({ mode: 'open' });

    // Create spans
    const wrapper = document.createElement('span');
    wrapper.setAttribute('class', 'wrapper');

    const icon = document.createElement('span');
    icon.setAttribute('class', 'icon');
    icon.setAttribute('tabindex', 0);

    const info = document.createElement('span');
    info.setAttribute('class', 'info');

    // Take attribute content and put it inside the info span
    const text = this.getAttribute('data-text');
    info.textContent = text;

    // Insert icon
    let imgUrl;
    if (this.hasAttribute('img')) {
      imgUrl = this.getAttribute('img');
    } else {
      imgUrl = 'img/default.png';
    }

    const img = document.createElement('img');
    img.src = imgUrl;
    icon.appendChild(img);

    // Create some CSS to apply to the shadow dom
    const style = document.createElement('style');
    console.log(style.isConnected);

    style.textContent = `
      .wrapper {
        position: relative;
      }

      .info {
        font-size: 0.8rem;
        width: 200px;
        display: inline-block;
        border: 1px solid black;
        padding: 10px;
        background: white;
        border-radius: 10px;
        opacity: 0;
        transition: 0.6s all;
        position: absolute;
        bottom: 20px;
        left: 10px;
        z-index: 3;
      }

      img {
        width: 1.2rem;
      }

      .icon:hover + .info, .icon:focus + .info {
        opacity: 1;
      }
    `;

    // Attach the created elements to the shadow dom
    shadow.appendChild(style);
    console.log(style.isConnected);
    shadow.appendChild(wrapper);
    wrapper.appendChild(icon);
    wrapper.appendChild(info);
  }
}

// Define the new element
customElements.define('popup-info', PopUpInfo);

//A custom element that looks like a square

class Square extends HTMLElement {
  constructor() {
    super();
    // Attach a shadow root to the element.
    const shadowRoot = this.attachShadow({ mode: 'open' });
    // Create a standard img element and set it's attributes.
    const img = document.createElement('img');
    img.alt = this.getAttribute('data-text');
    img.src = this.getAttribute('img');
    img.width = '150';
    img.height = '150';
    img.className = 'product-img';
    // Append it to the shadow root.
    shadowRoot.appendChild(img);
  }
}

customElements.define('product-img', Square);

//A custom element that looks like a circle

class Circle extends HTMLElement {
  constructor() {
    super();
    // Attach a shadow root to the element.
    const shadowRoot = this.attachShadow({ mode: 'open' });
    // Create a standard img element and set it's attributes.
    const img = document.createElement('img');
    img.alt = this.getAttribute('data-text');
    img.src = this.getAttribute('img');
    img.width = '150';
    img.height = '150';
    img.className = 'product-img';
    // Append it to the shadow root.
    shadowRoot.appendChild(img);
  }
}


document.getElementById("map").addEventListener("load", function () {
  var doc = this.getSVGDocument();
  var svg = doc.getElementById("map-svg");
  var circleNode = document.getElementById('myDrone');
  console.log(circle_x, circle_y);
  if (circleNode == null) {
    circleNode = doc.createElementNS("http://www.w3.org/2000/svg", "circle");
    circleNode.setAttributeNS(null, 'cx', circle_x);
    circleNode.setAttributeNS(null, 'cy', circle_y);
    circleNode.setAttributeNS(null, 'r', '5');
    circleNode.setAttributeNS(null, 'fill', 'red');
    circleNode.setAttributeNS(null, 'id', 'myDrone');
    svg.appendChild(circleNode);
  }
  else {
    circleNode.setAttributeNS(null, 'cx', circle_x);
    circleNode.setAttributeNS(null, 'cy', circle_y);
    circleNode.setAttributeNS(null, 'r', '5');
    circleNode.setAttributeNS(null, 'fill', 'red');
    circleNode.setAttributeNS(null, 'id', 'myDrone');
  }
});

