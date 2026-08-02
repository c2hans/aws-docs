---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_SchemaMappingSummary.html
---

# SchemaMappingSummary
<a name="API_SchemaMappingSummary"></a>

An object containing `schemaName`, `schemaArn`, `createdAt`, `updatedAt`, and `hasWorkflows`.

## Contents
<a name="API_SchemaMappingSummary_Contents"></a>

 ** createdAt **   <a name="API-Type-SchemaMappingSummary-createdAt"></a>
The timestamp of when the `SchemaMapping` was created.
Type: Timestamp
Required: Yes

 ** hasWorkflows **   <a name="API-Type-SchemaMappingSummary-hasWorkflows"></a>
Specifies whether the schema mapping has been applied to a workflow.
Type: Boolean
Required: Yes

 ** schemaArn **   <a name="API-Type-SchemaMappingSummary-schemaArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `SchemaMapping`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(schemamapping/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** schemaName **   <a name="API-Type-SchemaMappingSummary-schemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

 ** updatedAt **   <a name="API-Type-SchemaMappingSummary-updatedAt"></a>
The timestamp of when the `SchemaMapping` was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SchemaMappingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/SchemaMappingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/SchemaMappingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/SchemaMappingSummary)
