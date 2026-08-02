---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RetryCriteria.html
---

# RetryCriteria
<a name="API_RetryCriteria"></a>

The criteria that determines how many retries are allowed for each failure type for a job.

## Contents
<a name="API_RetryCriteria_Contents"></a>

 ** failureType **   <a name="iot-Type-RetryCriteria-failureType"></a>
The type of job execution failures that can initiate a job retry.
Type: String
Valid Values: `FAILED | TIMED_OUT | ALL`
Required: Yes

 ** numberOfRetries **   <a name="iot-Type-RetryCriteria-numberOfRetries"></a>
The number of retries allowed for a failure type for the job.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: Yes

## See Also
<a name="API_RetryCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RetryCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RetryCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RetryCriteria)
