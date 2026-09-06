---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationMetrics.html
---

# ApplicationMetrics
<a name="API_ApplicationMetrics"></a>

Application request metrics for an AWS Elastic Beanstalk environment.

## Contents
<a name="API_ApplicationMetrics_Contents"></a>

 ** Duration **
The amount of time that the metrics cover (usually 10 seconds). For example, you might have 5 requests (`request_count`) within the most recent time slice of 10 seconds (`duration`).
Type: Integer
Required: No

 ** Latency **
Represents the average latency for the slowest X percent of requests over the last 10 seconds. Latencies are in seconds with one millisecond resolution.
Type: [Latency](API_Latency.md) object
Required: No

 ** RequestCount **
Average number of requests handled by the web server per second over the last 10 seconds.
Type: Integer
Required: No

 ** StatusCodes **
Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response.
Type: [StatusCodes](API_StatusCodes.md) object
Required: No

## See Also
<a name="API_ApplicationMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ApplicationMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ApplicationMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ApplicationMetrics)
