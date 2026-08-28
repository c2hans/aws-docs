---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingSelectionForUpdate.html
---

# RestoreTestingSelectionForUpdate
<a name="API_RestoreTestingSelectionForUpdate"></a>

This contains metadata about a restore testing selection.

## Contents
<a name="API_RestoreTestingSelectionForUpdate_Contents"></a>

 ** IamRoleArn **   <a name="Backup-Type-RestoreTestingSelectionForUpdate-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example: `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: No

 ** ProtectedResourceArns **   <a name="Backup-Type-RestoreTestingSelectionForUpdate-ProtectedResourceArns"></a>
You can include a list of specific ARNs, such as `ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]` or you can include a wildcard: `ProtectedResourceArns: ["*"]`, but not both.
Type: Array of strings
Required: No

 ** ProtectedResourceConditions **   <a name="Backup-Type-RestoreTestingSelectionForUpdate-ProtectedResourceConditions"></a>
The conditions that you define for resources in your restore testing plan using tags.
Type: [ProtectedResourceConditions](API_ProtectedResourceConditions.md) object
Required: No

 ** RestoreMetadataOverrides **   <a name="Backup-Type-RestoreTestingSelectionForUpdate-RestoreMetadataOverrides"></a>
You can override certain restore metadata keys by including the parameter `RestoreMetadataOverrides` in the body of `RestoreTestingSelection`. Key values are not case sensitive.
See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html).
Type: String to string map
Required: No

 ** ValidationWindowHours **   <a name="Backup-Type-RestoreTestingSelectionForUpdate-ValidationWindowHours"></a>
This value represents the time, in hours, data is retained after a restore test so that optional validation can be completed.
Accepted value is an integer between 0 and 168 (the hourly equivalent of seven days).
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingSelectionForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
