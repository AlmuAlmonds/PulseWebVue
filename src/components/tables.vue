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
          to="/index"
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
            <router-link to="/index">
              <span class="icon">
                <!-- ...existing code... -->
              </span>
              <span class="text">Dashboard</span>
            </router-link>
          </li>
          <!-- ...existing code for sidebar links... -->
          <li class="nav-item active">
            <router-link to="/tables">
              <span class="icon">
                <!-- ...existing code... -->
              </span>
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
        <!-- ...existing code for header... -->
      </header>

      <!-- Table Components -->
      <section class="table-components">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Tables</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/index">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Tables
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <div class="tables-wrapper">
            <!-- Data Table -->
            <div class="row">
              <div class="col-lg-12">
                <div class="card-style mb-30">
                  <h6 class="mb-10">Data Table</h6>
                  <p class="text-sm mb-20">
                    For basic styling—light padding and only horizontal
                    dividers—use the class table.
                  </p>
                  <div class="table-wrapper table-responsive">
                    <table class="table">
                      <thead>
                        <tr>
                          <th class="lead-info"><h6>Lead</h6></th>
                          <th class="lead-email"><h6>Email</h6></th>
                          <th class="lead-phone"><h6>Phone No</h6></th>
                          <th class="lead-company"><h6>Company</h6></th>
                          <th><h6>Action</h6></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="lead in leads" :key="lead.name">
                          <td class="min-width">
                            <div class="lead">
                              <div class="lead-image">
                                <img :src="lead.image" alt="" />
                              </div>
                              <div class="lead-text">
                                <p>{{ lead.name }}</p>
                              </div>
                            </div>
                          </td>
                          <td class="min-width">
                            <p>
                              <a href="#0">{{ lead.email }}</a>
                            </p>
                          </td>
                          <td class="min-width">
                            <p>{{ lead.phone }}</p>
                          </td>
                          <td class="min-width">
                            <p>{{ lead.company }}</p>
                          </td>
                          <td>
                            <div class="action">
                              <button
                                class="text-danger"
                                @click="deleteLead(lead)"
                              >
                                <i class="lni lni-trash-can"></i>
                              </button>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>

            <!-- Striped Table -->
            <div class="row">
              <div class="col-lg-6">
                <div class="card-style mb-30">
                  <h6 class="mb-10">Striped Table</h6>
                  <p class="text-sm mb-20">
                    For Striped Table—light padding and only horizontal
                    dividers.
                  </p>
                  <div class="table-wrapper table-responsive">
                    <table class="table striped-table">
                      <thead>
                        <tr>
                          <th></th>
                          <th><h6>Account No</h6></th>
                          <th><h6>Balance</h6></th>
                          <th><h6>Action</h6></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="account in accounts" :key="account.number">
                          <td>
                            <div class="check-input-primary">
                              <input
                                class="form-check-input"
                                type="checkbox"
                                :id="'checkbox-' + account.id"
                                v-model="account.checked"
                              />
                            </div>
                          </td>
                          <td>
                            <p>{{ account.number }}</p>
                          </td>
                          <td>
                            <p>{{ account.balance }}</p>
                          </td>
                          <td>
                            <div class="action">
                              <button
                                class="text-danger"
                                @click="deleteAccount(account)"
                              >
                                <i class="lni lni-trash-can"></i>
                              </button>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              <div class="col-lg-6">
                <div class="card-style mb-30">
                  <h6 class="mb-10">Table head options</h6>
                  <p class="text-sm mb-20">
                    Use one of two modifier classes to make thead appear light
                    or dark gray.
                  </p>
                  <div class="table-wrapper table-responsive">
                    <table class="table striped-table">
                      <thead>
                        <tr>
                          <th></th>
                          <th><h6>First Name</h6></th>
                          <th><h6>Last Name</h6></th>
                          <th><h6>Username</h6></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="user in users" :key="user.username">
                          <td>
                            <h6 class="text-sm">{{ user.id }}</h6>
                          </td>
                          <td>
                            <p>{{ user.firstName }}</p>
                          </td>
                          <td>
                            <p>{{ user.lastName }}</p>
                          </td>
                          <td>
                            <p>{{ user.username }}</p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>

            <!-- Data Table 2 -->
            <div class="row">
              <div class="col-lg-12">
                <div class="card-style mb-30">
                  <h6 class="mb-10">Data Table</h6>
                  <p class="text-sm mb-20">
                    For basic styling—light padding and only horizontal
                    dividers—use the class table.
                  </p>
                  <div class="table-wrapper table-responsive">
                    <table class="table">
                      <thead>
                        <tr>
                          <th><h6>#</h6></th>
                          <th><h6>Name</h6></th>
                          <th><h6>Email</h6></th>
                          <th><h6>Project</h6></th>
                          <th><h6>Status</h6></th>
                          <th><h6>Action</h6></th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="employee in employees" :key="employee.name">
                          <td>
                            <div class="employee-image">
                              <img :src="employee.image" alt="" />
                            </div>
                          </td>
                          <td class="min-width">
                            <p>{{ employee.name }}</p>
                          </td>
                          <td class="min-width">
                            <p>
                              <a href="#0">{{ employee.email }}</a>
                            </p>
                          </td>
                          <td class="min-width">
                            <p>{{ employee.project }}</p>
                          </td>
                          <td class="min-width">
                            <span
                              :class="['status-btn', employee.statusClass]"
                              >{{ employee.status }}</span
                            >
                          </td>
                          <td>
                            <div class="action">
                              <button
                                class="text-danger"
                                @click="deleteEmployee(employee)"
                              >
                                <i class="lni lni-trash-can"></i>
                              </button>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer">
        <!-- ...existing code for footer... -->
      </footer>
    </main>
  </div>
</template>

<script>
export default {
  name: "tables",
  data() {
    return {
      leads: [
        {
          name: "Courtney Henry",
          image: "assets/images/lead/lead-1.png",
          email: "yourmail@gmail.com",
          phone: "(303)555 3343523",
          company: "UIdeck digital agency",
        },
        {
          name: "John Doe",
          image: "assets/images/lead/lead-2.png",
          email: "yourmail@gmail.com",
          phone: "(303)555 3343523",
          company: "Graygrids digital agency",
        },
        {
          name: "David Smith",
          image: "assets/images/lead/lead-3.png",
          email: "yourmail@gmail.com",
          phone: "(303)555 3343523",
          company: "Abc agency",
        },
        {
          name: "Jonathon",
          image: "assets/images/lead/lead-4.png",
          email: "yourmail@gmail.com",
          phone: "(303)555 3343523",
          company: "Creative IT Agency",
        },
        {
          name: "Anna Lee",
          image: "assets/images/lead/lead-5.png",
          email: "yourmail@gmail.com",
          phone: "(303)555 3343523",
          company: "Halal It agency",
        },
        {
          name: "Gray Simon",
          image: "assets/images/lead/lead-6.png",
          email: "yourmail@gmail.com",
          phone: "(303)555 3343523",
          company: "DesignCourse",
        },
      ],
      accounts: [
        { id: 1, number: "AC336 508 2157", balance: "$523", checked: false },
        { id: 2, number: "AC336 756 0987", balance: "$123", checked: false },
        { id: 3, number: "AC336 098 8765", balance: "$223", checked: false },
        { id: 4, number: "AC336 897 3242", balance: "$323", checked: false },
        { id: 5, number: "AC336 654 0987", balance: "$423", checked: false },
        { id: 6, number: "AC336 234 9804", balance: "$523", checked: false },
      ],
      users: [
        {
          id: "#1",
          firstName: "Albert",
          lastName: "Miles",
          username: "@albert_miles",
        },
        { id: "#2", firstName: "John", lastName: "Doe", username: "@john_doe" },
        {
          id: "#3",
          firstName: "David",
          lastName: "Smith",
          username: "@davidsmith",
        },
        {
          id: "#4",
          firstName: "Jameel",
          lastName: "Kareem",
          username: "@jkreem",
        },
        {
          id: "#5",
          firstName: "Anna",
          lastName: "Miles",
          username: "@anna_miles",
        },
        {
          id: "#6",
          firstName: "Hafiz",
          lastName: "Miles",
          username: "@hafiz_miles",
        },
      ],
      employees: [
        {
          name: "Esther Howard",
          image: "assets/images/lead/lead-1.png",
          email: "yourmail@gmail.com",
          project: "Admin Dashboard Design",
          status: "Active",
          statusClass: "active-btn",
        },
        {
          name: "D. Jonathon",
          image: "assets/images/lead/lead-2.png",
          email: "yourmail@gmail.com",
          project: "React Dashboard",
          status: "Active",
          statusClass: "active-btn",
        },
        {
          name: "John Doe",
          image: "assets/images/lead/lead-3.png",
          email: "yourmail@gmail.com",
          project: "Bootstrap Template",
          status: "Done",
          statusClass: "success-btn",
        },
        {
          name: "Rayhan Jamil",
          image: "assets/images/lead/lead-4.png",
          email: "yourmail@gmail.com",
          project: "Css Grid Template",
          status: "Pending",
          statusClass: "info-btn",
        },
        {
          name: "Esther Howard",
          image: "assets/images/lead/lead-5.png",
          email: "yourmail@gmail.com",
          project: "Admin Dashboard Design",
          status: "Close",
          statusClass: "close-btn",
        },
        {
          name: "Anee Doe",
          image: "assets/images/lead/lead-6.png",
          email: "yourmail@gmail.com",
          project: "Space Template Update",
          status: "Active",
          statusClass: "active-btn",
        },
      ],
    };
  },
  methods: {
    deleteLead(lead) {
      this.leads = this.leads.filter((l) => l !== lead);
    },
    deleteAccount(account) {
      this.accounts = this.accounts.filter((a) => a !== account);
    },
    deleteEmployee(employee) {
      this.employees = this.employees.filter((e) => e !== employee);
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here or import from assets/css/main.css */
</style>
