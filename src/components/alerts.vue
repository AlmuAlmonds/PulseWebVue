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
          <!-- ...existing code for sidebar navigation... -->
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>
    <!-- Main Wrapper -->
    <main class="main-wrapper">
      <header class="header">
        <div class="container-fluid">
          <div class="row">
            <div class="col-lg-5 col-md-5 col-6">
              <div class="header-left d-flex align-items-center">
                <div class="menu-toggle-btn mr-15">
                  <button id="menu-toggle" class="main-btn primary-btn btn-hover" @click="toggleMenu">
                    <i class="lni lni-chevron-left me-2"></i> Menu
                  </button>
                </div>
                <div class="header-search d-none d-md-flex">
                  <form @submit.prevent>
                    <input type="text" placeholder="Search..." v-model="headerSearch" />
                    <button><i class="lni lni-search-alt"></i></button>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-lg-7 col-md-7 col-6">
              <div class="header-right">
                <!-- ...existing code for notifications, messages, profile... -->
              </div>
            </div>
          </div>
        </div>
      </header>
      <!-- Alert Components -->
      <section class="alert-components">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Alerts</h2>
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
                        Alerts
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>
          <div class="alerts-wrapper">
            <div class="card-style mb-30">
              <h5 class="text-medium mb-25">Default Alert</h5>
              <p class="text-sm mb-30">
                Alerts are available for any length of text, as well as an optional dismiss button. For proper styling, use one of the four required contextual classes (e.g., .alert-success). For inline dismissal, use the alerts jQuery plugin
              </p>
              <div class="alert-list-wrapper">
                <div v-for="alert in alerts" :key="alert.type" :class="['alert-box', alert.class, 'pl-100']">
                  <div class="left">
                    <h5 class="text-bold">{{ alert.label }}</h5>
                  </div>
                  <div class="alert">
                    <h4 class="alert-heading">{{ alert.color }}</h4>
                    <p class="text-medium">{{ alert.text }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <footer class="footer">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6 order-last order-md-first">
              <div class="copyright text-center text-md-start">
                <p class="text-sm">
                  Designed and Developed by
                  <a href="https://plainadmin.com" rel="nofollow" target="_blank">PlainAdmin</a>
                </p>
              </div>
            </div>
            <div class="col-md-6">
              <div class="terms d-flex justify-content-center justify-content-md-end">
                <a href="#0" class="text-sm">Term & Conditions</a>
                <a href="#0" class="text-sm ml-15">Privacy & Policy</a>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headerSearch: '',
      alerts: [
        { type: 'primary', class: 'primary-alert', label: 'Primary', color: '#4A6CF7', text: 'Excitement, Energy, Passion, Courage, Attention' },
        { type: 'danger', class: 'danger-alert', label: 'Danger', color: '#D50100', text: 'Excitement, Energy, Passion, Courage, Attention' },
        { type: 'orange', class: 'orange-alert', label: 'Orange', color: '#D50100', text: 'Excitement, Energy, Passion, Courage, Attention' },
        { type: 'warning', class: 'warning-alert', label: 'Warning', color: '#D50100', text: 'Enthusiasm, Opportunity, Spontaneity, Happiness, Positivity' },
        { type: 'info', class: 'info-alert', label: 'Info', color: '#D50100', text: 'Growth, Harmony, Kindness, Dependability' },
        { type: 'success', class: 'success-alert', label: 'Success', color: '#D50100', text: 'Safety, Harmony, Stability, Reliability, Balance' },
        { type: 'secondary', class: 'secondary-alert', label: 'Secondary', color: '#D50100', text: 'Safety, Harmony, Stability, Reliability, Balance' },
        { type: 'gray', class: 'gray-alert', label: 'Gray', color: '#D50100', text: 'Safety, Harmony, Stability, Reliability, Balance' },
        { type: 'black', class: 'black-alert', label: 'Black', color: '#D50100', text: 'Safety, Harmony, Stability, Reliability, Balance' }
      ]
    };
  },
  methods: {
    toggleMenu() {
      // Implement menu toggle logic
    }
  }
};
</script>

<style scoped>
/* Move all CSS from the HTML file here, unchanged for now. */
</style>
