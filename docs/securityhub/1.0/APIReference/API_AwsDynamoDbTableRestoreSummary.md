---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableRestoreSummary.html
---

# AwsDynamoDbTableRestoreSummary
<a name="API_AwsDynamoDbTableRestoreSummary"></a>

Information about the restore for the table.

## Contents
<a name="API_AwsDynamoDbTableRestoreSummary_Contents"></a>

 ** RestoreDateTime **   <a name="securityhub-Type-AwsDynamoDbTableRestoreSummary-RestoreDateTime"></a>
Indicates the point in time that the table was restored to.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** RestoreInProgress **   <a name="securityhub-Type-AwsDynamoDbTableRestoreSummary-RestoreInProgress"></a>
Whether a restore is currently in progress.
Type: Boolean
Required: No

 ** SourceBackupArn **   <a name="securityhub-Type-AwsDynamoDbTableRestoreSummary-SourceBackupArn"></a>
The ARN of the source backup from which the table was restored.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceTableArn **   <a name="securityhub-Type-AwsDynamoDbTableRestoreSummary-SourceTableArn"></a>
The ARN of the source table for the backup.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableRestoreSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableRestoreSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableRestoreSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableRestoreSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
