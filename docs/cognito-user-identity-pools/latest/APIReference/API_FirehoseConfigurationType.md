---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_FirehoseConfigurationType.html
---

# FirehoseConfigurationType
<a name="API_FirehoseConfigurationType"></a>

Configuration for the Amazon Data Firehose stream destination of user activity log export with threat protection.

## Contents
<a name="API_FirehoseConfigurationType_Contents"></a>

 ** StreamArn **   <a name="CognitoUserPools-Type-FirehoseConfigurationType-StreamArn"></a>
The ARN of an Amazon Data Firehose stream that's the destination for threat protection log export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

## See Also
<a name="API_FirehoseConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/FirehoseConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/FirehoseConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/FirehoseConfigurationType)
