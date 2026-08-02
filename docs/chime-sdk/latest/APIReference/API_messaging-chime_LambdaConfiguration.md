---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_LambdaConfiguration.html
---

# LambdaConfiguration
<a name="API_messaging-chime_LambdaConfiguration"></a>

Stores metadata about a Lambda processor.

## Contents
<a name="API_messaging-chime_LambdaConfiguration_Contents"></a>

 ** InvocationType **   <a name="chimesdk-Type-messaging-chime_LambdaConfiguration-InvocationType"></a>
Controls how the Lambda function is invoked.
Type: String
Valid Values: `ASYNC`
Required: Yes

 ** ResourceArn **   <a name="chimesdk-Type-messaging-chime_LambdaConfiguration-ResourceArn"></a>
The ARN of the Lambda message processing function.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 2048.
Pattern: `arn:aws:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9\-_\.]+(:(\$LATEST|[a-zA-Z0-9\-_]+))?`
Required: Yes

## See Also
<a name="API_messaging-chime_LambdaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/LambdaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/LambdaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/LambdaConfiguration)
