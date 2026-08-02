---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/using-ssml-to-control-speech-synthesis.html
---

# Using SSML to control speech synthesis
<a name="using-ssml-to-control-speech-synthesis"></a>

The solution supports [Speech Synthesis Markup Language](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html) (SSML) reference—​providing additional control over the speech generation for your response. To use this feature, populate the **SSML answer** field in the content designer.

1. From the content designer, edit item `AWS-QnABot001` ` "What is Q and A Bot" ` by selecting the **Advanced** section and entering the following text in the SSML Answer field:

   ```
   <speak>AWS <sub alias="Q and A">QnA</sub> Bot is <amazon:effect name="drc">great</amazon:effect>. <sub alias="Q and A">QnA</sub> Bot supports <sub alias="Speech Synthesis Markup Language ">SSML</sub> using Polly's neural voice. <prosody rate="150%">I can speak very fast</prosody>, <prosody rate="75%">or very slowly</prosody>. <prosody volume="-16dB">I can speak quietly</prosody>, <amazon:effect name="drc">or speak loud and clear</amazon:effect>. I can say <phoneme alphabet="ipa" ph="təˈmɑːtəʊ">tomato</phoneme> and tomato. Visit docs.aws.amazon.com/polly/latest/dg/supportedtags for more information.</speak>
   ```

1. Choose **UPDATE** to save the modification.

1. Use the web UI to ask, using voice: ` "What is Q and A bot?" `, and listen to the whispered response.

1. Choose **UPDATE** to save the item.

1. Choose **ADD** to create a new item for our first follow-up question:

   1. Enter ID: `Alexa.Cost`

   1. Enter question: `How much does it cost?`

   1. Enter answer: `For latest prices on the Echo Show, see the Amazon retail site or`

   1. Enter topic: `EchoShow`
