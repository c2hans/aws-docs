---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeterminingPolicyItem.html
---

# DeterminingPolicyItem
<a name="API_DeterminingPolicyItem"></a>

Contains information about one of the policies that determined an authorization decision.

This data type is used as an element in a response parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html), [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html), and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

Example: `"determiningPolicies":[{"policyId":"SPEXAMPLEabcdefg111111"}]`

## Contents
<a name="API_DeterminingPolicyItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** policyId **   <a name="verifiedpermissions-Type-DeterminingPolicyItem-policyId"></a>
The Id of a policy that determined to an authorization decision.
Example: `"policyId":"SPEXAMPLEabcdefg111111"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

## See Also
<a name="API_DeterminingPolicyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/DeterminingPolicyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/DeterminingPolicyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/DeterminingPolicyItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
