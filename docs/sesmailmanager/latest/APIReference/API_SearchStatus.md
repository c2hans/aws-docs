---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SearchStatus.html
---

# SearchStatus
<a name="API_SearchStatus"></a>

The current status of an archive search job.

## Contents
<a name="API_SearchStatus_Contents"></a>

 ** CompletionTimestamp **   <a name="sesmailmanager-Type-SearchStatus-CompletionTimestamp"></a>
The timestamp of when the search completed (if finished).
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="sesmailmanager-Type-SearchStatus-ErrorMessage"></a>
An error message if the search failed.
Type: String
Required: No

 ** State **   <a name="sesmailmanager-Type-SearchStatus-State"></a>
The current state of the search job.
Type: String
Valid Values: `QUEUED | RUNNING | COMPLETED | FAILED | CANCELLED`
Required: No

 ** SubmissionTimestamp **   <a name="sesmailmanager-Type-SearchStatus-SubmissionTimestamp"></a>
The timestamp of when the search was submitted.
Type: Timestamp
Required: No

## See Also
<a name="API_SearchStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/SearchStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/SearchStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/SearchStatus)
