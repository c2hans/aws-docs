---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobRunAsUser.html
---

# JobRunAsUser
<a name="API_JobRunAsUser"></a>

Identifies the user for a job.

## Contents
<a name="API_JobRunAsUser_Contents"></a>

 ** runAs **   <a name="deadlinecloud-Type-JobRunAsUser-runAs"></a>
Specifies whether the job should run using the queue's system user or if the job should run using the worker agent system user.
Type: String
Valid Values: `QUEUE_CONFIGURED_USER | WORKER_AGENT_USER`
Required: Yes

 ** posix **   <a name="deadlinecloud-Type-JobRunAsUser-posix"></a>
The user and group that the jobs in the queue run as.
Type: [PosixUser](API_PosixUser.md) object
Required: No

 ** windows **   <a name="deadlinecloud-Type-JobRunAsUser-windows"></a>
Identifies a Microsoft Windows user.
Type: [WindowsUser](API_WindowsUser.md) object
Required: No

## See Also
<a name="API_JobRunAsUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobRunAsUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobRunAsUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobRunAsUser)
