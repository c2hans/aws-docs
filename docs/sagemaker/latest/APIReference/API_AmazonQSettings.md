---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AmazonQSettings.html
---

# AmazonQSettings
<a name="API_AmazonQSettings"></a>

A collection of settings that configure the Amazon Q experience within the domain.

## Contents
<a name="API_AmazonQSettings_Contents"></a>

 ** QProfileArn **   <a name="sagemaker-Type-AmazonQSettings-QProfileArn"></a>
The ARN of the Amazon Q profile used within the domain.
Type: String
Pattern: `arn:[-.a-z0-9]{1,63}:codewhisperer:([-.a-z0-9]{0,63}:){2}([a-zA-Z0-9-_:/]){1,1023}`
Required: No

 ** Status **   <a name="sagemaker-Type-AmazonQSettings-Status"></a>
Whether Amazon Q has been enabled within the domain.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_AmazonQSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AmazonQSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AmazonQSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AmazonQSettings)
