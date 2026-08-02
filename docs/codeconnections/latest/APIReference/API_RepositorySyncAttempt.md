---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositorySyncAttempt.html
---

# RepositorySyncAttempt
<a name="API_RepositorySyncAttempt"></a>

Information about a repository sync attempt for a repository with a sync configuration.

## Contents
<a name="API_RepositorySyncAttempt_Contents"></a>

 ** Events **   <a name="codeconnections-Type-RepositorySyncAttempt-Events"></a>
The events associated with a specific sync attempt.
Type: Array of [RepositorySyncEvent](API_RepositorySyncEvent.md) objects
Required: Yes

 ** StartedAt **   <a name="codeconnections-Type-RepositorySyncAttempt-StartedAt"></a>
The start time of a specific sync attempt.
Type: Timestamp
Required: Yes

 ** Status **   <a name="codeconnections-Type-RepositorySyncAttempt-Status"></a>
The status of a specific sync attempt. The following are valid statuses:
+ INITIATED - A repository sync attempt has been created and will begin soon.
+ IN\_PROGRESS - A repository sync attempt has started and work is being done to reconcile the branch.
+ SUCCEEDED - The repository sync attempt has completed successfully.
+ FAILED - The repository sync attempt has failed.
+ QUEUED - The repository sync attempt didn't execute and was queued.
Type: String
Valid Values: `FAILED | INITIATED | IN_PROGRESS | SUCCEEDED | QUEUED`
Required: Yes

## See Also
<a name="API_RepositorySyncAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/RepositorySyncAttempt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/RepositorySyncAttempt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/RepositorySyncAttempt)
