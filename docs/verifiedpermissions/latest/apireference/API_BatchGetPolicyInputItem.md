---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchGetPolicyInputItem.html
---

# BatchGetPolicyInputItem
<a name="API_BatchGetPolicyInputItem"></a>

Information about a policy that you include in a `BatchGetPolicy` API request.

## Contents
<a name="API_BatchGetPolicyInputItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** policyId **   <a name="verifiedpermissions-Type-BatchGetPolicyInputItem-policyId"></a>
The identifier of the policy you want information about.
You can use the policy name in place of the policy ID. When using a name, prefix it with `name/`. For example:
+ ID: `SPEXAMPLEabcdefg111111`
+ Name: `name/example-policy`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** policyStoreId **   <a name="verifiedpermissions-Type-BatchGetPolicyInputItem-policyStoreId"></a>
The identifier of the policy store where the policy you want information about is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

## See Also
<a name="API_BatchGetPolicyInputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchGetPolicyInputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchGetPolicyInputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchGetPolicyInputItem)
