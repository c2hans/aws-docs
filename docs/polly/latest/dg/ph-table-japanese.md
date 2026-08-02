---
source_url: https://docs.aws.amazon.com/polly/latest/dg/ph-table-japanese.html
---

# Japanese (ja-JP)
<a name="ph-table-japanese"></a>

Amazon Polly supports the Pronunciation Kana and Yomigana alphabets for Japanese. To make Amazon Polly use phonetic pronunciation with these alphabets, use the phoneme `alphabet="x-amazon-{{phonetic standard used}}"` attribute.
+ `x-amazon-pron-kana` – indicates that Pronunciation Kana is used. Pronunciation Kana are special Katakana characters used for phonetic transcription and can encode pitch accent.
+ `x-amazon-yomigana` – indicates that Yomigana is used. Yomigana can be conventional Katakana, Hiragana, and Latin alphabets interpreted as hepburn romanization.

The following examples show how these are used:

Pronunciation Kana

```
<speak>
     名前は<phoneme alphabet="x-amazon-pron-kana" ph="ヒロカ'ズ">浩一</phoneme>です。
</speak>
```

Yomigana

```
<speak>
     名前は<phoneme alphabet="x-amazon-yomigana" ph="ひろかず">浩一</phoneme>です。
     名前は<phoneme alphabet="x-amazon-yomigana" ph="ヒロカズ">浩一</phoneme>です。
     名前は<phoneme alphabet="x-amazon-yomigana" ph="Hirokazu">浩一</phoneme>です。
</speak>
```

The following table lists the International Phonetic Alphabet (IPA) phonemes, the Extended Speech Assessment Methods Phonetic Alphabet (X-SAMPA) symbols, and the corresponding visemes for the Japanese voice supported by Amazon Polly.

<table>
<thead>
  <tr><th>IPA</th><th>X-SAMPA</th><th>Description</th><th>Example</th><th>Viseme</th></tr>
</thead>
<tbody>
  <tr><td colspan="5">**Consonants**</td></tr>
  <tr><td>ɾ</td><td>4</td><td>alveolar flap</td><td>練習, **r**enshuu</td><td>t</td></tr>
  <tr><td>ʔ</td><td>?</td><td>glottal stop</td><td>あつっ, atsu**'**</td><td></td></tr>
  <tr><td>b</td><td>b</td><td>voiced bilabial plosive</td><td>舞踊, **b**uyou</td><td>p</td></tr>
  <tr><td>β</td><td>B</td><td>voiced bilabial fricative</td><td>ヴィンテージ, **v**inteeji</td><td>B</td></tr>
  <tr><td>c</td><td>c</td><td>voiceless palatal plosive</td><td>ききょう, **k**i**ky**ou</td><td>k</td></tr>
  <tr><td>ç</td><td>C</td><td>voiceless palatal fricative</td><td>人, **h**ito</td><td>k</td></tr>
  <tr><td>d</td><td>d</td><td>voiced alveolar plosive</td><td>濁点, **d**akuten</td><td>t</td></tr>
  <tr><td>d͡ʑ</td><td>dz\\</td><td>voiced alveolo-palatal affricate</td><td>純, **j**un</td><td>J</td></tr>
  <tr><td>ɡ</td><td>g</td><td>voiced velar plosive</td><td>ご飯, **g**ohan</td><td>k</td></tr>
  <tr><td>h</td><td>h</td><td>voiceless glottal fricative</td><td>本, **h**on</td><td>k</td></tr>
  <tr><td>j</td><td>j</td><td>palatal approximant</td><td>屋根, **y**ane</td><td>i</td></tr>
  <tr><td>ɟ</td><td>J\\</td><td>voiced palatal plosive</td><td>行儀, **gy**ou**g**i</td><td>J</td></tr>
  <tr><td>k</td><td>k</td><td>voiceless velar plosive</td><td>漢字, **k**anji</td><td>k</td></tr>
  <tr><td>ɺ</td><td>l\\</td><td>alveolar lateral flap</td><td>釣り, tsu**r**i</td><td>r</td></tr>
  <tr><td>ɺj</td><td>l\\j</td><td>alveolar lateral flap, palatal approximant</td><td>流行, **ry**uukou</td><td>r</td></tr>
  <tr><td>m</td><td>m</td><td>bilabial nasal</td><td>飯, **m**eshi</td><td>p</td></tr>
  <tr><td>n</td><td>n</td><td>alveolar nasal</td><td>猫, **n**eko</td><td>t</td></tr>
  <tr><td>ɲ</td><td>J</td><td>palatal nasal</td><td>日本, **n**ippon</td><td>J</td></tr>
  <tr><td>ɴ</td><td>N\\</td><td>uvular nasal</td><td>缶, ka**n**</td><td>k</td></tr>
  <tr><td>p</td><td>p</td><td>voiceless bilabial plosive</td><td>パン, **p**an</td><td>p</td></tr>
  <tr><td>ɸ</td><td>p\\</td><td>voiceless bilabial fricative</td><td>福, **h**uku</td><td>f</td></tr>
  <tr><td>s</td><td>s</td><td>voiceless alveolar fricative</td><td>層, **s**ou</td><td>s</td></tr>
  <tr><td>ɕ</td><td>s\\</td><td>voiceless alveolo-palatal fricative</td><td>書簡, **sh**okan</td><td>J</td></tr>
  <tr><td>t</td><td>t</td><td>voiceless alveolar plosive</td><td>手紙, **t**egami</td><td>t</td></tr>
  <tr><td>t͡s</td><td>ts</td><td>voiceless alveolar affricate</td><td>釣り, **ts**uri</td><td>s</td></tr>
  <tr><td>t͡ɕ</td><td>ts\\</td><td>voiceless alveolo-palatal affricate</td><td>吉, ki**ch**i</td><td>J</td></tr>
  <tr><td>w</td><td>w</td><td>labial-velar approximant</td><td>電話, den**w**a</td><td>u</td></tr>
  <tr><td>z</td><td>z</td><td>voiced alveolar fricative</td><td>座敷, **z**ashiki</td><td>s</td></tr>
  <tr><td colspan="5">**Vowels**</td></tr>
  <tr><td>äː</td><td>a:\_"</td><td>long open central unrounded vowel</td><td>羽蟻, h**aa**ri</td><td>a</td></tr>
  <tr><td>ä</td><td>a\_"</td><td>open central unrounded vowel</td><td>仮名, k**a**n**a**</td><td>a</td></tr>
  <tr><td>eː</td><td>e:\_o</td><td>long mid front unrounded vowel</td><td>学生, gakus**ei**</td><td>@</td></tr>
  <tr><td>e</td><td>e\_o</td><td>mid front unrounded vowel</td><td>歴, r**e**ki</td><td>@</td></tr>
  <tr><td>i</td><td>i</td><td>close front unrounded vowel</td><td>気, k**i**</td><td>i</td></tr>
  <tr><td>iː</td><td>i:</td><td>long close front unrounded vowel</td><td>詩歌, sh**ii**ka</td><td>i</td></tr>
  <tr><td>ɯ</td><td>M</td><td>close back unrounded vowel</td><td>運, **u**n</td><td>i</td></tr>
  <tr><td>ɯː</td><td>M:</td><td>long close back unrounded vowel</td><td>宗教, sh**uu**kyou</td><td>i</td></tr>
  <tr><td>oː</td><td>o:\_o</td><td>long mid back rounded vowel</td><td>購読, k**oo**doku</td><td>o</td></tr>
  <tr><td>o</td><td>o\_o</td><td>mid back rounded vowel</td><td>読者, d**o**kusha</td><td>o</td></tr>
</tbody>
</table>
