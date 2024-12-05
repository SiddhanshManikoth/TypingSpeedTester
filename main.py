from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import random
from sentance import sentence_list
import keyboard
from kivy.core.window import Window
from kivy.clock import Clock
Clock.max_iteration = 60


class TypingSpeedTest(FloatLayout):



    random_sentence=str(sentence_list[random.randint(0,len(sentence_list)-1)])
    compare_sentence=random_sentence
    typed=[]
    typed_str="".join(typed)
    r=0
    w=0
    r_list=[]
    w_list=[]

    timer=0

    ran_sen_list=[]

    def __init__(self, **kwargs):
        super(TypingSpeedTest, self).__init__(**kwargs)
        Window.bind(on_key_up=self.Text_Listener)
        Window.bind(on_key_down=self.space_Listener)
    def start_timer(self,*args):
            Clock.schedule_interval(self.cal, 0.5)



    def cal(self, *args):
        r = 0
        w = 0
        for i in range(0, len(self.typed_str)):
            if (self.typed_str[i]).upper() == (self.compare_sentence[i]).upper():
                r = r + 1
                user_input=self.ids['user_input']
                color=[0,0,0,1]
                user_input.foreground_color=color
            else:
                w = w + 1
                user_input = self.ids['user_input']
                color=[1, 0, 0, 1]
                user_input.foreground_color = color

        self.timer=round(self.timer+0.5,2)
        show_time=self.ids['timer']
        show_time.text=str(self.timer)
        if self.timer == 61:
            self.Stop_test()
            self.r_list.append(r)
            self.w_list.append(w)

        if len(self.typed_str)==len(self.compare_sentence):
            self.ran_sen_list.append(self.random_sentence)
            self.random_sentence = str(sentence_list[random.randint(0, len(sentence_list) - 1)])
            self.compare_sentence  =  (self.compare_sentence  +"")+ self.random_sentence
            written_text=self.ids['written_text']
            written_text.text=self.random_sentence
            user_input=self.ids['user_input']
            user_input.text=""
            self.r=r
            self.w=w
            self.r_list.append(r)
            self.w_list.append(w)




    def Stop_test(self):
        Clock.unschedule(self.cal)
        self.r_list.append(self.r)
        self.w_list.append(self.w)
        r=sum(self.r_list)
        w = sum(self.w_list)
        wpm=str((r / 5)-w)
        print()
        written_text=self.ids['written_text']
        written_text.text=f"your words per min is {wpm}!!"

    def Text_Listener(self,*args):

       user_input = self.ids['user_input']
       if user_input.text == '' :
           try:
            self.typed.append(user_input.text[0])
           except:
               self.typed.append(user_input.text)
       else:
           self.typed.append(user_input.text[-1])
       self.typed_str = ""+("".join(self.typed))
       print((self.compare_sentence).upper())
       print((self.typed_str).upper())

    timer_on = False
    def space_Listener(self,*args):
        user_input = self.ids['user_input']

        if self.timer_on==False:
            self.start_timer()
            self.timer_on=True



        if keyboard.is_pressed("Backspace"):
            try:
             self.typed.pop()
             self.typed.pop()
            except:
                self.typed=[]




class test(App):


    def build(self):


         return TypingSpeedTest()


if __name__=="__main__":
    test().run()

