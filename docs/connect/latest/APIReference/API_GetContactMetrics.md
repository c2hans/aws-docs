---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetContactMetrics.html
---

# GetContactMetrics
<a name="API_GetContactMetrics"></a>

Retrieves contact metric data for a specified contact.

 **Use cases**

Following are common use cases for position in queue and estimated wait time:
+ Customer-Facing Wait Time Announcements - Display or announce the estimated wait time and position in queue to customers before or during their queue experience.
+ Callback Offerings - Offer customers a callback option when the estimated wait time or position in queue exceeds a defined threshold.
+ Queue Routing Decisions - Route incoming contacts to less congested queues by comparing estimated wait time and position in queue across multiple queues.
+ Self-Service Deflection - Redirect customers to self-service options like chatbots or FAQs when estimated wait time is high or position in queue is unfavorable.

 **Important things to know**
+ Metrics are only available while the contact is actively in queue.
+ For more information, see the [Position in queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) metric in the *Connect Customer Administrator Guide*.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_GetContactMetrics_RequestSyntax"></a>

```
POST /metrics/contact HTTP/1.1
Content-type: application/json

{
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}",
   "Metrics": [
      {
         "Name": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetContactMetrics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetContactMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_GetContactMetrics_RequestSyntax) **   <a name="connect-GetContactMetrics-request-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [InstanceId](#API_GetContactMetrics_RequestSyntax) **   <a name="connect-GetContactMetrics-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [Metrics](#API_GetContactMetrics_RequestSyntax) **   <a name="connect-GetContactMetrics-request-Metrics"></a>
A list of contact level metrics to retrieve.Supported metrics include POSITION\_IN\_QUEUE (the contact's current position in the queue) and ESTIMATED\_WAIT\_TIME (the predicted time in seconds until the contact is connected to an agent)
Type: Array of [ContactMetricInfo](API_ContactMetricInfo.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_GetContactMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "MetricResults": [
      {
         "Name": "string",
         "Value": { ... }
      }
   ]
}
```

## Response Elements
<a name="API_GetContactMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetContactMetrics_ResponseSyntax) **   <a name="connect-GetContactMetrics-response-Arn"></a>
The ARN of the contact for which metrics were retrieved.
Type: String

 ** [Id](#API_GetContactMetrics_ResponseSyntax) **   <a name="connect-GetContactMetrics-response-Id"></a>
The unique identifier of the contact for which metrics were retrieved. This matches the ContactId provided in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [MetricResults](#API_GetContactMetrics_ResponseSyntax) **   <a name="connect-GetContactMetrics-response-MetricResults"></a>
A list of metric results containing the calculated values for each requested metric. Each result includes the metric name and its corresponding value. For example, POSITION\_IN\_QUEUE returns a numeric value representing the contact's position in queue, and ESTIMATED\_WAIT\_TIME returns the predicted wait time in seconds.
Type: Array of [ContactMetricResult](API_ContactMetricResult.md) objects

## Errors
<a name="API_GetContactMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_GetContactMetrics_Examples"></a>

### Example request to retrieve position in queue and estimated wait time
<a name="API_GetContactMetrics_Example_1"></a>

Following is an example of retrieving the position in queue and estimated wait time for a contact.

```
{
     "InstanceId":"12345678-1234-5678-aabb-123456abcdef",
     "ContactId":"12345678-1234-5678-aabb-123456abcdef",
     "Metrics":[ { "Name": "POSITION_IN_QUEUE"}, { "Name": "ESTIMATED_WAIT_TIME"} ]
     }
```

### Example response with the position in queue and estimated wait time
<a name="API_GetContactMetrics_Example_2"></a>

Following is an example response. In this case, the contact is number 3 in the queue with an estimated wait time of 120 seconds.

```
{
     "Id":"12345678-1234-5678-aabb-123456abcdef",
     "Arn":"arn:aws:connect:us-east-1:123456789012:instance/12345678-1234-5678-aabb-123456abcdef/contact/12345678-1234-5678-aabb-123456abcdef",
     "MetricResults":[ { "Name": "POSITION_IN_QUEUE","Value":{"Number":3.00}}, { "Name": "ESTIMATED_WAIT_TIME","Value":{"Number":120.00}}]
     }
```

## See Also
<a name="API_GetContactMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetContactMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetContactMetrics)
