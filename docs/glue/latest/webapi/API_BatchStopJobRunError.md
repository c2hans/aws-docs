---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchStopJobRunError.html
---

# BatchStopJobRunError
<a name="API_BatchStopJobRunError"></a>

Records an error that occurred when attempting to stop a specified job run.

## Contents
<a name="API_BatchStopJobRunError_Contents"></a>

 ** ErrorDetail **   <a name="Glue-Type-BatchStopJobRunError-ErrorDetail"></a>
Specifies details about the error that was encountered.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** JobName **   <a name="Glue-Type-BatchStopJobRunError-JobName"></a>
The name of the job definition that is used in the job run in question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobRunId **   <a name="Glue-Type-BatchStopJobRunError-JobRunId"></a>
The `JobRunId` of the job run in question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_BatchStopJobRunError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchStopJobRunError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchStopJobRunError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchStopJobRunError)
