---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_StepFailedDetails.html
---

# StepFailedDetails
<a name="API_StepFailedDetails"></a>

Details about a step that failed.

## Contents
<a name="API_StepFailedDetails_Contents"></a>

 ** Error **   <a name="lambda-Type-StepFailedDetails-Error"></a>
Details about the step failure.
Type: [EventError](API_EventError.md) object
Required: Yes

 ** RetryDetails **   <a name="lambda-Type-StepFailedDetails-RetryDetails"></a>
Information about retry attempts for this step operation.
Type: [RetryDetails](API_RetryDetails.md) object
Required: Yes

## See Also
<a name="API_StepFailedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/StepFailedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/StepFailedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/StepFailedDetails)
