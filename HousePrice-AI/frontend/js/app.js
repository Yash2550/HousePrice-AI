// Minimal JS to handle form validation and demo submit behavior.
// Forms will not actually send to a server by default — they simulate success messages.
// To connect to a backend, replace the "simulate" blocks with fetch() calls to your API.

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const signupForm = document.getElementById("signup-form");
  const contactForm = document.getElementById("contact-form");

  if (loginForm) setupLogin(loginForm);
  if (signupForm) setupSignup(signupForm);
  if (contactForm) setupContact(contactForm);
});

function showMessage(el, text, type = "success") {
  el.textContent = text;
  el.classList.remove("success", "error");
  el.classList.add(type);
}

function setupLogin(form) {
  const msg = document.getElementById("login-message");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const payload = Object.fromEntries(data.entries());

    // Basic validation
    if (!payload.email || !payload.password) {
      showMessage(msg, "Please enter email and password.", "error");
      return;
    }

    // Demo: simulate a server response
    showMessage(msg, "Logging in...", "success");
    setTimeout(() => {
      // For demo only: accept any password of length >=6
      if (payload.password.length >= 6) {
        showMessage(msg, "Login successful — demo only (no backend).", "success");
        // You could set localStorage token here after real auth: localStorage.setItem('token', '...')
      } else {
        showMessage(msg, "Invalid credentials (demo validation).", "error");
      }
    }, 500);
  });
}

function setupSignup(form) {
  const msg = document.getElementById("signup-message");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const payload = Object.fromEntries(data.entries());

    if (!payload.name || !payload.email || !payload.password || !payload.confirm_password) {
      showMessage(msg, "Please fill all fields.", "error");
      return;
    }
    if (payload.password.length < 6) {
      showMessage(msg, "Password must be at least 6 characters.", "error");
      return;
    }
    if (payload.password !== payload.confirm_password) {
      showMessage(msg, "Passwords do not match.", "error");
      return;
    }

    showMessage(msg, "Creating account...", "success");
    setTimeout(() => {
      // Demo: pretend account created
      showMessage(msg, "Account created (demo only). You can now log in.", "success");
      form.reset();
    }, 700);
  });
}

function setupContact(form) {
  const msg = document.getElementById("contact-message");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const payload = Object.fromEntries(data.entries());

    if (!payload.name || !payload.email || !payload.message) {
      showMessage(msg, "Please complete all fields.", "error");
      return;
    }

    showMessage(msg, "Sending message...", "success");
    setTimeout(() => {
      // Demo: pretend message sent
      showMessage(msg, "Thank you — message sent (demo only).", "success");
      form.reset();
    }, 700);
  });
}