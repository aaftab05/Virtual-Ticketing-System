import streamlit as st
import random

class StadiumBookingSystem:
    def __init__(self):
        self.total_income = 0
        self.total_seats = 0
        self.booked_seats = 0
        self.booked_ticket_person = []
        self.seat_chart = []
        self.matches_cricket = {}
        self.matches_basketball = {}
        self.matches_football = {}

    def add_match_cricket(self, match_name, match_function):
        self.matches_cricket[match_name] = match_function

    def add_match_basketball(self, match_name, match_function):
        self.matches_basketball[match_name] = match_function

    def add_match_football(self, match_name, match_function):
        self.matches_football[match_name] = match_function

    def book_tickets(self, match_name, num_seats):
        st.write(f"Booking {num_seats} tickets for {match_name}...")
        # Placeholder for booking logic
        pass

    def store_booking_details(self, match_name, num_seats, user_details):
        # Placeholder for storing booking details
        pass

    def collect_user_details(self):
        user_details = {}
        user_details['Name'] = st.text_input("Enter your name:")
        user_details['Email'] = st.text_input("Enter your email:")
        user_details['Phone'] = st.text_input("Enter your phone number:")
        return user_details

    def main(self):
        st.write("## Select a sport to book tickets")
        sport_selected = st.radio("Select a sport:", ("Cricket", "Basketball", "Football"))

        if sport_selected == "Cricket":
            if self.matches_cricket:
                st.image("C:/Users/DELL/Downloads/cricket.jpg", use_column_width=False, width=200)
                self.show_matches("Cricket")
            else:
                st.write("No cricket matches available.")
        elif sport_selected == "Basketball":
            if self.matches_basketball:
                st.image("C:/Users/DELL/Downloads/basketball.jpg", use_column_width=False, width=200)
                self.show_matches("Basketball")
            else:
                st.write("No basketball matches available.")
        elif sport_selected == "Football":
            if self.matches_football:
                st.image("C:/Users/DELL/Downloads/football.jpg", use_column_width=False, width=200)
                self.show_matches("Football")
            else:
                st.write("No football matches available.")

    def show_matches(self, sport):
        if sport == "Cricket" and self.matches_cricket:
            st.write("## Cricket Matches")
            selected_cricket_match = st.selectbox("Select a cricket match to book tickets for:", list(self.matches_cricket.keys()))
            if st.button("Select Cricket Match"):
                match_selected = self.matches_cricket[selected_cricket_match]
                num_seats = st.number_input("Enter the number of seats:", min_value=1, max_value=10, value=1)
                match_selected(selected_cricket_match, num_seats)
        elif sport == "Basketball" and self.matches_basketball:
            st.write("## Basketball Matches")
            selected_basketball_match = st.selectbox("Select a basketball match to book tickets for:", list(self.matches_basketball.keys()))
            if st.button("Select Basketball Match"):
                match_selected = self.matches_basketball[selected_basketball_match]
                num_seats = st.number_input("Enter the number of seats:", min_value=1, max_value=10, value=1)
                match_selected(selected_basketball_match, num_seats)
        elif sport == "Football" and self.matches_football:
            st.write("## Football Matches")
            selected_football_match = st.selectbox("Select a football match to book tickets for:", list(self.matches_football.keys()))
            if st.button("Select Football Match"):
                match_selected = self.matches_football[selected_football_match]
                num_seats = st.number_input("Enter the number of seats:", min_value=1, max_value=10, value=1)
                match_selected(selected_football_match, num_seats)
        else:
            st.write(f"No {sport.lower()} matches available.")

        prize_of_ticket = 0
        Total_Income = 0
        Row = st.sidebar.number_input(f'Enter number of Row for {sport}', min_value=1, value=5, key=f'row_input_{sport.lower()}')
        Seats = st.sidebar.number_input(f'Enter number of seats in a Row for {sport}', min_value=1, value=10, key=f'seats_input_{sport.lower()}')
        Total_seat = Row * Seats
        Booked_seat = 0
        Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

        class Chart:
            @staticmethod
            def chart_maker(Booked_seat):
                seats_chart = {}
                selected_seats = set()
                # Make first two seats in the first two rows permanently booked
                for i in range(2):
                    for j in range(2):
                        selected_seats.add((i, j))
                        Booked_seat += 1

                for i in range(Row):
                    seats_in_row = {}
                    for j in range(Seats):
                        if (i, j) in selected_seats:
                            seats_in_row[str(j+1)] = 'B'  # Booked seat
                        else:
                            seats_in_row[str(j+1)] = 'S'  # Empty seat
                    seats_chart[str(i)] = seats_in_row
                return seats_chart, Booked_seat

            @staticmethod
            def find_percentage(Booked_seat):
                percentage = (Booked_seat/Total_seat)*100
                return percentage

        class_call = Chart

        x = 1
        option_counter = 0
        while x != 0:
            option_counter += 1
            option_key = f'option_input_{option_counter}'
            st.write('1 for Select Randomly \n')
            st.write('2 for Seat Selection and ticket booking \n')
            st.write('3 for Statistics \n')
            st.write('4 for Show booked Tickets User Info')
            x = st.number_input('Select Option', min_value=0, max_value=4, step=1, key=option_key)

            if x == 1:
                st.write('Stadium View:')
                table_of_chart, Booked_seat = class_call.chart_maker(Booked_seat)
                for i in range(Row):
                    row_seats = ''
                    for j in range(Seats):
                        if table_of_chart[str(i)][str(j+1)] == 'S':
                            row_seats += '◻️ '  # Empty seat
                        else:
                            row_seats += '◼️ '  # Booked seat
                    st.write(row_seats)
                st.write('Selecting Randomly...')
                st.write('Proceed to payment details')
                # Placeholder for payment details

            elif x == 2:
                st.write('Selecting Seats Row and Column Wise:')
                Row_number = st.number_input('Enter Row Number', min_value=1, max_value=Row, key='row_number_input_2')
                Column_number = st.number_input('Enter Column Number', min_value=1, max_value=Seats, key='column_number_input_2')
                st.write('Stadium View:')
                table_of_chart, Booked_seat = class_call.chart_maker(Booked_seat)
                for i in range(Row):
                    row_seats = ''
                    for j in range(Seats):
                        if table_of_chart[str(i)][str(j+1)] == 'S':
                            row_seats += '◻️ '  # Empty seat
                        else:
                            row_seats += '◼️ '  # Booked seat
                    st.write(row_seats)
                if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
                    if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                        if Row*Seats <= 60:
                            prize_of_ticket = 10
                        elif Row_number <= int(Row/2):
                            prize_of_ticket = 5000
                        else:
                            prize_of_ticket = 500
                        st.write('prize_of_ticket - ', '$', prize_of_ticket)
                        conform = st.selectbox('Booking Confirmation', ['yes', 'no'], key='confirmation_input_2')
                        person_detail = {}
                        if conform == 'yes':
                            person_detail['Name'] = st.text_input('Enter Name', key='name_input_2')
                            person_detail['Gender'] = st.selectbox('Select Gender', ['Male', 'Female', 'Other'], key='gender_input_2')
                            person_detail['Age'] = st.number_input('Enter Age', min_value=1, key='age_input_2')
                            person_detail['Phone_No'] = st.text_input('Enter Phone number', key='phone_input_2')
                            person_detail['Payment Method'] = st.selectbox('Payment Method', ['Credit Card', 'Debit Card', 'PayPal'], key='payment_method_input_2')
                            person_detail['Card Number'] = st.text_input('Enter Card Number', key='card_number_input_2')
                            person_detail['Expiry Date'] = st.text_input('Enter Expiry Date', key='expiry_date_input_2')

                            payment_done = st.checkbox('Payment Done')
                            if payment_done:
                                if all(person_detail.values()):
                                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                                    Booked_seat += 1
                                    Total_Income += prize_of_ticket
                                    st.success('Booking Successfully')
                                else:
                                    st.warning("Please enter all details to proceed with booking.")
                            else:
                                st.warning('Payment not completed. Booking unsuccessful.')

                        else:
                            continue
                        Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                        st.button("Submit")
                        
                    else:
                        st.error('This seat already booked by someone')
                else:
                    st.error('***    ***')

            elif x == 3:
                st.write('Number of purchased Ticket - ', Booked_seat)
                st.write('Percentage - ', class_call.find_percentage(Booked_seat))
                st.write('Current  Income - ', '$', prize_of_ticket)
                st.write('Total Income - ', '$', Total_Income)

            elif x == 4:
                st.write('Show booked Tickets User Info:')
                # Placeholder for displaying booked tickets user info

            else:
                st.error('***   ***')

if __name__ == "__main__":
    stadium_booking_system = StadiumBookingSystem()
    
    # Add cricket matches
    stadium_booking_system.add_match_cricket("Match 1", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_cricket("Match 2", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_cricket("Match 3", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_cricket("Match 4", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_cricket("Match 5", stadium_booking_system.book_tickets)
    
    # Add basketball matches
    stadium_booking_system.add_match_basketball("Match 1", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_basketball("Match 2", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_basketball("Match 3", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_basketball("Match 4", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_basketball("Match 5", stadium_booking_system.book_tickets)
    
    # Add football matches
    stadium_booking_system.add_match_football("Match 1", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_football("Match 2", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_football("Match 3", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_football("Match 4", stadium_booking_system.book_tickets)
    stadium_booking_system.add_match_football("Match 5", stadium_booking_system.book_tickets)
    
    stadium_booking_system.main()
