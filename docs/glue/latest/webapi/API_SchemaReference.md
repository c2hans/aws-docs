---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SchemaReference.html
---

# SchemaReference
<a name="API_SchemaReference"></a>

An object that references a schema stored in the AWS Glue Schema Registry.

## Contents
<a name="API_SchemaReference_Contents"></a>

 ** SchemaId **   <a name="Glue-Type-SchemaReference-SchemaId"></a>
A structure that contains schema identity fields. Either this or the `SchemaVersionId` has to be provided.
Type: [SchemaId](API_SchemaId.md) object
Required: No

 ** SchemaVersionId **   <a name="Glue-Type-SchemaReference-SchemaVersionId"></a>
The unique ID assigned to a version of the schema. Either this or the `SchemaId` has to be provided.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** SchemaVersionNumber **   <a name="Glue-Type-SchemaReference-SchemaVersionNumber"></a>
The version number of the schema.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

## See Also
<a name="API_SchemaReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SchemaReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SchemaReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SchemaReference)
