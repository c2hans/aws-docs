---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html
---

# DescribeDeliveries
<a name="API_DescribeDeliveries"></a>

Retrieves a list of the deliveries that have been created in the account.

A *delivery* is a connection between a [*delivery source*](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) and a [*delivery destination*](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html).

A delivery source represents an AWS resource that sends logs to an logs delivery destination. The destination can be CloudWatch Logs, Amazon S3, Firehose or X-Ray. Only some AWS services support being configured as a delivery source. These services are listed in [Enable logging from AWS services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

## Request Syntax
<a name="API_DescribeDeliveries_RequestSyntax"></a>

```
{
   "limit": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDeliveries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [limit](#API_DescribeDeliveries_RequestSyntax) **   <a name="CWL-DescribeDeliveries-request-limit"></a>
Optionally specify the maximum number of deliveries to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_DescribeDeliveries_RequestSyntax) **   <a name="CWL-DescribeDeliveries-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeDeliveries_ResponseSyntax"></a>

```
{
   "deliveries": [
      {
         "arn": "string",
         "deliveryDestinationArn": "string",
         "deliveryDestinationType": "string",
         "deliverySourceName": "string",
         "fieldDelimiter": "string",
         "id": "string",
         "recordFields": [ "string" ],
         "s3DeliveryConfiguration": {
            "enableHiveCompatiblePath": boolean,
            "suffixPath": "string"
         },
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDeliveries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliveries](#API_DescribeDeliveries_ResponseSyntax) **   <a name="CWL-DescribeDeliveries-response-deliveries"></a>
An array of structures. Each structure contains information about one delivery in the account.
Type: Array of [Delivery](API_Delivery.md) objects

 ** [nextToken](#API_DescribeDeliveries_ResponseSyntax) **   <a name="CWL-DescribeDeliveries-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeDeliveries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDeliveries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeDeliveries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeDeliveries)
