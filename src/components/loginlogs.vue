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
          <li class="nav-item active">
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
                    @click="toggleMenu"
                  >
                    <i class="lni lni-chevron-left me-2"></i> Menu
                  </button>
                </div>
                <div class="header-search d-none d-md-flex">
                  <form @submit.prevent>
                    <input
                      type="text"
                      placeholder="Searching"
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
                          <h6>New login detected</h6>
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
                          <h6>Security Alert</h6>
                          <p>Suspicious login attempt detected</p>
                          <span>5 mins ago</span>
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
                  <h2 class="page-title">Security Audit Log</h2>
                  <p class="page-subtitle">
                    Monitor authentication activities and system access for
                    CEDOC emergency response system
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

          <!-- Statistics Cards -->
          <div class="stats-bar">
            <div class="stat-card success">
              <div class="stat-label">✓ Successful Logins</div>
              <div class="stat-value">{{ stats.successful }}</div>
            </div>
            <div class="stat-card failed">
              <div class="stat-label">✕ Failed Attempts</div>
              <div class="stat-value">{{ stats.failed }}</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">👥 Active Users</div>
              <div class="stat-value">{{ stats.active }}</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">⚠️ OTP Verifications</div>
              <div class="stat-value">{{ stats.otp }}</div>
            </div>
          </div>

          <!-- Filter Section -->
          <div class="filter-section">
            <div class="filter-title">Advanced Filters</div>
            <div class="filter-controls">
              <div class="filter-group">
                <label class="filter-label">Role</label>
                <select class="filter-dropdown" v-model="filters.role">
                  <option value="">All Roles</option>
                  <option value="citizen">Citizen</option>
                  <option value="responder">Responder</option>
                  <option value="admin">Admin</option>
                  <option value="dispatch">Dispatch</option>
                </select>
              </div>
              <div class="filter-group">
                <label class="filter-label">Action Type</label>
                <select class="filter-dropdown" v-model="filters.action">
                  <option value="">All Actions</option>
                  <option value="login">Login</option>
                  <option value="logout">Logout</option>
                  <option value="failed">Failed Login</option>
                  <option value="otp">OTP Verification</option>
                </select>
              </div>
              <div class="filter-group">
                <label class="filter-label">Status</label>
                <select class="filter-dropdown" v-model="filters.status">
                  <option value="">All Status</option>
                  <option value="success">Success</option>
                  <option value="failed">Failed</option>
                </select>
              </div>
              <div class="filter-group">
                <label class="filter-label">Date Range</label>
                <select class="filter-dropdown" v-model="filters.date">
                  <option value="">All Time</option>
                  <option value="today">Today</option>
                  <option value="7days">Last 7 Days</option>
                  <option value="30days">Last 30 Days</option>
                  <option value="90days">Last 90 Days</option>
                </select>
              </div>
              <div class="filter-actions">
                <button class="btn-filter" @click="applyFilters">
                  Apply Filters
                </button>
                <button class="btn-reset" @click="resetFilters">Reset</button>
              </div>
            </div>

            <!-- Audit Log Table -->
            <div class="table-responsive mt-4">
              <table class="audit-table">
                <thead>
                  <tr>
                    <th>Log ID</th>
                    <th>User Name</th>
                    <th>Role</th>
                    <th>Action Type</th>
                    <th>IP Address</th>
                    <th>Device Type</th>
                    <th>Date & Time</th>
                    <th>Status</th>
                    <th>Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="log in filteredLogs" :key="log.id">
                    <td>
                      <strong>{{ log.id }}</strong>
                    </td>
                    <td>{{ log.user }}</td>
                    <td>
                      <span :class="['role-badge', roleClass(log.role)]">{{
                        log.role
                      }}</span>
                    </td>
                    <td>
                      <span
                        :class="['action-badge', actionClass(log.action)]"
                        >{{ log.action }}</span
                      >
                    </td>
                    <td>{{ log.ip }}</td>
                    <td>
                      <span :class="deviceClass(log.device)">{{
                        log.device
                      }}</span>
                    </td>
                    <td>{{ log.timestamp }}</td>
                    <td>
                      <span :class="statusClass(log.status)">{{
                        log.status
                      }}</span>
                    </td>
                    <td>
                      <button
                        class="btn-details"
                        title="View Details"
                        @click="viewDetails(log.id)"
                      >
                        <i class="lni lni-eye"></i>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
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
                <p class="text-sm">PULSE Admin Dashboard</p>
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

    <!-- Accessibility FAB and Panel -->
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
  name: "loginlogs",
  data() {
    return {
      searchQuery: "",
      liveTime: "",
      stats: {
        successful: 284,
        failed: 12,
        active: 47,
        otp: 156,
      },
      filters: {
        role: "",
        action: "",
        status: "",
        date: "",
      },
      logs: [
        {
          id: "LOG-001",
          user: "Maria Santos",
          role: "Admin",
          action: "Login",
          ip: "192.168.1.50",
          device: "Desktop",
          timestamp: "Feb 7, 2026 | 14:32:15",
          status: "Success",
        },
        {
          id: "LOG-002",
          user: "Juan Dela Cruz",
          role: "Responder",
          action: "OTP Verification",
          ip: "192.168.1.100",
          device: "Mobile",
          timestamp: "Feb 7, 2026 | 14:28:45",
          status: "Success",
        },
        {
          id: "LOG-003",
          user: "Unknown User",
          role: "Citizen",
          action: "Failed Login",
          ip: "203.45.67.89",
          device: "Desktop",
          timestamp: "Feb 7, 2026 | 14:15:32",
          status: "Failed",
        },
        {
          id: "LOG-004",
          user: "Pedro Reyes",
          role: "Responder",
          action: "Logout",
          ip: "192.168.2.75",
          device: "Mobile",
          timestamp: "Feb 7, 2026 | 13:45:20",
          status: "Success",
        },
        {
          id: "LOG-005",
          user: "Ana Garcia",
          role: "Dispatch",
          action: "Login",
          ip: "192.168.3.120",
          device: "Desktop",
          timestamp: "Feb 7, 2026 | 13:20:18",
          status: "Success",
        },
        {
          id: "LOG-006",
          user: "Unknown User",
          role: "Citizen",
          action: "Failed Login",
          ip: "210.78.95.45",
          device: "Mobile",
          timestamp: "Feb 7, 2026 | 12:55:42",
          status: "Failed",
        },
        {
          id: "LOG-007",
          user: "Carlos Mendoza",
          role: "Admin",
          action: "Login",
          ip: "192.168.1.75",
          device: "Desktop",
          timestamp: "Feb 7, 2026 | 12:30:05",
          status: "Success",
        },
        {
          id: "LOG-008",
          user: "Rosa Martina",
          role: "Responder",
          action: "OTP Verification",
          ip: "192.168.4.88",
          device: "Mobile",
          timestamp: "Feb 6, 2026 | 22:15:33",
          status: "Success",
        },
        {
          id: "LOG-009",
          user: "Diego Santos",
          role: "Dispatch",
          action: "Logout",
          ip: "192.168.5.42",
          device: "Desktop",
          timestamp: "Feb 6, 2026 | 18:45:22",
          status: "Success",
        },
        {
          id: "LOG-010",
          user: "Lisa Fernandez",
          role: "Citizen",
          action: "Login",
          ip: "192.168.6.19",
          device: "Mobile",
          timestamp: "Feb 6, 2026 | 16:20:10",
          status: "Success",
        },
      ],
    };
  },
  computed: {
    filteredLogs() {
      return this.logs.filter((log) => {
        let show = true;
        if (
          this.filters.role &&
          log.role.toLowerCase() !== this.filters.role.toLowerCase()
        )
          show = false;
        if (
          this.filters.action &&
          log.action
            .toLowerCase()
            .indexOf(this.filters.action.toLowerCase()) === -1
        )
          show = false;
        if (
          this.filters.status &&
          log.status.toLowerCase() !== this.filters.status.toLowerCase()
        )
          show = false;
        // Date filter can be implemented with actual date parsing if needed
        return show;
      });
    },
  },
  methods: {
    toggleMenu() {
      // Implement sidebar toggle logic if needed
    },
    refreshPage() {
      window.location.reload();
    },
    signOut() {
      this.$router.push("/");
    },
    applyFilters() {
      if (this.filteredLogs.length === 0) {
        alert("No records match the selected filters.");
      } else {
        alert(
          `Showing ${this.filteredLogs.length} record(s) matching your filters.`,
        );
      }
    },
    resetFilters() {
      this.filters = { role: "", action: "", status: "", date: "" };
      alert("Filters have been reset. Showing all records.");
    },
    viewDetails(logId) {
      const details = {
        "LOG-001": {
          user: "Maria Santos",
          role: "Admin",
          action: "Login",
          status: "Success",
          ip: "192.168.1.50",
          device: "Desktop",
          timestamp: "Feb 7, 2026 14:32:15",
          browser: "Chrome 118.0",
          location: "San Juan City, Metro Manila",
        },
        "LOG-002": {
          user: "Juan Dela Cruz",
          role: "Responder",
          action: "OTP Verification",
          status: "Success",
          ip: "192.168.1.100",
          device: "Mobile",
          timestamp: "Feb 7, 2026 14:28:45",
          browser: "Safari Mobile",
          location: "Quezon City, Metro Manila",
        },
        "LOG-003": {
          user: "Unknown User",
          role: "Citizen",
          action: "Failed Login",
          status: "Failed",
          ip: "203.45.67.89",
          device: "Desktop",
          timestamp: "Feb 7, 2026 14:15:32",
          browser: "Firefox 121.0",
          location: "Unknown Location",
          error: "Invalid credentials",
        },
      };
      const detail = details[logId];
      if (detail) {
        let message = `Log ID: ${logId}\n\nUser: ${detail.user}\nRole: ${detail.role}\nAction: ${detail.action}\nStatus: ${detail.status}\nIP Address: ${detail.ip}\nDevice: ${detail.device}\nTimestamp: ${detail.timestamp}\nBrowser: ${detail.browser}\nLocation: ${detail.location}`;
        if (detail.error) {
          message += `\n\nError: ${detail.error}`;
        }
        alert(message);
      } else {
        alert(
          `Details for ${logId} - Full security audit trail available in detailed view.`,
        );
      }
    },
    roleClass(role) {
      switch (role.toLowerCase()) {
        case "citizen":
          return "role-citizen";
        case "responder":
          return "role-responder";
        case "admin":
          return "role-admin";
        case "dispatch":
          return "role-dispatch";
        default:
          return "";
      }
    },
    actionClass(action) {
      if (action.toLowerCase().includes("login")) return "action-login";
      if (action.toLowerCase().includes("logout")) return "action-logout";
      if (action.toLowerCase().includes("failed")) return "action-failed";
      if (action.toLowerCase().includes("otp")) return "action-otp";
      return "";
    },
    statusClass(status) {
      if (status.toLowerCase() === "success") return "status-success";
      if (status.toLowerCase() === "failed") return "status-failed";
      return "";
    },
    deviceClass(device) {
      if (device.toLowerCase() === "mobile") return "device-mobile";
      if (device.toLowerCase() === "desktop") return "device-desktop";
      return "";
    },
  },
  mounted() {
    this.updateLiveTime();
    setInterval(this.updateLiveTime, 1000);
  },
  methods: {
    ...this.methods,
    updateLiveTime() {
      const now = new Date();
      const hours = now.getHours();
      const minutes = String(now.getMinutes()).padStart(2, "0");
      const seconds = String(now.getSeconds()).padStart(2, "0");
      const ampm = hours >= 12 ? "PM" : "AM";
      const displayHours = String(hours % 12 || 12).padStart(2, "0");
      this.liveTime = `${displayHours}:${minutes}:${seconds} ${ampm}`;
    },
  },
};
</script>

<style scoped>
/* Place all styles from <style> in the original file here */
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
.page-title {
  font-size: 28px;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 8px;
}
.page-subtitle {
  font-size: 14px;
  color: #666;
  margin-bottom: 25px;
}
.filter-section {
  background: white;
  border-radius: 12px;
  padding: 25px 30px;
  margin-bottom: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}
.filter-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.filter-title::before {
  content: "⚙️";
  font-size: 18px;
}
.filter-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  align-items: end;
}
.filter-group {
  display: flex;
  flex-direction: column;
}
.filter-label {
  font-size: 13px;
  font-weight: 600;
  color: #666;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.filter-dropdown {
  background: white;
  color: #333;
  border: 1.5px solid #e0e7ff;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='%23365CF5'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 35px;
  transition: all 0.3s ease;
}
.filter-dropdown:hover {
  border-color: #365cf5;
  background-color: #f5f8fc;
}
.filter-dropdown:focus {
  outline: none;
  border-color: #365cf5;
  box-shadow: 0 0 0 3px rgba(54, 92, 245, 0.1);
}
.filter-actions {
  display: flex;
  gap: 10px;
}
.btn-filter {
  background: #365cf5;
  color: white;
  border: none;
  padding: 12px 28px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 100px;
}
.btn-filter:hover {
  background: #254dbd;
  box-shadow: 0 4px 12px rgba(54, 92, 245, 0.3);
}
.btn-reset {
  background: #e0e7ff;
  color: #365cf5;
  border: none;
  padding: 12px 28px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}
.btn-reset:hover {
  background: #d0deff;
}
.audit-table-wrapper {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}
.audit-table {
  width: 100%;
  border-collapse: collapse;
}
.audit-table th {
  background: linear-gradient(135deg, #f5f7fa 0%, #f0f4f8 100%);
  font-weight: 700;
  font-size: 12px;
  color: #1a1a2e;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 16px 18px;
  border-bottom: 2px solid #e0e7ff;
}
.audit-table td {
  padding: 16px 18px;
  vertical-align: middle;
  border-bottom: 1px solid #f0f0f0;
  font-size: 14px;
  color: #333;
}
.audit-table tbody tr {
  transition: all 0.2s ease;
}
.audit-table tbody tr:hover {
  background: #f8faff;
}
.role-badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.role-citizen {
  background: #e3f2fd;
  color: #1976d2;
}
.role-responder {
  background: #fff3e0;
  color: #f57c00;
}
.role-admin {
  background: #f3e5f5;
  color: #7b1fa2;
}
.role-dispatch {
  background: #e8f5e9;
  color: #388e3c;
}
.action-badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
}
.action-login {
  background: #c8e6c9;
  color: #1b5e20;
}
.action-logout {
  background: #b3e5fc;
  color: #01579b;
}
.action-failed {
  background: #ffcdd2;
  color: #b71c1c;
}
.action-otp {
  background: #ffe0b2;
  color: #e65100;
}
.status-success {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #27ae60;
  font-weight: 600;
}
.status-success::before {
  content: "✓";
  display: inline-block;
  width: 20px;
  height: 20px;
  background: #d4edda;
  border-radius: 50%;
  text-align: center;
  line-height: 20px;
  font-size: 12px;
}
.status-failed {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #dc3545;
  font-weight: 600;
}
.status-failed::before {
  content: "✕";
  display: inline-block;
  width: 20px;
  height: 20px;
  background: #f8d7da;
  border-radius: 50%;
  text-align: center;
  line-height: 20px;
  font-size: 12px;
}
.btn-details {
  color: #365cf5;
  font-size: 16px;
  cursor: pointer;
  background: none;
  border: none;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
}
.btn-details:hover {
  background: #f5f8fc;
  color: #254dbd;
}
.device-mobile::before {
  content: "📱 ";
}
.device-desktop::before {
  content: "🖥️ ";
}
.stats-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}
.stat-card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  border-left: 4px solid #365cf5;
}
.stat-card.success {
  border-left-color: #27ae60;
}
.stat-card.failed {
  border-left-color: #dc3545;
}
.stat-label {
  font-size: 12px;
  color: #666;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.stat-value {
  font-size: 28px;
  font-weight: 700;
  color: #1a1a2e;
}
.table-responsive {
  overflow-x: auto;
}
</style>
