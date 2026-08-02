---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclCondition.html
---

# DocumentAclCondition
<a name="API_DocumentAclCondition"></a>

Represents a condition in the document's ACL, specifying access rules for users and groups.

## Contents
<a name="API_DocumentAclCondition_Contents"></a>

 ** groups **   <a name="qbusiness-Type-DocumentAclCondition-groups"></a>
An array of group identifiers that this condition applies to. Groups listed here are subject to the access rule defined by this condition.
Type: Array of [DocumentAclGroup](API_DocumentAclGroup.md) objects
Required: No

 ** memberRelation **   <a name="qbusiness-Type-DocumentAclCondition-memberRelation"></a>
The logical relation between members in the condition, determining how multiple user or group conditions are combined.
Type: String
Valid Values: `AND | OR`
Required: No

 ** users **   <a name="qbusiness-Type-DocumentAclCondition-users"></a>
An array of user identifiers that this condition applies to. Users listed here are subject to the access rule defined by this condition.
Type: Array of [DocumentAclUser](API_DocumentAclUser.md) objects
Required: No

## See Also
<a name="API_DocumentAclCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAclCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAclCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAclCondition)
