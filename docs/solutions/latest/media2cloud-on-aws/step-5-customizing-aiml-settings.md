---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/step-5-customizing-aiml-settings.html
---

# Step 5: Customizing AI/ML settings
<a name="step-5-customizing-aiml-settings"></a>

 In this version of Media2Cloud on AWS, users have a lot of flexibility on the AI/ML services that are used. They also have the ability to configure those services for their use cases.

1.  In the web interface select **Settings** from the top navigation bar.

1.  In the **Amazon Rekognition Settings** section:
   +  You can set the minimum confidence level that you want results from.
   +  Toggle on or off specific detection types.
   +  Select the face collection that you want to use when analyzing assets.
   +  When using Amazon Rekognition to detect text on screen, you can select the specific regions of the screen for analysis.
   +  If you have created a custom AI/ML model using Amazon Rekognition Custom Labels, you can use that model when analyzing assets.
   +  The **Frame Based Analysis** section give the flexibility to switch from the Amazon Rekognition Video API to the Amazon Rekognition Image API. When you toggle the **Frame Based Analysis** button on, you can determine the frequency that frames are analyzed.

1.  In the **Amazon Transcribe** settings section:
   +  Select the language that you want Amazon Transcribe to create a transcript of the video in. For a complete list of supported languages, refer to [Amazon Transcribe Supported Languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html#table-language-matrix).
   +  If you have created a **Custom Vocabulary** to improve the accuracy of Amazon Transcribe, you can select that model for the analysis of your assets.
   +  If you have created a **Custom Language Model** you can activate that model for the analysis of your assets.

1.  In the **Amazon Comprehend** settings section:
   +  Activate **Entity Detection, Sentiment Analysis,** and **Key phrase Detection**.
   +  If you have built a **Custom Entity Recognizer** to identify custom entities for your business needs, you can activate that as well.

1.  In the **Amazon Textract** settings section, you can activate the service to extract text from documents that you are analyzing.
