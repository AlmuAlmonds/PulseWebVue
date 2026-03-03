<template>
  <div>
    <!-- ======== Preloader =========== -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>
    <!-- ======== sidebar-nav start =========== -->
    <aside class="sidebar-nav-wrapper">
      <div class="navbar-logo">
        <router-link to="/admin">
          <img src="https://via.placeholder.com/40" alt="logo" style="width: 45px; height: 45px; object-fit: contain;" />
          <span style="font-size: 18px; font-weight: 600; color: #3b5998;">PULSE Admin</span>
        </router-link>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <li class="nav-item">
            <router-link to="/admin"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 13H10C10.55 13 11 12.55 11 12V4C11 3.45 10.55 3 10 3H4C3.45 3 3 3.45 3 4V12C3 12.55 3.45 13 4 13ZM4 21H10C10.55 21 11 20.55 11 20V16C11 15.45 10.55 15 10 15H4C3.45 15 3 15.45 3 16V20C3 20.55 3.45 21 4 21ZM14 21H20C20.55 21 21 20.55 21 20V12C21 11.45 20.55 11 20 11H14C13.45 11 13 11.45 13 12V20C13 20.55 13.45 21 14 21ZM13 4V8C13 8.55 13.45 9 14 9H20C20.55 9 21 8.55 21 8V4C21 3.45 20.55 3 20 3H14C13.45 3 13 3.45 13 4Z" fill="currentColor"/></svg></span><span class="text">Dashboard</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link to="/admin/accounts"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V19C4 19.55 4.45 20 5 20H19C19.55 20 20 19.55 20 19V18C20 15.34 14.67 14 12 14Z" fill="currentColor"/></svg></span><span class="text">User Management</span></router-link>
          </li>
          <li class="nav-item" style="margin-bottom: 15px;">
            <router-link to="/admin/news-events"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 3H4C2.9 3 2 3.9 2 5V19C2 20.1 2.9 21 4 21H20C21.1 21 22 20.1 22 19V5C22 3.9 21.1 3 20 3ZM5 7H10V13H5V7ZM19 17H5V15H19V17ZM19 13H12V11H19V13ZM19 9H12V7H19V9Z" fill="currentColor"/></svg></span><span class="text">News & Events</span></router-link>
          </li>
          <li class="nav-item" style="pointer-events: none; margin-top: 10px;">
            <span style="display: flex; align-items: center; padding: 12px 20px; color: #ffc107; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;"><span class="icon" style="margin-right: 10px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 1L3 5V11C3 16.55 6.84 21.74 12 23C17.16 21.74 21 16.55 21 11V5L12 1ZM12 11.99H19C18.47 16.11 15.72 19.78 12 20.93V12H5V6.3L12 3.19V11.99Z" fill="#ffc107"/></svg></span>Security</span>
          </li>
          <li class="nav-item">
            <router-link to="/admin/loginlogs"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.99 2C6.47 2 2 6.48 2 12C2 17.52 6.47 22 11.99 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 11.99 2ZM12 20C7.58 20 4 16.42 4 12C4 7.58 7.58 4 12 4C16.42 4 20 7.58 20 12C20 16.42 16.42 20 12 20ZM12.5 7H11V13L16.25 16.15L17 14.92L12.5 12.25V7Z" fill="currentColor"/></svg></span><span class="text">Logs</span></router-link>
          </li>
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>
    <!-- ======== main-wrapper start =========== -->
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
                    <input type="text" placeholder="Search for something" v-model="headerSearch" />
                    <button><i class="lni lni-search-alt"></i></button>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-lg-7 col-md-7 col-6">
              <div class="header-right">
                <!-- notification start -->
                <div class="notification-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button" id="notification" data-bs-toggle="dropdown" aria-expanded="false">
                    <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11 20.1667C9.88317 20.1667 8.88718 19.63 8.23901 18.7917H13.761C13.113 19.63 12.1169 20.1667 11 20.1667Z" fill="" /><path d="M10.1157 2.74999C10.1157 2.24374 10.5117 1.83333 11 1.83333C11.4883 1.83333 11.8842 2.24374 11.8842 2.74999V2.82604C14.3932 3.26245 16.3051 5.52474 16.3051 8.24999V14.287C16.3051 14.5301 16.3982 14.7633 16.564 14.9352L18.2029 16.6342C18.4814 16.9229 18.2842 17.4167 17.8903 17.4167H4.10961C3.71574 17.4167 3.5185 16.9229 3.797 16.6342L5.43589 14.9352C5.6017 14.7633 5.69485 14.5301 5.69485 14.287V8.24999C5.69485 5.52474 7.60672 3.26245 10.1157 2.82604V2.74999Z" fill="" /></svg>
                    <span></span>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="notification">
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="https://via.placeholder.com/40" alt="" />
                        </div>
                        <div class="content">
                          <h6>New account registered</h6>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- notification end -->
                <!-- message start -->
                <div class="header-message-box ml-15 d-none d-md-flex">
                  <button class="dropdown-toggle" type="button" id="message" data-bs-toggle="dropdown" aria-expanded="false">
                    <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M7.74866 5.97421C7.91444 5.96367 8.08162 5.95833 8.25005 5.95833C12.5532 5.95833 16.0417 9.4468 16.0417 13.75C16.0417 13.9184 16.0364 14.0856 16.0259 14.2514C16.3246 14.138 16.6127 14.003 16.8883 13.8482L19.2306 14.629C19.7858 14.8141 20.3141 14.2858 20.129 13.7306L19.3482 11.3882C19.8694 10.4604 20.1667 9.38996 20.1667 8.25C20.1667 4.70617 17.2939 1.83333 13.75 1.83333C11.0077 1.83333 8.66702 3.55376 7.74866 5.97421Z" fill="" /><path d="M14.6667 13.75C14.6667 17.2938 11.7939 20.1667 8.25004 20.1667C7.11011 20.1667 6.03962 19.8694 5.11182 19.3482L2.76946 20.129C2.21421 20.3141 1.68597 19.7858 1.87105 19.2306L2.65184 16.8882C2.13062 15.9604 1.83338 14.89 1.83338 13.75C1.83338 10.2062 4.70622 7.33333 8.25004 7.33333C11.7939 7.33333 14.6667 10.2062 14.6667 13.75ZM5.95838 13.75C5.95838 13.2437 5.54797 12.8333 5.04171 12.8333C4.53545 12.8333 4.12504 13.2437 4.12504 13.75C4.12504 14.2563 4.53545 14.6667 5.04171 14.6667C5.54797 14.6667 5.95838 14.2563 5.95838 13.75ZM9.16671 13.75C9.16671 13.2437 8.7563 12.8333 8.25004 12.8333C7.74379 12.8333 7.33338 13.2437 7.33338 13.75C7.33338 14.2563 7.74379 14.6667 8.25004 14.6667C8.7563 14.6667 9.16671 14.2563 9.16671 13.75ZM11.4584 14.6667C11.9647 14.6667 12.375 14.2563 12.375 13.75C12.375 13.2437 11.9647 12.8333 11.4584 12.8333C10.9521 12.8333 10.5417 13.2437 10.5417 13.75C10.5417 14.2563 10.9521 14.6667 11.4584 14.6667Z" fill="" /></svg>
                    <span></span>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="message">
                    <li>
                      <a href="#0">
                        <div class="image">
                          <img src="https://via.placeholder.com/40" alt="" />
                        </div>
                        <div class="content">
                          <h6>Jacob Jones</h6>
                          <p>Account verified successfully</p>
                          <span>10 mins ago</span>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <!-- message end -->
                <!-- profile start -->
                <div class="profile-box ml-15">
                  <button class="dropdown-toggle bg-transparent border-0" type="button" id="profile" data-bs-toggle="dropdown" aria-expanded="false">
                    <div class="profile-info">
                      <div class="info">
                        <div class="image">
                          <img src="https://via.placeholder.com/40" alt="" />
                        </div>
                        <div>
                          <h6 class="fw-500">Adam Joe</h6>
                          <p>Admin</p>
                        </div>
                      </div>
                    </div>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="profile">
                    <li>
                      <div class="author-info flex items-center !p-1">
                        <div class="image">
                          <img src="https://via.placeholder.com/40" alt="image">
                        </div>
                        <div class="content">
                          <h4 class="text-sm">Adam Joe</h4>
                          <a class="text-black/40 dark:text-white/40 hover:text-black dark:hover:text-white text-xs" href="#">Email@gmail.com</a>
                        </div>
                      </div>
                    </li>
                    <li class="divider"></li>
                    <li>
                      <a href="#0"><i class="lni lni-user"></i> View Profile</a>
                    </li>
                    <li class="divider"></li>
                    <li>
                      <a href="#0" @click.prevent="signOut"><i class="lni lni-exit"></i> Sign Out</a>
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
          <!-- Page Header -->
          <div class="page-header pt-30">
            <div class="d-flex align-items-center gap-3">
              <div>
                <h1>User Management</h1>
                <p style="color: #666; font-size: 14px; margin-top: 5px; margin-bottom: 0;">Manage user accounts, roles, and system access across all platforms</p>
              </div>
            </div>
            <div class="header-actions">
              <span class="time-display" id="liveTime">{{ liveTime }}</span>
              <button class="btn-refresh-icon" @click="refreshPage" title="Refresh">
                <i class="lni lni-reload"></i>
              </button>
            </div>
          </div>
          <!-- Stats Cards -->
          <div class="row g-3 mb-4">
            <div class="col-lg-2 col-md-4 col-sm-6" v-for="stat in stats" :key="stat.label">
              <div class="stat-card">
                <div class="icon-box" :class="stat.class">
                  <span v-html="stat.icon"></span>
                </div>
                <div>
                  <div class="stat-number">{{ stat.value }}</div>
                  <div class="stat-label">{{ stat.label }}</div>
                </div>
              </div>
            </div>
          </div>
          <!-- Tab Bar -->
          <div class="tab-bar">
            <div class="tab-buttons">
              <button v-for="tab in tabs" :key="tab.filter" class="tab-btn" :class="{active: currentFilter === tab.filter}" @click="filterUsers(tab.filter)">{{ tab.label }}</button>
            </div>
            <div class="action-buttons">
              <button class="btn-export" @click="exportUsers"><i class="lni lni-download"></i> Export</button>
              <button class="btn-add-user" @click="openAddModal"><i class="lni lni-plus"></i> Add User</button>
            </div>
          </div>
          <!-- Search Bar -->
          <div class="search-bar">
            <input type="text" class="search-input" v-model="searchTerm" placeholder="Search by name, email, or phone..." @input="searchUsers">
            <select class="status-select" v-model="statusFilter" @change="searchUsers">
              <option value="">All Status</option>
              <option value="active">Active</option>
              <option value="blacklisted">Blacklisted</option>
            </select>
          </div>
          <!-- Users Table -->
          <div class="card-style mb-30" style="padding: 0; overflow: hidden;">
            <div class="table-responsive">
              <table class="users-table">
                <thead>
                  <tr>
                    <th>USER</th>
                    <th>ROLE</th>
                    <th>PHONE</th>
                    <th>REGISTERED</th>
                    <th>STATUS</th>
                    <th>ACTIONS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="u in filteredUsers" :key="u.id">
                    <td>
                      <div class="user-cell">
                        <div class="user-avatar" :style="{background: avatarColors[u.role]}">{{ getInitials(u.name) }}</div>
                        <div>
                          <div class="user-name">{{ u.name }}</div>
                          <div class="user-email">{{ u.email }}</div>
                        </div>
                      </div>
                    </td>
                    <td><span class="role-badge" :class="u.role">{{ capitalize(u.role) }}</span></td>
                    <td>{{ u.phone }}</td>
                    <td>{{ u.registered }}</td>
                    <td>
                      <div class="status-cell">
                        <span class="status-dot" :class="u.status"></span>
                        {{ capitalize(u.status) }}
                      </div>
                    </td>
                    <td>
                      <div class="action-icons">
                        <button class="action-icon" title="View" @click="viewUser(u.id)"><i class="lni lni-eye"></i></button>
                        <button class="action-icon" title="Edit" @click="editUser(u.id)"><i class="lni lni-pencil"></i></button>
                        <button class="action-icon" :title="u.status === 'active' ? 'Disable' : 'Enable'" @click="toggleStatus(u.id)">
                          <i :class="'lni lni-' + (u.status === 'active' ? 'close' : 'checkmark')"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <!-- User Modal -->
          <!-- <UserModal :show="showModal" :user="modalUser" :isEdit="isEdit" @close="closeModal" @save="saveUser" /> -->
        </div>
      </section>
      <footer class="footer">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6 order-last order-md-first">
              <div class="copyright text-center text-md-start">
                <p class="text-sm">PULSE Admin Dashboard</p>
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
// import UserModal from './UserModal.vue';
export default {
  // components: { UserModal },
  data() {
    return {
      headerSearch: '',
      liveTime: '',
      showModal: false,
      isEdit: false,
      modalUser: null,
      searchTerm: '',
      statusFilter: '',
      currentFilter: 'all',
      users: [
        { id: 1, name: 'Juan Dela Cruz', email: 'juan@email.com', phone: '+63 917 123 4567', role: 'citizen', status: 'active', registered: '2025-06-15' },
        { id: 2, name: 'Maria Santos', email: 'maria@cedoc.gov.ph', phone: '+63 918 234 5678', role: 'responder', status: 'active', registered: '2025-03-22' },
        { id: 3, name: 'Pedro Reyes', email: 'pedro@cedoc.gov.ph', phone: '+63 919 345 6789', role: 'admin', status: 'active', registered: '2025-01-10' },
        { id: 4, name: 'Ana Garcia', email: 'ana@email.com', phone: '+63 920 456 7890', role: 'citizen', status: 'blacklisted', registered: '2025-08-05' },
        { id: 5, name: 'Diego Santos', email: 'diego@cedoc.gov.ph', phone: '+63 921 567 8901', role: 'dispatcher', status: 'active', registered: '2025-07-03' },
        { id: 6, name: 'Sofia Ramos', email: 'sofia@cedoc.gov.ph', phone: '+63 922 678 9012', role: 'dispatcher', status: 'active', registered: '2025-05-30' },
        { id: 7, name: 'Carlos Mendoza', email: 'carlos@email.com', phone: '+63 921 567 8901', role: 'citizen', status: 'active', registered: '2025-04-18' },
        { id: 8, name: 'Elena Villanueva', email: 'elena@cedoc.gov.ph', phone: '+63 922 678 9012', role: 'responder', status: 'active', registered: '2025-02-28' },
        { id: 9, name: 'Roberto Cruz', email: 'roberto@email.com', phone: '+63 923 789 0123', role: 'citizen', status: 'active', registered: '2025-07-12' },
        { id: 10, name: 'Juan Dela Cruz', email: 'juan@email.com', phone: '+63 925 901 2345', role: 'admin', status: 'blacklisted', registered: '2025-06-15' },
        { id: 11, name: 'Sofia Ramos', email: 'sofia@cedoc.gov.ph', phone: '+63 924 890 1234', role: 'admin', status: 'active', registered: '2025-05-30' }
      ],
      avatarColors: { citizen: '#3b82f6', responder: '#f97316', admin: '#8b5cf6', dispatcher: '#dc2626' },
      tabs: [
        { label: 'All Users', filter: 'all' },
        { label: 'Citizens', filter: 'citizen' },
        { label: 'Responders', filter: 'responder' },
        { label: 'Admins', filter: 'admin' },
        { label: 'Dispatchers', filter: 'dispatcher' },
        { label: 'Blacklisted', filter: 'blacklisted' }
      ]
    };
  },
  computed: {
    filteredUsers() {
      return this.users.filter(u => {
        let matchFilter;
        if (this.currentFilter === 'all') {
          matchFilter = true;
        } else if (this.currentFilter === 'blacklisted') {
          matchFilter = u.status === 'blacklisted';
        } else {
          matchFilter = u.role === this.currentFilter;
        }
        const matchSearch = u.name.toLowerCase().includes(this.searchTerm.toLowerCase()) || u.email.toLowerCase().includes(this.searchTerm.toLowerCase()) || u.phone.includes(this.searchTerm);
        const matchStatus = !this.statusFilter || u.status === this.statusFilter;
        return matchFilter && matchSearch && matchStatus;
      });
    },
    stats() {
      return [
        { label: 'Citizens', value: this.users.filter(u => u.role === 'citizen').length, class: 'citizens', icon: `<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v1c0 .55.45 1 1 1h14c.55 0 1-.45 1-1v-1c0-2.66-5.33-4-8-4z"/></svg>` },
        { label: 'Responders', value: this.users.filter(u => u.role === 'responder').length, class: 'responders', icon: `<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>` },
        { label: 'Admins', value: this.users.filter(u => u.role === 'admin').length, class: 'admins', icon: `<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>` },
        { label: 'Dispatchers', value: this.users.filter(u => u.role === 'dispatcher').length, class: 'dispatchers', icon: `<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>` },
        { label: 'Blacklisted', value: this.users.filter(u => u.status === 'blacklisted').length, class: 'inactive', icon: `<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zM4 12c0-4.42 3.58-8 8-8 1.85 0 3.55.63 4.9 1.69L5.69 16.9C4.63 15.55 4 13.85 4 12zm8 8c-1.85 0-3.55-.63-4.9-1.69L18.31 7.1C19.37 8.45 20 10.15 20 12c0 4.42-3.58 8-8 8z"/></svg>` }
      ];
    }
  },
  methods: {
    getInitials(name) {
      return name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
    },
    capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
    filterUsers(filter) {
      this.currentFilter = filter;
    },
    searchUsers() {},
    openAddModal() {
      this.isEdit = false;
      this.modalUser = { name: '', email: '', phone: '', role: 'citizen', status: 'active' };
      this.showModal = true;
    },
    editUser(id) {
      const user = this.users.find(u => u.id === id);
      if (user) {
        this.isEdit = true;
        this.modalUser = { ...user };
        this.showModal = true;
      }
    },
    viewUser(id) {
      const user = this.users.find(u => u.id === id);
      if (user) {
        alert(`Viewing: ${user.name}\nEmail: ${user.email}\nPhone: ${user.phone}\nRole: ${user.role}\nStatus: ${user.status}`);
      }
    },
    toggleStatus(id) {
      const user = this.users.find(u => u.id === id);
      if (user) {
        user.status = user.status === 'active' ? 'inactive' : 'active';
      }
    },
    saveUser(user) {
      if (this.isEdit) {
        const idx = this.users.findIndex(u => u.id === user.id);
        if (idx !== -1) this.users.splice(idx, 1, user);
      } else {
        user.id = Math.max(...this.users.map(u => u.id)) + 1;
        user.registered = new Date().toISOString().split('T')[0];
        this.users.push(user);
      }
      this.showModal = false;
    },
    closeModal() {
      this.showModal = false;
    },
    refreshPage() {
      window.location.reload();
    },
    signOut() {
      this.$router.push('/');
    },
    exportUsers() {
      // Implement export logic
      alert('Exporting users...');
    },
    toggleMenu() {
      // Implement menu toggle logic
    },
    updateTime() {
      const now = new Date();
      this.liveTime = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    }
  },
  mounted() {
    this.updateTime();
    setInterval(this.updateTime, 1000);
  }
};
</script>

<style scoped>
/* Move all CSS from the HTML file here, unchanged for now. */
</style>
