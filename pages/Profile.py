import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="images/me.png",
)
st.title("About the Creator")

# Gambar tim beserta universitas
team_data = {
    "Imroatu Solicah": {
        "university": "Universitas Stikubank",
        "image_path": "images/imroatu.png"  # Menggunakan path lokal
    },
}

# Menampilkan gambar dan deskripsi biodata berdampingan
for member, data in team_data.items():
    university = data["university"]
    image_path = data["image_path"]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(image_path, width=300)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 30px; font-weight: bold; padding-top: 20px">\
           Imroatu Solicah</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 18px; padding-bottom: 20px">Final year students of Stikubank University Semarang</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: justify; font-size: 18px">She is a final year student of Informatics Engineering Study Program at STIKUBANK University Semarang.\
             I have extensive experience in the field, starting from education at Vocational High School for 3 years, continued to College for 4 years, and completed with participation in the Field Work Practice program for 6 months and twice participated in the Independent Study Program of Merdeka Campus.\
             During my educational journey, I have gained a deep understanding of system development, system analysis, network security, artificial intelligence, machine learning, people management, and graphic design. I continue to push myself to learn and hone my skills in order to become a professional who is not only competent, but also ready to compete in a dynamic and ever-evolving world of work.</div>', unsafe_allow_html=True)
