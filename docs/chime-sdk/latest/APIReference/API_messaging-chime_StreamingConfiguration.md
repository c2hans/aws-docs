---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_StreamingConfiguration.html
---

# StreamingConfiguration
<a name="API_messaging-chime_StreamingConfiguration"></a>

The configuration for connecting a messaging stream to Amazon Kinesis.

## Contents
<a name="API_messaging-chime_StreamingConfiguration_Contents"></a>

 ** DataType **   <a name="chimesdk-Type-messaging-chime_StreamingConfiguration-DataType"></a>
The data type of the configuration.
Type: String
Valid Values: `Channel | ChannelMessage`
Required: Yes

 ** ResourceArn **   <a name="chimesdk-Type-messaging-chime_StreamingConfiguration-ResourceArn"></a>
The ARN of the resource in the configuration.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## See Also
<a name="API_messaging-chime_StreamingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/StreamingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/StreamingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/StreamingConfiguration)
