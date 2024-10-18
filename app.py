import streamlit as st

def check_balance():
    st.write(f"Your current balance is : ${st.session_state.balance}")
#function to deposit money
def deposit(amount):
    st.session_state.balance += amount
    st.write(f"${amount} is deposited successfully!")
    check_balance()
#function to withdraw money
def withdraw(amount):
    if amount > st.session_state.balance:
        st.error("insufficient balance!")
    else:
        st.session_state.balance -= amount
        st.write(f"${amount} withdrawn successfully!")
        check_balance()

#streamlit app layout 
def main():
    st.title("Web Banking Application!")
    st.sidebar.title("MENU")

    if 'balance' not in st.session_state:
        st.session_state.balance = 1000
    menu = ['Check Balance','Deposit','Withdraw']
    choice = st.sidebar.selectbox("SELECT AN OPTION",menu)

    if choice == "Check Balance":
        st.subheader("Check your balance")
        check_balance()
    elif choice == "Deposit":
        st.subheader("Deposit Money")
        amount = st.number_input("Enter deposit amount",min_value=1)
        if st.button("DEPOSIT"):
            deposit(amount)
    elif choice == "Withdraw":
        st.subheader("Withdraw Money")
        amount = st.number_input("Enter withdrawal amount",min_value=1)
        if st.button("WITHDRAW"):
            withdraw(amount)
#run and initialize the app
if __name__ == '__main__':
    main()
