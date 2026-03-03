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

      <!-- Icons Section -->
      <section class="section">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Icons</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/admin">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Icons
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>
          <div class="icons-wrapper">
            <div class="row">
              <div class="col-12">
                <div class="card-style">
                  <div class="title d-flex justify-content-between">
                    <div class="left">
                      <h6 class="text-medium mb-10">Icons Pack</h6>
                    </div>
                  </div>
                  <!-- End Title -->
                  <ul class="icons">
                    <li v-for="icon in icons" :key="icon.name" class="trigger Free">
                      <i :class="icon.class"></i><span>{{ icon.name }}</span>
                    </li>
                  </ul>
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
  name: "Icons",
  data() {
    return {
      icons: [
        { name: "500px", class: "lni lni-500px" },
        { name: "add-files", class: "lni lni-add-files" },
        { name: "adobe", class: "lni lni-adobe" },
        { name: "agenda", class: "lni lni-agenda" },
        { name: "airbnb", class: "lni lni-airbnb" },
        { name: "alarm", class: "lni lni-alarm" },
        { name: "alarm-clock", class: "lni lni-alarm-clock" },
        { name: "amazon", class: "lni lni-amazon" },
        { name: "amazon-original", class: "lni lni-amazon-original" },
        { name: "amazon-pay", class: "lni lni-amazon-pay" },
        { name: "ambulance", class: "lni lni-ambulance" },
        { name: "amex", class: "lni lni-amex" },
        { name: "anchor", class: "lni lni-anchor" },
        { name: "android", class: "lni lni-android" },
        { name: "android-original", class: "lni lni-android-original" },
        { name: "angellist", class: "lni lni-angellist" },
        { name: "angle-double-down", class: "lni lni-angle-double-down" },
        { name: "angle-double-left", class: "lni lni-angle-double-left" },
        { name: "angle-double-right", class: "lni lni-angle-double-right" },
        { name: "angle-double-up", class: "lni lni-angle-double-up" },
        { name: "angular", class: "lni lni-angular" },
        { name: "apartment", class: "lni lni-apartment" },
        { name: "app-store", class: "lni lni-app-store" },
        { name: "apple-brand", class: "lni lni-apple-brand" },
        { name: "apple-pay", class: "lni lni-apple-pay" },
        { name: "archive", class: "lni lni-archive" },
        { name: "arrow-down", class: "lni lni-arrow-down" },
        { name: "arrow-down-circle", class: "lni lni-arrow-down-circle" },
        { name: "arrow-left", class: "lni lni-arrow-left" },
        { name: "arrow-left-circle", class: "lni lni-arrow-left-circle" },
        { name: "arrow-right", class: "lni lni-arrow-right" },
        { name: "arrow-right-circle", class: "lni lni-arrow-right-circle" },
        { name: "arrow-top-left", class: "lni lni-arrow-top-left" },
        { name: "arrow-top-right", class: "lni lni-arrow-top-right" },
        { name: "arrow-up", class: "lni lni-arrow-up" },
        { name: "arrow-up-circle", class: "lni lni-arrow-up-circle" },
        { name: "arrows-horizontal", class: "lni lni-arrows-horizontal" },
        { name: "arrows-vertical", class: "lni lni-arrows-vertical" },
        // ...add all other icons here...
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
