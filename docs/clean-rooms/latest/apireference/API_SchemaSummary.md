---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SchemaSummary.html
---

# SchemaSummary
<a name="API_SchemaSummary"></a>

The schema summary for the objects listed by the request.

## Contents
<a name="API_SchemaSummary_Contents"></a>

 ** analysisRuleTypes **   <a name="API-Type-SchemaSummary-analysisRuleTypes"></a>
The types of analysis rules that are associated with this schema object.
Type: Array of strings
Valid Values: `AGGREGATION | LIST | CUSTOM | ID_MAPPING_TABLE`
Required: Yes

 ** collaborationArn **   <a name="API-Type-SchemaSummary-collaborationArn"></a>
The unique ARN for the collaboration that the schema belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-SchemaSummary-collaborationId"></a>
The unique ID for the collaboration that the schema belongs to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-SchemaSummary-createTime"></a>
The time the schema object was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-SchemaSummary-creatorAccountId"></a>
The unique account ID for the AWS account that owns the schema.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** name **   <a name="API-Type-SchemaSummary-name"></a>
The name for the schema object.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** type **   <a name="API-Type-SchemaSummary-type"></a>
The type of schema object.
Type: String
Valid Values: `TABLE | ID_MAPPING_TABLE | INTERMEDIATE_TABLE`
Required: Yes

 ** updateTime **   <a name="API-Type-SchemaSummary-updateTime"></a>
The time the schema object was last updated.
Type: Timestamp
Required: Yes

 ** analysisMethod **   <a name="API-Type-SchemaSummary-analysisMethod"></a>
The analysis method for the associated schema.
 `DIRECT_QUERY` allows SQL queries to be run directly on this table.
 `DIRECT_JOB` allows PySpark jobs to be run directly on this table.
 `MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.
Type: String
Valid Values: `DIRECT_QUERY | DIRECT_JOB | MULTIPLE`
Required: No

 ** resourceArn **   <a name="API-Type-SchemaSummary-resourceArn"></a>
The Amazon Resource Name (ARN) of the schema summary resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership\/[\d\w-]+\/(configuredtableassociation|idmappingtable)\/[\d\w-]+`
Required: No

 ** selectedAnalysisMethods **   <a name="API-Type-SchemaSummary-selectedAnalysisMethods"></a>
 The selected analysis methods for the schema.
Type: Array of strings
Valid Values: `DIRECT_QUERY | DIRECT_JOB`
Required: No

## See Also
<a name="API_SchemaSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SchemaSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SchemaSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SchemaSummary)
