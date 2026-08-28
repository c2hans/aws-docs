---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicyErrorItem.html
---

# BatchGetPolicyErrorItem
<a name="API_BatchGetPolicyErrorItem"></a>

Contains the information about an error resulting from a `BatchGetPolicy` API call.

## Contents
<a name="API_BatchGetPolicyErrorItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** code **   <a name="verifiedpermissions-Type-BatchGetPolicyErrorItem-code"></a>
The error code that was returned.
Type: String
Valid Values: `POLICY_STORE_NOT_FOUND | POLICY_NOT_FOUND | POLICY_STORE_ALIAS_NOT_FOUND`
Required: Yes

 ** message **   <a name="verifiedpermissions-Type-BatchGetPolicyErrorItem-message"></a>
A detailed error message.
Type: String
Required: Yes

 ** policyId **   <a name="verifiedpermissions-Type-BatchGetPolicyErrorItem-policyId"></a>
The identifier of the policy associated with the failed request.
Type: String
Required: Yes

 ** policyStoreId **   <a name="verifiedpermissions-Type-BatchGetPolicyErrorItem-policyStoreId"></a>
The identifier of the policy store associated with the failed request.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetPolicyErrorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchGetPolicyErrorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchGetPolicyErrorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchGetPolicyErrorItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
