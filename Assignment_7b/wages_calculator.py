# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This program calculates the user's approximate hourly, daily, weekly, monthly and yearly wages and then 
# shows them to the user

import ui
import dialogs

# constants and variables
AVG_DAILY_HOURS = 8.0
AVG_WORK_WEEK_DAYS = 5.0
WEEKS_IN_YEAR = 52.0
AVG_WEEKS_IN_MONTH = WEEKS_IN_YEAR/12.0

wages_history = []

def calculate_button_touch_up_inside(sender):
    # Calculates wages; returns and shows them to user
    
    global wages_history
    
    # input
    hourly_wage = float(view['hourly_wage_textfield'].text)
    
    # process
    if hourly_wage < 0:
        view['wages_output_textview'].text = "Please input a positive value."
    else:
        daily_wage = hourly_wage * AVG_DAILY_HOURS
        weekly_wage = daily_wage * AVG_WORK_WEEK_DAYS
        monthly_wage = weekly_wage * AVG_WEEKS_IN_MONTH
        yearly_wage = weekly_wage * WEEKS_IN_YEAR
        
        wages_history.extend([hourly_wage, daily_wage, weekly_wage, monthly_wage, yearly_wage])
        
        # output
        view['wages_output_textview'].text = "Hourly Wage:\t\t\t" + '${:,.2f}'.format(hourly_wage) + "\n" + "Daily Wage:\t\t\t\t" +  '${:,.2f}'.format(daily_wage) + "\n" + "Weekly Wage:\t\t\t" + '${:,.2f}'.format(weekly_wage) + "\n" + "Monthly Wage:\t\t\t" + '${:,.2f}'.format(monthly_wage) + "\n" + "Yearly Wage:\t\t\t" + '${:,.2f}'.format(yearly_wage)
        
        view['hourly_wage_textfield'].text = ""

def view_history_button_touch_up_inside(sender):
    # This shows the user the wage calculations they've done and gotten so far
    view['history_title_label'].hidden = False
    view['wages_history_textview'].hidden = False
    view['view_back_button'].hidden = False
    
    view['info_button'].enabled = False
    view['clear_history_button'].enabled = False
    view['calculate_button'].enabled = False
    
    if len(wages_history) == 0:
        view['wages_history_textview'].text = "You haven't entered anything."
    else:
        for wage in wages_history:
            view['wages_history_textview'].text = view['wages_history_textview'].text + "\n" + '${:,.2f}'.format(wage) + "\n"
        
def view_back_button_touch_up_inside(sender):
    # Hides view history scene; "returns" user to calculator scene
    view['view_back_button'].hidden = True
    view['history_title_label'].hidden = True
    view['wages_history_textview'].hidden = True
    
    view['info_button'].enabled = True
    view['clear_history_button'].enabled = True
    view['calculate_button'].enabled = True

def clear_history_button_touch_up_inside(sender):
    # This clears the current history of wage calculations they've done so far
    global wages_history
    
    warning = dialogs.alert(title = "Are you sure?",
                            message = "By clearing your wages history, you'll be clearing the history of calculations you've done so far.",
                            button1 = "Yes",
                            button2 = "No",
                            hide_cancel_button = True)
    if warning == 1:
        wages_history = []
    else:
        pass

def info_button_touch_up_inside(sender):
    # Shows user the more information screen
    view['info_title_label'].hidden = False
    view['information_textview'].hidden = False
    view['info_back_button'].hidden = False
    
    view['view_history_button'].enabled = False
    view['clear_history_button'].enabled = False
    view['calculate_button'].enabled = False

def info_back_button_touch_up_inside(sender):
    # Hides info scene; "returns" user to calculator scene
    view['information_textview'].hidden = True
    view['info_title_label'].hidden = True
    view['info_back_button'].hidden = True
    
    view['view_history_button'].enabled = True
    view['clear_history_button'].enabled = True
    view['calculate_button'].enabled = True

view = ui.load_view()
view['hourly_wage_textfield'].keyboard_type = ui.KEYBOARD_NUMBERS
view['wages_history_textview'].hidden = True
view['history_title_label'].hidden = True
view['view_back_button'].hidden = True
view['information_textview'].hidden = True
view['info_title_label'].hidden = True
view['info_back_button'].hidden = True
view.present('full_view')
