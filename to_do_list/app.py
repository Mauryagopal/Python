import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="To-Do List", page_icon="✅", layout="centered")

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .task {
            font-size: 20px;
            margin: 10px 0;
        }
        .stButton>button {
            border-radius: 10px;
            height: 3em;
            width: 100%;
            margin-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Session State for Tasks ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "completed" not in st.session_state:
    st.session_state.completed = []

# --- App Title ---
st.markdown('<p class="title">📝 To-Do List</p>', unsafe_allow_html=True)

# --- Add Task ---
new_task = st.text_input("Add a new task:")
if st.button("➕ Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Task cannot be empty!")

st.divider()

# --- Display Tasks ---
if st.session_state.tasks:
    st.subheader("Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([6,1,1])
        with col1:
            st.markdown(f'<p class="task">✅ {task}</p>', unsafe_allow_html=True)
        with col2:
            if st.button("✔️", key=f"done_{i}"):
                st.session_state.completed.append(task)
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
        with col3:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
else:
    st.info("No tasks yet! Add one above ⬆️")

st.divider()

# --- Completed Tasks ---
if st.session_state.completed:
    st.subheader("✅ Completed Tasks")
    for task in st.session_state.completed:
        st.markdown(f"- ~~{task}~~")

