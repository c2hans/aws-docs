---
source_url: https://docs.aws.amazon.com/polly/latest/dg/ph-table-mandarin.html
---

# Chinese (Mandarin) (cmn-CN)
<a name="ph-table-mandarin"></a>

The following table lists the Pinyin and International Phonetic Alphabet (IPA) phonemes for the Mandarin Chinese voice that is supported by Amazon Polly. Pinyin is the international standard for Standard Chinese romanization. IPA and X-SAMPA are not commonly used but are available for English support. The IPA and X-SAMPA symbols in the table are for reference only and should not be used for Chinese transcription. Pinyin examples and the corresponding visemes are also shown.

To make Amazon Polly use phonetic pronunciation with Pinyin, use the `phoneme alphabet="x-amazon-{{phonetic standard used}}"` tag.

The following examples show this with each standard.

Pinyin:

```
<speak>
     你说 <phoneme alphabet="x-amazon-pinyin" ph="bo2">薄</phoneme>。
     我说 <phoneme alphabet="x-amazon-pinyin" ph="bao2">薄</phoneme>。
</speak>
```

IPA:

```
<speak>
     你说 <phoneme alphabet="ipa" ph="pɪˈkɑːn">pecan</phoneme>。
     我说 <phoneme alphabet="ipa" ph="ˈpi.kæn">pecan</phoneme>。
</speak>
```

X-SAMPA:

```
<speak>
     你说 <phoneme alphabet='x-sampa' ph='pI"kA:n'>pecan</phoneme>。
     我说 <phoneme alphabet='x-sampa' ph='"pi.k{n'>pecan</phoneme>。
</speak>
```

**Note**
Amazon Polly accepts Mandarin Chinese input encoded in UTF-8 only. The GB 18030 encoding standard is not currently supported by Amazon Polly.

**Phoneme/Viseme Table**

<table>
<thead>
  <tr><th>Pinyin</th><th>IPA</th><th>X-SAMPA</th><th>Description</th><th>Pinyin Example</th><th>Viseme</th></tr>
</thead>
<tbody>
  <tr><td colspan="6">**Consonants**</td></tr>
  <tr><td>f</td><td>f </td><td>f</td><td>voiceless labiodental fricative </td><td>发, **f**a1</td><td>f </td></tr>
  <tr><td>h</td><td>h </td><td>h</td><td>voiceless glottal fricative </td><td>和, **h**e2</td><td>k </td></tr>
  <tr><td>g</td><td>k </td><td>k</td><td>voiceless velar plosive </td><td>古, **g**u3 </td><td>k </td></tr>
  <tr><td>k</td><td>kʰ </td><td>k\_h</td><td>aspirated voiceless velar plosive </td><td>苦, **k**u3 </td><td>k </td></tr>
  <tr><td>l</td><td>l </td><td>l</td><td>alveolar lateral approximant </td><td>拉, **l**a1</td><td>t </td></tr>
  <tr><td>m</td><td>m </td><td>m</td><td>bilabial nasal </td><td>骂, **m**a4 </td><td>p </td></tr>
  <tr><td>n</td><td>n </td><td>n</td><td>alveolar nasal </td><td>那, **n**a4 </td><td>t </td></tr>
  <tr><td>ng</td><td>ŋ </td><td>N</td><td>velar nasal </td><td>正, zhe**ng**4 </td><td>k </td></tr>
  <tr><td>b</td><td>p </td><td>p</td><td>voiceless bilabial plosive </td><td>爸, **b**a4</td><td>p </td></tr>
  <tr><td>p</td><td>pʰ </td><td>p\_h</td><td>aspirated voiceless bilabial plosive </td><td>怕, **p**a4 </td><td>p </td></tr>
  <tr><td>s</td><td>s </td><td>s</td><td>voiceless alveolar fricative </td><td>四, **s**i4 </td><td>s </td></tr>
  <tr><td>x</td><td>ɕ </td><td>s\\</td><td>voiceless alveolo-palatal fricative </td><td>西, **x**i1 </td><td>J </td></tr>
  <tr><td>sh</td><td>ʂ </td><td>s`</td><td>voiceless retroflex fricative </td><td>是, **sh**i4 </td><td>S </td></tr>
  <tr><td>d</td><td>t </td><td>t</td><td>voiceless alveolar plosive </td><td>打, **d**a3 </td><td>t </td></tr>
  <tr><td>t</td><td>tʰ </td><td>t\_h</td><td>aspirated voiceless alveolar plosive </td><td>他, **t**a1 </td><td>t </td></tr>
  <tr><td>zh</td><td>ʈ͡ʂ </td><td>t`s` </td><td>voiceless retroflex affricate </td><td>之, **zh**i1 </td><td>S</td></tr>
  <tr><td>ch</td><td>ʈ͡ʂʰ </td><td>t`s`\_h</td><td>aspirated voiceless retroflex affricate </td><td>吃, **ch**i1 </td><td>S </td></tr>
  <tr><td>s</td><td>t͡s </td><td>ts</td><td>voiceless alveolar affricate </td><td>字, **z**i4 </td><td>s </td></tr>
  <tr><td>j</td><td>t͡ɕ </td><td>ts\\</td><td>voiceless alveolo-palatal affricate </td><td>鸡, **j**i1 </td><td>J </td></tr>
  <tr><td>q</td><td>t͡ɕʰ </td><td>ts\\\_h</td><td>aspirated voiceless alveolo-palatal affricate </td><td>七, **q**i1 </td><td>J </td></tr>
  <tr><td>c</td><td>t͡sʰ </td><td>ts\_h</td><td>aspirated voiceless alveolar affricate </td><td>次, **c**i4 </td><td>s </td></tr>
  <tr><td>w</td><td>w </td><td>w</td><td>labio-velar approximant </td><td>我, **w**o3 </td><td>u </td></tr>
  <tr><td>r</td><td>ʐ </td><td>z`</td><td>voiced retroflex fricative </td><td>日, **r**i4 </td><td>S </td></tr>
  <tr><td colspan="6">**"er" and "r" colored syllables**</td></tr>
  <tr><td>er</td><td>ɚ </td><td>@` </td><td>r-coloured mid central vowel</td><td>二, **er**4 </td><td>@ </td></tr>
  <tr><td>-r</td><td> </td><td></td><td>r-colored syllable </td><td>馅儿, xian**r**4 </td><td>@ </td></tr>
  <tr><td colspan="6">**Vowels**</td></tr>
  <tr><td>e</td><td>ɤ </td><td>7</td><td>close-mid back unrounded vowel </td><td>恶, **e**4</td><td>e </td></tr>
  <tr><td>e</td><td>ə </td><td>@</td><td>mid central vowel </td><td>恩, **e**n1</td><td>@ </td></tr>
  <tr><td>a</td><td>a </td><td>a</td><td>open front unrounded vowel </td><td>安, **a**n1</td><td>a </td></tr>
  <tr><td>ai</td><td>aɪ </td><td>aI </td><td>diphthong </td><td>爱, **ai**4</td><td>a </td></tr>
  <tr><td>ao</td><td>aʊ </td><td>aU</td><td>diphthong </td><td>奥, **ao**4</td><td>a </td></tr>
  <tr><td>ei</td><td>eɪ </td><td>e</td><td>diphthong </td><td>诶, **ei**4</td><td>e </td></tr>
  <tr><td>e</td><td>ɛ </td><td>E</td><td>open-mid front unrounded vowel </td><td>姐, ji**e**3</td><td>E </td></tr>
  <tr><td>i</td><td>i </td><td>i</td><td>close front unrounded vowel </td><td>鸡, j**i**1</td><td>i </td></tr>
  <tr><td>ou</td><td>oʊ </td><td>oU</td><td>diphthong </td><td>欧, **ou**1</td><td>o </td></tr>
  <tr><td>o</td><td>ɔ </td><td>O</td><td>open-mid back rounded vowel </td><td>哦, **o**4</td><td>o </td></tr>
  <tr><td>u</td><td>u </td><td>u</td><td>close back rounded vowel </td><td>主, zh**u**3</td><td>u </td></tr>
  <tr><td>yu</td><td>y </td><td>y</td><td>close front rounded vowel </td><td>于, yu2</td><td>u </td></tr>
  <tr><td colspan="6">**Tone marks and Additional Symbols**</td></tr>
  <tr><td>1</td><td> </td><td></td><td>high level tone</td><td>淤, yu1 </td><td></td></tr>
  <tr><td>2</td><td> </td><td></td><td>rising tone</td><td>鱼, yu2 </td><td></td></tr>
  <tr><td>3</td><td> </td><td></td><td>low (falling-rising) tone</td><td>语, yu3 </td><td></td></tr>
  <tr><td>4</td><td> </td><td></td><td>falling tone</td><td>育, yu4 </td><td></td></tr>
  <tr><td>0</td><td> </td><td></td><td>neutral tone</td><td>的, de0 </td><td></td></tr>
  <tr><td>-</td><td>.</td><td>.</td><td>syllable boundary</td><td>语音 yu3-yin1</td><td> </td></tr>
</tbody>
</table>
