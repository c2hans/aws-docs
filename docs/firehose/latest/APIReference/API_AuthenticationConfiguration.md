---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AuthenticationConfiguration.html
---

# AuthenticationConfiguration
<a name="API_AuthenticationConfiguration"></a>

The authentication configuration of the Amazon MSK cluster.

## Contents
<a name="API_AuthenticationConfiguration_Contents"></a>

 ** Connectivity **   <a name="Firehose-Type-AuthenticationConfiguration-Connectivity"></a>
The type of connectivity used to access the Amazon MSK cluster.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-AuthenticationConfiguration-RoleARN"></a>
The ARN of the role used to access the Amazon MSK cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_AuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AuthenticationConfiguration)
