---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCapacityReservations.html
---

# ListCapacityReservations

Lists the SageMaker Capacity Reservations in your account.

An empty list is a valid response.

## Request Syntax
<a name="API_ListCapacityReservations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCapacityReservations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListCapacityReservations_RequestSyntax) **   <a name="sagemaker-ListCapacityReservations-request-Filters"></a>
A filter that returns only the reservations that match it. You can specify one filter. If you don't specify a filter, the response includes all reservations in your account.
Type: Array of [CapacityReservationFilter](API_CapacityReservationFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [MaxResults](#API_ListCapacityReservations_RequestSyntax) **   <a name="sagemaker-ListCapacityReservations-request-MaxResults"></a>
The maximum number of results to return in the response. If more results are available, the response includes a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCapacityReservations_RequestSyntax) **   <a name="sagemaker-ListCapacityReservations-request-NextToken"></a>
If the previous response was truncated, the response includes a `NextToken` value. To retrieve the next set of results, use that token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListCapacityReservations_ResponseSyntax"></a>

```
{
   "CapacityReservationSummaries": [
      {
         "AvailabilityZone": "string",
         "AvailabilityZoneId": "string",
         "CreationTime": number,
         "EndTime": number,
         "InstanceType": "string",
         "Owner": "string",
         "SMCapacityReservationArn": "string",
         "SMCapacityReservationId": "string",
         "StartTime": number,
         "Status": "string",
         "TotalInstanceCount": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCapacityReservations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityReservationSummaries](#API_ListCapacityReservations_ResponseSyntax) **   <a name="sagemaker-ListCapacityReservations-response-CapacityReservationSummaries"></a>
Summaries of the SageMaker Capacity Reservations in your account.
Type: Array of [CapacityReservationSummary](API_CapacityReservationSummary.md) objects

 ** [NextToken](#API_ListCapacityReservations_ResponseSyntax) **   <a name="sagemaker-ListCapacityReservations-response-NextToken"></a>
If the response is truncated, SageMaker AI returns this token. To retrieve the next set of results, use this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListCapacityReservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCapacityReservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListCapacityReservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListCapacityReservations)
