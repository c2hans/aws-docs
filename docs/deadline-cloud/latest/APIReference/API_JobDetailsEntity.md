---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobDetailsEntity.html
---

# JobDetailsEntity
<a name="API_JobDetailsEntity"></a>

The job details for a specific job.

## Contents
<a name="API_JobDetailsEntity_Contents"></a>

 ** jobId **   <a name="deadlinecloud-Type-JobDetailsEntity-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** logGroupName **   <a name="deadlinecloud-Type-JobDetailsEntity-logGroupName"></a>
The log group name.
Type: String
Required: Yes

 ** schemaVersion **   <a name="deadlinecloud-Type-JobDetailsEntity-schemaVersion"></a>
The schema version.
Type: String
Required: Yes

 ** jobAttachmentSettings **   <a name="deadlinecloud-Type-JobDetailsEntity-jobAttachmentSettings"></a>
The job attachment settings.
Type: [JobDetailsJobAttachmentSettings](API_JobDetailsJobAttachmentSettings.md) object
Required: No

 ** jobRunAsUser **   <a name="deadlinecloud-Type-JobDetailsEntity-jobRunAsUser"></a>
The user name and group that the job uses when run.
Type: [JobRunAsUser](API_JobRunAsUser.md) object
Required: No

 ** parameters **   <a name="deadlinecloud-Type-JobDetailsEntity-parameters"></a>
The parameters.
Type: String to [JobParameter](API_JobParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** pathMappingRules **   <a name="deadlinecloud-Type-JobDetailsEntity-pathMappingRules"></a>
The path mapping rules.
Type: Array of [PathMappingRule](API_PathMappingRule.md) objects
Required: No

 ** queueRoleArn **   <a name="deadlinecloud-Type-JobDetailsEntity-queueRoleArn"></a>
The queue role ARN.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`
Required: No

## See Also
<a name="API_JobDetailsEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsEntity)
