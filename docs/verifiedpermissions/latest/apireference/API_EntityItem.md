---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityItem.html
---

# EntityItem
<a name="API_EntityItem"></a>

Contains information about an entity that can be referenced in a Cedar policy.

This data type is used as one of the fields in the [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html) structure.

 `{ "identifier": { "entityType": "Photo", "entityId": "VacationPhoto94.jpg" }, "attributes": {}, "parents": [ { "entityType": "Album", "entityId": "alice_folder" } ] }`

## Contents
<a name="API_EntityItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** identifier **   <a name="verifiedpermissions-Type-EntityItem-identifier"></a>
The identifier of the entity.
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: Yes

 ** attributes **   <a name="verifiedpermissions-Type-EntityItem-attributes"></a>
A list of attributes for the entity.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** parents **   <a name="verifiedpermissions-Type-EntityItem-parents"></a>
The parent entities in the hierarchy that contains the entity. A principal or resource entity can be defined with at most 99 *transitive parents* per authorization request.
A transitive parent is an entity in the hierarchy of entities including all direct parents, and parents of parents. For example, a user can be a member of 91 groups if one of those groups is a member of eight groups, for a total of 100: one entity, 91 entity parents, and eight parents of parents.
Type: Array of [EntityIdentifier](API_EntityIdentifier.md) objects
Required: No

 ** tags **   <a name="verifiedpermissions-Type-EntityItem-tags"></a>
A list of cedar tags for the entity.
Type: String to [CedarTagValue](API_CedarTagValue.md) object map
Required: No

## See Also
<a name="API_EntityItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/EntityItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/EntityItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/EntityItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
