---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AbortCriteria.html
---

# AbortCriteria
<a name="API_AbortCriteria"></a>

The criteria that determine when and how a job abort takes place.

## Contents
<a name="API_AbortCriteria_Contents"></a>

 ** action **   <a name="iot-Type-AbortCriteria-action"></a>
The type of job action to take to initiate the job abort.
Type: String
Valid Values: `CANCEL`
Required: Yes

 ** failureType **   <a name="iot-Type-AbortCriteria-failureType"></a>
The type of job execution failures that can initiate a job abort.
Type: String
Valid Values: `FAILED | REJECTED | TIMED_OUT | ALL`
Required: Yes

 ** minNumberOfExecutedThings **   <a name="iot-Type-AbortCriteria-minNumberOfExecutedThings"></a>
The minimum number of things which must receive job execution notifications before the job can be aborted.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** thresholdPercentage **   <a name="iot-Type-AbortCriteria-thresholdPercentage"></a>
The minimum percentage of job execution failures that must occur to initiate the job abort.
 AWS IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
Type: Double
Valid Range: Maximum value of 100.
Required: Yes

## See Also
<a name="API_AbortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AbortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AbortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AbortCriteria)
