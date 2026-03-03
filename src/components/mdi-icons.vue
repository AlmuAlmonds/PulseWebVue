<template>
  <div>
    <!-- Preloader -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>

    <!-- Sidebar Navigation -->
    <aside class="sidebar-nav-wrapper">
      <div class="navbar-logo">
        <router-link
          to="/admin/index"
          style="
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
          "
        >
          <img
            src="../images/PULSE OG.png"
            alt="logo"
            style="width: 45px; height: 45px; object-fit: contain"
          />
          <span style="font-size: 18px; font-weight: 600; color: #3b5998"
            >PULSE Admin</span
          >
        </router-link>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <li class="nav-item">
            <router-link to="/admin/index">
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Dashboard</span>
            </router-link>
          </li>
          <li class="nav-item nav-item-has-children">
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_2"
              aria-controls="ddmenu_2"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Pages</span>
            </a>
            <ul id="ddmenu_2" class="collapse dropdown-nav">
              <li><router-link to="/admin/settings">Settings</router-link></li>
              <li>
                <router-link to="/admin/blank-page">Blank Page</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link to="/admin/invoice">
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Invoice</span>
            </router-link>
          </li>
          <span class="divider"><hr /></span>
          <li class="nav-item nav-item-has-children">
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_4"
              aria-controls="ddmenu_4"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">UI Elements</span>
            </a>
            <ul id="ddmenu_4" class="collapse dropdown-nav">
              <li><router-link to="/admin/alerts">Alerts</router-link></li>
              <li><router-link to="/admin/buttons">Buttons</router-link></li>
              <li><router-link to="/admin/cards">Cards</router-link></li>
              <li>
                <router-link to="/admin/typography">Typography</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item nav-item-has-children">
            <router-link
              to="/admin/icons"
              class=""
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_55"
              aria-controls="ddmenu_55"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Icons</span>
            </router-link>
            <ul id="ddmenu_55" class="collapse show dropdown-nav">
              <li><router-link to="/admin/icons">LineIcons</router-link></li>
              <li>
                <router-link to="/admin/mdi-icons" class="active"
                  >MDI Icons</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item nav-item-has-children">
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_5"
              aria-controls="ddmenu_5"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Forms</span>
            </a>
            <ul id="ddmenu_5" class="collapse dropdown-nav">
              <li>
                <router-link to="/admin/form-elements"
                  >Form Elements</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link to="/admin/tables">
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Tables</span>
            </router-link>
          </li>
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>

    <!-- Main Wrapper -->
    <main class="main-wrapper">
      <!-- Header -->
      <header class="header">
        <div class="container-fluid">
          <div class="row">
            <div class="col-lg-5 col-md-5 col-6">
              <div class="header-left d-flex align-items-center">
                <div class="menu-toggle-btn mr-15">
                  <button
                    id="menu-toggle"
                    class="main-btn primary-btn btn-hover"
                    @click="toggleMenu"
                  >
                    <i class="lni lni-chevron-left me-2"></i> Menu
                  </button>
                </div>
                <div class="header-search d-none d-md-flex">
                  <form @submit.prevent>
                    <input
                      type="text"
                      placeholder="Search..."
                      v-model="searchQuery"
                    />
                    <button><i class="lni lni-search-alt"></i></button>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-lg-7 col-md-7 col-6">
              <div class="header-right">
                <!-- Notification -->
                <div class="notification-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button">
                    <svg
                      width="22"
                      height="22"
                      viewBox="0 0 22 22"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <!-- ...SVG... -->
                    </svg>
                    <span></span>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end">
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="assets/images/lead/lead-6.png" alt="" />
                        </div>
                        <div class="content">
                          <h6>
                            John Doe
                            <span class="text-regular"
                              >comment on a product.</span
                            >
                          </h6>
                          <p>
                            Lorem ipsum dolor sit amet, consect etur adipiscing
                            elit Vivamus tortor.
                          </p>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="assets/images/lead/lead-1.png" alt="" />
                        </div>
                        <div class="content">
                          <h6>
                            Jonathon
                            <span class="text-regular">like on a product.</span>
                          </h6>
                          <p>
                            Lorem ipsum dolor sit amet, consect etur adipiscing
                            elit Vivamus tortor.
                          </p>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- Message -->
                <div class="header-message-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button">
                    <svg
                      width="22"
                      height="22"
                      viewBox="0 0 22 22"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <!-- ...SVG... -->
                    </svg>
                    <span></span>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end">
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="assets/images/lead/lead-5.png" alt="" />
                        </div>
                        <div class="content">
                          <h6>Jacob Jones</h6>
                          <p>Hey!I can across your profile and ...</p>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="assets/images/lead/lead-3.png" alt="" />
                        </div>
                        <div class="content">
                          <h6>John Doe</h6>
                          <p>Would you mind please checking out</p>
                          <span>12 mins ago</span>
                        </div>
                      </a>
                    </li>
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="assets/images/lead/lead-2.png" alt="" />
                        </div>
                        <div class="content">
                          <h6>Anee Lee</h6>
                          <p>Hey! are you available for freelance?</p>
                          <span>1h ago</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- Profile -->
                <div class="profile-box ml-15">
                  <button
                    class="dropdown-toggle bg-transparent border-0"
                    type="button"
                  >
                    <div class="profile-info">
                      <div class="info">
                        <div class="image">
                          <img
                            src="assets/images/profile/profile-image.png"
                            alt=""
                          />
                        </div>
                        <div>
                          <h6 class="fw-500">Adam Joe</h6>
                          <p>Admin</p>
                        </div>
                      </div>
                    </div>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end">
                    <li>
                      <div class="author-info flex items-center !p-1">
                        <div class="image">
                          <img
                            src="assets/images/profile/profile-image.png"
                            alt="image"
                          />
                        </div>
                        <div class="content">
                          <h4 class="text-sm">Adam Joe</h4>
                          <a
                            class="text-black/40 dark:text-white/40 hover:text-black dark:hover:text-white text-xs"
                            href="#"
                            >Email@gmail.com</a
                          >
                        </div>
                      </div>
                    </li>
                    <li class="divider"></li>
                    <li>
                      <a href="#0"><i class="lni lni-user"></i> View Profile</a>
                    </li>
                    <li>
                      <a href="#0"
                        ><i class="lni lni-alarm"></i> Notifications</a
                      >
                    </li>
                    <li>
                      <a href="#0"> <i class="lni lni-inbox"></i> Messages </a>
                    </li>
                    <li>
                      <a href="#0"> <i class="lni lni-cog"></i> Settings </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                      <a href="#0"> <i class="lni lni-exit"></i> Sign Out </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- Section -->
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
                        <router-link to="/admin/index">Dashboard</router-link>
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
                  <div class="icons" id="newIcons">
                    <div v-for="icon in icons" :key="icon.name">
                      <i :class="icon.class"></i><span>{{ icon.name }}</span>
                    </div>
                  </div>
                  <a
                    href="https://materialdesignicons.com/"
                    class="text-primary"
                    target="_blank"
                    >and 5000+ icons.</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6 order-last order-md-first">
              <div class="copyright text-center text-md-start">
                <p class="text-sm">
                  Designed and Developed by
                  <a
                    href="https://plainadmin.com"
                    rel="nofollow"
                    target="_blank"
                    >PlainAdmin</a
                  >
                </p>
              </div>
            </div>
            <div class="col-md-6">
              <div
                class="terms d-flex justify-content-center justify-content-md-end"
              >
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
  name: "mdi-icons",
  data() {
    return {
      searchQuery: "",
      icons: [
        { class: "mdi mdi-abacus", name: "abacus" },
        { class: "mdi mdi-alarm-light-off", name: "alarm-light-off" },
        {
          class: "mdi mdi-alarm-light-off-outline",
          name: "alarm-light-off-outline",
        },
        { class: "mdi mdi-broadcast", name: "broadcast" },
        { class: "mdi mdi-broadcast-off", name: "broadcast-off" },
        {
          class: "mdi mdi-calendar-clock-outline",
          name: "calendar-clock-outline",
        },
        { class: "mdi mdi-chat-question", name: "chat-question" },
        {
          class: "mdi mdi-chat-question-outline",
          name: "chat-question-outline",
        },
        {
          class: "mdi mdi-check-decagram-outline",
          name: "check-decagram-outline",
        },
        { class: "mdi mdi-clipboard-clock", name: "clipboard-clock" },
        {
          class: "mdi mdi-clipboard-clock-outline",
          name: "clipboard-clock-outline",
        },
        { class: "mdi mdi-cookie-clock", name: "cookie-clock" },
        { class: "mdi mdi-cookie-clock-outline", name: "cookie-clock-outline" },
        { class: "mdi mdi-cookie-edit", name: "cookie-edit" },
        { class: "mdi mdi-cookie-edit-outline", name: "cookie-edit-outline" },
        { class: "mdi mdi-cookie-lock", name: "cookie-lock" },
        { class: "mdi mdi-cookie-lock-outline", name: "cookie-lock-outline" },
        { class: "mdi mdi-cookie-off", name: "cookie-off" },
        { class: "mdi mdi-cookie-off-outline", name: "cookie-off-outline" },
        { class: "mdi mdi-cookie-refresh", name: "cookie-refresh" },
        {
          class: "mdi mdi-cookie-refresh-outline",
          name: "cookie-refresh-outline",
        },
        { class: "mdi mdi-dog-side-off", name: "dog-side-off" },
        { class: "mdi mdi-fan-auto", name: "fan-auto" },
        { class: "mdi mdi-fire-off", name: "fire-off" },
        { class: "mdi mdi-firework-off", name: "firework-off" },
        { class: "mdi mdi-food-turkey", name: "food-turkey" },
        { class: "mdi mdi-gift-off", name: "gift-off" },
        { class: "mdi mdi-gift-off-outline", name: "gift-off-outline" },
        { class: "mdi mdi-gift-open", name: "gift-open" },
        { class: "mdi mdi-gift-open-outline", name: "gift-open-outline" },
        { class: "mdi mdi-kettle-pour-over", name: "kettle-pour-over" },
        { class: "mdi mdi-koala", name: "koala" },
        { class: "mdi mdi-message-question", name: "message-question" },
        {
          class: "mdi mdi-message-question-outline",
          name: "message-question-outline",
        },
        {
          class: "mdi mdi-message-reply-outline",
          name: "message-reply-outline",
        },
        {
          class: "mdi mdi-message-reply-text-outline",
          name: "message-reply-text-outline",
        },
        { class: "mdi mdi-movie-check", name: "movie-check" },
        { class: "mdi mdi-movie-check-outline", name: "movie-check-outline" },
        { class: "mdi mdi-movie-cog", name: "movie-cog" },
        { class: "mdi mdi-movie-cog-outline", name: "movie-cog-outline" },
        { class: "mdi mdi-movie-minus", name: "movie-minus" },
        { class: "mdi mdi-movie-minus-outline", name: "movie-minus-outline" },
        { class: "mdi mdi-movie-off", name: "movie-off" },
        { class: "mdi mdi-movie-off-outline", name: "movie-off-outline" },
        { class: "mdi mdi-movie-open-check", name: "movie-open-check" },
        {
          class: "mdi mdi-movie-open-check-outline",
          name: "movie-open-check-outline",
        },
        { class: "mdi mdi-movie-open-cog", name: "movie-open-cog" },
        {
          class: "mdi mdi-movie-open-cog-outline",
          name: "movie-open-cog-outline",
        },
        { class: "mdi mdi-movie-open-edit", name: "movie-open-edit" },
        {
          class: "mdi mdi-movie-open-edit-outline",
          name: "movie-open-edit-outline",
        },
        { class: "mdi mdi-movie-open-minus", name: "movie-open-minus" },
        {
          class: "mdi mdi-movie-open-minus-outline",
          name: "movie-open-minus-outline",
        },
        { class: "mdi mdi-movie-open-off", name: "movie-open-off" },
        {
          class: "mdi mdi-movie-open-off-outline",
          name: "movie-open-off-outline",
        },
        { class: "mdi mdi-movie-open-play", name: "movie-open-play" },
        {
          class: "mdi mdi-movie-open-play-outline",
          name: "movie-open-play-outline",
        },
        { class: "mdi mdi-movie-open-plus", name: "movie-open-plus" },
        {
          class: "mdi mdi-movie-open-plus-outline",
          name: "movie-open-plus-outline",
        },
        { class: "mdi mdi-movie-open-remove", name: "movie-open-remove" },
        {
          class: "mdi mdi-movie-open-remove-outline",
          name: "movie-open-remove-outline",
        },
        { class: "mdi mdi-movie-open-settings", name: "movie-open-settings" },
        {
          class: "mdi mdi-movie-open-settings-outline",
          name: "movie-open-settings-outline",
        },
        { class: "mdi mdi-movie-open-star", name: "movie-open-star" },
        {
          class: "mdi mdi-movie-open-star-outline",
          name: "movie-open-star-outline",
        },
        { class: "mdi mdi-movie-play", name: "movie-play" },
        { class: "mdi mdi-movie-play-outline", name: "movie-play-outline" },
        { class: "mdi mdi-movie-plus", name: "movie-plus" },
        { class: "mdi mdi-movie-plus-outline", name: "movie-plus-outline" },
        { class: "mdi mdi-movie-remove", name: "movie-remove" },
        { class: "mdi mdi-movie-remove-outline", name: "movie-remove-outline" },
        { class: "mdi mdi-movie-settings", name: "movie-settings" },
        {
          class: "mdi mdi-movie-settings-outline",
          name: "movie-settings-outline",
        },
        { class: "mdi mdi-movie-star", name: "movie-star" },
        { class: "mdi mdi-movie-star-outline", name: "movie-star-outline" },
        {
          class: "mdi mdi-projector-screen-outline",
          name: "projector-screen-outline",
        },
        { class: "mdi mdi-robot-happy", name: "robot-happy" },
        { class: "mdi mdi-robot-happy-outline", name: "robot-happy-outline" },
        { class: "mdi mdi-script-text-key", name: "script-text-key" },
        {
          class: "mdi mdi-script-text-key-outline",
          name: "script-text-key-outline",
        },
        { class: "mdi mdi-script-text-play", name: "script-text-play" },
        {
          class: "mdi mdi-script-text-play-outline",
          name: "script-text-play-outline",
        },
        { class: "mdi mdi-star-shooting", name: "star-shooting" },
        {
          class: "mdi mdi-star-shooting-outline",
          name: "star-shooting-outline",
        },
        { class: "mdi mdi-surround-sound-2-1", name: "surround-sound-2-1" },
        { class: "mdi mdi-surround-sound-5-1-2", name: "surround-sound-5-1-2" },
        { class: "mdi mdi-table-picnic", name: "table-picnic" },
        { class: "mdi mdi-tag-arrow-down", name: "tag-arrow-down" },
        {
          class: "mdi mdi-tag-arrow-down-outline",
          name: "tag-arrow-down-outline",
        },
        { class: "mdi mdi-tag-arrow-left", name: "tag-arrow-left" },
        {
          class: "mdi mdi-tag-arrow-left-outline",
          name: "tag-arrow-left-outline",
        },
        { class: "mdi mdi-tag-arrow-right", name: "tag-arrow-right" },
        {
          class: "mdi mdi-tag-arrow-right-outline",
          name: "tag-arrow-right-outline",
        },
        { class: "mdi mdi-tag-arrow-up", name: "tag-arrow-up" },
        { class: "mdi mdi-tag-arrow-up-outline", name: "tag-arrow-up-outline" },
        { class: "mdi mdi-train-car-passenger", name: "train-car-passenger" },
        {
          class: "mdi mdi-train-car-passenger-door",
          name: "train-car-passenger-door",
        },
        {
          class: "mdi mdi-train-car-passenger-door-open",
          name: "train-car-passenger-door-open",
        },
        {
          class: "mdi mdi-train-car-passenger-variant",
          name: "train-car-passenger-variant",
        },
        { class: "mdi mdi-turkey", name: "turkey" },
        { class: "mdi mdi-webcam-off", name: "webcam-off" },
      ],
    };
  },
  methods: {
    toggleMenu() {
      // Implement sidebar toggle logic if needed
    },
  },
};
</script>

<style scoped>
/* You can move styles from main.css or add custom styles here for the icons page */
.icons-wrapper {
  margin-top: 30px;
}
.icons {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.icons > div {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 120px;
  margin-bottom: 20px;
}
.icons i {
  font-size: 32px;
  margin-bottom: 8px;
}
.icons span {
  font-size: 14px;
  color: #333;
}
</style>
