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

      <!-- Button Components Section -->
      <section class="button-components">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Buttons</h2>
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
                        Buttons
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <!-- Button Cards Wrapper -->
          <div class="buttons-cards-wrapper">
            <div class="row">
              <div class="col-lg-6" v-for="(group, idx) in buttonGroups" :key="idx">
                <div class="card-style mb-30">
                  <h5 class="text-medium mb-25">
                    {{ group.title }}
                    <span v-if="group.subtitle" class="text-sm text-regular">{{ group.subtitle }}</span>
                  </h5>
                  <ul class="buttons-group">
                    <li v-for="(btn, bidx) in group.buttons" :key="bidx">
                      <a href="#0" :class="btn.class">
                        <i v-if="btn.icon" :class="btn.icon"></i>
                        {{ btn.text }}
                      </a>
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
  name: "Buttons",
  data() {
    return {
      buttonGroups: [
        {
          title: "Square Buttons",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn square-btn btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn square-btn btn-hover" },
            { text: "Success", class: "main-btn success-btn square-btn btn-hover" },
            { text: "Danger", class: "main-btn danger-btn square-btn btn-hover" },
            { text: "Warning", class: "main-btn warning-btn square-btn btn-hover" },
            { text: "Info", class: "main-btn info-btn square-btn btn-hover" },
            { text: "Dark", class: "main-btn dark-btn square-btn btn-hover" },
            { text: "Light", class: "main-btn light-btn square-btn btn-hover" },
            { text: "Active", class: "main-btn active-btn square-btn btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn square-btn btn-hover" },
          ],
        },
        {
          title: "Default Buttons",
          subtitle: "(3px Corner Round)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn btn-hover" },
            { text: "Success", class: "main-btn success-btn btn-hover" },
            { text: "Danger", class: "main-btn danger-btn btn-hover" },
            { text: "Warning", class: "main-btn warning-btn btn-hover" },
            { text: "Info", class: "main-btn info-btn btn-hover" },
            { text: "Dark", class: "main-btn dark-btn btn-hover" },
            { text: "Light", class: "main-btn light-btn btn-hover" },
            { text: "Active", class: "main-btn active-btn btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn btn-hover" },
          ],
        },
        {
          title: "Rounded Buttons",
          subtitle: "(Full Rounded)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn rounded-full btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn rounded-full btn-hover" },
            { text: "Success", class: "main-btn success-btn rounded-full btn-hover" },
            { text: "Danger", class: "main-btn danger-btn rounded-full btn-hover" },
            { text: "Warning", class: "main-btn warning-btn rounded-full btn-hover" },
            { text: "Info", class: "main-btn info-btn rounded-full btn-hover" },
            { text: "Dark", class: "main-btn dark-btn rounded-full btn-hover" },
            { text: "Light", class: "main-btn light-btn rounded-full btn-hover" },
            { text: "Active", class: "main-btn active-btn rounded-full btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn rounded-full btn-hover" },
          ],
        },
        {
          title: "Square Outline Buttons",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-outline square-btn btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn-outline square-btn btn-hover" },
            { text: "Success", class: "main-btn success-btn-outline square-btn btn-hover" },
            { text: "Danger", class: "main-btn danger-btn-outline square-btn btn-hover" },
            { text: "Warning", class: "main-btn warning-btn-outline square-btn btn-hover" },
            { text: "Info", class: "main-btn info-btn-outline square-btn btn-hover" },
            { text: "Dark", class: "main-btn dark-btn-outline square-btn btn-hover" },
            { text: "Light", class: "main-btn light-btn-outline square-btn btn-hover" },
            { text: "Active", class: "main-btn active-btn-outline square-btn btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn-outline square-btn btn-hover" },
          ],
        },
        {
          title: "Default Outline Buttons",
          subtitle: "(3 Px Round)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-outline btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn-outline btn-hover" },
            { text: "Success", class: "main-btn success-btn-outline btn-hover" },
            { text: "Danger", class: "main-btn danger-btn-outline btn-hover" },
            { text: "Warning", class: "main-btn warning-btn-outline btn-hover" },
            { text: "Info", class: "main-btn info-btn-outline btn-hover" },
            { text: "Dark", class: "main-btn dark-btn-outline btn-hover" },
            { text: "Light", class: "main-btn light-btn-outline btn-hover" },
            { text: "Active", class: "main-btn active-btn-outline btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn-outline btn-hover" },
          ],
        },
        {
          title: "Default Outline Buttons",
          subtitle: "(Full Rounded)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-outline rounded-full btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn-outline rounded-full btn-hover" },
            { text: "Success", class: "main-btn success-btn-outline rounded-full btn-hover" },
            { text: "Danger", class: "main-btn danger-btn-outline rounded-full btn-hover" },
            { text: "Warning", class: "main-btn warning-btn-outline rounded-full btn-hover" },
            { text: "Info", class: "main-btn info-btn-outline rounded-full btn-hover" },
            { text: "Dark", class: "main-btn dark-btn-outline rounded-full btn-hover" },
            { text: "Light", class: "main-btn light-btn-outline rounded-full btn-hover" },
            { text: "Active", class: "main-btn active-btn-outline rounded-full btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn-outline rounded-full btn-hover" },
          ],
        },
        {
          title: "Square Light Buttons",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-light square-btn btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn-light square-btn btn-hover" },
            { text: "Success", class: "main-btn success-btn-light square-btn btn-hover" },
            { text: "Danger", class: "main-btn danger-btn-light square-btn btn-hover" },
            { text: "Warning", class: "main-btn warning-btn-light square-btn btn-hover" },
            { text: "Info", class: "main-btn info-btn-light square-btn btn-hover" },
            { text: "Dark", class: "main-btn dark-btn-light square-btn btn-hover" },
            { text: "Light", class: "main-btn light-btn-light square-btn btn-hover" },
            { text: "Active", class: "main-btn active-btn-light square-btn btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn-light square-btn btn-hover" },
          ],
        },
        {
          title: "Default Light Buttons",
          subtitle: "(3px Corner Round)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-light btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn-light btn-hover" },
            { text: "Success", class: "main-btn success-btn-light btn-hover" },
            { text: "Danger", class: "main-btn danger-btn-light btn-hover" },
            { text: "Warning", class: "main-btn warning-btn-light btn-hover" },
            { text: "Info", class: "main-btn info-btn-light btn-hover" },
            { text: "Dark", class: "main-btn dark-btn-light btn-hover" },
            { text: "Light", class: "main-btn light-btn-light btn-hover" },
            { text: "Active", class: "main-btn active-btn-light btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn-light btn-hover" },
          ],
        },
        {
          title: "Rounded Light Buttons",
          subtitle: "(Full Rounded)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-light rounded-full btn-hover" },
            { text: "Secondary", class: "main-btn secondary-btn-light rounded-full btn-hover" },
            { text: "Success", class: "main-btn success-btn-light rounded-full btn-hover" },
            { text: "Danger", class: "main-btn danger-btn-light rounded-full btn-hover" },
            { text: "Warning", class: "main-btn warning-btn-light rounded-full btn-hover" },
            { text: "Info", class: "main-btn info-btn-light rounded-full btn-hover" },
            { text: "Dark", class: "main-btn dark-btn-light rounded-full btn-hover" },
            { text: "Light", class: "main-btn light-btn-light rounded-full btn-hover" },
            { text: "Active", class: "main-btn active-btn-light rounded-full btn-hover" },
            { text: "Deactive", class: "main-btn deactive-btn-light rounded-full btn-hover" },
          ],
        },
        {
          title: "Square Buttons With Icon",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Secondary", class: "main-btn secondary-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Success", class: "main-btn success-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Danger", class: "main-btn danger-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Warning", class: "main-btn warning-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Info", class: "main-btn info-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Dark", class: "main-btn dark-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Light", class: "main-btn light-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Active", class: "main-btn active-btn square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Deactive", class: "main-btn deactive-btn square-btn btn-hover", icon: "lni lni-heart" },
          ],
        },
        {
          title: "Default Buttons With Icon",
          subtitle: "(3px Corner Round)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn btn-hover", icon: "lni lni-heart" },
            { text: "Secondary", class: "main-btn secondary-btn btn-hover", icon: "lni lni-heart" },
            { text: "Success", class: "main-btn success-btn btn-hover", icon: "lni lni-heart" },
            { text: "Danger", class: "main-btn danger-btn btn-hover", icon: "lni lni-heart" },
            { text: "Warning", class: "main-btn warning-btn btn-hover", icon: "lni lni-heart" },
            { text: "Info", class: "main-btn info-btn btn-hover", icon: "lni lni-heart" },
            { text: "Dark", class: "main-btn dark-btn btn-hover", icon: "lni lni-heart" },
            { text: "Light", class: "main-btn light-btn btn-hover", icon: "lni lni-heart" },
            { text: "Active", class: "main-btn active-btn btn-hover", icon: "lni lni-heart" },
            { text: "Deactive", class: "main-btn deactive-btn btn-hover", icon: "lni lni-heart" },
          ],
        },
        {
          title: "Rounded Buttons With Icon",
          subtitle: "(Full Rounded)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Secondary", class: "main-btn secondary-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Success", class: "main-btn success-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Danger", class: "main-btn danger-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Warning", class: "main-btn warning-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Info", class: "main-btn info-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Dark", class: "main-btn dark-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Light", class: "main-btn light-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Active", class: "main-btn active-btn rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Deactive", class: "main-btn deactive-btn rounded-full btn-hover", icon: "lni lni-heart" },
          ],
        },
        {
          title: "Square Light Buttons With Icon",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Secondary", class: "main-btn secondary-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Success", class: "main-btn success-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Danger", class: "main-btn danger-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Warning", class: "main-btn warning-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Info", class: "main-btn info-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Dark", class: "main-btn dark-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Light", class: "main-btn light-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Active", class: "main-btn active-btn-light square-btn btn-hover", icon: "lni lni-heart" },
            { text: "Deactive", class: "main-btn deactive-btn-light square-btn btn-hover", icon: "lni lni-heart" },
          ],
        },
        {
          title: "Default Light Buttons With Icon",
          subtitle: "(3px Corner Round)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Secondary", class: "main-btn secondary-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Success", class: "main-btn success-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Danger", class: "main-btn danger-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Warning", class: "main-btn warning-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Info", class: "main-btn info-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Dark", class: "main-btn dark-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Light", class: "main-btn light-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Active", class: "main-btn active-btn-light btn-hover", icon: "lni lni-heart" },
            { text: "Deactive", class: "main-btn deactive-btn-light btn-hover", icon: "lni lni-heart" },
          ],
        },
        {
          title: "Rounded Light Buttons With Icon",
          subtitle: "(Full Rounded)",
          buttons: [
            { text: "Primary", class: "main-btn primary-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Secondary", class: "main-btn secondary-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Success", class: "main-btn success-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Danger", class: "main-btn danger-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Warning", class: "main-btn warning-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Info", class: "main-btn info-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Dark", class: "main-btn dark-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Light", class: "main-btn light-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Active", class: "main-btn active-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
            { text: "Deactive", class: "main-btn deactive-btn-light rounded-full btn-hover", icon: "lni lni-heart" },
          ],
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
