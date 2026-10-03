---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_JobResult.html
---

# JobResult
<a name="API_JobResult"></a>

Pairs an asynchronous job with the resource identifier from your request that the job processes.

## Contents
<a name="API_JobResult_Contents"></a>

 ** jobId **   <a name="endusermessaging-Type-JobResult-jobId"></a>
The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** resourceIdentifier **   <a name="endusermessaging-Type-JobResult-resourceIdentifier"></a>
The identifier from your request that this job is processing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`
Required: Yes

## See Also
<a name="API_JobResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/JobResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/JobResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/JobResult)
