---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AmazonQPropertiesOutput.html
---

# AmazonQPropertiesOutput
<a name="API_AmazonQPropertiesOutput"></a>

The Amazon Q properties of the connection.

## Contents
<a name="API_AmazonQPropertiesOutput_Contents"></a>

 ** isEnabled **   <a name="datazone-Type-AmazonQPropertiesOutput-isEnabled"></a>
Specifies whether Amazon Q is enabled for the connection.
Type: Boolean
Required: Yes

 ** authMode **   <a name="datazone-Type-AmazonQPropertiesOutput-authMode"></a>
The authentication mode of the connection's Amazon Q properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** profileArn **   <a name="datazone-Type-AmazonQPropertiesOutput-profileArn"></a>
The profile ARN of the connection's Amazon Q properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:[a-z0-9\-]+:[a-z0-9\-]*:[0-9]*:.*`
Required: No

## See Also
<a name="API_AmazonQPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AmazonQPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AmazonQPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AmazonQPropertiesOutput)
