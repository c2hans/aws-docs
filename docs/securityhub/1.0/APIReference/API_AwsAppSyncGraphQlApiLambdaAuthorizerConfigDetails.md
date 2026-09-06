---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails.html
---

# AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails
<a name="API_AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails"></a>

 Specifies the authorization configuration for using an Lambda function with your AWS AppSync GraphQL API endpoint.

## Contents
<a name="API_AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails_Contents"></a>

 ** AuthorizerResultTtlInSeconds **   <a name="securityhub-Type-AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails-AuthorizerResultTtlInSeconds"></a>
 The number of seconds a response should be cached for. The default is 5 minutes (300 seconds).
Type: Integer
Required: No

 ** AuthorizerUri **   <a name="securityhub-Type-AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails-AuthorizerUri"></a>
 The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (.../v3), or an alias ARN.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IdentityValidationExpression **   <a name="securityhub-Type-AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails-IdentityValidationExpression"></a>
 A regular expression for validation of tokens before the Lambda function is called.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails)
