---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyItem.html
---

# PolicyItem
<a name="API_PolicyItem"></a>

Contains information about a policy.

This data type is used as a response parameter for the [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html) operation.

## Contents
<a name="API_PolicyItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** createdDate **   <a name="verifiedpermissions-Type-PolicyItem-createdDate"></a>
The date and time the policy was created.
Type: Timestamp
Required: Yes

 ** definition **   <a name="verifiedpermissions-Type-PolicyItem-definition"></a>
The policy definition of an item in the list of policies returned.
Type: [PolicyDefinitionItem](API_PolicyDefinitionItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** lastUpdatedDate **   <a name="verifiedpermissions-Type-PolicyItem-lastUpdatedDate"></a>
The date and time the policy was most recently updated.
Type: Timestamp
Required: Yes

 ** policyId **   <a name="verifiedpermissions-Type-PolicyItem-policyId"></a>
The identifier of the policy you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** policyStoreId **   <a name="verifiedpermissions-Type-PolicyItem-policyStoreId"></a>
The identifier of the policy store where the policy you want information about is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** policyType **   <a name="verifiedpermissions-Type-PolicyItem-policyType"></a>
The type of the policy. This is one of the following values:
+  `STATIC`
+  `TEMPLATE_LINKED`
Type: String
Valid Values: `STATIC | TEMPLATE_LINKED`
Required: Yes

 ** actions **   <a name="verifiedpermissions-Type-PolicyItem-actions"></a>
The action that a policy permits or forbids. For example, `{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}`.
Type: Array of [ActionIdentifier](API_ActionIdentifier.md) objects
Required: No

 ** effect **   <a name="verifiedpermissions-Type-PolicyItem-effect"></a>
The effect of the decision that a policy returns to an authorization request. For example, `"effect": "Permit"`.
Type: String
Valid Values: `Permit | Forbid`
Required: No

 ** name **   <a name="verifiedpermissions-Type-PolicyItem-name"></a>
The name of the policy, if one was assigned when the policy was created or last updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 150.
Pattern: `[a-zA-Z0-9-/_]*`
Required: No

 ** principal **   <a name="verifiedpermissions-Type-PolicyItem-principal"></a>
The principal associated with the policy.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** resource **   <a name="verifiedpermissions-Type-PolicyItem-resource"></a>
The resource associated with the policy.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

## See Also
<a name="API_PolicyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/PolicyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/PolicyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/PolicyItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
