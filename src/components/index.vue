<template>
  <div>
    <!-- Preloader -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>
    <!-- Sidebar Navigation -->
    <aside class="sidebar-nav-wrapper">
      <div class="navbar-logo">
        <router-link to="/admin/index">
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
          <li class="nav-item active">
            <router-link to="/admin/index">
              <span class="icon">
                <!-- ...SVG... -->
              </span>
              <span class="text">Dashboard</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/admin/accounts">
              <span class="icon">
                <!-- ...SVG... -->
              </span>
              <span class="text">User Management</span>
            </router-link>
          </li>
          <li class="nav-item" style="margin-bottom: 15px">
            <router-link to="/admin/news-events">
              <span class="icon">
                <!-- ...SVG... -->
              </span>
              <span class="text">News & Events</span>
            </router-link>
          </li>
          <li class="nav-item" style="pointer-events: none; margin-top: 10px">
            <span
              style="
                display: flex;
                align-items: center;
                padding: 12px 20px;
                color: #ffc107;
                font-weight: 600;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 1px;
              "
            >
              <span class="icon" style="margin-right: 10px">
                <!-- ...SVG... -->
              </span>
              Security
            </span>
          </li>
          <li class="nav-item">
            <router-link to="/admin/loginlogs">
              <span class="icon">
                <!-- ...SVG... -->
              </span>
              <span class="text">Logs</span>
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
                  <button
                    class="dropdown-toggle"
                    type="button"
                    id="notification"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
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
                  <ul
                    class="dropdown-menu dropdown-menu-end"
                    aria-labelledby="notification"
                  >
                    <li v-for="(note, i) in notifications" :key="i">
                      <a href="#0">
                        <div class="image">
                          <img :src="note.img" alt="" />
                        </div>
                        <div class="content">
                          <h6>
                            {{ note.name }}
                            <span class="text-regular">{{ note.action }}</span>
                          </h6>
                          <p>{{ note.text }}</p>
                          <span>{{ note.time }}</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- Message -->
                <div class="header-message-box ml-15 d-none d-md-flex">
                  <button
                    class="dropdown-toggle"
                    type="button"
                    id="message"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
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
                  <ul
                    class="dropdown-menu dropdown-menu-end"
                    aria-labelledby="message"
                  >
                    <li v-for="(msg, i) in messages" :key="i">
                      <a href="#0">
                        <div class="image">
                          <img :src="msg.img" alt="" />
                        </div>
                        <div class="content">
                          <h6>{{ msg.name }}</h6>
                          <p>{{ msg.text }}</p>
                          <span>{{ msg.time }}</span>
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
                    id="profile"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
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
                  <ul
                    class="dropdown-menu dropdown-menu-end"
                    aria-labelledby="profile"
                  >
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
                      <a href="#0">
                        <i class="lni lni-user"></i> View Profile
                      </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                      <a href="#0" @click.prevent="signOut">
                        <i class="lni lni-exit"></i> Sign Out
                      </a>
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
                  <h2>PULSE System Analytics</h2>
                  <p class="text-sm text-gray" style="margin-top: 6px">
                    Real-time research evaluation and system performance metrics
                  </p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="header-actions">
                  <span class="time-display" id="liveTime">{{ liveTime }}</span>
                  <button
                    class="btn-refresh-icon"
                    @click="refreshPage"
                    title="Refresh"
                  >
                    <i class="lni lni-reload"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
          <!-- Analytics Cards -->
          <div class="row">
            <div
              class="col-xl-3 col-lg-4 col-sm-6"
              v-for="(card, i) in analyticsCards"
              :key="i"
            >
              <div class="icon-card mb-30">
                <div class="icon" :style="{ background: card.bg }">
                  <i :class="card.icon" :style="{ color: card.color }"></i>
                </div>
                <div class="content">
                  <h6 class="mb-10">{{ card.title }}</h6>
                  <h3 class="text-bold mb-10">{{ card.value }}</h3>
                  <p class="text-sm" :style="{ color: card.color }">
                    <i :class="card.trendIcon"></i> {{ card.trendText }}
                  </p>
                </div>
              </div>
            </div>
          </div>
          <!-- Emergency Reports & Incidents -->
          <div class="row">
            <div class="col-lg-6">
              <div class="card-style mb-30">
                <div
                  class="title d-flex justify-content-between align-items-center"
                >
                  <h6 class="text-medium mb-0">
                    <i
                      class="lni lni-alarm"
                      style="margin-right: 8px; color: #e74c3c"
                    ></i
                    >Total Emergency Reports
                  </h6>
                  <select v-model="reportPeriod" class="form-select">
                    <option>Yearly</option>
                    <option>Monthly</option>
                    <option>Weekly</option>
                  </select>
                </div>
                <div style="margin-top: 20px">
                  <h3
                    class="text-bold"
                    style="font-size: 32px; margin-bottom: 5px"
                  >
                    2,847
                  </h3>
                  <p style="color: #666; font-size: 14px; margin-bottom: 20px">
                    Reports this year (2026)
                  </p>
                </div>
                <div class="chart">
                  <canvas
                    id="Chart1"
                    style="width: 100%; height: 300px; margin-left: -35px"
                  ></canvas>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="card-style mb-30">
                <div
                  class="title d-flex justify-content-between align-items-center"
                >
                  <h6 class="text-medium mb-0">
                    <i
                      class="lni lni-alert"
                      style="margin-right: 8px; color: #fd7e14"
                    ></i
                    >Active Incidents
                  </h6>
                  <span
                    style="
                      background: #e74c3c;
                      color: white;
                      padding: 4px 10px;
                      border-radius: 4px;
                      font-size: 11px;
                      font-weight: 600;
                    "
                    >LIVE</span
                  >
                </div>
                <div style="margin-top: 20px">
                  <h3
                    class="text-bold"
                    style="font-size: 32px; margin-bottom: 5px"
                  >
                    47
                  </h3>
                  <p style="color: #666; font-size: 14px; margin-bottom: 20px">
                    Currently being handled
                  </p>
                </div>
                <div
                  class="d-flex flex-column gap-2"
                  style="margin-bottom: 20px"
                >
                  <div
                    v-for="(incident, i) in incidents"
                    :key="i"
                    :style="incident.style"
                  >
                    <div style="display: flex; align-items: center; gap: 12px">
                      <span :style="incident.dotStyle"></span>
                      <span style="font-size: 14px; color: #333">{{
                        incident.label
                      }}</span>
                    </div>
                    <span :style="incident.countStyle">{{
                      incident.count
                    }}</span>
                  </div>
                </div>
                <div
                  class="chart"
                  style="display: flex; justify-content: center"
                >
                  <canvas
                    id="Chart2"
                    style="width: 220px; height: 220px"
                  ></canvas>
                </div>
              </div>
            </div>
          </div>
          <!-- Incident Categories & Peak Usage Times -->
          <div class="row">
            <div class="col-lg-6">
              <div class="card-style mb-30">
                <div
                  class="title d-flex justify-content-between align-items-center"
                >
                  <h6 class="text-medium mb-0">
                    <i
                      class="lni lni-pie-chart"
                      style="margin-right: 8px; color: #9b59b6"
                    ></i
                    >Incident Categories
                  </h6>
                  <select v-model="categoryPeriod" class="form-select">
                    <option>This Year</option>
                    <option>Last Year</option>
                    <option>All Time</option>
                  </select>
                </div>
                <p
                  style="
                    color: #666;
                    font-size: 14px;
                    margin-top: 10px;
                    margin-bottom: 20px;
                  "
                >
                  Breakdown by type this year
                </p>
                <div class="d-flex align-items-center" style="gap: 20px">
                  <div class="chart" style="flex: 1; max-width: 160px">
                    <canvas
                      id="Chart3"
                      style="width: 100%; height: 160px"
                    ></canvas>
                  </div>
                  <div style="flex: 1">
                    <ul style="list-style: none; padding: 0; margin: 0">
                      <li
                        v-for="(cat, i) in categories"
                        :key="i"
                        style="margin-bottom: 12px"
                      >
                        <div
                          class="d-flex justify-content-between align-items-center"
                        >
                          <div class="d-flex align-items-center">
                            <span :style="cat.dotStyle"></span>
                            <span style="font-size: 13px; color: #333">{{
                              cat.label
                            }}</span>
                          </div>
                          <span :style="cat.countStyle">{{ cat.count }}</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="card-style mb-30">
                <div class="title">
                  <h6 class="text-medium mb-15">
                    <i
                      class="lni lni-timer"
                      style="margin-right: 8px; color: #fd7e14"
                    ></i
                    >Peak Usage Times (Last 30 Days)
                  </h6>
                </div>
                <div class="chart">
                  <canvas
                    id="Chart4"
                    style="width: 100%; height: 300px; margin-left: -35px"
                  ></canvas>
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
                <p class="text-sm">PULSE CEDOC Administration Panel</p>
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
    <!-- Accessibility FAB & Panel -->
    <button
      id="a11yFab"
      class="a11y-fab"
      title="Accessibility Settings"
      aria-label="Open Accessibility Settings"
    >
      <!-- ...SVG... -->
    </button>
    <div id="a11yOverlay" class="a11y-overlay"></div>
    <div
      id="a11yPanel"
      class="a11y-panel"
      role="dialog"
      aria-label="Accessibility Settings"
    >
      <!-- ...Accessibility Panel Content... -->
    </div>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      searchQuery: "",
      liveTime: "",
      reportPeriod: "Yearly",
      categoryPeriod: "This Year",
      notifications: [
        {
          name: "John Doe",
          action: "comment on a product.",
          text: "Lorem ipsum dolor sit amet, consect etur adipiscing elit Vivamus tortor.",
          time: "10 mins ago",
          img: "assets/images/lead/lead-6.png",
        },
        {
          name: "Jonathon",
          action: "like on a product.",
          text: "Lorem ipsum dolor sit amet, consect etur adipiscing elit Vivamus tortor.",
          time: "10 mins ago",
          img: "assets/images/lead/lead-1.png",
        },
      ],
      messages: [
        {
          name: "Jacob Jones",
          text: "Hey!I can across your profile and ...",
          time: "10 mins ago",
          img: "assets/images/lead/lead-5.png",
        },
        {
          name: "John Doe",
          text: "Would you mind please checking out",
          time: "12 mins ago",
          img: "assets/images/lead/lead-3.png",
        },
        {
          name: "Anee Lee",
          text: "Hey! are you available for freelance?",
          time: "1h ago",
          img: "assets/images/lead/lead-2.png",
        },
      ],
      analyticsCards: [
        {
          title: "Total Users",
          value: "2,847",
          icon: "lni lni-users",
          color: "#0dcaf0",
          bg: "#e8f4fd",
          trendIcon: "lni lni-trending-up",
          trendText: "12% growth this month",
        },
        {
          title: "Active Users (Last 30d)",
          value: "1,923",
          icon: "lni lni-checkmark-circle",
          color: "#27ae60",
          bg: "#e8f8f5",
          trendIcon: "lni lni-arrow-up",
          trendText: "67.6% engagement rate",
        },
        {
          title: "New Registrations",
          value: "324",
          icon: "lni lni-user-add",
          color: "#fd7e14",
          bg: "#fff3e0",
          trendIcon: "lni lni-alert",
          trendText: "This month",
        },
        {
          title: "Total Reports",
          value: "5,246",
          icon: "lni lni-alarm",
          color: "#e74c3c",
          bg: "#fdeaea",
          trendIcon: "lni lni-arrow-up",
          trendText: "All-time aggregate",
        },
      ],
      incidents: [
        {
          label: "Open",
          count: 18,
          style: {
            padding: "12px",
            background: "#fff3e0",
            borderRadius: "8px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          },
          dotStyle: {
            width: "12px",
            height: "12px",
            background: "#fd7e14",
            borderRadius: "50%",
          },
          countStyle: { fontWeight: "600", color: "#fd7e14", fontSize: "16px" },
        },
        {
          label: "In-Progress",
          count: 21,
          style: {
            padding: "12px",
            background: "#e8f4fd",
            borderRadius: "8px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          },
          dotStyle: {
            width: "12px",
            height: "12px",
            background: "#3498db",
            borderRadius: "50%",
          },
          countStyle: { fontWeight: "600", color: "#3498db", fontSize: "16px" },
        },
        {
          label: "Resolved Today",
          count: 8,
          style: {
            padding: "12px",
            background: "#e8f8f5",
            borderRadius: "8px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          },
          dotStyle: {
            width: "12px",
            height: "12px",
            background: "#27ae60",
            borderRadius: "50%",
          },
          countStyle: { fontWeight: "600", color: "#27ae60", fontSize: "16px" },
        },
      ],
      categories: [
        {
          label: "Medical",
          count: 892,
          dotStyle: {
            width: "10px",
            height: "10px",
            background: "#e74c3c",
            borderRadius: "2px",
            marginRight: "8px",
          },
          countStyle: { fontWeight: "600", color: "#e74c3c", fontSize: "13px" },
        },
        {
          label: "Fire",
          count: 423,
          dotStyle: {
            width: "10px",
            height: "10px",
            background: "#fd7e14",
            borderRadius: "2px",
            marginRight: "8px",
          },
          countStyle: { fontWeight: "600", color: "#fd7e14", fontSize: "13px" },
        },
        {
          label: "Crime",
          count: 756,
          dotStyle: {
            width: "10px",
            height: "10px",
            background: "#3498db",
            borderRadius: "2px",
            marginRight: "8px",
          },
          countStyle: { fontWeight: "600", color: "#3498db", fontSize: "13px" },
        },
        {
          label: "Disaster",
          count: 198,
          dotStyle: {
            width: "10px",
            height: "10px",
            background: "#9b59b6",
            borderRadius: "2px",
            marginRight: "8px",
          },
          countStyle: { fontWeight: "600", color: "#9b59b6", fontSize: "13px" },
        },
        {
          label: "Rescue",
          count: 578,
          dotStyle: {
            width: "10px",
            height: "10px",
            background: "#1abc9c",
            borderRadius: "2px",
            marginRight: "8px",
          },
          countStyle: { fontWeight: "600", color: "#1abc9c", fontSize: "13px" },
        },
      ],
    };
  },
  mounted() {
    this.updateLiveTime();
    setInterval(this.updateLiveTime, 1000);
    // Chart.js initialization can be done here
  },
  methods: {
    updateLiveTime() {
      const now = new Date();
      const hours = now.getHours();
      const minutes = String(now.getMinutes()).padStart(2, "0");
      const seconds = String(now.getSeconds()).padStart(2, "0");
      const ampm = hours >= 12 ? "PM" : "AM";
      const displayHours = String(hours % 12 || 12).padStart(2, "0");
      this.liveTime = `${displayHours}:${minutes}:${seconds} ${ampm}`;
    },
    refreshPage() {
      window.location.reload();
    },
    signOut() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.header-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
}
.time-display {
  font-size: 14px;
  color: #6b7280;
  font-weight: 500;
  white-space: nowrap;
}
.btn-refresh-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.btn-refresh-icon:hover {
  background: #f3f4f6;
}
</style>
