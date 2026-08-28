---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingSelectionForGet.html
---

# RestoreTestingSelectionForGet
<a name="API_RestoreTestingSelectionForGet"></a>

This contains metadata about a restore testing selection.

## Contents
<a name="API_RestoreTestingSelectionForGet_Contents"></a>

 ** CreationTime **   <a name="Backup-Type-RestoreTestingSelectionForGet-CreationTime"></a>
The date and time that a restore testing selection was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 201812:11:30.087 AM.
Type: Timestamp
Required: Yes

 ** IamRoleArn **   <a name="Backup-Type-RestoreTestingSelectionForGet-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example:`arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: Yes

 ** ProtectedResourceType **   <a name="Backup-Type-RestoreTestingSelectionForGet-ProtectedResourceType"></a>
The type of AWS resource included in a resource testing selection; for example, an Amazon EBS volume or an Amazon RDS database.
Type: String
Required: Yes

 ** RestoreTestingPlanName **   <a name="Backup-Type-RestoreTestingSelectionForGet-RestoreTestingPlanName"></a>
The RestoreTestingPlanName is a unique string that is the name of the restore testing plan.
Type: String
Required: Yes

 ** RestoreTestingSelectionName **   <a name="Backup-Type-RestoreTestingSelectionForGet-RestoreTestingSelectionName"></a>
The unique name of the restore testing selection that belongs to the related restore testing plan.
The name consists of only alphanumeric characters and underscores. Maximum length is 50.
Type: String
Required: Yes

 ** CreatorRequestId **   <a name="Backup-Type-RestoreTestingSelectionForGet-CreatorRequestId"></a>
This identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a `CreatorRequestId` that matches an existing backup plan, that plan is returned. This parameter is optional.
If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: No

 ** ProtectedResourceArns **   <a name="Backup-Type-RestoreTestingSelectionForGet-ProtectedResourceArns"></a>
You can include specific ARNs, such as `ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]` or you can include a wildcard: `ProtectedResourceArns: ["*"]`, but not both.
Type: Array of strings
Required: No

 ** ProtectedResourceConditions **   <a name="Backup-Type-RestoreTestingSelectionForGet-ProtectedResourceConditions"></a>
In a resource testing selection, this parameter filters by specific conditions such as `StringEquals` or `StringNotEquals`.
Type: [ProtectedResourceConditions](API_ProtectedResourceConditions.md) object
Required: No

 ** RestoreMetadataOverrides **   <a name="Backup-Type-RestoreTestingSelectionForGet-RestoreMetadataOverrides"></a>
You can override certain restore metadata keys by including the parameter `RestoreMetadataOverrides` in the body of `RestoreTestingSelection`. Key values are not case sensitive.
See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html).
Type: String to string map
Required: No

 ** ValidationWindowHours **   <a name="Backup-Type-RestoreTestingSelectionForGet-ValidationWindowHours"></a>
This is amount of hours (1 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingSelectionForGet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForGet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForGet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForGet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
