import tkinter as tk
import tkinter.messagebox 
from customtkinter import *
from PIL import ImageTk, Image
import random
import requests
import urllib.request
import io
import winsound

# ---------------- GLOBAL VARIABLES ----------------

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a").json()

winsound.PlaySound('.\\media\\Snowfall.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
# Song is from Va-11 Hal-A by Garoad

itemList = ['Select your drink.',]

allDrinks = []
for item in response['drinks']:
    allDrinks.append(item['strDrink'])

itemList.append(allDrinks)

introDialog = ["Hi there! First time here?", 
               "Welcome to the Quiet Hollow, how may we serve you today?", 
               "You're a new face, what can I get ya?"]

talkDialog = ["This bar doesn't only sell alcoholic drinks, you should also check out the non alcoholic ones!",
              "Remember to always check if you're allergic to the drink's ingredients.",
              "A&T is simply refreshing, easy to make as well if you have the ingredients.",
              "The Algonquin is a new York Classic!",
              "Afterglow is rather basic but it's famous for mimicking 'Sunrise' cocktails.",
              "Avalanche is my personal favorite."
            ]

ViewAllDialog = ["Undecided? Well we got a wide variety of drinks, just choose whatever sticks out to you!",
                "You wanna see all of the drinks? Sure, go ahead!",
                "The menu? Here it is. Tell me what you would like today!"]

randomDrinkDialog = ["You want to spice it up a bit? Alright, here's what I got",
                    "Let's see if you get what you want!",
                    "Hmm? You want my choice? Alright, today's special is...",
                    "Leaving it to lady luck huh? Lets hope you get a good one!"]

specificDrinkDialog = ["Are you sure you want this? There are other drinks.",
                       "Good choice! I would have the same if I wasn't on duty",
                       "Anything else to go along with that?",
                       "Hmm, okay coming right up!",
                       "Lemme check the stock... looks like there's still more!"]

# This class inherits the window where the application can be seen
class App(CTk):
    # __init__ method is used to create/initialize objects of the given class.
    def __init__(self):
        """ This function is used to initialize the application's
        main container and some global functions. """

        # This returns any methods and properties inside the definition to the parent class.
        super().__init__()

        # ---------------- BASIC APP LAYOUT ----------------

        # This specifies the width and height of the window.
        self.geometry("1000x600")
        # This disables the resizability of the window
        self.resizable(0, 0)
        # This creates a title for the application.
        self.title("The Quiet Hollow")
        # This creates the app's icon.
        self.iconbitmap("./media/AppIcon.ico")

        # ---------------- Frames Settings ----------------

        """ This is used to create a frame to easily configure other frames """

        self.container = CTkFrame(self, width=1100, height=700)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
        
        # ---------------- Frames Viewer ----------------

        self.frames = {}
        
        # This creates a list of each frame.
        for F in (TitlePage, InstructionPage, MainPage):
            frame = F(self.container, self)

            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky="nsew")
        
        # This calls the function which uses the list from before.c
        self.show_frame(TitlePage)

    def show_frame(self, cont):
        """ This function is used to switch around the current 
            page of the application. """

        # This finds the selected layer using a specified parameter.
        self.frame = self.frames[cont]
        # raises the current frame to the top layer.
        self.frame.lift()

class TitlePage(CTkFrame):
    """ This class is used to display the titlepage frame. """

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        self.configure(fg_color="#23272d")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        
        self.Title = CTkLabel(self, 
                            text="The Quiet Hollows", 
                            font=("New Times Roman", 40),
                            text_color=("#f3f3f3")
                        )
        self.Title.grid(column=0, columnspan=2, row=0, sticky="s")

        self.instructionButton = CTkButton(self,
                                        width=170,
                                        height=40,
                                        corner_radius=5,
                                        border_width=1,
                                        border_spacing=5,
                                           
                                        fg_color=("#23272d"),
                                        hover_color=("#37373d"),
                                        border_color=("#047bd9"),
                                        text_color=("#f3f3f3"),
                                           
                                        text="Instruction",
                                        font=("saveur-sans-regular", 15),

                                        command=lambda: controller.show_frame(InstructionPage)
                                    )            
        self.instructionButton.grid(column=0, row=1, padx=165, pady=10, sticky="w")

        self.mainMenuButton = CTkButton(self,
                                        width=170,
                                        height=40,
                                        corner_radius=5,
                                        border_width=1,
                                        border_spacing=5,
                                        
                                        fg_color=("#23272d"),
                                        hover_color=("#37373d"),
                                        border_color=("#047bd9"),
                                        text_color=("#f3f3f3"),
                                        
                                        text="Continue",
                                        font=("saveur-sans-regular", 15),
                                        command=lambda: controller.show_frame(MainPage)
                                    )
        self.mainMenuButton.grid(column=1, row=1, padx=165, pady=10, sticky="w")

class InstructionPage(CTkFrame):
    """ This class is used to display the instructions. """
    
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        self.configure(fg_color="#23272d")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 2), weight=1)

        self.Title = CTkLabel(self,
                            text="Instructions",
                            font=("New Times Roman", 40),
                            text_color=("#f3f3f3")
                            )
        self.Title.grid(column=0, row=0, sticky="s", pady=50)

        self.Content = CTkLabel(self,
                            text="""Hello! Welcome to The Quiet Hollows, an application used for viewing several cocktails 
                            \ninside the CocktailDB API. Which you can find here. 
                            \nhttps://www.thecocktaildb.com/
                            \nMouse controls are used to navigate. Click the continue button to begin. Have fun!""",
                            font=("New Times Roman", 17),
                            text_color=("#f3f3f3")
                            )
        self.Content.grid(column=0, row=1, sticky="n")

        self.mainMenuButton = CTkButton(self,
                                        width=170,
                                        height=40,
                                        corner_radius=5,
                                        border_width=1,
                                        border_spacing=5,
                                        
                                        fg_color=("#23272d"),
                                        hover_color=("#37373d"),
                                        border_color=("#047bd9"),
                                        text_color=("#f3f3f3"),
                                        
                                        text="Continue",
                                        font=("saveur-sans-regular", 15),
                                        command=lambda: controller.show_frame(MainPage)
                                    )
        self.mainMenuButton.grid(column=0, row=2, pady=25)

class MainPage(CTkFrame):
    """ This class is used to display the main content of this
    assessment, where the user will be viewing cocktails with
    the cocktailAPI. """

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        
        OutputFrm = CTkFrame(self, height=270, corner_radius=0, fg_color="#23272d")
        OutputFrm.pack(side='bottom', fill="x")

        # Propagate prevents elements from using all of the unused space in the frame.
        OutputFrm.grid_propagate(0)
        OutputFrm.grid_columnconfigure((1, 2, 3, 4), weight=2)
        OutputFrm.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.TestMessage = CTkLabel(OutputFrm, 
            text='Click on one of the top-left buttons to start.',
            corner_radius=0,
            text_color='white')
        self.TestMessage.grid(column=0, columnspan=5, row=0, rowspan=6)
        
        AppMenuFrm = CTkFrame(self, width=380, corner_radius=0, fg_color="#5d6775")
        AppMenuFrm.pack(side='left', fill="y")

        AppMenuFrm.grid_propagate(0)
        AppMenuFrm.grid_columnconfigure((0, 1, 2), weight=1)
        AppMenuFrm.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        CTkLabel(AppMenuFrm,
            corner_radius=0,

            text='The Quiet Hollow',
            font=("saveur-sans-regular", 22),
            text_color=("#f3f3f3")
        ).grid(column=0, columnspan=3, row=0, sticky='nsw', padx=15)

        self.musicButton = CTkButton(AppMenuFrm,
                                     width = 60,
                                     height = 30,
                                     corner_radius=0,

                                     text='Mute Music',
                                     font=("saveur-sans-regular", 15),

                                     command=lambda:self.musicSwitch()
        )
        self.musicButton.grid(column=0, columnspan=3, row=0, sticky='e', padx=15)
        
        self.viewAll = CTkButton(AppMenuFrm,
            corner_radius=0,
            text='View All Drinks',

            command=lambda:self.ViewAll(OutputFrm, filter_var)
        ).grid(column=0, columnspan=3, row=1)

        self.getRandom = CTkButton(AppMenuFrm,
            corner_radius=0,
            text='Get Random Drink',
            text_color=("#f3f3f3"),

            command= lambda:self.ViewRandom(OutputFrm)
        ).grid(column=0, columnspan=3, row=2)

        self.getSpecific = CTkButton(AppMenuFrm,
            corner_radius=0,

            text='Get Specific Drink',
            text_color=("#f3f3f3"),

            command=lambda:self.ViewSpecific(OutputFrm, specificResponseName=self.drinkChoice_var.get())
        ).grid(column=0, columnspan=3, row=3, sticky='w', padx=15)

        self.drinkChoice_var = StringVar(value='')

        self.specificDrink = CTkComboBox(AppMenuFrm, 
                                        values=allDrinks, 
                                        variable=self.drinkChoice_var)
        self.specificDrink.grid(column=0, columnspan=3, row=3, sticky='e', padx=15)

        CTkLabel(AppMenuFrm,
            corner_radius=0,

            text='Filters',
            font=("saveur-sans-regular", 20),
            text_color=("#f3f3f3")
        ).grid(column=0, row=4, sticky='w', padx=15)

        # This filter variable changes based on the user's current filter
        # Though, it only affects the view all function.
        filter_var = IntVar(value=0)

        filter1 = CTkRadioButton(AppMenuFrm, 
                             text="No Filter",
                             text_color=("#f3f3f3"),

                             variable=filter_var,
                             value=0)
        filter1.grid(column=0, row=5, sticky='new', padx=15)

        filter2 = CTkRadioButton(AppMenuFrm, 
                             text="Alcoholic",
                             text_color=("#f3f3f3"),

                             variable=filter_var,
                             value=1)
        filter2.grid(column=1, row=5, sticky='new', padx=15)

        filter3 = CTkRadioButton(AppMenuFrm, 
                             text="No Alcohol",
                             text_color=("#f3f3f3"),

                             variable=filter_var,
                             value=2)
        filter3.grid(column=2, row=5, sticky='new', padx=15)

        DisplayFrm = CTkFrame(self, width=620, corner_radius=0, fg_color="#9bb2d4")
        DisplayFrm.pack(side='right', fill="y")

        self.bg_image = CTkImage(Image.open(".\\media\\DisplayFrame.png"), size=(620, 330))
        self.bg_image_label = CTkLabel(DisplayFrm, image=self.bg_image, text="")
        self.bg_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # bind is used to add commands to labels and other widgets.
        self.bg_image_label.bind('<Button-1>', lambda event: self.BartendDialog(dialogType="talk"))

        self.bartenderdialog = CTkLabel(DisplayFrm, width=130, height=60, fg_color="white", bg_color="white", text="test", wraplength=150)
        self.bartenderdialog.place(relx=0.83, rely=0.23, anchor="center")

        self.BartendDialog(dialogType="intro")

        self.responseCheck = False
        self.musicSwitchCheck = FALSE
    
    def musicSwitch(self):
        """ This function is used to turn off/on the music with
        a single button press. """
        
        if (self.musicSwitchCheck):
            self.musicSwitchCheck = False
            self.musicButton.configure(text = "Mute Music")

            # This plays the music again.
            winsound.PlaySound('.\\media\\Snowfall.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        else:
            self.musicSwitchCheck = True
            self.musicButton.configure(text = "Play Music")

            # This stops the music in the background.
            winsound.PlaySound(None, winsound.SND_LOOP + winsound.SND_ASYNC)

    def BartendDialog(self, dialogType):
        """ This function is used to manage the dialogue of
        the bartender using the random module and configuring
        the text to be different. """

        if (dialogType == "intro"):
            self.bartenderdialog.configure(text = introDialog[random.randint(0, len(introDialog)-1)])
        elif (dialogType == "talk"):
            self.bartenderdialog.configure(text = talkDialog[random.randint(0, len(talkDialog)-1)])
        elif (dialogType == "viewAll"):
            self.bartenderdialog.configure(text = ViewAllDialog[random.randint(0, len(ViewAllDialog)-1)])
        elif (dialogType == "viewRandom"):
            self.bartenderdialog.configure(text = randomDrinkDialog[random.randint(0, len(randomDrinkDialog)-1)])
        elif (dialogType == "viewSpecific"):
            self.bartenderdialog.configure(text = specificDrinkDialog[random.randint(0, len(specificDrinkDialog)-1)])

    def ViewAll(self, OutputFrm, filter_var):
        """ This function is used to view an overview of all drinks
        in the provided API. """

        self.clearFrame(OutputFrm)

        self.BartendDialog(dialogType="viewAll")

        self.drink = {
            "drinkName"  : "",
            "drinkThumb" : ""
        }
        self.drinkcollection = []
        self.drinkNumberint = 0
        count = 0
        self.responseCheck = False

        # This checks which filter is currently on
        #   0 = No filter (represented by the else condition)
        #   1 = Alcoholic
        #   2 = Non Alcoholic
        if (filter_var.get() == 1):
            for item in filter(lambda a: (a["strAlcoholic"] == "Alcoholic"), response["drinks"]):
                # This stores each drink's name and thumbnail inside a dictionary.
                self.drink["drinkName"] = item["strDrink"]
                self.drink["drinkThumb"] = item["strDrinkThumb"]

                # .copy returns a copy of an element, so that when it changes
                # in the future, it doesn't alter the previous elements. 
                self.drinkcollection.append(self.drink.copy())

        elif (filter_var.get() == 2):
            for item in filter(lambda a: (a["strAlcoholic"] == "Non alcoholic"), response["drinks"]):
                self.drink["drinkName"] = item["strDrink"]
                self.drink["drinkThumb"] = item["strDrinkThumb"]

                self.drinkcollection.append(self.drink.copy())

        else:
            while count < len(response["drinks"]):
                self.drink["drinkName"] = response["drinks"][count]["strDrink"]
                self.drink["drinkThumb"] = response["drinks"][count]["strDrinkThumb"]

                self.drinkcollection.append(self.drink.copy())
                count += 1
    
        count = 0
        photos = []

        while count < 4:
            try:
                # urllib.request fetches a url and reads the type of variable it is
                # in this instance it is a str of an image. 
                with urllib.request.urlopen((self.drinkcollection[count].get("drinkThumb"))) as u:
                    self.raw_data = u.read()
            except Exception as e:
                # This acts as a way to test if anything went wrong.
                # I do want to note that this will appear if there are no other
                # images to be displated e.g. if you have the non-alcoholic filter on.
                print(f"Error fetching image: {e}")
                return
            
            try:
                # io.BytesIO allows the raw data to be read correctly as an image.
                self.image = Image.open(io.BytesIO(self.raw_data))
                # This resizes the image to the correct width and height.
                self.resize_image = self.image.resize((200, 200))
                # This allows the image to be used in tkinter.
                self.photo = ImageTk.PhotoImage(self.resize_image)
                # This appends the variable so it can be used in the future.
                photos.append(self.photo)
            except Exception as e:
                # Again a test error in case it has trouble with opening the image.
                print(f"Error opening image: {e}")
                return

            # normal tkinter was used for url images due to the lack of documentation on the custom variant.
            self.drinkThumbnail = tk.Label(OutputFrm, width=200, height=200, bg="#23272d", image=photos[count])
            self.drinkName = CTkLabel(OutputFrm, 
                                      text=(self.drinkcollection[count].get("drinkName")),
                                      text_color='white')

            # columnspan and rowspan allows the element to occupy more space using the grid system.
            self.drinkThumbnail.grid(row=0, rowspan=4, column=1+count, pady=12)
            self.drinkName.grid(row=4, rowspan=1, column=1+count, pady=15)

            self.drinkThumbnail.bind('<Button-1>', lambda event, dName=self.drinkcollection[count].get("drinkName"): self.ViewSpecific(OutputFrm, dName))
            self.drinkName.bind('<Button-1>', lambda event, dName=self.drinkcollection[count].get("drinkName"): self.ViewSpecific(OutputFrm, dName))

            count += 1
        
        rightArrowimage = CTkImage(light_image=Image.open(".\\media\\right-arrow.png"), size=(35, 35))

        nextPage = CTkButton(OutputFrm, 
                            width=25, 
                            height=25,

                            fg_color="transparent",
                            hover_color="#23272d",

                            image=rightArrowimage,
                            text="",
                            
                            command=lambda:self.ViewAllScroll(OutputFrm, photos, drinksetcount = 0, nextPageCheck=TRUE))
                            # nextPageCheck allows the function to identify if it is scrolling forward or backwards.
        nextPage.grid(row=0, rowspan=5, column=6, sticky='nsew', padx=10)
        
    def ViewAllScroll(self, OutputFrm, photos, drinksetcount, nextPageCheck):
        """ This function is used to scroll to other drinks
         as it is a continuation of ViewAll. """

        self.clearFrame(OutputFrm)

        if (nextPageCheck):
            # drinksetcount is how the function keep track of which drinks have been displayed.
            drinksetcount += 4
        else:
            drinksetcount -= 4

        leftArrowimage = CTkImage(light_image=Image.open(".\\media\\left-arrow.png"), size=(35, 35))
        
        backPage = CTkButton(OutputFrm, 
                            width=25, 
                            height=25,

                            image=leftArrowimage,
                            text="",
                            
                            fg_color="transparent",
                            hover_color="#23272d"
                            )
        backPage.grid(row=0, rowspan=5, column=0, sticky='nsew', padx=10)

        # Checks if it should switch to the start function.
        if drinksetcount <= 4:
            backPage.configure(command=lambda:self.ViewAll(self, OutputFrm))
        else:
            backPage.configure(command=lambda:self.ViewAllScroll(OutputFrm, photos, drinksetcount, nextPageCheck=False))

        count = 0

        while count < 4:
            try:
                with urllib.request.urlopen((self.drinkcollection[drinksetcount+count].get("drinkThumb"))) as u:
                    self.raw_data = u.read()
            except Exception:
                print("No other image available")
                return
            
            try:
                self.image = Image.open(io.BytesIO(self.raw_data))
                self.resize_image = self.image.resize((200, 200))
                self.photo = ImageTk.PhotoImage(self.resize_image)
                photos.append(self.photo)
            except Exception as e:
                print(f"Error opening image: {e}")
                return

            self.drinkThumbnail = tk.Label(OutputFrm, width=200, height=200, bg="#23272d", image=photos[drinksetcount+count])
            self.drinkName = CTkLabel(OutputFrm, 
                                      text=(self.drinkcollection[drinksetcount+count].get("drinkName")),
                                      text_color='white')

            self.drinkThumbnail.grid(row=0, rowspan=4, column=1+count, pady=12, sticky='ew')
            self.drinkName.grid(row=4, rowspan=1, column=1+count, pady=15, sticky='ew')

            self.drinkThumbnail.bind('<Button-1>', lambda event, dName=self.drinkcollection[drinksetcount+count].get("drinkName"): self.ViewSpecific(OutputFrm, dName))
            self.drinkName.bind('<Button-1>', lambda event, dName=self.drinkcollection[drinksetcount+count].get("drinkName"): self.ViewSpecific(OutputFrm, dName))

            count += 1
        
        if (len(self.drinkcollection) - drinksetcount >= 4):
            rightArrowimage = CTkImage(light_image=Image.open(".\\media\\right-arrow.png"), size=(35, 35))

            nextPage = CTkButton(OutputFrm, 
                                width=25, 
                                height=25,
                                fg_color="transparent",
                                hover_color="#23272d",
                                
                                image=rightArrowimage,
                                text="",
                                
                                command=lambda:self.ViewAllScroll(OutputFrm, photos, drinksetcount, nextPageCheck=TRUE))
            nextPage.grid(row=0, rowspan=5, column=6, sticky='nsew', padx=11)
    
    def ViewSpecific(self, OutputFrm, specificResponseName):
        """ This function is used to view a specific drink's
        information. """
        
        # Checks if specificResponseName is blank
        if specificResponseName == '':
            # This shows an popup.
            tkinter.messagebox.showinfo("Error Message",  "Please select a drink. ")
            return
        
        self.BartendDialog(dialogType="viewSpecific")
    
        self.clearFrame(OutputFrm)
        # instead of trying to search for the drink in the all drink search.php, you can request to get a specific drink.
        # by removing 'a=' at the end and adding 's=' + the drink you want to learn about.
        specificResponse = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + specificResponseName).json()
        
        print(specificResponse["drinks"][0]["strDrink"] + "\n")

        try:
            with urllib.request.urlopen((specificResponse["drinks"][0]["strDrinkThumb"])) as u:
                self.raw_data = u.read()
        except Exception as e:
            print(f"Error fetching image: {e}")
            return
            
        try:
            self.image = Image.open(io.BytesIO(self.raw_data))
            self.resize_image = self.image.resize((200, 200))
            self.photo = ImageTk.PhotoImage(self.resize_image)
        except Exception as e:
            print(f"Error opening image: {e}")
            return

        self.drinkThumbnail = tk.Label(OutputFrm, width=200, height=200, image=self.photo)
        self.drinkThumbnail.grid(row=0, rowspan=4, column=0, columnspan=1, padx=20)

        self.drinkName = CTkLabel(OutputFrm,
                                  text_color='white',

                                  text = specificResponse["drinks"][0]["strDrink"],
                                  font=("saveur-sans-regular", 25))
        self.drinkName.grid(row=0, column=1, padx=20, pady=18, sticky='w')
        
        self.drinkCategory = CTkLabel(OutputFrm,
                                  text_color='white',

                                  text = 'Category: ' + specificResponse["drinks"][0]["strCategory"],
                                  font=("saveur-sans-regular", 20))
        self.drinkCategory.grid(row=1, column=1, padx=20, sticky='nw')

        self.drinkGlassType = CTkLabel(OutputFrm,
                                  text_color='white',

                                  text = 'Type of Glass: ' + specificResponse["drinks"][0]["strGlass"],
                                  font=("saveur-sans-regular", 20))
        self.drinkGlassType.grid(row=2, column=1, padx=20, sticky='nw')

        self.drinkAlcoholicType = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = 'Alcoholic: ' + specificResponse["drinks"][0]["strAlcoholic"],
                                  font=("saveur-sans-regular", 20))
        self.drinkAlcoholicType.grid(row=3, column=1, padx=20, sticky='nw')

        self.drinkIngredientsTitle = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = 'Ingredients:',
                                  font=("saveur-sans-regular", 22))
        self.drinkIngredientsTitle.grid(row=0, column=2, columnspan=1, padx=20, pady=30, sticky='nw')

        self.drinkIngredient1 = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = '1. ' + specificResponse["drinks"][0]["strIngredient1"],
                                  font=("saveur-sans-regular", 18))
        self.drinkIngredient1.grid(row=1, column=2, padx=20, sticky='nw')

        self.drinkIngredient2 = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = '2. ' + specificResponse["drinks"][0]["strIngredient2"],
                                  font=("saveur-sans-regular", 18))
        self.drinkIngredient2.grid(row=2, column=2, padx=20, sticky='nw')

        # Each one of these try-except blocks checks if the ingredient is present. 
        try:
            self.drinkIngredient3 = CTkLabel(OutputFrm,
                                    
                                    text_color='white',

                                    text = '3. ' + specificResponse["drinks"][0]["strIngredient3"],
                                    font=("saveur-sans-regular", 18))
            self.drinkIngredient3.grid(row=3, column=2, padx=20, sticky='nw')
        except Exception:
            print("no 3th ingredient")

        try:
            self.drinkIngredient4 = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = '4. ' + specificResponse["drinks"][0]["strIngredient4"],
                                  font=("saveur-sans-regular", 18))
            self.drinkIngredient4.grid(row=1, column=3, padx=20, sticky='nw')
        except Exception:
            print("no 4th ingredient")

        try:
            self.drinkIngredient5 = CTkLabel(OutputFrm,
                                    
                                    text_color='white',

                                    text = '5. ' + specificResponse["drinks"][0]["strIngredient5"],
                                    font=("saveur-sans-regular", 18))
            self.drinkIngredient5.grid(row=2, column=3, padx=20, sticky='nw')
        except Exception:
            print("no 5th ingredient")

        try:
            self.drinkIngredient6 = CTkLabel(OutputFrm,
                                    
                                    text_color='white',

                                    text = '6. ' + specificResponse["drinks"][0]["strIngredient6"],
                                    font=("saveur-sans-regular", 18))
            self.drinkIngredient6.grid(row=3, column=3, padx=20, sticky='nw')
        except Exception:
            print("no 6th ingredient")
        
        print("")

        rightArrowimage = CTkImage(light_image=Image.open(".\\media\\right-arrow.png"), size=(35, 35))

        nextPage = CTkButton(OutputFrm, 
                            width=25, 
                            height=25,

                            fg_color="transparent",
                            hover_color="#23272d",

                            image=rightArrowimage,
                            text="",
                            
                            command=lambda:self.ViewInstructions(OutputFrm, specificResponse, specificResponseName))
        nextPage.grid(row=0, rowspan=5, column=6, sticky='nsew', padx=10)

    def ViewRandom(self, OutputFrm):
        """ This function is used to view a random drink's
        information. """

        self.clearFrame(OutputFrm)

        self.BartendDialog(dialogType="viewRandom")

        specificResponseName = allDrinks[random.randint(0, len(allDrinks)-1)]
        specificResponse = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + specificResponseName).json()
        
        print (specificResponse["drinks"][0]["strDrink"] + "\n")

        try:
            with urllib.request.urlopen((specificResponse["drinks"][0]["strDrinkThumb"])) as u:
                self.raw_data = u.read()
        except Exception as e:
            print(f"Error fetching image: {e}")
            return
            
        try:
            self.image = Image.open(io.BytesIO(self.raw_data))
            self.resize_image = self.image.resize((200, 200))
            self.photo = ImageTk.PhotoImage(self.resize_image)
        except Exception as e:
            print(f"Error opening image: {e}")
            return

        self.drinkThumbnail = tk.Label(OutputFrm, width=200, height=200, image=self.photo)
        self.drinkThumbnail.grid(row=0, rowspan=4, column=0, columnspan=1, padx=20)

        self.drinkName = CTkLabel(OutputFrm,
                                  text_color='white',

                                  text = specificResponse["drinks"][0]["strDrink"],
                                  font=("saveur-sans-regular", 25))
        self.drinkName.grid(row=0, column=1, padx=20, pady=18, sticky='w')
        
        self.drinkCategory = CTkLabel(OutputFrm,
                                  text_color='white',

                                  text = 'Category: ' + specificResponse["drinks"][0]["strCategory"],
                                  font=("saveur-sans-regular", 20))
        self.drinkCategory.grid(row=1, column=1, padx=20, sticky='nw')

        self.drinkGlassType = CTkLabel(OutputFrm,
                                  text_color='white',

                                  text = 'Type of Glass: ' + specificResponse["drinks"][0]["strGlass"],
                                  font=("saveur-sans-regular", 20))
        self.drinkGlassType.grid(row=2, column=1, padx=20, sticky='nw')

        self.drinkAlcoholicType = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = 'Alcoholic: ' + specificResponse["drinks"][0]["strAlcoholic"],
                                  font=("saveur-sans-regular", 20))
        self.drinkAlcoholicType.grid(row=3, column=1, padx=20, sticky='nw')

        self.drinkIngredientsTitle = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = 'Ingredients:',
                                  font=("saveur-sans-regular", 22))
        self.drinkIngredientsTitle.grid(row=0, column=2, columnspan=1, padx=20, pady=30, sticky='nw')

        self.drinkIngredient1 = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = '1. ' + specificResponse["drinks"][0]["strIngredient1"],
                                  font=("saveur-sans-regular", 18))
        self.drinkIngredient1.grid(row=1, column=2, padx=20, sticky='nw')

        self.drinkIngredient2 = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = '2. ' + specificResponse["drinks"][0]["strIngredient2"],
                                  font=("saveur-sans-regular", 18))
        self.drinkIngredient2.grid(row=2, column=2, padx=20, sticky='nw')

        try:
            self.drinkIngredient3 = CTkLabel(OutputFrm,
                                    
                                    text_color='white',

                                    text = '3. ' + specificResponse["drinks"][0]["strIngredient3"],
                                    font=("saveur-sans-regular", 18))
            self.drinkIngredient3.grid(row=3, column=2, padx=20, sticky='nw')
        except Exception:
            print("no 3th ingredient")

        try:
            self.drinkIngredient4 = CTkLabel(OutputFrm,
                                  
                                  text_color='white',

                                  text = '4. ' + specificResponse["drinks"][0]["strIngredient4"],
                                  font=("saveur-sans-regular", 18))
            self.drinkIngredient4.grid(row=1, column=3, padx=20, sticky='nw')
        except Exception:
            print("no 4th ingredient")

        try:
            self.drinkIngredient5 = CTkLabel(OutputFrm,
                                    
                                    text_color='white',

                                    text = '5. ' + specificResponse["drinks"][0]["strIngredient5"],
                                    font=("saveur-sans-regular", 18))
            self.drinkIngredient5.grid(row=2, column=3, padx=20, sticky='nw')
        except Exception:
            print("no 5th ingredient")

        try:
            self.drinkIngredient6 = CTkLabel(OutputFrm,
                                    
                                    text_color='white',

                                    text = '6. ' + specificResponse["drinks"][0]["strIngredient6"],
                                    font=("saveur-sans-regular", 18))
            self.drinkIngredient6.grid(row=3, column=3, padx=20, sticky='nw')
        except Exception:
            print("no 6th ingredient")
        
        print("")

        rightArrowimage = CTkImage(light_image=Image.open(".\\media\\right-arrow.png"), size=(35, 35))

        nextPage = CTkButton(OutputFrm, 
                            width=25, 
                            height=25,

                            fg_color="transparent",
                            hover_color="#23272d",

                            image=rightArrowimage,
                            text="",
                            
                            command=lambda:self.ViewInstructions(OutputFrm, specificResponse, specificResponseName))
        nextPage.grid(row=0, rowspan=5, column=6, sticky='nsew', padx=10)

    def ViewInstructions(self, OutputFrm, specificResponse, specificResponseName):
        """ This function is used to view a drink's instructions. """

        self.clearFrame(OutputFrm)
        
        leftArrowimage = CTkImage(light_image=Image.open(".\\media\\left-arrow.png"), size=(35, 35))

        backPage = CTkButton(OutputFrm, 
                            width=25, 
                            height=25,

                            image=leftArrowimage,
                            text="",
                            
                            fg_color="transparent",
                            hover=False,

                            # It all leads back to view specific drink.
                            command=lambda:self.ViewSpecific(OutputFrm, specificResponseName)
                            )
        backPage.grid(row=0, rowspan=5, column=0, sticky='nsew', padx=10)

        CTkLabel(OutputFrm,
                text_color='white',
                text = "Instructions",
                font=("saveur-sans-regular", 25)).grid(row=0, column=1, columnspan=5, padx=20, pady=18, sticky='w')

        CTkLabel(OutputFrm,
                text_color='white',
                text = specificResponse["drinks"][0]["strInstructions"],
                justify = 'left',
                wraplength=850,
                font=("saveur-sans-regular", 20)).grid(row=1, rowspan=5, column=1, padx=20, pady=18, sticky='nw')

    def clearFrame(self, frame):
        """ This function is used to erase all of the items within
        a certain frame. """

        for item in frame.winfo_children():                           # The for loop is used to select every item inside the frame.
            item.destroy()                                            # The ".destory" deletes the item from the window.

app = App()
app.mainloop()
