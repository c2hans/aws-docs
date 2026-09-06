---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_Schema.html
---

# Schema
<a name="API_Schema"></a>

A schema is a relation within a collaboration.

## Contents
<a name="API_Schema_Contents"></a>

 ** analysisRuleTypes **   <a name="API-Type-Schema-analysisRuleTypes"></a>
The analysis rule types that are associated with the schema. Currently, only one entry is present.
Type: Array of strings
Valid Values: `AGGREGATION | LIST | CUSTOM | ID_MAPPING_TABLE`
Required: Yes

 ** collaborationArn **   <a name="API-Type-Schema-collaborationArn"></a>
The unique Amazon Resource Name (ARN) for the collaboration that the schema belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-Schema-collaborationId"></a>
The unique ID for the collaboration that the schema belongs to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** columns **   <a name="API-Type-Schema-columns"></a>
The columns for the relation that this schema represents.
Type: Array of [Column](API_Column.md) objects
Required: Yes

 ** createTime **   <a name="API-Type-Schema-createTime"></a>
The time at which the schema was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-Schema-creatorAccountId"></a>
The unique account ID for the AWS account that owns the schema.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** description **   <a name="API-Type-Schema-description"></a>
A description for the schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: Yes

 ** name **   <a name="API-Type-Schema-name"></a>
A name for the schema. The schema relation is referred to by this name when queried by a protected query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** partitionKeys **   <a name="API-Type-Schema-partitionKeys"></a>
The partition keys for the dataset underlying this schema.
Type: Array of [Column](API_Column.md) objects
Required: Yes

 ** schemaStatusDetails **   <a name="API-Type-Schema-schemaStatusDetails"></a>
Details about the status of the schema. Currently, only one entry is present.
Type: Array of [SchemaStatusDetail](API_SchemaStatusDetail.md) objects
Required: Yes

 ** type **   <a name="API-Type-Schema-type"></a>
The type of schema.
Type: String
Valid Values: `TABLE | ID_MAPPING_TABLE | INTERMEDIATE_TABLE`
Required: Yes

 ** updateTime **   <a name="API-Type-Schema-updateTime"></a>
The most recent time at which the schema was updated.
Type: Timestamp
Required: Yes

 ** analysisMethod **   <a name="API-Type-Schema-analysisMethod"></a>
The analysis method for the schema.
 `DIRECT_QUERY` allows SQL queries to be run directly on this table.
 `DIRECT_JOB` allows PySpark jobs to be run directly on this table.
 `MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.
Type: String
Valid Values: `DIRECT_QUERY | DIRECT_JOB | MULTIPLE`
Required: No

 ** resourceArn **   <a name="API-Type-Schema-resourceArn"></a>
The Amazon Resource Name (ARN) of the schema resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership\/[\d\w-]+\/(configuredtableassociation|idmappingtable)\/[\d\w-]+`
Required: No

 ** schemaTypeProperties **   <a name="API-Type-Schema-schemaTypeProperties"></a>
The schema type properties.
Type: [SchemaTypeProperties](API_SchemaTypeProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** selectedAnalysisMethods **   <a name="API-Type-Schema-selectedAnalysisMethods"></a>
 The selected analysis methods for the schema.
Type: Array of strings
Valid Values: `DIRECT_QUERY | DIRECT_JOB`
Required: No

## See Also
<a name="API_Schema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/Schema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/Schema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/Schema)
