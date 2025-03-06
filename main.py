import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Streamlit App", page_icon="🌟", layout="wide")

# สร้าง Sidebar สำหรับ Navigation
st.sidebar.title("Menu Navigation Bar")  # ชื่อ Sidebar
page = st.sidebar.selectbox("Choose a page", ["Main", "Login", "About", "Contact"])

# หน้า Main
if page == "Main":
    st.title("🏠 Welcome to the Main Page")

    # แสดงโค้ด Python ด้วย st.echo()
    with st.echo():
        st.title('Getting Started with Streamlit')
        st.write('This is an introduction to Streamlit')

        st.markdown('## Code Example')
        code = '''
        def hello():
            print("Hello, Streamlit!")
        '''

        show_btn = st.button('Show code!')
        if show_btn:
            st.code(code, language="python")

        # แบ่ง Column ออกเป็น 2 ส่วน
        cols = st.columns(2)

        # ส่วนที่ 1: รับค่าอายุ
        with cols[0]:
            age_inp = st.number_input("Input your age")
            st.markdown(f'Your age is **{age_inp}**')

        # ส่วนที่ 2: Tokenize ข้อความ
        with cols[1]:
            text_inp = st.text_input("Enter your text here")
            word_tokensize = " | ".join(text_inp.split())
            st.markdown(f"Tokenized: **{word_tokensize}**")

        # แสดง DataFrame และ Chart
        df = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 60, 90]
        })

        st.dataframe(df)

        show_plot_btn = st.button('Show Chart!!')
        if show_plot_btn:
            st.line_chart(df, x='first column', y='second column')

# หน้า Login
elif page == "Login":
    st.title("🔐 Login Page")
    st.write("Please enter your username and password")

    # ฟังก์ชันตรวจสอบล็อกอิน
    def check_login(username, password):
        valid_users = {"admin": "1234", "user": "password"}
        return username in valid_users and valid_users[username] == password

    # ใช้ session_state เพื่อตรวจสอบสถานะล็อกอิน
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # ถ้ายังไม่ล็อกอิน ให้แสดงหน้า Login
    if not st.session_state.logged_in:
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")

        if st.button("Login"):
            if check_login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.experimental_rerun()  # รีเฟรชหน้าใหม่
            else:
                st.error("Invalid username or password")

    # ถ้าล็อกอินแล้ว ให้แสดงเนื้อหาหลัก
    else:
        st.title("🎉 Welcome!")
        st.write(f"Hello, **{st.session_state.username}**! You are now logged in.")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()

# หน้า About
elif page == "About":
    st.title("ℹ️ About Page")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=250)  
    st.markdown("### About This App")
    st.write("This is a simple web application built with Streamlit. It demonstrates how to create multiple pages, handle login authentication, and display interactive components.")

    st.markdown("### About the Developer")
    st.info("👨‍💻 Developed by: John Doe")
    st.write("📧 Email: johndoe@example.com")
    st.write("🌍 Website: [johndoe.dev](https://johndoe.dev)")
    st.write("📌 GitHub: [github.com/johndoe](https://github.com/johndoe)")

# หน้า Contact
elif page == "Contact":
    st.title("📞 Contact Page")
    st.markdown("## Get in Touch")
    
    # แสดงข้อมูลติดต่อ
    st.write("📧 Email: contact@example.com")
    st.write("📞 Phone: +66 987-654-321")
    st.write("🌍 Website: [example.com](https://example.com)")

    # Social Media Links
    st.markdown("""
    **Follow us on:**
    - [Facebook](https://facebook.com/example)
    - [Twitter](https://twitter.com/example)
    - [LinkedIn](https://linkedin.com/in/example)
    """)

    # แบบฟอร์มติดต่อ
    st.markdown("## Contact Form")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully.")
            else:
                st.error("⚠️ Please fill in all the fields before submitting.")
