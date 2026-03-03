<template>
  <div>
    <!-- ======== Preloader =========== -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>
    <!-- ======== sidebar-nav start =========== -->
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
          <li class="nav-item">
            <router-link to="/admin/index">
              <span class="icon"
                ><svg width="20" height="20" viewBox="0 0 24 24">
                  <path
                    d="M4 13H10C10.55 13 11 12.55 11 12V4C11 3.45 10.55 3 10 3H4C3.45 3 3 3.45 3 4V12C3 12.55 3.45 13 4 13ZM4 21H10C10.55 21 11 20.55 11 20V16C11 15.45 10.55 15 10 15H4C3.45 15 3 15.45 3 16V20C3 20.55 3.45 21 4 21ZM14 21H20C20.55 21 21 20.55 21 20V12C21 11.45 20.55 11 20 11H14C13.45 11 13 11.45 13 12V20C13 20.55 13.45 21 14 21ZM13 4V8C13 8.55 13.45 9 14 9H20C20.55 9 21 8.55 21 8V4C21 3.45 20.55 3 20 3H14C13.45 3 13 3.45 13 4Z"
                    fill="currentColor"
                  /></svg
              ></span>
              <span class="text">Dashboard</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/admin/accounts">
              <span class="icon"
                ><svg width="20" height="20" viewBox="0 0 24 24">
                  <path
                    d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V19C4 19.55 4.45 20 5 20H19C19.55 20 20 19.55 20 19V18C20 15.34 14.67 14 12 14Z"
                    fill="currentColor"
                  /></svg
              ></span>
              <span class="text">User Management</span>
            </router-link>
          </li>
          <li class="nav-item active" style="margin-bottom: 15px">
            <router-link to="/admin/news-events">
              <span class="icon"
                ><svg width="20" height="20" viewBox="0 0 24 24">
                  <path
                    d="M20 3H4C2.9 3 2 3.9 2 5V19C2 20.1 2.9 21 4 21H20C21.1 21 22 20.1 22 19V5C22 3.9 21.1 3 20 3ZM5 7H10V13H5V7ZM19 17H5V15H19V17ZM19 13H12V11H19V13ZM19 9H12V7H19V9Z"
                    fill="currentColor"
                  /></svg
              ></span>
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
              <span class="icon" style="margin-right: 10px"
                ><svg width="20" height="20" viewBox="0 0 24 24">
                  <path
                    d="M12 1L3 5V11C3 16.55 6.84 21.74 12 23C17.16 21.74 21 16.55 21 11V5L12 1ZM12 11.99H19C18.47 16.11 15.72 19.78 12 20.93V12H5V6.3L12 3.19V11.99Z"
                    fill="#ffc107"
                  /></svg
              ></span>
              Security
            </span>
          </li>
          <li class="nav-item">
            <router-link to="/admin/loginlogs">
              <span class="icon"
                ><svg width="20" height="20" viewBox="0 0 24 24">
                  <path
                    d="M11.99 2C6.47 2 2 6.48 2 12C2 17.52 6.47 22 11.99 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 11.99 2ZM12 20C7.58 20 4 16.42 4 12C4 7.58 7.58 4 12 4C16.42 4 20 7.58 20 12C20 16.42 16.42 20 12 20ZM12.5 7H11V13L16.25 16.15L17 14.92L12.5 12.25V7Z"
                    fill="currentColor"
                  /></svg
              ></span>
              <span class="text">Logs</span>
            </router-link>
          </li>
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>
    <!-- ======== main-wrapper start =========== -->
    <main class="main-wrapper">
      <!-- ========== header start ========== -->
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
                    <input type="text" placeholder="Search for something" />
                    <button><i class="lni lni-search-alt"></i></button>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-lg-7 col-md-7 col-6">
              <div class="header-right">
                <!-- notification start -->
                <div class="notification-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button">
                    <svg width="22" height="22" viewBox="0 0 22 22">
                      <path
                        d="M11 20.1667C9.88317 20.1667 8.88718 19.63 8.23901 18.7917H13.761C13.113 19.63 12.1169 20.1667 11 20.1667Z"
                      />
                      <path
                        d="M10.1157 2.74999C10.1157 2.24374 10.5117 1.83333 11 1.83333C11.4883 1.83333 11.8842 2.24374 11.8842 2.74999V2.82604C14.3932 3.26245 16.3051 5.52474 16.3051 8.24999V14.287C16.3051 14.5301 16.3982 14.7633 16.564 14.9352L18.2029 16.6342C18.4814 16.9229 18.2842 17.4167 17.8903 17.4167H4.10961C3.71574 17.4167 3.5185 16.9229 3.797 16.6342L5.43589 14.9352C5.6017 14.7633 5.69485 14.5301 5.69485 14.287V8.24999C5.69485 5.52474 7.60672 3.26245 10.1157 2.82604V2.74999Z"
                      />
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
                          <h6>New event posted</h6>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- notification end -->
                <!-- message start -->
                <div class="header-message-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button">
                    <svg width="22" height="22" viewBox="0 0 22 22">
                      <path
                        d="M7.74866 5.97421C7.91444 5.96367 8.08162 5.95833 8.25005 5.95833C12.5532 5.95833 16.0417 9.4468 16.0417 13.75C16.0417 13.9184 16.0364 14.0856 16.0259 14.2514C16.3246 14.138 16.6127 14.003 16.8883 13.8482L19.2306 14.629C19.7858 14.8141 20.3141 14.2858 20.129 13.7306L19.3482 11.3882C19.8694 10.4604 20.1667 9.38996 20.1667 8.25C20.1667 4.70617 17.2939 1.83333 13.75 1.83333C11.0077 1.83333 8.66702 3.55376 7.74866 5.97421Z"
                      />
                      <path
                        d="M14.6667 13.75C14.6667 17.2938 11.7939 20.1667 8.25004 20.1667C7.11011 20.1667 6.03962 19.8694 5.11182 19.3482L2.76946 20.129C2.21421 20.3141 1.68597 19.7858 1.87105 19.2306L2.65184 16.8882C2.13062 15.9604 1.83338 14.89 1.83338 13.75C1.83338 10.2062 4.70622 7.33333 8.25004 7.33333C11.7939 7.33333 14.6667 10.2062 14.6667 13.75ZM5.95838 13.75C5.95838 13.2437 5.54797 12.8333 5.04171 12.8333C4.53545 12.8333 4.12504 13.2437 4.12504 13.75C4.12504 14.2563 4.53545 14.6667 5.04171 14.6667C5.54797 14.6667 5.95838 14.2563 5.95838 13.75ZM9.16671 13.75C9.16671 13.2437 8.7563 12.8333 8.25004 12.8333C7.74379 12.8333 7.33338 13.2437 7.33338 13.75C7.33338 14.2563 7.74379 14.6667 8.25004 14.6667C8.7563 14.6667 9.16671 14.2563 9.16671 13.75ZM11.4584 14.6667C11.9647 14.6667 12.375 14.2563 12.375 13.75C12.375 13.2437 11.9647 12.8333 11.4584 12.8333C10.9521 12.8333 10.5417 13.2437 10.5417 13.75C10.5417 14.2563 10.9521 14.6667 11.4584 14.6667Z"
                      />
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
                          <p>News article approved</p>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- message end -->
                <!-- profile start -->
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
                    <li class="divider"></li>
                    <li>
                      <a href="#0" @click.prevent="$router.push('/')"
                        ><i class="lni lni-exit"></i> Sign Out</a
                      >
                    </li>
                  </ul>
                </div>
                <!-- profile end -->
              </div>
            </div>
          </div>
        </div>
      </header>
      <!-- ========== section start ========== -->
      <section class="section">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Public Advisory & Emergency Bulletin Board</h2>
                  <p style="color: #666; font-size: 14px; margin-top: 5px">
                    Real-time alerts, safety notices, and emergency
                    announcements for San Juan CEDOC
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
          <div class="filter-buttons" style="margin-bottom: 25px">
            <button
              type="button"
              id="btnActive"
              class="filter-badge"
              :class="{ active: activeSection === 'active' }"
              @click="switchSection('active')"
            >
              <i class="lni lni-check-circle"></i> Active Advisories
            </button>
            <button
              type="button"
              id="btnAll"
              class="filter-badge"
              :class="{ active: activeSection === 'all' }"
              @click="switchSection('all')"
            >
              <i class="lni lni-list"></i> All Advisories
            </button>
            <button
              type="button"
              id="btnExpired"
              class="filter-badge"
              :class="{ active: activeSection === 'expired' }"
              @click="switchSection('expired')"
            >
              <i class="lni lni-archive"></i> Expired
            </button>
          </div>
          <!-- Active Advisories Section -->
          <div
            id="news-section"
            class="card-style mb-30 switchable-section"
            v-show="activeSection === 'active'"
          >
            <h3 class="section-title" style="margin-bottom: 20px">
              <i class="lni lni-alert"></i> Active Advisory Bulletins
            </h3>
            <div class="entries-controls">
              <label>FILTER BY PRIORITY</label>
              <select v-model="priorityFilter">
                <option>All Levels</option>
                <option>🔴 Critical</option>
                <option>🟠 High</option>
                <option>🔵 Medium/Informational</option>
              </select>
              <label>SEARCH</label>
              <input
                type="text"
                v-model="searchQuery"
                placeholder="Search advisories..."
              />
            </div>
            <div class="table-responsive">
              <table class="table events-table">
                <thead>
                  <tr>
                    <th style="width: 5%">PIN</th>
                    <th style="width: 8%">ADVISORY ID</th>
                    <th style="width: 10%">TYPE</th>
                    <th style="width: 20%">TITLE</th>
                    <th style="width: 12%">PRIORITY</th>
                    <th style="width: 15%">TARGET AUDIENCE</th>
                    <th style="width: 15%">DATE POSTED</th>
                    <th style="width: 8%">EXPIRES</th>
                    <th style="width: 10%">STATUS</th>
                    <th style="width: 12%">ACTIONS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="advisory in filteredActiveAdvisories"
                    :key="advisory.id"
                    :class="advisory.priorityClass"
                  >
                    <td>
                      <span
                        class="pin-btn"
                        :class="{ pinned: advisory.pinned }"
                        >{{ advisory.pinned ? "📌" : "📍" }}</span
                      >
                    </td>
                    <td>
                      <strong>{{ advisory.id }}</strong>
                    </td>
                    <td>
                      <span
                        :class="['priority-badge', advisory.priorityBadgeClass]"
                        >{{ advisory.type }}</span
                      >
                    </td>
                    <td>
                      <strong>{{ advisory.title }}</strong>
                    </td>
                    <td>
                      <span
                        :class="['priority-badge', advisory.priorityBadgeClass]"
                        >{{ advisory.priority }}</span
                      >
                    </td>
                    <td>
                      <span
                        v-for="aud in advisory.audience"
                        :key="aud"
                        :class="['audience-badge', audienceClass(aud)]"
                        >{{ aud }}</span
                      >
                    </td>
                    <td>{{ advisory.date }}</td>
                    <td>{{ advisory.expires }}</td>
                    <td>
                      <span :class="advisory.statusClass">{{
                        advisory.status
                      }}</span>
                    </td>
                    <td>
                      <button
                        class="btn btn-sm btn-primary"
                        @click="viewAdvisory(advisory)"
                      >
                        View
                      </button>
                      <button
                        class="btn btn-sm btn-warning"
                        @click="editAdvisory(advisory)"
                      >
                        Edit
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <button
              class="btn-add-new"
              style="background: #27ae60"
              @click="showAddModal = true"
            >
              <i class="lni lni-plus"></i> ADD NEW ADVISORY
            </button>
            <div style="clear: both"></div>
          </div>
          <!-- All/Expired Advisories Section -->
          <div
            id="events-section"
            class="card-style mb-30 switchable-section"
            v-show="activeSection !== 'active'"
          >
            <h3 class="section-title" style="margin-bottom: 20px">
              <i class="lni lni-folder-alt"></i> All Public Advisories
            </h3>
            <div class="entries-controls">
              <label>FILTER BY TYPE</label>
              <select v-model="typeFilter">
                <option>All Types</option>
                <option>Emergency Advisory</option>
                <option>Weather Alert</option>
                <option>Safety Notice</option>
                <option>News</option>
              </select>
              <label>SEARCH</label>
              <input
                type="text"
                v-model="searchQuery"
                placeholder="Search all advisories..."
              />
            </div>
            <div class="table-responsive">
              <table class="table events-table">
                <thead>
                  <tr>
                    <th style="width: 5%">PIN</th>
                    <th style="width: 8%">ADVISORY ID</th>
                    <th style="width: 10%">TYPE</th>
                    <th style="width: 20%">TITLE</th>
                    <th style="width: 12%">PRIORITY</th>
                    <th style="width: 15%">TARGET AUDIENCE</th>
                    <th style="width: 15%">DATE POSTED</th>
                    <th style="width: 10%">STATUS</th>
                    <th style="width: 12%">ACTIONS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="advisory in filteredAllAdvisories"
                    :key="advisory.id"
                    :style="
                      advisory.expired ? 'opacity:0.7;background:#f5f5f5;' : ''
                    "
                  >
                    <td><span class="pin-btn">📍</span></td>
                    <td>
                      <strong>{{ advisory.id }}</strong>
                    </td>
                    <td>
                      <span
                        :class="['priority-badge', advisory.priorityBadgeClass]"
                        >{{ advisory.type }}</span
                      >
                    </td>
                    <td>{{ advisory.title }}</td>
                    <td>
                      <span
                        :class="['priority-badge', advisory.priorityBadgeClass]"
                        >{{ advisory.priority }}</span
                      >
                    </td>
                    <td>
                      <span
                        v-for="aud in advisory.audience"
                        :key="aud"
                        :class="['audience-badge', audienceClass(aud)]"
                        >{{ aud }}</span
                      >
                    </td>
                    <td>{{ advisory.date }}</td>
                    <td>
                      <span :class="advisory.statusClass">{{
                        advisory.status
                      }}</span>
                    </td>
                    <td>
                      <button
                        v-if="!advisory.expired"
                        class="btn btn-sm btn-primary"
                        @click="viewAdvisory(advisory)"
                      >
                        View
                      </button>
                      <button
                        v-if="!advisory.expired"
                        class="btn btn-sm btn-warning"
                        @click="editAdvisory(advisory)"
                      >
                        Edit
                      </button>
                      <button
                        v-if="advisory.expired"
                        class="btn btn-sm btn-secondary"
                      >
                        Archive
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <button
              class="btn-add-new"
              style="background: #27ae60"
              @click="showAddModal = true"
            >
              <i class="lni lni-plus"></i> ADD NEW ADVISORY
            </button>
            <div style="clear: both"></div>
          </div>
        </div>
      </section>
      <!-- ========== footer start =========== -->
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
    <!-- Advisory Modals -->
    <advisory-modal
      v-if="showViewModal"
      :advisory="selectedAdvisory"
      @close="showViewModal = false"
      @edit="editAdvisory(selectedAdvisory)"
    />
    <advisory-edit-modal
      v-if="showEditModal"
      :advisory="selectedAdvisory"
      @close="showEditModal = false"
      @save="saveAdvisory"
      @delete="deleteAdvisory"
    />
    <advisory-add-modal
      v-if="showAddModal"
      @close="showAddModal = false"
      @add="addAdvisory"
    />
  </div>
</template>

<script>
import AdvisoryModal from "./advisory-modal.vue";
import AdvisoryEditModal from "./advisory-edit-modal.vue";
import AdvisoryAddModal from "./advisory-add-modal.vue";
export default {
  name: "newsEvents",
  components: {
    AdvisoryModal,
    AdvisoryEditModal,
    AdvisoryAddModal,
  },
  data() {
    return {
      activeSection: "active",
      priorityFilter: "All Levels",
      typeFilter: "All Types",
      searchQuery: "",
      liveTime: "",
      showViewModal: false,
      showEditModal: false,
      showAddModal: false,
      selectedAdvisory: null,
      advisories: [
        // ... advisories data (see HTML for details, convert each <tr> to an object)
        {
          id: "ADV-2026-001",
          type: "🚨 Emergency Advisory",
          title: "SEVERE WEATHER WARNING: High Wind Alert",
          priority: "CRITICAL",
          audience: ["🌐 All Citizens"],
          date: "Feb 7, 2026 | 14:30",
          expires: "Feb 8, 12:00",
          status: "✓ Active",
          description:
            "A severe high wind weather alert has been issued for San Juan City and surrounding areas. Sustained winds of 60-80 km/h with gusts up to 100 km/h are expected. All citizens are advised to stay indoors, secure loose outdoor items, avoid traveling if possible, and monitor local news for updates. This alert expires on Feb 8, 12:00 PM.",
          priorityClass: "priority-critical",
          priorityBadgeClass: "priority-critical-badge",
          statusClass: "status-active",
          pinned: true,
          expired: false,
        },
        {
          id: "ADV-2026-002",
          type: "⚠️ Safety Notice",
          title: "Community Health Outreach - Free Medical Clinic",
          priority: "HIGH",
          audience: ["♿ PWDs & Elderly"],
          date: "Feb 7, 2026 | 12:15",
          expires: "Feb 10, 18:00",
          status: "✓ Active",
          description:
            "The San Juan City Health Department is conducting a free medical clinic specially designed for Persons with Disabilities (PWDs) and elderly citizens. Services include general health check-ups, blood pressure screening, consultation with medical professionals, and assistance with health insurance enrollment. Location: City Convention Center, 2nd Floor. Hours: 8:00 AM - 5:00 PM daily until Feb 10.",
          priorityClass: "priority-high",
          priorityBadgeClass: "priority-high-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
        {
          id: "ADV-2026-003",
          type: "🌦️ Weather Alert",
          title: "Heat Index Advisory: Extreme Heat Expected Today",
          priority: "HIGH",
          audience: ["👥 Citizens"],
          date: "Feb 7, 2026 | 08:00",
          expires: "Feb 7, 20:00",
          status: "✓ Active",
          description:
            "The Philippine Atmospheric, Geophysical and Astronomical Services Administration (PAGASA) has issued a Heat Index Advisory for San Juan City. Heat Index levels are expected to reach 40-42°C today. Heat safety tips: Stay hydrated, avoid prolonged sun exposure, wear light-colored clothing, check on elderly neighbors, and limit outdoor activities. This advisory expires at 8:00 PM today.",
          priorityClass: "priority-high",
          priorityBadgeClass: "priority-high-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
        {
          id: "ADV-2026-004",
          type: "📰 News",
          title: "San Juan City Launches Community Safety Program",
          priority: "MEDIUM",
          audience: ["🌐 All Citizens"],
          date: "Feb 6, 2026 | 10:30",
          expires: "Feb 13, 23:59",
          status: "✓ Active",
          description:
            "San Juan City Government has officially launched the 'Community Safety First' program aimed at reducing crime and improving public safety. Key initiatives include increased patrols in high-risk areas, community-police partnerships, street lighting improvements, and youth engagement programs. Citizens are encouraged to report suspicious activities to the hotline: 02-234-5678. Community meetings scheduled for Feb 10 and Feb 17 at city hall.",
          priorityClass: "priority-medium",
          priorityBadgeClass: "priority-medium-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
        {
          id: "ADV-2026-005",
          type: "👮 Responder Notice",
          title:
            "Traffic Advisory: Road Closure on Main Street for Maintenance",
          priority: "MEDIUM",
          audience: ["👮 Responders"],
          date: "Feb 6, 2026 | 16:45",
          expires: "Feb 9, 18:00",
          status: "✓ Active",
          description:
            "Main Street will be closed from 10:00 PM to 5:00 AM from Feb 7-9 for urgent road maintenance and pothole repairs. All emergency responders should use alternate routes: San Pedro Avenue or Jorge Avenue. For dispatch coordination, contact CEDOC at extension 204. Affected area: Main Street between Bonifacio and Luna intersections. Estimated completion: Feb 9, 6:00 AM.",
          priorityClass: "priority-medium",
          priorityBadgeClass: "priority-medium-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
        {
          id: "ADV-2026-006",
          type: "ℹ️ Information",
          title: "Schedule: Barangay Assembly Meeting Next Week",
          priority: "LOW",
          audience: ["🌐 All Citizens"],
          date: "Feb 5, 2026 | 14:00",
          expires: "Feb 12, 23:59",
          status: "✓ Active",
          description:
            "The monthly Barangay Assembly meeting of Barangay Kristong Hari is scheduled for Feb 12, 2026 at 2:00 PM at the Barangay Hall. All residents are welcome to attend. Topics to be discussed: infrastructure projects, community programs, and budget allocation. For more information, contact the Barangay Secretary at (02) 123-4567 or visit the official barangay website.",
          priorityClass: "priority-low",
          priorityBadgeClass: "priority-low-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
        // All/Expired Section
        {
          id: "ADV-2026-009",
          type: "🌦️ Weather",
          title: "Heavy Rain Warning - Expired",
          priority: "MEDIUM",
          audience: ["🌐 All"],
          date: "Feb 4, 2026 | 09:00",
          expires: "",
          status: "✕ Expired (Feb 5)",
          description: "",
          priorityClass: "priority-low",
          priorityBadgeClass: "priority-low-badge",
          statusClass: "status-expired",
          pinned: false,
          expired: true,
        },
        {
          id: "ADV-2026-007",
          type: "📰 News",
          title: "Municipal Hall Renovation Project Updates",
          priority: "LOW",
          audience: ["🌐 All Citizens"],
          date: "Feb 3, 2026 | 11:20",
          expires: "",
          status: "✓ Active",
          description:
            "Updates on the San Juan City Municipal Hall renovation project: Phase 2 (interior electrical systems) began on Feb 1 and is 40% complete. Expected completion of all phases: June 2026. Temporary offices have been set up at the Extension Building across the street. Walk-in services available Monday-Friday 8:00 AM - 4:00 PM. For inquiries, call the main hotline at 02-456-7890.",
          priorityClass: "priority-medium",
          priorityBadgeClass: "priority-medium-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
        {
          id: "ADV-2026-008",
          type: "⚠️ Safety Notice",
          title: "Dengue Prevention Awareness Campaign",
          priority: "HIGH",
          audience: ["👥 Citizens"],
          date: "Feb 2, 2026 | 15:45",
          expires: "",
          status: "✓ Active",
          description:
            "The San Juan City Health Office launches an intensive Dengue Prevention Awareness Campaign. Dengue cases have increased by 15% in the city. Preventive measures: Eliminate standing water, use mosquito screens, wear protective clothing during dawn/dusk, and report vector problems to the city health office. Free fumigation services available in all barangays. Dengue hotline: 02-789-0123. Symptoms: sudden fever, severe headache, muscle pain, rash. Seek medical attention immediately.",
          priorityClass: "priority-high",
          priorityBadgeClass: "priority-high-badge",
          statusClass: "status-active",
          pinned: false,
          expired: false,
        },
      ],
    };
  },
  computed: {
    filteredActiveAdvisories() {
      return this.advisories.filter(
        (a) => !a.expired && this.filterPriority(a) && this.filterSearch(a),
      );
    },
    filteredAllAdvisories() {
      return this.advisories.filter(
        (a) => this.filterType(a) && this.filterSearch(a),
      );
    },
  },
  methods: {
    switchSection(section) {
      this.activeSection = section;
    },
    refreshPage() {
      window.location.reload();
    },
    audienceClass(aud) {
      if (aud.includes("Citizens")) return "audience-all";
      if (aud.includes("PWD")) return "audience-pwds";
      if (aud.includes("Responders")) return "audience-responders";
      if (aud.includes("Residents")) return "audience-citizens";
      return "audience-all";
    },
    filterPriority(a) {
      if (this.priorityFilter === "All Levels") return true;
      if (this.priorityFilter.includes("Critical"))
        return a.priority === "CRITICAL";
      if (this.priorityFilter.includes("High")) return a.priority === "HIGH";
      if (this.priorityFilter.includes("Medium"))
        return a.priority === "MEDIUM";
      if (this.priorityFilter.includes("Low")) return a.priority === "LOW";
      return true;
    },
    filterType(a) {
      if (this.typeFilter === "All Types") return true;
      if (this.typeFilter === "Emergency Advisory")
        return a.type.includes("Emergency");
      if (this.typeFilter === "Weather Alert")
        return a.type.includes("Weather");
      if (this.typeFilter === "Safety Notice") return a.type.includes("Safety");
      if (this.typeFilter === "News") return a.type.includes("News");
      return true;
    },
    filterSearch(a) {
      if (!this.searchQuery) return true;
      const q = this.searchQuery.toLowerCase();
      return (
        a.title.toLowerCase().includes(q) ||
        a.id.toLowerCase().includes(q) ||
        a.type.toLowerCase().includes(q) ||
        a.priority.toLowerCase().includes(q) ||
        a.audience.join(",").toLowerCase().includes(q) ||
        a.description.toLowerCase().includes(q)
      );
    },
    viewAdvisory(advisory) {
      this.selectedAdvisory = advisory;
      this.showViewModal = true;
    },
    editAdvisory(advisory) {
      this.selectedAdvisory = advisory;
      this.showEditModal = true;
    },
    saveAdvisory(updated) {
      const idx = this.advisories.findIndex((a) => a.id === updated.id);
      if (idx !== -1) this.advisories.splice(idx, 1, updated);
      this.showEditModal = false;
    },
    deleteAdvisory(id) {
      this.advisories = this.advisories.filter((a) => a.id !== id);
      this.showEditModal = false;
    },
    addAdvisory(newAdvisory) {
      this.advisories.unshift(newAdvisory);
      this.showAddModal = false;
    },
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
  mounted() {
    this.updateLiveTime();
    this._timer = setInterval(this.updateLiveTime, 1000);
  },
  beforeUnmount() {
    clearInterval(this._timer);
  },
};
</script>

<style scoped>
/* ...existing CSS from <style> blocks in HTML... */
</style>
