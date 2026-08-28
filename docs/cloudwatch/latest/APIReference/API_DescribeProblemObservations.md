---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblemObservations.html
---

# DescribeProblemObservations
<a name="API_DescribeProblemObservations"></a>

Describes the anomalies or errors associated with the problem.

## Request Syntax
<a name="API_DescribeProblemObservations_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ProblemId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProblemObservations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_DescribeProblemObservations_RequestSyntax) **   <a name="appinsights-DescribeProblemObservations-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ProblemId](#API_DescribeProblemObservations_RequestSyntax) **   <a name="appinsights-DescribeProblemObservations-request-ProblemId"></a>
The ID of the problem.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `p-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeProblemObservations_ResponseSyntax"></a>

```
{
   "RelatedObservations": {
      "ObservationList": [
         {
            "CloudWatchEventDetailType": "string",
            "CloudWatchEventId": "string",
            "CloudWatchEventSource": "string",
            "CodeDeployApplication": "string",
            "CodeDeployDeploymentGroup": "string",
            "CodeDeployDeploymentId": "string",
            "CodeDeployInstanceGroupId": "string",
            "CodeDeployState": "string",
            "EbsCause": "string",
            "EbsEvent": "string",
            "EbsRequestId": "string",
            "EbsResult": "string",
            "Ec2State": "string",
            "EndTime": number,
            "HealthEventArn": "string",
            "HealthEventDescription": "string",
            "HealthEventTypeCategory": "string",
            "HealthEventTypeCode": "string",
            "HealthService": "string",
            "Id": "string",
            "LineTime": number,
            "LogFilter": "string",
            "LogGroup": "string",
            "LogText": "string",
            "MetricName": "string",
            "MetricNamespace": "string",
            "RdsEventCategories": "string",
            "RdsEventMessage": "string",
            "S3EventName": "string",
            "SourceARN": "string",
            "SourceType": "string",
            "StartTime": number,
            "StatesArn": "string",
            "StatesExecutionArn": "string",
            "StatesInput": "string",
            "StatesStatus": "string",
            "Unit": "string",
            "Value": number,
            "XRayErrorPercent": number,
            "XRayFaultPercent": number,
            "XRayNodeName": "string",
            "XRayNodeType": "string",
            "XRayRequestAverageLatency": number,
            "XRayRequestCount": number,
            "XRayThrottlePercent": number
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeProblemObservations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RelatedObservations](#API_DescribeProblemObservations_ResponseSyntax) **   <a name="appinsights-DescribeProblemObservations-response-RelatedObservations"></a>
Observations related to the problem.
Type: [RelatedObservations](API_RelatedObservations.md) object

## Errors
<a name="API_DescribeProblemObservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProblemObservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/DescribeProblemObservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/DescribeProblemObservations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
