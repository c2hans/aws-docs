---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SchemaVersionListItem.html
---

# SchemaVersionListItem
<a name="API_SchemaVersionListItem"></a>

An object containing the details about a schema version.

## Contents
<a name="API_SchemaVersionListItem_Contents"></a>

 ** CreatedTime **   <a name="Glue-Type-SchemaVersionListItem-CreatedTime"></a>
The date and time the schema version was created.
Type: String
Required: No

 ** SchemaArn **   <a name="Glue-Type-SchemaVersionListItem-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
Required: No

 ** SchemaVersionId **   <a name="Glue-Type-SchemaVersionListItem-SchemaVersionId"></a>
The unique identifier of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** Status **   <a name="Glue-Type-SchemaVersionListItem-Status"></a>
The status of the schema version.
Type: String
Valid Values: `AVAILABLE | PENDING | FAILURE | DELETING`
Required: No

 ** VersionNumber **   <a name="Glue-Type-SchemaVersionListItem-VersionNumber"></a>
The version number of the schema.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

## See Also
<a name="API_SchemaVersionListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SchemaVersionListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SchemaVersionListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SchemaVersionListItem)
