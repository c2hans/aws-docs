---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SchemaId.html
---

# SchemaId
<a name="API_SchemaId"></a>

The unique ID of the schema in the AWS Glue schema registry.

## Contents
<a name="API_SchemaId_Contents"></a>

 ** RegistryName **   <a name="Glue-Type-SchemaId-RegistryName"></a>
The name of the schema registry that contains the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: No

 ** SchemaArn **   <a name="Glue-Type-SchemaId-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema. One of `SchemaArn` or `SchemaName` has to be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
Required: No

 ** SchemaName **   <a name="Glue-Type-SchemaId-SchemaName"></a>
The name of the schema. One of `SchemaArn` or `SchemaName` has to be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: No

## See Also
<a name="API_SchemaId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SchemaId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SchemaId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SchemaId)
