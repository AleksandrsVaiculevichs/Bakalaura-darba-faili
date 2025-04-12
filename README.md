Pamatinformācija
-
1) Datu kopu un YOLO algoritma modeļu apmācības un salīdzināšanas rezultātus var apskatīt Rezultati.xlsx failā.
2) Divu iegūto rezultātu salidzinājums ir redzāms pie png attēlā.
3) 4 Kadri no video testēšanās var redzēt arī png attēlā ar to pašu nosaukumu.
4) Tiek pievienots arī neliels uzlabojums priekš teksta atazīšanu, izmantojot OCR (nav galīgs varians)

---
Vienkāršs uzlabojuma apraksts:
-
- Pirmkārt, tiek paņemts attēls ar ceļazīmi, kuru notestēja uz apmacīta modeļa. Attēlā redzams, kā algoritms veiksmīgi atrada zīmi, pēc kuras tas tika apmācīts.

  ![Original_road_sign](https://github.com/user-attachments/assets/3a35383d-8c96-4b74-a1af-bb976abca4aa)
- Otrkārt, testēšanas laikā algoritms, pamatojoties uz koordinātēm, izveido ierobežojošos laukumus. Šīs koordinātas var izmantot, lai izgrieztu noteiktu sākotnējā attēla daļu, tādējādi izveidojot nākamo attēlu.
  
  ![Road_sign_in_bb](https://github.com/user-attachments/assets/8a5d8e48-4bcd-4c75-9aa7-9100446dbf5b)
- Atbrīvojoties no liekas informācijas, var izmantot OCR, lai atpazītu tekstu. Rezultāts tiek paradīts nākoša attēlā.

  ![image](https://github.com/user-attachments/assets/3b6388ad-a6c2-4a5d-b904-59e7c7f5cf88)

---
Turpmākie uzlabojumi:
- 
- Pašlaik šis uzlabojums darbojas tikai ar atsevišķiem attēliem un spēj apstrādāt tikai vienu ceļa zīmes klasi. Nākotnē ir plānots paplašināt šīs sistēmas iespējas un pārbaudīt to video testēšanas laikā.
