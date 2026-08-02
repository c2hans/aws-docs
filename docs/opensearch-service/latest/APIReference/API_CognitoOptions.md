---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CognitoOptions.html
---

# CognitoOptions
<a name="API_CognitoOptions"></a>

Container for the parameters required to enable Cognito authentication for an OpenSearch Service domain. For more information, see [Configuring Amazon Cognito authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html).

## Contents
<a name="API_CognitoOptions_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-CognitoOptions-Enabled"></a>
Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.
Type: Boolean
Required: No

 ** IdentityPoolId **   <a name="opensearchservice-Type-CognitoOptions-IdentityPoolId"></a>
The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

 ** RoleArn **   <a name="opensearchservice-Type-CognitoOptions-RoleArn"></a>
The `AmazonOpenSearchServiceCognitoAccess` role that allows OpenSearch Service to configure your user pool and identity pool.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
Required: No

 ** UserPoolId **   <a name="opensearchservice-Type-CognitoOptions-UserPoolId"></a>
The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_CognitoOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CognitoOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CognitoOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CognitoOptions)
