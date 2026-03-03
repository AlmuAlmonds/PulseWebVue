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
            <router-link to="/admin/index"
              ><span class="icon">...</span
              ><span class="text">Dashboard</span></router-link
            >
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
              <span class="icon">...</span><span class="text">Pages</span>
            </a>
            <ul id="ddmenu_2" class="collapse dropdown-nav">
              <li><router-link to="/admin/settings">Settings</router-link></li>
              <li>
                <router-link to="/admin/blank-page">Blank Page</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link to="/admin/invoice"
              ><span class="icon">...</span
              ><span class="text">Invoice</span></router-link
            >
          </li>
          <span class="divider"><hr /></span>
          <li class="nav-item nav-item-has-children">
            <!-- UI Elements -->
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_4"
              aria-controls="ddmenu_4"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon">...</span><span class="text">UI Elements</span>
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
            <!-- Icons -->
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_55"
              aria-controls="#ddmenu_55"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon">...</span><span class="text">Icons</span>
            </a>
            <ul id="ddmenu_55" class="collapse dropdown-nav">
              <li><router-link to="/admin/icons">LineIcons</router-link></li>
              <li>
                <router-link to="/admin/mdi-icons">MDI Icons</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item nav-item-has-children">
            <!-- Forms -->
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_5"
              aria-controls="#ddmenu_5"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon">...</span><span class="text">Forms</span>
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
            <router-link to="/admin/tables"
              ><span class="icon">...</span
              ><span class="text">Tables</span></router-link
            >
          </li>
          <span class="divider"><hr /></span>
          <li class="nav-item active">
            <router-link to="/admin/notification"
              ><span class="icon">...</span
              ><span class="text">Notifications</span></router-link
            >
          </li>
        </ul>
      </nav>
      <div class="promo-box">
        <div class="promo-icon">
          <img
            class="mx-auto"
            src="./assets/images/logo/logo-icon-big.svg"
            alt="Logo"
          />
        </div>
        <h3>Upgrade to PRO</h3>
        <p>
          Improve your development process and start doing more with PlainAdmin
          PRO!
        </p>
        <a
          href="https://plainadmin.com/pro"
          target="_blank"
          rel="nofollow"
          class="main-btn primary-btn btn-hover"
          >Upgrade to PRO</a
        >
      </div>
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
                <!-- Notification Dropdown -->
                <div class="notification-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button">
                    <svg width="22" height="22" viewBox="0 0 22 22">...</svg>
                    <span></span>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end">
                    <li v-for="item in headerNotifications" :key="item.id">
                      <a href="#0">
                        <div class="image"><img :src="item.img" alt="" /></div>
                        <div class="content">
                          <h6>
                            {{ item.title
                            }}<span class="text-regular">{{
                              item.action
                            }}</span>
                          </h6>
                          <p>{{ item.text }}</p>
                          <span>{{ item.time }}</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- Message Dropdown -->
                <div class="header-message-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button">
                    <svg width="22" height="22" viewBox="0 0 22 22">...</svg>
                    <span></span>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end">
                    <li v-for="msg in headerMessages" :key="msg.id">
                      <a href="#0">
                        <div class="image"><img :src="msg.img" alt="" /></div>
                        <div class="content">
                          <h6>{{ msg.name }}</h6>
                          <p>{{ msg.text }}</p>
                          <span>{{ msg.time }}</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- Profile Dropdown -->
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
                      <a href="#0"><i class="lni lni-inbox"></i> Messages</a>
                    </li>
                    <li>
                      <a href="#0"><i class="lni lni-cog"></i> Settings</a>
                    </li>
                    <li class="divider"></li>
                    <li>
                      <a href="#0"><i class="lni lni-exit"></i> Sign Out</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
      <!-- Notification Wrapper -->
      <div class="notification-wrapper">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title"><h2>Notifications</h2></div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/admin/index">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Notifications
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>
          <div class="card-style">
            <div
              v-for="(notification, idx) in notifications"
              :key="idx"
              :class="['single-notification', { readed: notification.read }]"
            >
              <div class="checkbox">
                <div class="form-check checkbox-style mb-20">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    v-model="notification.checked"
                  />
                </div>
              </div>
              <div class="notification">
                <div class="image" :class="notification.bgClass">
                  <span>{{ notification.icon }}</span>
                </div>
                <a href="#0" class="content">
                  <h6>{{ notification.title }}</h6>
                  <p class="text-sm text-gray">{{ notification.text }}</p>
                  <span class="text-sm text-medium text-gray">{{
                    notification.time
                  }}</span>
                </a>
              </div>
              <div class="action">
                <button class="delete-btn" @click="deleteNotification(idx)">
                  <i class="lni lni-trash-can"></i>
                </button>
                <button
                  class="more-btn dropdown-toggle"
                  :id="'moreAction' + idx"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  <i class="lni lni-more-alt"></i>
                </button>
                <ul
                  class="dropdown-menu dropdown-menu-end"
                  :aria-labelledby="'moreAction' + idx"
                >
                  <li class="dropdown-item">
                    <a
                      href="#0"
                      class="text-gray"
                      @click.prevent="markAsRead(idx)"
                      >Mark as Read</a
                    >
                  </li>
                  <li class="dropdown-item">
                    <a href="#0" class="text-gray">Reply</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
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
  name: "notification",
  data() {
    return {
      searchQuery: "",
      headerNotifications: [
        {
          id: 1,
          img: "assets/images/lead/lead-6.png",
          title: "John Doe",
          action: " comment on a product.",
          text: "Lorem ipsum dolor sit amet, consect etur adipiscing elit Vivamus tortor.",
          time: "10 mins ago",
        },
        {
          id: 2,
          img: "assets/images/lead/lead-1.png",
          title: "Jonathon",
          action: " like on a product.",
          text: "Lorem ipsum dolor sit amet, consect etur adipiscing elit Vivamus tortor.",
          time: "10 mins ago",
        },
      ],
      headerMessages: [
        {
          id: 1,
          img: "assets/images/lead/lead-5.png",
          name: "Jacob Jones",
          text: "Hey!I can across your profile and ...",
          time: "10 mins ago",
        },
        {
          id: 2,
          img: "assets/images/lead/lead-3.png",
          name: "John Doe",
          text: "Would you mind please checking out",
          time: "12 mins ago",
        },
        {
          id: 3,
          img: "assets/images/lead/lead-2.png",
          name: "Anee Lee",
          text: "Hey! are you available for freelance?",
          time: "1h ago",
        },
      ],
      notifications: [
        {
          icon: "W",
          title: "Wrapped Bitcoin is now listed on Unity Exchange",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "25 min ago",
          bgClass: "warning-bg",
          checked: false,
          read: false,
        },
        {
          icon: "V",
          title: "Vivamus tortor, odio viverra malesuada sapien dui.",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "30 min ago",
          bgClass: "secondary-bg",
          checked: false,
          read: false,
        },
        {
          icon: "S",
          title: "Srapped Citcoin is now listed on Unity Exchange",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "35 min ago",
          bgClass: "success-bg",
          checked: false,
          read: false,
        },
        {
          icon: "T",
          title: "Trapped Eitcoin is now listed on Unity Exchange",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "25 min ago",
          bgClass: "primary-bg",
          checked: false,
          read: true,
        },
        {
          icon: "U",
          title: "Urapped Bitcoin is now listed on Unity Exchange",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "25 min ago",
          bgClass: "info-bg",
          checked: false,
          read: true,
        },
        {
          icon: "W",
          title: "Wrapped Space is now listed on producthunt",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "25 min ago",
          bgClass: "info-bg",
          checked: false,
          read: true,
        },
        {
          icon: "L",
          title: "Lindy Uikit on trending",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "25 min ago",
          bgClass: "warning-bg",
          checked: false,
          read: true,
        },
        {
          icon: "C",
          title: "Classify is on sell",
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor, odio viverra malesuada sapien dui. Penatibus id amet lectus facilisi tincidunt at non.",
          time: "25 min ago",
          bgClass: "danger-bg",
          checked: false,
          read: false,
        },
      ],
    };
  },
  methods: {
    deleteNotification(idx) {
      this.notifications.splice(idx, 1);
    },
    markAsRead(idx) {
      this.notifications[idx].read = true;
    },
  },
};
</script>

<style scoped>
/* ...existing CSS from main.css and notification page... */
</style>
