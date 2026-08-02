---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListEntitiesFilter.html
---

# ListEntitiesFilter
<a name="API_ListEntitiesFilter"></a>

An object that filters items in a list of entities.

## Contents
<a name="API_ListEntitiesFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** componentTypeId **   <a name="tm-Type-ListEntitiesFilter-componentTypeId"></a>
The ID of the component type in the entities in the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** externalId **   <a name="tm-Type-ListEntitiesFilter-externalId"></a>
The external-Id property of a component. The external-Id property is the primary key of an external storage system.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** parentEntityId **   <a name="tm-Type-ListEntitiesFilter-parentEntityId"></a>
The parent of the entities in the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_ListEntitiesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListEntitiesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListEntitiesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListEntitiesFilter)
