---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_AuthorizationConfig.html
---

# AuthorizationConfig
<a name="API_AuthorizationConfig"></a>

The authorization configuration in case the HTTP endpoint requires authorization.

## Contents
<a name="API_AuthorizationConfig_Contents"></a>

 ** authorizationType **   <a name="appsync-Type-AuthorizationConfig-authorizationType"></a>
The authorization type that the HTTP endpoint requires.
+  **AWS\_IAM**: The authorization type is Signature Version 4 (SigV4).
Type: String
Valid Values: `AWS_IAM`
Required: Yes

 ** awsIamConfig **   <a name="appsync-Type-AuthorizationConfig-awsIamConfig"></a>
The AWS Identity and Access Management (IAM) settings.
Type: [AwsIamConfig](API_AwsIamConfig.md) object
Required: No

## See Also
<a name="API_AuthorizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/AuthorizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/AuthorizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/AuthorizationConfig)
