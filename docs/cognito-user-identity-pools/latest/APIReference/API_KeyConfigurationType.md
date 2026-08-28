---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_KeyConfigurationType.html
---

# KeyConfigurationType
<a name="API_KeyConfigurationType"></a>

Specifies the key configuration for a user pool. Contains settings for encryption keys used to secure user pool data.

This data type is a request parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_KeyConfigurationType_Contents"></a>

 ** KeyType **   <a name="CognitoUserPools-Type-KeyConfigurationType-KeyType"></a>
The type of encryption key used for the user pool.
AWS\_OWNED\_KEY
A key owned by AWS in AWS Key Management Service.
CUSTOMER\_MANAGED\_KEY
A key managed by the customer in AWS Key Management Service. You must use a multi-region key to enable multi-region replication for a user pool.
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
Required: No

 ** KmsKeyArn **   <a name="CognitoUserPools-Type-KeyConfigurationType-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used for encryption. If not specified, AWS managed keys are used.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

## See Also
<a name="API_KeyConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/KeyConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/KeyConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/KeyConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
