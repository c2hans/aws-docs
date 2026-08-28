---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableVersionSummary.html
---

# IntermediateTableVersionSummary
<a name="API_IntermediateTableVersionSummary"></a>

Contains summary information about a version of an intermediate table.

## Contents
<a name="API_IntermediateTableVersionSummary_Contents"></a>

 ** analysisId **   <a name="API-Type-IntermediateTableVersionSummary-analysisId"></a>
The identifier of the protected query that created this version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** analysisType **   <a name="API-Type-IntermediateTableVersionSummary-analysisType"></a>
The type of analysis that created this version.
Type: String
Valid Values: `QUERY`
Required: Yes

 ** createTime **   <a name="API-Type-IntermediateTableVersionSummary-createTime"></a>
The time the version was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="API-Type-IntermediateTableVersionSummary-status"></a>
The status of the version.
Type: String
Valid Values: `POPULATE_STARTED | POPULATE_SUCCESS | POPULATE_FAILED | RETENTION_PERIOD_EXPIRED`
Required: Yes

 ** tableId **   <a name="API-Type-IntermediateTableVersionSummary-tableId"></a>
The unique identifier of the intermediate table that this version belongs to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** versionId **   <a name="API-Type-IntermediateTableVersionSummary-versionId"></a>
The unique identifier of the version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** expirationTime **   <a name="API-Type-IntermediateTableVersionSummary-expirationTime"></a>
The time when this version expires based on the retention period.
Type: Timestamp
Required: No

 ** kmsKeyArn **   <a name="API-Type-IntermediateTableVersionSummary-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt this version's data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_IntermediateTableVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
