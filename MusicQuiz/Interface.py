from _musicQuizDatabase import Reader
import os
import tkinter as tk
import time
test: Reader = Reader((os.path.dirname(os.path.realpath(__file__)) + "/Quiz Songs.db"))
class cancelButton(tk.Button):

    def __init__(self, frameRef:tk.Frame):
        super().__init__(frameRef, text="Cancel",font= ["Century Gothic", 30], command=lambda: frameRef.destroy())
class finalFrame(tk.Frame):
    def __init__(self, givenPackId: int, windowRef: tk.Tk, oldFrame: tk.Frame, given_Score: int, given_max: int):
        if oldFrame is not None:
            oldFrame.destroy()
        super().__init__(windowRef)
        self.packID = givenPackId
        self.score = given_Score
        self.max = given_max
        self.configure(bg="#b52121")
        self.SetupLayout()
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        for i in range(50):
                self.rowconfigure(i, weight=1)
                self.columnconfigure(i, weight=1)
        tk.Label(self,text=f"Score on : {" - ".join(test.GetPackMetadata(self.packID))}").grid(row=15, column = 12)
        tk.Label(self,text=f"{self.score}/{self.max}").grid(row=20, column = 12)

class QuizFrame(tk.Frame):
    answerEntry: tk.Entry
    def __init__(self, givenPackId: int, windowRef: tk.Tk, oldFrame: tk.Frame = None):
        if oldFrame is not None:
            oldFrame.destroy()
        super().__init__(windowRef)
        self.packID = givenPackId
        self.configure(bg = "#b52121")
        self.SetupLayout()
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        for i in range(50):
                self.rowconfigure(i, weight=1)
                self.columnconfigure(i, weight=1)
        tk.Label(self, text=f"You are Playing - {test.GetPackMetadata(self.packID)[0]} by {test.GetPackMetadata(self.packID)[1]}", font=["Century Gothic", 25]).grid(row=0,column=0)
        self.songs = test.GetPackSongsData(self.packID)
        self.SongMetaData = tk.Label(self, text="", font=["Century Gothic", 25], width=60)
        self.SongMetaData.grid(row=15, column=12)
        self.SongLine = tk.Label(self, text="", font=["Century Gothic", 25], width=40)
        self.SongLine.grid(row=20, column=12)
        self.answerEntry = tk.Entry(self)
        self.answerEntry.grid(row=25, column=12)
        song_num = 1
        score = 0
        self.showQuestion(self.songs[song_num], song_num,score)

        
    def NextQuestion(self,blank,song_num,score):
        answer: str = self.answerEntry.get()
        if answer.lower() == blank:
            temp4 = tk.Label(self, text="Correct!", font=["Century Gothic", 25], width=40, bg='#fff',
                             fg='#3eb521')
            temp4.grid(row=35, column=12)
            song_num+=1
            score += 1
            self.after(1000, lambda: [temp4.destroy(), self.showQuestion(self.songs[song_num], song_num , score)])
        else:
            temp5 = tk.Label(self, text="Incorrect", font=["Century Gothic", 25], width=40, bg='#fff',
                             fg='#ff0000')
            temp5.grid(row=35, column=12)
            song_num += 1
            self.after(1000, lambda: [temp5.destroy(), self.showQuestion(self.songs[song_num], song_num,score)])

    def showQuestion(self,song:list ,song_num,score):
        self.answerEntry.delete(0, tk.END)
        self.SongMetaData.configure(text=f"{' - '.join([str(i) if type(i) != list else ', '.join(i) for i in test.GetSongMetadata(song[0])])}")
        line = test.GetSongLyrics(song[0]).split("\n")[song[1]]
        blank = line.split(" ")[song[2]]
        self.SongLine.configure(text= line.replace(blank, "____"))
        if song_num < len(self.songs) -1 :
            temp = tk.Button(self, text="Next", font=["Century Gothic", 25], width=40, command=lambda: self.NextQuestion(blank,song_num,score))
            temp.grid(row=30, column = 12)
        else:
            out_of = len(self.songs) - 1
            finalFrame(self.packID, self.master, self, score, out_of)



        # for songData in songs:
        #     song_num += 1
        #     temp1 = tk.Label(self,text=f"{song_num}/{len(songs)}",font=["Century Gothic", 15])
        #     temp1.grid(row=0, column=49)
        #     temp2 = tk.Label(self, text=f"{' - '.join([str(i) if type(i) != list else ', '.join(i) for i in test.GetSongMetadata(songData[0])])}", font=["Century Gothic", 25], width=40)
        #     temp2.grid(row=15, column= 12)
        #     line = test.GetSongLyrics(songData[0]).split("\n")[songData[1]]
        #     blank = line.split(" ")[songData[2]]
        #     print(blank)
        #     temp3 = tk.Label(self,text= line.replace(blank, "____"),font=["Century Gothic", 25],  width = 40)
        #     temp3.grid(row=20, column= 12)
        #     self.answerEntry = tk.Entry(self)
        #     self.answerEntry.grid(row=25, column=12)
        #     def self.NextQuestion():
        #         answer: str = self.answerEntry.get()
        #         if answer.lower() == blank:
        #             temp4 = tk.Label(self, text="Correct!", font=["Century Gothic", 25], width=40, bg='#fff',
        #                              fg='#3eb521')
        #             temp4.grid(row=30, column=12)
        #             self.after(1000, lambda: [temp1.destroy(), temp2.destroy(), temp3.destroy(), temp4.destroy(),
        #                                       temp6.destroy()])
        #             self.answerEntry.delete(0, tk.END)
        #         else:
        #             temp5 = tk.Label(self, text="Incorrect", font=["Century Gothic", 25], width=40, bg='#fff',
        #                              fg='#ff0000')
        #             temp5.grid(row=30, column=12)
        #             self.after(1000, lambda: [temp1.destroy(), temp2.destroy(), temp3.destroy(), temp5.destroy(),
        #                                       temp6.destroy()])
        #             self.answerEntry.delete(0, tk.END)
        #
        #
        #
        #
        #     temp6 = tk.Button(self, text = "Next",font=["Century Gothic", 25],  width = 40, command = lambda: self.NextQuestion())
        #     temp6.grid(row=30, column = 12)



# for songData in test.GetPackSongsData(packId):
#     # Print the song's details like song name, album name, and artist(s)
#     # If there are multiple artists, show them separated by commas
#     print(" - ".join([str(i) if type(i) != list else ", ".join(i) for i in test.GetSongMetadata(songData[0])]))
#
#     # Get the lyrics for this song, split them into lines, and pick the correct line
#     line = test.GetSongLyrics(songData[0]).split("\n")[songData[1]]
#
#     # Find the word to replace based on the lyric word number
#     blank = line.split(" ")[songData[2]]
#
#     # Replace the word with "____" (a blank) and print the modified line
#     print(line.replace(blank, "____"))
#     # Also print the blank (answer)
#     print("(" + blank + ")")
#
#     print()


class MainMenuFrame(tk.Frame):

    def __init__(self, windowRef: tk.Tk):
        super().__init__(windowRef)
        self.configure(bg= "#b52121")
        self.SetupLayout()
        self.pack(fill="both", expand=True)


    def SetupLayout(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        tk.Label(self, text="Music Quiz", font=["Century Gothic", 40]).grid(row=0, column=1,columnspan= 3)
        tk.Label(self, text="What Pack Do You Want To Play?", font=["Century Gothic", 30]).grid(row=1, column=1, columnspan= 3)
        for packId in test.GetAllPacks():
            tk.Button(self, text=f"{" - ".join(test.GetPackMetadata(packId))}", command=lambda tempId=packId: QuizFrame(tempId, self.master, self), font=["Century Gothic", 20], width=20).grid(row=2,column=0+packId, padx=(10,5), pady=10)

        cancelButton(self).grid(row=2, column=0)




class MainPage(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.configure(bg="#ff8803")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        MainMenuFrame(self)
        self.mainloop()


mainPage: MainPage = MainPage()