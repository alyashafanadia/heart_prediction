import numpy as np
import pickle
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

# Load the trained SVM model
with open('svm_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

class HeartDiseaseApp(App):
    def build(self):
        self.layout = GridLayout(cols=1, spacing=2, padding=40, size_hint=(1, 3))
        Window.size = (300, 600)
        
        self.layout.add_widget(Label(text='Masukkan Data Pasien', font_size=25, bold=True))

        self.layout.add_widget(Label(text='Usia:', font_size=22))
        self.age_input = TextInput(hint_text='Usia', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.age_input)

        self.layout.add_widget(Label(text='Jenis kelamin:', font_size=22))
        self.sex_input = TextInput(hint_text='Jenis kelamin', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.sex_input)

        radio_group = [
            ToggleButton(text='Perempuan', group='jenis_kelamin', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='Laki-laki', group='jenis_kelamin', font_size=20, size_hint=(1, None), height=40)
        ]

        for button in radio_group:
            button.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button)

        self.layout.add_widget(Label(text='Tipe nyeri dada:', font_size=22))
        self.chp_input = TextInput(hint_text='Tipe nyeri dada', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.chp_input)

        radio_group2 = [
            ToggleButton(text='1: Angina tipikal', group='nyeri_dada', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='2: Angina atipikal', group='nyeri_dada', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='3: Nyeri non-anginal', group='nyeri_dada', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='4: Asimtomatik', group='nyeri_dada', font_size=20, size_hint=(1, None), height=40)
        ]

        for button2 in radio_group2:
            button2.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button2)

        self.layout.add_widget(Label(text='Tekanan darah:', font_size=22))
        self.bp_input = TextInput(hint_text='Tekanan darah', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.bp_input)

        self.layout.add_widget(Label(text='Kolesterol serum:', font_size=22))
        self.sch_input = TextInput(hint_text='Kolesterol serum', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.sch_input)

        self.layout.add_widget(Label(text='Gula darah puasa:', font_size=22))
        self.fbs_input = TextInput(hint_text='Gula darah puasa', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.fbs_input)

        radio_group3 = [
            ToggleButton(text='0: < 120 mg/dL', group='gula_darah', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='1: >= 120 mg/dL', group='gula_darah', font_size=20, size_hint=(1, None), height=40)
        ]

        for button3 in radio_group3:
            button3.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button3)

        self.layout.add_widget(Label(text='Elektrokardiografi saat istirahat:', font_size=22))
        self.ecg_input = TextInput(hint_text='Elektrokardiografi saat istirahat', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.ecg_input)

        radio_group4 = [
            ToggleButton(text='0: Normal', group='ekg', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='1: Kelainan gelombang ST-T', group='ekg', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='2: Hipertrofi ventrikel kiri', group='ekg', font_size=20, size_hint=(1, None), height=40)
        ]

        for button4 in radio_group4:
            button4.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button4)

        self.layout.add_widget(Label(text='Detak jantung maksimum:', font_size=22))
        self.mhrt_input = TextInput(hint_text='Detak jantung maksimum', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.mhrt_input)

        self.layout.add_widget(Label(text='Angina disebabkan olahraga:', font_size=22))
        self.exian_input = TextInput(hint_text='Angina disebabkan olahraga', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.exian_input)

        radio_group5 = [
            ToggleButton(text='0: Tidak', group='exian', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='1: Ya', group='exian', font_size=20, size_hint=(1, None), height=40),
        ]

        for button5 in radio_group5:
            button5.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button5)

        self.layout.add_widget(Label(text='Depresi ST:', font_size=22))
        self.opk_input = TextInput(hint_text='Depresi ST', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.opk_input)

        self.layout.add_widget(Label(text='Kemiringan:', font_size=22))
        self.slope_input = TextInput(hint_text='Kemiringan', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.slope_input)

        radio_group6 = [
            ToggleButton(text='1: Miring naik', group='kemiringan', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='2: Datar', group='kemiringan', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='3: Miring turun', group='kemiringan', font_size=20, size_hint=(1, None), height=40)
        ]

        for button6 in radio_group6:
            button6.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button6)

        self.layout.add_widget(Label(text='Jumlah pembuluh darah:', font_size=22))
        self.vessel_input = TextInput(hint_text='Jumlah pembuluh darah', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.vessel_input)

        self.layout.add_widget(Label(text='Thalassemia:', font_size=22))
        self.thal_input = TextInput(hint_text='Thalassemia', multiline=False, font_size=20, size_hint=(1, None), height=35)
        self.layout.add_widget(self.thal_input)

        radio_group7 = [
            ToggleButton(text='3: Normal', group='thal', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='6: Defek tetap', group='thal', font_size=20, size_hint=(1, None), height=40),
            ToggleButton(text='7: Reversabel', group='thal', font_size=20, size_hint=(1, None), height=40)
        ]

        for button7 in radio_group7:
            button7.bind(on_press=self.on_toggle_button_pressed)
            self.layout.add_widget(button7)

        self.result_label = Label(text='', size_hint_y=None, height=40)
        self.layout.add_widget(self.result_label)

        self.predict_button = Button(text='Prediksi', on_press=self.predict, size_hint=(None, None), size=(100, 40))
        self.layout.add_widget(self.predict_button)

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll_view.add_widget(self.layout)
        
        return scroll_view
    

    def predict(self, instance):
        try:
            age = float(self.age_input.text)
            sex = float(self.sex_input.text)
            chp = float(self.chp_input.text)
            bp = float(self.bp_input.text)
            sch = float(self.sch_input.text)
            fbs = float(self.fbs_input.text)
            ecg = float(self.ecg_input.text)
            mhrt = float(self.mhrt_input.text)
            exian = float(self.exian_input.text)
            opk = float(self.opk_input.text)
            slope = float(self.slope_input.text)
            vessel = float(self.vessel_input.text)
            thal = float(self.thal_input.text)

            # Data untuk prediksi
            input_features = np.array([[age, sex, chp, bp, sch, fbs, ecg, mhrt, exian, opk, slope, vessel, thal]])
            input_features = scaler.transform(input_features)

            # Melakukan prediksi
            prediction = model.predict(input_features)
            
            if prediction[0] == 1:
                self.result_label.text = "Ada kemungkinan penyakit jantung."
            elif prediction[0] == 0:
                self.result_label.text = "Tidak ada kemungkinan penyakit jantung."

        except ValueError:
            self.result_label.text = "Masukkan angka valid untuk semua input."

    def on_toggle_button_pressed(self, instance):
        if instance.group == 'jenis_kelamin':    
            if instance.text == 'Perempuan':
                self.sex_input.text = '0'
            elif instance.text == 'Laki-laki':
                self.sex_input.text = '1'
        elif instance.group == 'nyeri_dada':
            if instance.text == '1: Angina tipikal':
                self.chp_input.text = '1'
            elif instance.text == '2: Angina atipikal':
                self.chp_input.text = '2'
            elif instance.text == '3: Nyeri non-anginal':
                self.chp_input.text = '3'
            elif instance.text == '4: Asimtomatik':
                self.chp_input.text = '4'
        elif instance.group == 'gula_darah':
            if instance.text == '0: < 120 mg/dL':
                self.fbs_input.text = '0'
            elif instance.text == '1: >= 120 mg/dL':
                self.fbs_input.text = '1'
        elif instance.group == 'ekg':
            if instance.text == '0: Normal':
                self.ecg_input.text = '0'
            elif instance.text == '1: Kelainan gelombang ST-T':
                self.ecg_input.text = '1'
            elif instance.text == '2: Hipertrofi ventrikel kiri':
                self.ecg_input.text = '2'
        elif instance.group == 'exian':
            if instance.text == '0: Tidak':
                self.exian_input.text = '0'
            elif instance.text == '1: Ya':
                self.exian_input.text = '1'
        elif instance.group == 'kemiringan':
            if instance.text == '1: Miring naik':
                self.slope_input.text = '1'
            elif instance.text == '2: Datar':
                self.slope_input.text = '2'
            elif instance.text == '3: Miring turun':
                self.slope_input.text = '3'
        elif instance.group == 'thal':
            if instance.text == '3: Normal':
                self.thal_input.text = '3'
            elif instance.text == '6: Defek tetap':
                self.thal_input.text = '6'
            elif instance.text == '7: Reversabel':
                self.thal_input.text = '7'
        

if __name__ == '__main__':
    HeartDiseaseApp().run()