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
          <li class="nav-item active">
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
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_55"
            >
              <span class="icon"><!-- ...SVG... --></span>
              <span class="text">Icons</span>
            </a>
            <ul id="ddmenu_55" class="collapse dropdown-nav">
              <li><router-link to="/admin/icons">LineIcons</router-link></li>
              <li>
                <router-link to="/admin/mdi-icons">MDI Icons</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item nav-item-has-children">
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_5"
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
                        <div class="image"><img :src="note.img" alt="" /></div>
                        <div class="content">
                          <h6>
                            {{ note.name
                            }}<span class="text-regular">{{
                              note.action
                            }}</span>
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
      <!-- Section -->
      <section>
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title d-flex align-items-center flex-wrap">
                  <h2 class="mr-40">Invoice</h2>
                  <a href="#0" class="main-btn primary-btn btn-hover btn-sm">
                    <i class="lni lni-plus mr-5"></i> New Invoice</a
                  >
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
                        Invoice
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>
          <!-- Invoice Wrapper -->
          <div class="invoice-wrapper">
            <div class="row">
              <div class="col-12">
                <div class="invoice-card card-style mb-30">
                  <div class="invoice-header">
                    <div class="invoice-for">
                      <h2 class="mb-10">Invoice</h2>
                      <p class="text-sm">
                        Admin Dashboard Design & Development
                      </p>
                    </div>
                    <div class="invoice-logo">
                      <img src="assets/images/invoice/uideck-logo.svg" alt="" />
                    </div>
                    <div class="invoice-date">
                      <p><span>Date Issued:</span> 20/02/2024</p>
                      <p><span>Date Due:</span> 20/02/2028</p>
                      <p><span>Order ID:</span> #5467</p>
                    </div>
                  </div>
                  <div class="invoice-address">
                    <div class="address-item">
                      <h5 class="text-bold">From</h5>
                      <h1>John Doe</h1>
                      <p class="text-sm">
                        3891 Ranchview Dr. Richardson, California 62639
                      </p>
                      <p class="text-sm">
                        <span class="text-medium">Email:</span>
                        admin@example.com
                      </p>
                    </div>
                    <div class="address-item">
                      <h5 class="text-bold">To</h5>
                      <h1>Santa Gosh</h1>
                      <p class="text-sm">
                        2972 Westheimer Rd. Santa Ana, Illinois 85486
                      </p>
                      <p class="text-sm">
                        <span class="text-medium">Email:</span>
                        admin@example.com
                      </p>
                    </div>
                  </div>
                  <div class="table-responsive">
                    <table class="invoice-table table">
                      <thead>
                        <tr>
                          <th class="service">
                            <h6 class="text-sm text-medium">Service</h6>
                          </th>
                          <th class="desc">
                            <h6 class="text-sm text-medium">Descriptions</h6>
                          </th>
                          <th class="qty">
                            <h6 class="text-sm text-medium">Qty</h6>
                          </th>
                          <th class="amount">
                            <h6 class="text-sm text-medium">Amounts</h6>
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, i) in invoiceItems" :key="i">
                          <td>
                            <p class="text-sm">{{ item.service }}</p>
                          </td>
                          <td>
                            <p class="text-sm">{{ item.description }}</p>
                          </td>
                          <td>
                            <p class="text-sm">{{ item.qty }}</p>
                          </td>
                          <td>
                            <p class="text-sm">{{ item.amount }}</p>
                          </td>
                        </tr>
                        <tr>
                          <td></td>
                          <td></td>
                          <td><h6 class="text-sm text-medium">Subtotal</h6></td>
                          <td><h6 class="text-sm text-bold">$5700</h6></td>
                        </tr>
                        <tr>
                          <td></td>
                          <td></td>
                          <td><h6 class="text-sm text-medium">Discount</h6></td>
                          <td><h6 class="text-sm text-bold">45%</h6></td>
                        </tr>
                        <tr>
                          <td></td>
                          <td></td>
                          <td>
                            <h6 class="text-sm text-medium">Shipping Charge</h6>
                          </td>
                          <td><h6 class="text-sm text-bold">Free</h6></td>
                        </tr>
                        <tr>
                          <td></td>
                          <td></td>
                          <td><h4>Total</h4></td>
                          <td><h4>$3135</h4></td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div class="note-wrapper warning-alert py-4 px-sm-3 px-lg-5">
                    <div class="alert">
                      <h5 class="text-bold mb-15">Notes:</h5>
                      <p class="text-sm text-gray">
                        All accounts are to be paid within 7 days from receipt
                        of invoice. To be paid by cheque or credit card or
                        direct payment online. If account is not paid within 7
                        days the credits details supplied as confirmation of
                        work undertaken will be charged the agreed quoted fee
                        noted above.
                      </p>
                    </div>
                  </div>
                  <div class="invoice-action">
                    <ul
                      class="d-flex flex-wrap align-items-center justify-content-center"
                    >
                      <li class="m-2">
                        <a
                          href="#0"
                          class="main-btn primary-btn-outline btn-hover"
                          >Download Invoice</a
                        >
                      </li>
                      <li class="m-2">
                        <a href="#0" class="main-btn primary-btn btn-hover"
                          >Send Invoice</a
                        >
                      </li>
                    </ul>
                  </div>
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
  name: "invoice",
  data() {
    return {
      searchQuery: "",
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
      invoiceItems: [
        {
          service: "Admin Dashboard",
          description: "Design and Development Service",
          qty: 3,
          amount: "$700",
        },
        {
          service: "Landing Page",
          description: "Landing Page Ui kit design and Development",
          qty: 1,
          amount: "$1000",
        },
        {
          service: "Web design",
          description: "Web Design and Development and Seo",
          qty: 2,
          amount: "$4000",
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Add any invoice-specific styles here */
</style>
