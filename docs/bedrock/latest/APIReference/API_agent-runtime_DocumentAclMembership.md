---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DocumentAclMembership.html
---

# DocumentAclMembership
<a name="API_agent-runtime_DocumentAclMembership"></a>

The membership entry for a document access control list (ACL), containing conditions and their logical relation.

## Contents
<a name="API_agent-runtime_DocumentAclMembership_Contents"></a>

 ** conditions **   <a name="bedrock-Type-agent-runtime_DocumentAclMembership-conditions"></a>
The list of conditions that determine membership.
Type: Array of [DocumentAclCondition](API_agent-runtime_DocumentAclCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** memberRelation **   <a name="bedrock-Type-agent-runtime_DocumentAclMembership-memberRelation"></a>
The logical relation between conditions. Valid values: `AND` – All conditions must match. `OR` – At least one condition must match.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_agent-runtime_DocumentAclMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/DocumentAclMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/DocumentAclMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/DocumentAclMembership)
