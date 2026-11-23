---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_SensitiveDataConfiguration.html
---

# SensitiveDataConfiguration

Controls detection and redaction of sensitive data, such as personally identifiable information (PII), in the output.

## Contents
<a name="API_SensitiveDataConfiguration_Contents"></a>

 ** DetectionMode **   <a name="Textract-Type-SensitiveDataConfiguration-DetectionMode"></a>
The detection mode. Valid values:
+  `DETECTION` - Only detects sensitive data.
+  `DETECTION_AND_REDACTION` - Detects and redacts sensitive data in the output.
+  `DISABLED` - Does not detect sensitive data.
Type: String
Valid Values: `DETECTION | DETECTION_AND_REDACTION | DISABLED`
Required: Yes

 ** PiiEntitiesConfiguration **   <a name="Textract-Type-SensitiveDataConfiguration-PiiEntitiesConfiguration"></a>
The configuration that specifies which PII entity types to detect and how to mask them. If you omit it, Amazon Textract detects all PII entity types (`ALL`) and masks them with `ENTITY_TYPE`.
Type: [PIIEntitiesConfiguration](API_PIIEntitiesConfiguration.md) object
Required: No

## See Also
<a name="API_SensitiveDataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/SensitiveDataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/SensitiveDataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/SensitiveDataConfiguration)
