---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.html
---

# DescribeDeliveryDestinations
<a name="API_DescribeDeliveryDestinations"></a>

Retrieves a list of the delivery destinations that have been created in the account.

## Request Syntax
<a name="API_DescribeDeliveryDestinations_RequestSyntax"></a>

```
{
   "limit": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDeliveryDestinations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [limit](#API_DescribeDeliveryDestinations_RequestSyntax) **   <a name="CWL-DescribeDeliveryDestinations-request-limit"></a>
Optionally specify the maximum number of delivery destinations to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_DescribeDeliveryDestinations_RequestSyntax) **   <a name="CWL-DescribeDeliveryDestinations-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeDeliveryDestinations_ResponseSyntax"></a>

```
{
   "deliveryDestinations": [
      {
         "arn": "string",
         "deliveryDestinationConfiguration": {
            "destinationResourceArn": "string"
         },
         "deliveryDestinationType": "string",
         "name": "string",
         "outputFormat": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDeliveryDestinations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deliveryDestinations](#API_DescribeDeliveryDestinations_ResponseSyntax) **   <a name="CWL-DescribeDeliveryDestinations-response-deliveryDestinations"></a>
An array of structures. Each structure contains information about one delivery destination in the account.
Type: Array of [DeliveryDestination](API_DeliveryDestination.md) objects

 ** [nextToken](#API_DescribeDeliveryDestinations_ResponseSyntax) **   <a name="CWL-DescribeDeliveryDestinations-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeDeliveryDestinations_Errors"></a>

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
<a name="API_DescribeDeliveryDestinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeDeliveryDestinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeDeliveryDestinations)
