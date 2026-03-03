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
                <!-- SVG icon -->
                ...existing code...
              </span>
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
              <span class="icon">...existing code...</span>
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
              <span class="icon">...existing code...</span>
              <span class="text">Invoice</span>
            </router-link>
          </li>
          <span class="divider"><hr /></span>
          <li class="nav-item nav-item-has-children">
            <a
              href="#0"
              class=""
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_4"
              aria-controls="ddmenu_4"
              aria-expanded="true"
              aria-label="Toggle navigation"
            >
              <span class="icon">...existing code...</span>
              <span class="text">UI Elements</span>
            </a>
            <ul id="ddmenu_4" class="collapsed show dropdown-nav">
              <li><router-link to="/admin/alerts">Alerts</router-link></li>
              <li><router-link to="/admin/buttons">Buttons</router-link></li>
              <li><router-link to="/admin/cards">Cards</router-link></li>
              <li>
                <router-link to="/admin/typography" class="active"
                  >Typography</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item nav-item-has-children">
            <a
              href="#0"
              class="collapsed"
              data-bs-toggle="collapse"
              data-bs-target="#ddmenu_55"
              aria-controls="ddmenu_55"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon">...existing code...</span>
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
              aria-controls="ddmenu_5"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="icon">...existing code...</span>
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
              <span class="icon">...existing code...</span>
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
                    ...existing code...
                  </button>
                  <ul
                    class="dropdown-menu dropdown-menu-end"
                    aria-labelledby="notification"
                  >
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
                  <button
                    class="dropdown-toggle"
                    type="button"
                    id="message"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    ...existing code...
                  </button>
                  <ul
                    class="dropdown-menu dropdown-menu-end"
                    aria-labelledby="message"
                  >
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

      <!-- Typography Section -->
      <section class="section">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Typography</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/admin/index">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item">
                        <router-link to="#0">UI Components</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Typography
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-lg-6">
              <div class="card-style mb-30">
                <h5 class="text-medium mb-10">Heading</h5>
                <p class="text-sm mb-30">
                  All HTML headings, <code>&lt;h1&gt;&lt;/h1&gt;</code> through
                  <code>&lt;h6&gt;&lt;/h6&gt;</code>, are available.
                </p>
                <div class="heading-one mb-30">
                  <h1 class="mb-10">Heading 1- Bold</h1>
                  <p class="text-sm">
                    Font- size 24 line-height 29 letter-spacing _0.0 px
                  </p>
                </div>
                <div class="heading-two mb-30">
                  <h2 class="mb-10">Heading 2- Semi-bold</h2>
                  <p class="text-sm">
                    Font- size 24 line-height 29 letter-spacing _0.0 px
                  </p>
                </div>
                <div class="heading-three mb-30">
                  <h3 class="mb-10">Heading 3- Medium</h3>
                  <p class="text-sm">
                    Font- size 24 line-height 29 letter-spacing _0.0 px
                  </p>
                </div>
                <div class="heading-four mb-30">
                  <h4 class="mb-10">Heading 4- Semi-bold</h4>
                  <p class="text-sm">
                    Font- size 20 line-height 24 letter-spacing _0.0 px
                  </p>
                </div>
                <div class="heading-five mb-30">
                  <h5 class="mb-10">Heading 5-Bold</h5>
                  <p class="text-sm">
                    Font- size 16 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
                <div class="heading-six">
                  <h6 class="mb-10">Heading 6- Semi-bold</h6>
                  <p class="text-sm">
                    Font- size 16 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
              </div>
              <div class="card-style mb-30">
                <h1 class="mb-30">Title Text</h1>
                <p>
                  <span class="text-success text-medium">Paragraph text</span>
                  sit amet, consectetur adipiscing elit. Orci pellentesque amet
                  quam massa in aliquet pulvinar tincidunt. Enim sit elit
                  scelerisque vel aliquam vel quam a tincidunt. Nunc diam at sed
                  fames integer turpis libero. Id nunc quisque sed ut nec
                  phasellus turpis enim elit. Turpis lobortis pellentesque ac
                  massa risus faucibus tempus ut neque. Faucibus orci faucibus
                  malesuada imperdiet vitae.Lorem ipsum dolor sit amet,
                  consectetur adipiscing elit. Orci pellentesque amet quam massa
                  in aliquet pulvinar tincidunt. Enim sit elit scelerisque vel
                  aliquam vel quam a tincidunt. Nunc diam at sed fames integer
                  turpis libero. Id nunc quisque sed ut nec phasellus turpis
                  enim elit. Turpis lobortis pellentesque ac massa risus
                  faucibus tempus ut neque. Faucibus orci faucibus malesuada
                  imperdiet vitae.
                </p>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="card-style mb-30">
                <h5 class="mb-30 text-medium">Content Text</h5>
                <div class="mb-30">
                  <h5 class="text-medium mb-10">Content 1- Medium</h5>
                  <p class="text-sm">
                    Font- size 16 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
                <div class="mb-30">
                  <h5 class="text-sm text-medium mb-10">Content 1- Medium</h5>
                  <p class="text-sm">
                    Font- size 14 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
                <div>
                  <h5 class="text-sm text-regular mb-10">Content 1- Medium</h5>
                  <p class="text-sm">
                    Font- size 14 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
              </div>
              <div class="card-style mb-30">
                <h5 class="mb-30 text-medium">Button Text</h5>
                <div class="mb-30">
                  <h5 class="text-sm text-medium mb-10">Content 1- Medium</h5>
                  <p class="text-sm">
                    Font- size 14 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
                <div>
                  <h5 class="text-sm text-regular mb-10">Content 1- Medium</h5>
                  <p class="text-sm">
                    Font- size 14 line-height 19 letter-spacing _0.0 px
                  </p>
                </div>
              </div>
              <div class="card-style mb-30">
                <h5 class="mb-30 text-medium">Text Color</h5>
                <p class="text-medium text-dark mb-30">
                  This is Dark text You can archive this adding
                  <mark class="text-dark bg-dark-100">.text-dark</mark> class
                </p>
                <p class="text-medium text-gray mb-30">
                  This is Gray text You can archive this adding
                  <mark class="text-gray bg-dark-100">.text-gray</mark> class
                </p>
                <p class="text-medium text-success mb-30">
                  This is Success text You can archive this adding
                  <mark class="text-success bg-success-100">.text-success</mark>
                  class
                </p>
                <p class="text-medium text-warning mb-30">
                  This is Warning text You can archive this adding
                  <mark class="text-warning bg-warning-100">.text-warning</mark>
                  class
                </p>
                <p class="text-medium text-danger mb-30">
                  This is Danger text You can archive this adding
                  <mark class="text-danger bg-danger-100">.text-danger</mark>
                  class
                </p>
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
  name: "typography",
  data() {
    return {
      searchQuery: "",
    };
  },
};
</script>

<style scoped>
@import "../assets/css/bootstrap.min.css";
@import "../assets/css/lineicons.css";
@import "../assets/css/materialdesignicons.min.css";
@import "../assets/css/fullcalendar.css";
@import "../assets/css/main.css";
</style>
