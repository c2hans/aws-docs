---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_TextTranslationJobFilter.html
---

# TextTranslationJobFilter
<a name="API_TextTranslationJobFilter"></a>

Provides information for filtering a list of translation jobs. For more information, see [ListTextTranslationJobs](API_ListTextTranslationJobs.md).

## Contents
<a name="API_TextTranslationJobFilter_Contents"></a>

 ** JobName **   <a name="translate-Type-TextTranslationJobFilter-JobName"></a>
Filters the list of jobs by name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobStatus **   <a name="translate-Type-TextTranslationJobFilter-JobStatus"></a>
Filters the list of jobs based by job status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERROR | FAILED | STOP_REQUESTED | STOPPED`
Required: No

 ** SubmittedAfterTime **   <a name="translate-Type-TextTranslationJobFilter-SubmittedAfterTime"></a>
Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
Type: Timestamp
Required: No

 ** SubmittedBeforeTime **   <a name="translate-Type-TextTranslationJobFilter-SubmittedBeforeTime"></a>
Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
Type: Timestamp
Required: No

## See Also
<a name="API_TextTranslationJobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/TextTranslationJobFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/TextTranslationJobFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/TextTranslationJobFilter)
