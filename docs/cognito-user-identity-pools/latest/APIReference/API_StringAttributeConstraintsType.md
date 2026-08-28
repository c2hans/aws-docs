---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StringAttributeConstraintsType.html
---

# StringAttributeConstraintsType
<a name="API_StringAttributeConstraintsType"></a>

The minimum and maximum length values of an attribute that is of the string type, for example `custom:department`.

This data type is part of [SchemaAttributeType](API_SchemaAttributeType.md). It defines the length constraints on string-type attributes that you configure in [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and displays the length constraints of all string-type attributes in the response to [DescribeUserPool](API_DescribeUserPool.md)

## Contents
<a name="API_StringAttributeConstraintsType_Contents"></a>

 ** MaxLength **   <a name="CognitoUserPools-Type-StringAttributeConstraintsType-MaxLength"></a>
The maximum length of a string attribute value. Must be a number less than or equal to `2^1023`, represented as a string with a length of 131072 characters or fewer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** MinLength **   <a name="CognitoUserPools-Type-StringAttributeConstraintsType-MinLength"></a>
The minimum length of a string attribute value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_StringAttributeConstraintsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/StringAttributeConstraintsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/StringAttributeConstraintsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/StringAttributeConstraintsType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
