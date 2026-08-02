---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_StepSucceededDetails.html
---

# StepSucceededDetails
<a name="API_StepSucceededDetails"></a>

Details about a step that succeeded.

## Contents
<a name="API_StepSucceededDetails_Contents"></a>

 ** Result **   <a name="lambda-Type-StepSucceededDetails-Result"></a>
The response payload from the successful operation.
Type: [EventResult](API_EventResult.md) object
Required: Yes

 ** RetryDetails **   <a name="lambda-Type-StepSucceededDetails-RetryDetails"></a>
Information about retry attempts for this step operation.
Type: [RetryDetails](API_RetryDetails.md) object
Required: Yes

## See Also
<a name="API_StepSucceededDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/StepSucceededDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/StepSucceededDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/StepSucceededDetails)
