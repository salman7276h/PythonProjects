// 🌟 Product Database
const products = [
  {
    name: "Realme Narzo 60 5G",
    image: "https://m.media-amazon.com/images/I/61u9zN1HYCL._SX679_.jpg",
    amazonLink: "https://amzn.to/3RhC6cA",
    flipkartLink: "https://www.flipkart.com/",
  },
  {
    name: "boAt Airdopes 141",
    image: "https://m.media-amazon.com/images/I/51HBom8xz7L._SX679_.jpg",
    amazonLink: "https://amzn.to/3uWvjQx",
    flipkartLink: "https://www.flipkart.com/",
  },
  {
    name: "Samsung Galaxy M14 5G",
    image: "https://m.media-amazon.com/images/I/81ZSn2rk9WL._SX679_.jpg",
    amazonLink: "https://amzn.to/4bfUwI5",
    flipkartLink: "https://www.flipkart.com/",
  }
];

// 🌟 Function: Search Product
function searchProduct() {
  const input = document.getElementById("searchInput").value.toLowerCase().trim();
  const productListContainer = document.getElementById("productListContainer");
  productListContainer.innerHTML = "";

  // 🌀 Show loading spinner
  productListContainer.innerHTML = `<div class="loader"></div>`;

  // Simulate loading delay (for smooth animation)
  setTimeout(() => {
    const matchedProducts = products.filter(product =>
      product.name.toLowerCase().includes(input)
    );

    productListContainer.innerHTML = ""; // clear loader

    if (!input) {
      productListContainer.innerHTML = `<p class="fade-text">Please type a product name to search 🔍</p>`;
      return;
    }

    if (matchedProducts.length > 0) {
      matchedProducts.forEach((product, index) => {
        const card = document.createElement("div");
        card.className = "product";
        card.style.animation = `fadeUp 0.8s ease forwards`;
        card.style.animationDelay = `${index * 0.2}s`;
        card.innerHTML = `
          <h3>${product.name}</h3>
          <img src="${product.image}" alt="${product.name}" width="200"/>
          <p>
            <a href="${product.amazonLink}" target="_blank">Buy on Amazon</a><br/>
            <a href="${product.flipkartLink}" target="_blank">Buy on Flipkart</a>
          </p>
        `;
        productListContainer.appendChild(card);
      });
    } else {
      productListContainer.innerHTML = `<p class="fade-text">❌ No matching products found. Try another name.</p>`;
    }
  }, 800);
}

// 🌟 Function: Show Trending Products
function showTrendingProducts() {
  const trendingDiv = document.getElementById("productListContainer");
  trendingDiv.innerHTML = "";

  products.slice(0, 3).forEach((p, index) => {
    const card = document.createElement("div");
    card.className = "product";
    card.style.animation = `fadeUp 0.8s ease forwards`;
    card.style.animationDelay = `${index * 0.3}s`;
    card.innerHTML = `
      <h3>${p.name}</h3>
      <img src="${p.image}" alt="${p.name}" />
      <p>
        <a href="${p.amazonLink}" target="_blank">Amazon</a>
        <a href="${p.flipkartLink}" target="_blank">Flipkart</a>
      </p>
    `;
    trendingDiv.appendChild(card);
  });
}

// 🌟 Call Trending Products on Load
window.onload = showTrendingProducts;
