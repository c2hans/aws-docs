---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_NumberAttributeConstraintsType.html
---

# NumberAttributeConstraintsType
<a name="API_NumberAttributeConstraintsType"></a>

The minimum and maximum values of an attribute that is of the number type, for example `custom:age`.

This data type is part of [SchemaAttributeType](API_SchemaAttributeType.md). It defines the length constraints on number-type attributes that you configure in [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and displays the length constraints of all number-type attributes in the response to [DescribeUserPool](API_DescribeUserPool.md)

## Contents
<a name="API_NumberAttributeConstraintsType_Contents"></a>

 ** MaxValue **   <a name="CognitoUserPools-Type-NumberAttributeConstraintsType-MaxValue"></a>
The maximum length of a number attribute value. Must be a number less than or equal to `2^1023`, represented as a string with a length of 131072 characters or fewer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** MinValue **   <a name="CognitoUserPools-Type-NumberAttributeConstraintsType-MinValue"></a>
The minimum value of an attribute that is of the number data type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_NumberAttributeConstraintsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/NumberAttributeConstraintsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/NumberAttributeConstraintsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/NumberAttributeConstraintsType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
