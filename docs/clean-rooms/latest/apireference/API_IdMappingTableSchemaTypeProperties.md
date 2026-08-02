---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IdMappingTableSchemaTypeProperties.html
---

# IdMappingTableSchemaTypeProperties
<a name="API_IdMappingTableSchemaTypeProperties"></a>

Additional properties that are specific to the type of the associated schema.

## Contents
<a name="API_IdMappingTableSchemaTypeProperties_Contents"></a>

 ** idMappingTableInputSource **   <a name="API-Type-IdMappingTableSchemaTypeProperties-idMappingTableInputSource"></a>
Defines which ID namespace associations are used to create the ID mapping table.
Type: Array of [IdMappingTableInputSource](API_IdMappingTableInputSource.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

 ** idMappingTableId **   <a name="API-Type-IdMappingTableSchemaTypeProperties-idMappingTableId"></a>
The unique identifier of the ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_IdMappingTableSchemaTypeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IdMappingTableSchemaTypeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IdMappingTableSchemaTypeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IdMappingTableSchemaTypeProperties)
