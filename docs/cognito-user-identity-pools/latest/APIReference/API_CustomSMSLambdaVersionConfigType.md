---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CustomSMSLambdaVersionConfigType.html
---

# CustomSMSLambdaVersionConfigType
<a name="API_CustomSMSLambdaVersionConfigType"></a>

The properties of a custom SMS sender Lambda trigger.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_CustomSMSLambdaVersionConfigType_Contents"></a>

 ** LambdaArn **   <a name="CognitoUserPools-Type-CustomSMSLambdaVersionConfigType-LambdaArn"></a>
The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: Yes

 ** LambdaVersion **   <a name="CognitoUserPools-Type-CustomSMSLambdaVersionConfigType-LambdaVersion"></a>
The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.
You must use a `LambdaVersion` of `V1_0` with a custom sender function.
Type: String
Valid Values: `V1_0`
Required: Yes

## See Also
<a name="API_CustomSMSLambdaVersionConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CustomSMSLambdaVersionConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CustomSMSLambdaVersionConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CustomSMSLambdaVersionConfigType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
