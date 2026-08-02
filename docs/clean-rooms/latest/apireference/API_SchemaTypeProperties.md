---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SchemaTypeProperties.html
---

# SchemaTypeProperties
<a name="API_SchemaTypeProperties"></a>

Information about the schema type properties.

## Contents
<a name="API_SchemaTypeProperties_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configuredTableAssociation **   <a name="API-Type-SchemaTypeProperties-configuredTableAssociation"></a>
The schema type properties for a configured table association.
Type: [ConfiguredTableAssociationSchemaTypeProperties](API_ConfiguredTableAssociationSchemaTypeProperties.md) object
Required: No

 ** idMappingTable **   <a name="API-Type-SchemaTypeProperties-idMappingTable"></a>
The ID mapping table for the schema type properties.
Type: [IdMappingTableSchemaTypeProperties](API_IdMappingTableSchemaTypeProperties.md) object
Required: No

 ** intermediateTable **   <a name="API-Type-SchemaTypeProperties-intermediateTable"></a>
The schema type properties for an intermediate table.
Type: [IntermediateTableSchemaTypeProperties](API_IntermediateTableSchemaTypeProperties.md) object
Required: No

## See Also
<a name="API_SchemaTypeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SchemaTypeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SchemaTypeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SchemaTypeProperties)
