---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchStopJobRunSuccessfulSubmission.html
---

# BatchStopJobRunSuccessfulSubmission
<a name="API_BatchStopJobRunSuccessfulSubmission"></a>

Records a successful request to stop a specified `JobRun`.

## Contents
<a name="API_BatchStopJobRunSuccessfulSubmission_Contents"></a>

 ** JobName **   <a name="Glue-Type-BatchStopJobRunSuccessfulSubmission-JobName"></a>
The name of the job definition used in the job run that was stopped.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobRunId **   <a name="Glue-Type-BatchStopJobRunSuccessfulSubmission-JobRunId"></a>
The `JobRunId` of the job run that was stopped.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_BatchStopJobRunSuccessfulSubmission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchStopJobRunSuccessfulSubmission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchStopJobRunSuccessfulSubmission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchStopJobRunSuccessfulSubmission)
