Pamatinformācija
-
1) Datu kopu un YOLO algoritma modeļu apmācības un salīdzināšanas rezultātus var apskatīt Rezultati.xlsx failā.
2) Divu iegūto rezultātu salidzinājums ir redzāms pie png attēlā.
3) 4 Kadri no video testēšanās var redzēt arī png attēlā ar to pašu nosaukumu.
4) Tiek pievienots uzlabojums ar vienīgo attēlu, kur tiek pievienota teksta atpazīšana no ceļazīmēm.
5) Tiek pārstradāts iepriekšējāis uzlabojums, lai apstradāt video formātu. (Nepieciešams papildināt)
---
Galvēna idēja
-

  ![Untitled](https://github.com/user-attachments/assets/60d28b1d-07d0-4969-9829-69d55388ee82)
  
Ideja ir tāda, ka, kad tiek filmētas ceļa zīmes, yolo apstrādā katru kadru un saglabā visu zīmju koordinātas. Ja yolo saglabā koordinātes, tas var izgriezt atrasto saturu. Tādējādi ir iespējams izgriezt tikai ceļa zīmi. Pēc tam, apstrādājot attēlu, uzlabojot tā kvalitāti vai izmēru, var izmantot OCR, kas atradīs tekstu uz ceļa zīmēm.

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
- Videoklipa apstrādei ir līdzīga sistēma kā apstrādei ar vienu attēlū. Taču šajā gadījumā kadri vispirms tiek izvilkti no videoklipa, tādējādi katru sekundi tiek izveidots jauns fails.
- Pēc tam ir papildu funkcija, kas pagriež attēlus un noņem tumšās joslas sānos.
- Talāk iet funkcija kas aplūko katru izveidotu attēlu un izmanto yolo, lai atpazītu zīmi. Testēšanas laikā tiek veikta pārbaude, ja zīmes klase atbilst izvēlētām, tiek saglabātas tās koordinātas. Nosaukums tiek saglabāts un pievienots masīvam. 
- Sākotnēji yolo izveido tuples list, kas izskatās apmēram šādi: [(1, coord), (2, coord)...], 
tātad cipari viens, divi... šaja gadījumā ir koordinātes apzimējumi, tas ir x1, x2, y1 un y2. Šī funkcija vispirms sadala koordinātas no šīs lapas uz updating_boxes, kas tagad izskatās šādi: [(coord, coord, coord, coord), (coord, coord, ...)]. Un pēc tam, tā kā ir ērtāk izmantot lielu koordinātu lapu, tā tālāk sadala tuples lapu uz convert_to_list, kas tagad izskatās šādi: 
[coord, coord, coord, coord, ...]. Pēc tam tas printē visus rezultātus.
- Talākā funkcija  iterē caur darba failiem, kuros ir saglabāti nosaukumi, nolasa attēlu nosaukumu, ņemot vērā pilnu ceļu. Pēc tam ar katru jaunu iterāciju tiek aprēķinātas 4 koordinātas lapā, no sākuma līdz beigām un katru reizi par +4. Tas ir iespējams, jo visas koordinātas nav sakārtotas un seko viena aiz otrai vienmērīgi, kas ļauj tās izmantot šādā veidā. Pēc tam iterē pār šīm koordinātēm, aprēķina x1, x2, y1, y2 un izgriež attēlu atbilstoši kadru koordinātēm. Pēc tam teksta labākai atpazīšanai var mainīt attēla izmēru, un vēl stradāt ar attēla kvalitātes uzlabojumiem, principā pietiek ar 300 x 300 izmēru, un attēls tiek saglabāts jaunā mapē.
- Un pēdēja funkcija iterē caur visām failām un izmanto OCR lai atazīt tekstu.
  
  ![image](https://github.com/user-attachments/assets/f968ec0a-35a1-4b11-8cff-bb05bd04e961)

  ![image](https://github.com/user-attachments/assets/c50bc613-7778-4ae5-a465-376b8fc1e484)


- Variants ar video apstrādi nav galīgais, ir jāveic papildu testēšanu. Ja ceļa zīme atradīsies liela attālumā var būt grūtības ar teksta atpazīšanu, līdz ar to var būt implementēti papildus uzlabojumi.
