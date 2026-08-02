---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SchemaListItem.html
---

# SchemaListItem
<a name="API_SchemaListItem"></a>

An object that contains minimal details for a schema.

## Contents
<a name="API_SchemaListItem_Contents"></a>

 ** CreatedTime **   <a name="Glue-Type-SchemaListItem-CreatedTime"></a>
The date and time that a schema was created.
Type: String
Required: No

 ** Description **   <a name="Glue-Type-SchemaListItem-Description"></a>
A description for the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** RegistryName **   <a name="Glue-Type-SchemaListItem-RegistryName"></a>
the name of the registry where the schema resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: No

 ** SchemaArn **   <a name="Glue-Type-SchemaListItem-SchemaArn"></a>
The Amazon Resource Name (ARN) for the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
Required: No

 ** SchemaName **   <a name="Glue-Type-SchemaListItem-SchemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: No

 ** SchemaStatus **   <a name="Glue-Type-SchemaListItem-SchemaStatus"></a>
The status of the schema.
Type: String
Valid Values: `AVAILABLE | PENDING | DELETING`
Required: No

 ** UpdatedTime **   <a name="Glue-Type-SchemaListItem-UpdatedTime"></a>
The date and time that a schema was updated.
Type: String
Required: No

## See Also
<a name="API_SchemaListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SchemaListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SchemaListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SchemaListItem)
