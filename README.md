# Yolo-V3-Image-sorter-GUI

To get the Crack detection interface working, we first need to download a few dependencies.

->pip3 install Pillow

->sudo apt-get install python3-pil python3-pil.image

->apt-get install python-tk

->sudo apt-get install python-imaging python-imaging-tk

Now we can proceed to install the GUI and the Image Viewer from the GitHub directory:

https://github.com/MUNE35H/Yolo-V3-Image-sorter-GUI.git 

Paste the link in your browser and download this repository as a zip file. You can do this by clicking the drop down bar on the green button "code" and "Download ZIP"

Next, Extract the zip file to your "Home" directory and place the "Crack UI" and "imageviewer" files into the home directory and the "Crack Detection Menu.desktop" to your desktop and NOT all together under the "Yolo-V3-Image-sorter-Gui-main"

Now run these commands to set up the image viewer

 -> cd imageviewer

 -> pip install -r requirements.txt

 -> apt-get install python3-tk

Now that we have all the files in the proper location, we can configure the interface into how we like it.


Configuration of the Python GUI:

Open the CrackUI folder and open the YOLO_GUI.py script. You should see the tkinter programming done by us. The part where you need to take note of is the crack detection as if you use a different model for detection, you need to edit this location.

Scroll down to line 41. You should see the code which you would normally key into your terminal. IF you are running a different model with a different name or config file, replace the new information in that line

NOTE: Remember to put the & after the command line as it is required to ensure your GUI does not get stuck in 1 command.

SIMILARLY, scroll to line 56 and replace the old command with your new one you replaced in line 41.

                                                       END OF GUI CONFIGURATION

Configuration of python Image sorter:

Open the imageviewer folder and open the file called "settings.py" 

Inside the python code, scroll to line 14 and under the source directory, you want to have the location of where the screenshots of your crack images are located. Currently, it is located as "/home/eee/darknet-yolo/screenshot".

                                                      END OF IMAGE SORTER CONFIGURATION

Now that everything has been configured, we can launch the GUI by simply just clicking the desktop icon lablled "Crack Detection Menu.desktop". and the crack detection should start by clicking the start button.

                                                      HOW TO USE THE IMAGE SORTER

Once the image sorter has been successfully set up, you can either open the GUI and click on the eye icon or manually input "python3 image_viewer.py" into the command terminal to launch the sorter. Once opened, an image of the detected crack should show up. Use the left and right arrow keys to scroll through the images.

Now, for a use case scenario, press "1" on your keyboard to send the image to the delete file if you find that the image is not up to standard or if it is a duplicate. Press "2" on you keyboard to send the image to the "Good" file. These two files can be found in the screenshot folder of the darknet-yolo path itself.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you need to edit the file path of the GUI python code to allow the desktop icon to launch it, right click the desktop icon and open it with text editor. This will allow you to change edit the code used to launch the application.

Credits for the Imageviewer goes to josvromans 
Link to imageviewer: https://github.com/josvromans/imageviewer/blob/master/image_viewer.py













 












 







 
