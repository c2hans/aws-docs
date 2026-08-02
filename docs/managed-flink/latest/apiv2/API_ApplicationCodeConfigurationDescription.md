---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationCodeConfigurationDescription.html
---

# ApplicationCodeConfigurationDescription
<a name="API_ApplicationCodeConfigurationDescription"></a>

Describes code configuration for an application.

## Contents
<a name="API_ApplicationCodeConfigurationDescription_Contents"></a>

 ** CodeContentType **   <a name="APIReference-Type-ApplicationCodeConfigurationDescription-CodeContentType"></a>
Specifies whether the code content is in text or zip format.
Type: String
Valid Values: `PLAINTEXT | ZIPFILE`
Required: Yes

 ** CodeContentDescription **   <a name="APIReference-Type-ApplicationCodeConfigurationDescription-CodeContentDescription"></a>
Describes details about the location and format of the application code.
Type: [CodeContentDescription](API_CodeContentDescription.md) object
Required: No

## See Also
<a name="API_ApplicationCodeConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfigurationDescription)
