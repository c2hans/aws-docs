---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_GenerativeConfiguration.html
---

# GenerativeConfiguration

Controls the generative capabilities applied during a document insights job, such as summarization and figure captioning.

## Contents
<a name="API_GenerativeConfiguration_Contents"></a>

 ** FigureCaption **   <a name="Textract-Type-GenerativeConfiguration-FigureCaption"></a>
Controls whether generative captions are produced for figures detected in the document. If you omit it, no figure captions are produced.
Type: [FigureCaptionConfiguration](API_FigureCaptionConfiguration.md) object
Required: No

 ** Summarization **   <a name="Textract-Type-GenerativeConfiguration-Summarization"></a>
Controls whether a generative summary of the document is produced. If you omit it, no summary is produced.
Type: [SummarizationConfiguration](API_SummarizationConfiguration.md) object
Required: No

## See Also
<a name="API_GenerativeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/GenerativeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/GenerativeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/GenerativeConfiguration)
