# Numberfier

### Beskrivning
Mitt projekt har gått ut på att skapa en AI som kan känna igen husnumer om man i streetview i Google Maps. Det genom att träna den på datan som finns på [denna länk.](http://ufldl.stanford.edu/housenumbers/)
Databasen innehåller två huvuddelar. En del där alla husnummer i bilderna är färdigmarkerade med rutor för att lättare kunna identifiera numrena. Den andra delen är färdigbeskurna nummer så man kan träna upp en AI att känna igen varje sorts nummer.
Min uppgift var då att jag ville träna en AI som kan identifiera alla olika sorters nummer oavsett hur de är utformade då biblioteket innehåller nästan 34 000 olika nummer att träna med.

### Uförande
Min del i det hela var att jag skulle skapa en tyf av algoritm som känner igen genom att använda computer vision och då främst aanvända mig av Open CV. Sedan skulle jag träna upp vikterna genom att använda mig av Google Colab som kan utföra processer på andra maskiner som inte är din egen utan placerad på en server hos Google. Det hjälper att med att slippa sänka datorns prestanda när man arbetar och även att man kan låta processerna gå medan man gör andra saker. Vid själva valideringen av träningen var det meningen att jag skulle kunna öppna Streetview och att datorn skulle kunna identifiera när man visar den ett husnummer. I praktiken har detta projekt inte någon direkt praktisk implementering utan det skulle mest vara ett sett att ha något projekt att hålla på med medan jag ville lära mig mer om AI och mer specifikt computer vision.

### Resultat
Då jag sent kom på exakt vad det var jag ville göra och att jag inte riktit visste hur man skulle gå till väga när man utvecklar den kom jag aldrig riktigt till skott med att ordentligt arbeta med projektet. Mesta delen av tiden satt jag och funderade på vad jag ville göra för projekt och när jag väl kom på denna idé var det inte många timmar kvar av projekttiden. Därav har jag inte kommit särskilt långt i mitt projektarbete. Det jag hunnit med är att hitta den data som krävts för träningen samt att kolla på hur strukturen för datat ser ut. Jag har därefter letat efter smidiga sett att genomföra min träning ch ha hittat ett projekt som gjorde liknande i Python JuPyter. Jag förstod den generella strukturen en hade svårt för att veta hur jag skulle kunna implementera något liknande i mitt projekt. Kolla i filen med .ipynb efter namnet.
