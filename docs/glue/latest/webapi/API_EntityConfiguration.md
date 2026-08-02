---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EntityConfiguration.html
---

# EntityConfiguration
<a name="API_EntityConfiguration"></a>

Configuration that defines how to interact with a specific data entity through the REST API, including its access patterns and schema definition.

## Contents
<a name="API_EntityConfiguration_Contents"></a>

 ** Schema **   <a name="Glue-Type-EntityConfiguration-Schema"></a>
The schema definition for this entity, including field names, types, and other metadata that describes the structure of the data.
Type: String to [FieldDefinition](API_FieldDefinition.md) object map
Key Length Constraints: Minimum length of 1.
Required: No

 ** SourceConfiguration **   <a name="Glue-Type-EntityConfiguration-SourceConfiguration"></a>
The source configuration that defines how to make requests to access this entity's data through the REST API.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: No

## See Also
<a name="API_EntityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EntityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EntityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EntityConfiguration)
