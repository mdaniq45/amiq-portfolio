import streamlit as st
import smtplib
from email.message import EmailMessage

def send_email(name, email, message):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password
    receiver_email = "mohammad.amiq4@gmail.com"
    
    msg = EmailMessage()
    msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg["Subject"] = "New Contact Form Submission"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

st.set_page_config(page_title="Mohammad Amique Uzzama - Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Experience", "Education", "Skills", "Awards", "Contact"])

if page == "Home":
    st.title("Mohammad Amiq Uzzama")
    st.write("## 🔬 Experienced Laboratory Technician | Precision & Excellence in Diagnostics 🏥")
    st.write("With over 4 years of hands-on experience in laboratory testing, phlebotomy, and diagnostics, I am dedicated to delivering accurate and reliable results that enhance patient care.")
    
    st.write("🔹 Passionate about ensuring precise diagnostic outcomes through rigorous quality control and adherence to medical standards.")
    st.write("🔹 Proficient in advanced laboratory procedures, including hematology, serology, urinalysis, and blood banking.")
    st.write("🔹 Skilled in handling laboratory apparatus with expertise in infection control and sample analysis.")
    st.write("🔹 Adept at leveraging modern technology and laboratory information systems for efficiency and accuracy.")
    
    st.write("I thrive in fast-paced environments where attention to detail, analytical thinking, and a commitment to excellence are paramount. Always eager to learn and adopt new techniques, I continuously strive to improve my skills and contribute to the medical field in innovative ways.")

elif page == "Experience":
    st.header("Work Experience")
    st.subheader("Lab Technician - Ford Hospital and Research Center (2021-2025)")
    st.write("- Spearheaded high-precision laboratory diagnostics and state-of-the-art phlebotomy procedures, utilizing innovative techniques and automation to optimize accuracy, efficiency, and patient-centric healthcare solutions..")
    st.write("- Analyzed specimens for diagnostics and research.")
    st.write("- Maintained lab equipment and handled administrative duties.")

elif page == "Education":
    st.header("Education")
    st.write("**BMLT (2017 - 2020)** - Dr. Zakir Husain Institute, Patna, Tata Institute of Social Science, Mumbai")
    st.write("**Intermediate (2015 - 2017)** - B.S.E.B Patna")
    st.write("**Matriculation (2014 - 2015)** - B.S.E.B Patna")

elif page == "Skills":
    st.header("Skills")
    st.write("### Core Medical Skills")
    st.write("- DHA-Certified Medical Lab Technician")
    st.write("- Hematology, Biochemistry, Clinical Pathology, Immunology, Microbiology")
    st.write("- Blood Bank Testing, Bacteriology, Phlebotomy")
    
    st.write("### Laboratory & Technical Skills")
    st.write("- Ensuring Lab Accuracy, Safety & Quality")
    st.write("- Laboratory Apparatus Handling")
    st.write("- Specimen Collection & Analysis")
    st.write("- Infection Control & Quality Assurance")
    
    st.write("### Software & Tools")
    st.write("- Windows, MS Office, Excel")
    st.write("- Laboratory Information Systems (LIS)")
    st.write("- Electronic Medical Records (EMR)")

elif page == "Awards":
    st.header("Awards & Achievements")
    st.write("🏆 Best Employee of the Year (2023)")
    st.write("🏆 Corona Warrior Award for Covid-19 Contributions")
    st.write("🏆 First Prize in Cricket Tournament")

elif page == "Contact":
    st.header("Contact Me")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        if name and email and message:
            send_email(name, email, message)
            st.success("Message sent successfully!")
        else:
            st.error("Please fill in all fields.")
