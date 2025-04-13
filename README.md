Pamatinformācija
-
1) Datu kopu un YOLO algoritma modeļu apmācības un salīdzināšanas rezultātus var apskatīt Rezultati.xlsx failā.
2) Divu iegūto rezultātu salidzinājums ir redzāms pie png attēlā.
3) 4 Kadri no video testēšanās var redzēt arī png attēlā ar to pašu nosaukumu.
4) Tiek pievienots uzlabojums ar vienīgo attēlu, kur tiek pievienota teksta atpazīšana no ceļazīmēm.
5) Tiek pārstradāts iepriekšējāis uzlabojums, lai apstradāt video formātu. (Nepieciešams papildināt)

---
Vienkāršs uzlabojums ar vienu attēlu:
-
- Pirmkārt, tiek paņemts attēls ar ceļazīmi, kuru notestēja uz apmacīta modeļa. Attēlā redzams, kā algoritms veiksmīgi atrada zīmi, pēc kuras tas tika apmācīts.

  ![Original_road_sign](https://github.com/user-attachments/assets/3a35383d-8c96-4b74-a1af-bb976abca4aa)
- Otrkārt, testēšanas laikā algoritms, pamatojoties uz koordinātēm, izveido ierobežojošos laukumus. Šīs koordinātas var izmantot, lai izgrieztu noteiktu sākotnējā attēla daļu, tādējādi izveidojot nākamo attēlu.
  
  ![Road_sign_in_bb](https://github.com/user-attachments/assets/8a5d8e48-4bcd-4c75-9aa7-9100446dbf5b)
- Atbrīvojoties no liekas informācijas, var izmantot OCR, lai atpazītu tekstu. Rezultāts tiek paradīts nākoša attēlā.

  ![image](https://github.com/user-attachments/assets/3b6388ad-a6c2-4a5d-b904-59e7c7f5cf88)

---
Uzlabojums ar video apstrādi:
- 
- Videoklipa apstrādei ir līdzīga sistēma kā vienai bildei. Taču šajā gadījumā kadri vispirms tiek izvilkti no videoklipa, tādējādi katru sekundi tiek izveidots jauns fails.
- Pēc tam ir papildu funkcija, kas pagriež attēlus un noņem tumšās joslas sānos.
- Talāk iet funkcija kas aplūko katru izveidotu attēlu un izmanto yolo, lai atpazītu zīmi. Testēšanas laikā tiek veikta pārbaude, ja zīmes klase atbilst izvēlētām, tiek saglabātas tās koordinātas. Nosaukums tiek saglabāts un pievienots masīvam. Pēc tam vēlreiz iet filtrēšana caur visām failām, ja faila nosaukums ir masīvā, tas tiek pārdēvēts uz citu nosaukumu turpmākajam darbam.
- Un pēdējā funkcija ņem izveidoto attēlu no iepriekšējās funkcijas, pēc tam izmanto koordinātes un izgriež jaunu attēlu, pēc tam tajā tiek izmantota OCR.

  ![image](https://github.com/user-attachments/assets/74a4df24-195f-4fe8-b411-0c9c63f184e8)
- Variants ar video apstrādi nav galīgais, ir jāveic papildu testēšanu. Var arī redzēt, ka var tikt izmantota papildu attēlu apstrāde, jo easyocr slikti atpazīst tekstu. Arī pašlaik nav gluži ērti izmantot šo kodu, jo pēc yolo apstrādes ir pastāvīgi jādzēš kadrus, nākotnē tas tiks uzlabots. Tāpat šobrīd nav skaidrs, kā kods uzvedīsies, ja būs vairākas ceļa zīmes.
