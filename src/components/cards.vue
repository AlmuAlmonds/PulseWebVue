<template>
  <div>
    <!-- Preloader -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>

    <!-- Sidebar Navigation -->
    <aside class="sidebar-nav-wrapper">
      <div class="navbar-logo">
        <router-link to="/admin">
          <img src="../images/PULSE OG.png" alt="logo" style="width: 45px; height: 45px; object-fit: contain;" />
          <span style="font-size: 18px; font-weight: 600; color: #3b5998;">PULSE Admin</span>
        </router-link>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <li class="nav-item">
            <router-link to="/admin" class="nav-link">
              <span class="icon">
                <!-- Dashboard SVG -->
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M8.74999 18.3333C12.2376 18.3333 15.1364 15.8128 15.7244 12.4941C15.8448 11.8143 15.2737 11.25 14.5833 11.25H9.99999C9.30966 11.25 8.74999 10.6903 8.74999 10V5.41666C8.74999 4.7263 8.18563 4.15512 7.50586 4.27556C4.18711 4.86357 1.66666 7.76243 1.66666 11.25C1.66666 15.162 4.83797 18.3333 8.74999 18.3333Z" />
                  <path d="M17.0833 10C17.7737 10 18.3432 9.43708 18.2408 8.75433C17.7005 5.14918 14.8508 2.29947 11.2457 1.75912C10.5629 1.6568 10 2.2263 10 2.91665V9.16666C10 9.62691 10.3731 10 10.8333 10H17.0833Z" />
                </svg>
              </span>
              <span class="text">Dashboard</span>
            </router-link>
          </li>
          <!-- ...existing sidebar items, replace <a> with <router-link> as needed... -->
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>

    <!-- Main Wrapper -->
    <main class="main-wrapper">
      <!-- Header -->
      <header class="header">
        <!-- ...existing header code... -->
      </header>

      <!-- Card Components Section -->
      <section class="card-components">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Cards</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/admin">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item">
                        <router-link to="#">UI Components</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Cards
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <!-- Card Styles -->
          <div class="cards-styles">
            <!-- Card Style 1 -->
            <div class="row">
              <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6" v-for="(card, idx) in cardStyle1" :key="'cs1-' + idx">
                <div class="card-style-1 mb-30">
                  <div class="card-meta">
                    <div class="image">
                      <img :src="card.adminImg" alt="" />
                    </div>
                    <div class="text">
                      <p class="text-sm text-medium">
                        Posted by : <a href="#0">{{ card.author }}</a>
                      </p>
                    </div>
                  </div>
                  <div class="card-image">
                    <a href="#0">
                      <img :src="card.cardImg" alt="" />
                    </a>
                  </div>
                  <div class="card-content">
                    <h4><a href="#0">{{ card.title }}</a></h4>
                    <p>{{ card.text }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Card Style 2 -->
            <div class="row">
              <div class="col-12">
                <div class="title mt-30 mb-30">
                  <h2>Cards</h2>
                </div>
              </div>
              <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6" v-for="(card, idx) in cardStyle2" :key="'cs2-' + idx">
                <div class="card-style-2 mb-30">
                  <div class="card-image">
                    <a href="#0">
                      <img :src="card.img" alt="" />
                    </a>
                  </div>
                  <div class="card-content">
                    <h4><a href="#0">{{ card.title }}</a></h4>
                    <p>{{ card.text }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Card Style 3 -->
            <div class="row">
              <div class="col-12">
                <div class="title mt-30 mb-30">
                  <h2>Cards</h2>
                </div>
              </div>
              <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6" v-for="(card, idx) in cardStyle3" :key="'cs3-' + idx">
                <div class="card-style-3 mb-30">
                  <div class="card-content">
                    <h4><a href="#0">{{ card.title }}</a></h4>
                    <p>{{ card.text }}</p>
                    <a href="#0" class="read-more">Read More</a>
                  </div>
                </div>
              </div>
            </div>

            <!-- Card Style 4 -->
            <div class="row">
              <div class="col-12">
                <div class="title mt-30 mb-30">
                  <h2>Cards</h2>
                </div>
              </div>
              <div class="col-xl-4 col-lg-4 col-md-6" v-for="(card, idx) in cardStyle4" :key="'cs4-' + idx">
                <div class="card-style-4 mb-30">
                  <div class="card-image">
                    <a href="#0">
                      <img :src="card.img" alt="" />
                    </a>
                  </div>
                  <div class="card-content">
                    <h4><a href="#0">{{ card.title }}</a></h4>
                    <p>{{ card.text }}</p>
                    <a href="#0" class="read-more">Read More</a>
                  </div>
                </div>
              </div>
            </div>

            <!-- Card Style 5 -->
            <div class="row">
              <div class="col-12">
                <div class="title mt-30 mb-30">
                  <h2>Cards</h2>
                </div>
              </div>
              <div class="col-xl-6 col-lg-6" v-for="(card, idx) in cardStyle5" :key="'cs5-' + idx">
                <div class="card-style-5 mb-30">
                  <div class="card-image">
                    <a href="#0">
                      <img :src="card.img" alt="" />
                    </a>
                  </div>
                  <div class="card-content">
                    <h4><a href="#0">{{ card.title }}</a></h4>
                    <p>{{ card.text }}</p>
                    <a href="#0" class="main-btn primary-btn btn-hover">Read More</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer">
        <!-- ...existing footer code... -->
      </footer>
    </main>
  </div>
</template>

<script>
export default {
  name: "Cards",
  data() {
    return {
      cardStyle1: [
        {
          adminImg: "assets/images/cards/card-style-1/admin-1.png",
          author: "Hammad",
          cardImg: "assets/images/cards/card-style-1/card-1.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          adminImg: "assets/images/cards/card-style-1/admin-2.png",
          author: "Mahmud",
          cardImg: "assets/images/cards/card-style-1/card-2.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          adminImg: "assets/images/cards/card-style-1/admin-3.png",
          author: "Jamil Kareem",
          cardImg: "assets/images/cards/card-style-1/card-3.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
      ],
      cardStyle2: [
        {
          img: "assets/images/cards/card-style-2/card-1.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          img: "assets/images/cards/card-style-2/card-2.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          img: "assets/images/cards/card-style-2/card-3.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
      ],
      cardStyle3: [
        {
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante. With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante. With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante. With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
      ],
      cardStyle4: [
        {
          img: "assets/images/cards/card-style-4/card-1.png",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          img: "assets/images/cards/card-style-4/card-2.png",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          img: "assets/images/cards/card-style-4/card-3.png",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
      ],
      cardStyle5: [
        {
          img: "assets/images/cards/card-style-5/card-1.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
        {
          img: "assets/images/cards/card-style-5/card-2.jpg",
          title: "Card Title here",
          text: "With supporting text below as a natural lead-in to additional content. consectetur adipiscing elit. Integer posuere erat a ante.",
        },
      ],
    };
  },
};
</script>

<style scoped>
@import "assets/css/bootstrap.min.css";
@import "assets/css/lineicons.css";
@import "assets/css/materialdesignicons.min.css";
@import "assets/css/fullcalendar.css";
@import "assets/css/main.css";
</style>
