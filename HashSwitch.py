import pysimplegui as sg

# Define the hashSwitch entry
hashSwitch = hbmenu.HBMenuEntry(
    name="hashSwitch",
    description="A homebrew app store for the Nintendo Switch",
    icon="icon.png",
    launch=launch_hashSwitch,
    id="hashSwitch"
)

# Launch hashSwitch
def launch_hashSwitch():
  # TODO: Implement the hashSwitch logic here
  print("hashSwitch launched!")

# Create a window
window = sg.Window("hashSwitch", layout=[[sg.Button("Launch hashSwitch")]])

# Event loop
while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED:
    break

  elif event == "Launch hashSwitch":
    launch_hashSwitch()

# Close the window
window.close()

# Add the hashSwitch entry to the hbmenu
hbmenu.add_entry(hashSwitch)

# Start the hbmenu
hbmenu.start()

# Wait for the user to press the A button before returning to the Atmosphere bootloader
while hbmenu.poll_input() != hbmenu.HBMENU_BUTTON_PRESS_A:
  pass

# Return to the Atmosphere bootloader
hbmenu.return_to_bootloader()
