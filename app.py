import streamlit as st
import json
import os

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()
st.title("📒 Contact Manager")
st.subheader("All Contacts")
if contacts:
    for name, info in contacts.items():
        st.write(f"**{name}** | {info['phone']} | {info['email']}")
else:
    st.write("No Contacts yet.")        

st.subheader("Add Contact")
name = st.text_input("Name")
phone = st.text_input("Phone")
email = st.text_input("Email")

if st.button("Add Contact"):
    if name and phone and email:
        contacts[name] = {"phone":phone,"email":email}
        save_contacts(contacts)
        st.success(name+" added!")
        st.rerun()
    else:
        st.error("Please fill all fields")    

st.subheader("Search Contact")
search = st.text_input("Search by name, phone or email")

if search:
    found = False
    for name, info in contacts.items():
        if search in name or search in info['phone'] or search in info['email']:
            st.write(f"**{name}** | {info['phone']} | {info['email']}")
            found = True
    if not found:
        st.write("No contact found")    

st.subheader("Delete COntact")
delete_name = st.selectbox("Select contact to delete", [""] + list(contacts.keys()))
if st.button("Delete"):
    if delete_name:
        contacts.pop(delete_name)
        save_contacts(contacts)
        st.success(delete_name + " deleted!")
        st.rerun()
    else:
        st.error("Please select a contact")     
                
st.subheader("Edit Contact")
edit_name = st.selectbox("Select contact to edit", [""] + list(contacts.keys()), key="edit")
if edit_name:
    new_phone = st.text_input("New phone", value=contacts[edit_name]['phone'])
    new_email = st.text_input("New email", value=contacts[edit_name]['email'])                
    if st.button("update"):
        contacts[edit_name]['phone'] = new_phone
        contacts[edit_name]['email'] = new_email
        save_contacts(contacts)
        st.success(edit_name + " updated!")
        st.rerun()