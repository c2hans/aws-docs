---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_S3ConfigurationType.html
---

# S3ConfigurationType
<a name="API_S3ConfigurationType"></a>

Configuration for the Amazon S3 bucket destination of user activity log export with threat protection.

## Contents
<a name="API_S3ConfigurationType_Contents"></a>

 ** BucketArn **   <a name="CognitoUserPools-Type-S3ConfigurationType-BucketArn"></a>
The ARN of an Amazon S3 bucket that's the destination for threat protection log export.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1024.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:::[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

## See Also
<a name="API_S3ConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/S3ConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/S3ConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/S3ConfigurationType)
