---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableSummary.html
---

# IntermediateTableSummary
<a name="API_IntermediateTableSummary"></a>

Contains summary information about an intermediate table.

## Contents
<a name="API_IntermediateTableSummary_Contents"></a>

 ** arn **   <a name="API-Type-IntermediateTableSummary-arn"></a>
The Amazon Resource Name (ARN) of the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership\/[\d\w-]+\/intermediatetable\/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-IntermediateTableSummary-collaborationArn"></a>
The Amazon Resource Name (ARN) of the collaboration that contains the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-IntermediateTableSummary-collaborationId"></a>
The unique identifier of the collaboration that contains the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-IntermediateTableSummary-createTime"></a>
The time the intermediate table was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-IntermediateTableSummary-id"></a>
The unique identifier of the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-IntermediateTableSummary-membershipArn"></a>
The Amazon Resource Name (ARN) of the membership that contains the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-IntermediateTableSummary-membershipId"></a>
The unique identifier of the membership that contains the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-IntermediateTableSummary-name"></a>
The name of the intermediate table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-IntermediateTableSummary-status"></a>
The current status of the intermediate table.
Type: String
Valid Values: `CREATED | POPULATE_STARTED | POPULATE_SUCCESS | POPULATE_FAILED | DISALLOWED_BY_DATA_PROVIDER | BASE_TABLE_REMOVED | RETENTION_PERIOD_EXPIRED`
Required: Yes

 ** updateTime **   <a name="API-Type-IntermediateTableSummary-updateTime"></a>
The time the intermediate table was last updated.
Type: Timestamp
Required: Yes

 ** analysisRuleTypes **   <a name="API-Type-IntermediateTableSummary-analysisRuleTypes"></a>
The types of analysis rules associated with the intermediate table.
Type: Array of strings
Valid Values: `CUSTOM`
Required: No

 ** description **   <a name="API-Type-IntermediateTableSummary-description"></a>
The description of the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** retentionInDays **   <a name="API-Type-IntermediateTableSummary-retentionInDays"></a>
The number of days that populated data is retained before expiring.
Type: Integer
Required: No

## See Also
<a name="API_IntermediateTableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
