---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_CognitoStreams.html
---

# CognitoStreams
<a name="API_CognitoStreams"></a>

Configuration options for configure Cognito streams.

## Contents
<a name="API_CognitoStreams_Contents"></a>

 ** DisabledReason **   <a name="Cognito-Type-CognitoStreams-DisabledReason"></a>
A string containing the reason why streaming of updates to the identity pool was disabled.
Type: String
Required: No

 ** RoleArn **   <a name="Cognito-Type-CognitoStreams-RoleArn"></a>
The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:iam::\d+:role/.*`
Required: No

 ** StreamingStatus **   <a name="Cognito-Type-CognitoStreams-StreamingStatus"></a>
Status of the Cognito streams. Valid values are:
+ ENABLED - Streaming of updates to identity pool is enabled.
+ DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** StreamName **   <a name="Cognito-Type-CognitoStreams-StreamName"></a>
The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_CognitoStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/CognitoStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/CognitoStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/CognitoStreams)
