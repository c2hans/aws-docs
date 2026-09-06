---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTable.html
---

# IntermediateTable
<a name="API_IntermediateTable"></a>

Contains the details of an intermediate table in AWS Clean Rooms. An intermediate table stores a query definition and its materialized results within a collaboration.

## Contents
<a name="API_IntermediateTable_Contents"></a>

 ** arn **   <a name="API-Type-IntermediateTable-arn"></a>
The Amazon Resource Name (ARN) of the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership\/[\d\w-]+\/intermediatetable\/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-IntermediateTable-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-IntermediateTable-collaborationId"></a>
The unique identifier of the collaboration that contains the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-IntermediateTable-createTime"></a>
The time the intermediate table was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-IntermediateTable-id"></a>
The unique identifier of the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-IntermediateTable-membershipArn"></a>
The Amazon Resource Name (ARN) of the membership that contains the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-IntermediateTable-membershipId"></a>
The unique identifier of the membership that contains the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-IntermediateTable-name"></a>
The name of the intermediate table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** populationAnalysisConfiguration **   <a name="API-Type-IntermediateTable-populationAnalysisConfiguration"></a>
The analysis configuration that defines the query used to populate the intermediate table.
Type: [PopulationAnalysisConfiguration](API_PopulationAnalysisConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** status **   <a name="API-Type-IntermediateTable-status"></a>
The current status of the intermediate table.
Type: String
Valid Values: `CREATED | POPULATE_STARTED | POPULATE_SUCCESS | POPULATE_FAILED | DISALLOWED_BY_DATA_PROVIDER | BASE_TABLE_REMOVED | RETENTION_PERIOD_EXPIRED`
Required: Yes

 ** updateTime **   <a name="API-Type-IntermediateTable-updateTime"></a>
The time the intermediate table was last updated.
Type: Timestamp
Required: Yes

 ** analysisRuleTypes **   <a name="API-Type-IntermediateTable-analysisRuleTypes"></a>
The types of analysis rules associated with the intermediate table.
Type: Array of strings
Valid Values: `CUSTOM`
Required: No

 ** childResources **   <a name="API-Type-IntermediateTable-childResources"></a>
The child resources that depend on this intermediate table.
Type: Array of [ChildResource](API_ChildResource.md) objects
Required: No

 ** description **   <a name="API-Type-IntermediateTable-description"></a>
The description of the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** intermediateTableVersion **   <a name="API-Type-IntermediateTable-intermediateTableVersion"></a>
The details of the currently active version of the intermediate table.
Type: [IntermediateTableActiveVersion](API_IntermediateTableActiveVersion.md) object
Required: No

 ** kmsKeyArn **   <a name="API-Type-IntermediateTable-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the intermediate table data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
Required: No

 ** retentionInDays **   <a name="API-Type-IntermediateTable-retentionInDays"></a>
The number of days that populated data is retained before expiring.
Type: Integer
Required: No

 ** schema **   <a name="API-Type-IntermediateTable-schema"></a>
The schema of the intermediate table, containing column definitions. Available after the table has been successfully populated.
Type: [IntermediateTableSchema](API_IntermediateTableSchema.md) object
Required: No

 ** statusReason **   <a name="API-Type-IntermediateTable-statusReason"></a>
The reason for the current status of the intermediate table.
Type: String
Required: No

 ** tableDependencies **   <a name="API-Type-IntermediateTable-tableDependencies"></a>
The list of base tables that this intermediate table depends on.
Type: Array of [IntermediateTableDependency](API_IntermediateTableDependency.md) objects
Required: No

## See Also
<a name="API_IntermediateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTable)
