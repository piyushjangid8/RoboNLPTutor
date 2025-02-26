import streamlit as st

st.set_page_config(page_title="Learning Resources", page_icon="📚")

st.title("📚 Learning Resources")

# Resource categories
categories = {
    "Python Programming": [
        {"name": "Python Documentation", "url": "https://docs.python.org/3/"},
        {"name": "Real Python Tutorials", "url": "https://realpython.com/"}
    ],
    "Data Science": [
        {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"},
        {"name": "DataCamp", "url": "https://www.datacamp.com/"}
    ],
    "Robotics": [
        {"name": "ROS Tutorials", "url": "http://wiki.ros.org/ROS/Tutorials"},
        {"name": "MIT OpenCourseWare Robotics", "url": "https://ocw.mit.edu/courses/mechanical-engineering/2-12-introduction-to-robotics-fall-2005/"}
    ]
}

# Display resources by category
for category, resources in categories.items():
    st.header(category)
    
    for resource in resources:
        with st.container():
            col1, col2 = st.columns([0.8, 0.2])
            
            with col1:
                st.write(f"🔗 [{resource['name']}]({resource['url']})")
            
            with col2:
                st.link_button("Visit", resource['url'])
    
    st.divider()

# Additional resources section
st.header("📱 Recommended Tools")
tools = [
    "Visual Studio Code - Popular code editor",
    "Jupyter Notebooks - Interactive computing",
    "Git - Version control system",
    "ROS - Robot Operating System"
]

for tool in tools:
    st.write(f"- {tool}")
