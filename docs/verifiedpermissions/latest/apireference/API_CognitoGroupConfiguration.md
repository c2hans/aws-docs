---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoGroupConfiguration.html
---

# CognitoGroupConfiguration
<a name="API_CognitoGroupConfiguration"></a>

The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.

This data type is part of a [CognitoUserPoolConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfiguration.html) structure and is a request parameter in [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Contents
<a name="API_CognitoGroupConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** groupEntityType **   <a name="verifiedpermissions-Type-CognitoGroupConfiguration-groupEntityType"></a>
The name of the schema entity type that's mapped to the user pool group. Defaults to `AWS::CognitoGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `([_a-zA-Z][_a-zA-Z0-9]*::)*[_a-zA-Z][_a-zA-Z0-9]*`
Required: Yes

## See Also
<a name="API_CognitoGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CognitoGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CognitoGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CognitoGroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
