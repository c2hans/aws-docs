---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_ExtractionConfiguration.html
---

# ExtractionConfiguration

Controls how Amazon Textract extracts content from a document, including whether bounding boxes are returned, the granularity of extraction, and the output format.

## Contents
<a name="API_ExtractionConfiguration_Contents"></a>

 ** BoundingBox **   <a name="Textract-Type-ExtractionConfiguration-BoundingBox"></a>
Controls whether bounding box geometry is included in the extraction output.
Type: [BoundingBoxConfiguration](API_BoundingBoxConfiguration.md) object
Required: Yes

 ** Granularity **   <a name="Textract-Type-ExtractionConfiguration-Granularity"></a>
Controls the granularity levels at which content is extracted.
Type: [ExtractionGranularity](API_ExtractionGranularity.md) object
Required: Yes

 ** OutputFormat **   <a name="Textract-Type-ExtractionConfiguration-OutputFormat"></a>
Controls the format of the extraction output.
Type: [OutputFormat](API_OutputFormat.md) object
Required: Yes

## See Also
<a name="API_ExtractionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/ExtractionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/ExtractionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/ExtractionConfiguration)
