---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorEntity.html
---

# ConnectorEntity
<a name="API_ConnectorEntity"></a>

 The high-level entity that can be queried in Amazon AppFlow. For example, a Salesforce entity might be an *Account* or *Opportunity*, whereas a ServiceNow entity might be an *Incident*.

## Contents
<a name="API_ConnectorEntity_Contents"></a>

 ** name **   <a name="appflow-Type-ConnectorEntity-name"></a>
 The name of the connector entity.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: Yes

 ** hasNestedEntities **   <a name="appflow-Type-ConnectorEntity-hasNestedEntities"></a>
 Specifies whether the connector entity is a parent or a category and has more entities nested underneath it. If another call is made with `entitiesPath = "the_current_entity_name_with_hasNestedEntities_true"`, then it returns the nested entities underneath it. This provides a way to retrieve all supported entities in a recursive fashion.
Type: Boolean
Required: No

 ** label **   <a name="appflow-Type-ConnectorEntity-label"></a>
 The label applied to the connector entity.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `.*`
Required: No

## See Also
<a name="API_ConnectorEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorEntity)
