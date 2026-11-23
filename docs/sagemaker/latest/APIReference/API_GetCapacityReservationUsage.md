---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetCapacityReservationUsage.html
---

# GetCapacityReservationUsage

Returns the number of instances in use from a SageMaker Capacity Reservation, for each account that uses them.

SageMaker AI refreshes the usage counts periodically. The `LastRefreshTime` value shows when the counts were last refreshed.

## Request Syntax
<a name="API_GetCapacityReservationUsage_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SMCapacityReservationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCapacityReservationUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetCapacityReservationUsage_RequestSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-request-MaxResults"></a>
The maximum number of results to return in the response. If more results are available, the response includes a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetCapacityReservationUsage_RequestSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-request-NextToken"></a>
If the previous response was truncated, the response includes a `NextToken` value. To retrieve the next set of results, use that token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SMCapacityReservationArn](#API_GetCapacityReservationUsage_RequestSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-request-SMCapacityReservationArn"></a>
The Amazon Resource Name (ARN) of the SageMaker Capacity Reservation. The ARN has the format `arn:aws:sagemaker:region:account-id:sm-capacity-reservation/smcr-id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:sm-capacity-reservation/smcr-[0-9a-z]{12}`
Required: Yes

## Response Syntax
<a name="API_GetCapacityReservationUsage_ResponseSyntax"></a>

```
{
   "AvailableInstanceCount": number,
   "InstanceUsageSet": [
      {
         "AccountId": "string",
         "InUseInstanceCount": number,
         "ResourcesUsage": [
            {
               "InUseInstanceCount": number,
               "ResourceType": "string"
            }
         ]
      }
   ],
   "LastRefreshTime": number,
   "NextToken": "string",
   "SMCapacityReservationId": "string",
   "TotalInstanceCount": number
}
```

## Response Elements
<a name="API_GetCapacityReservationUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailableInstanceCount](#API_GetCapacityReservationUsage_ResponseSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-response-AvailableInstanceCount"></a>
The number of instances in the SageMaker Capacity Reservation that are not in use.
Type: Integer
Valid Range: Minimum value of 0.

 ** [InstanceUsageSet](#API_GetCapacityReservationUsage_ResponseSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-response-InstanceUsageSet"></a>
The instance usage for each account that uses instances from the SageMaker Capacity Reservation, sorted by account ID. Each account appears at most once across all pages. The list is empty when no instances are in use.
Type: Array of [CapacityReservationInstanceUsage](API_CapacityReservationInstanceUsage.md) objects

 ** [LastRefreshTime](#API_GetCapacityReservationUsage_ResponseSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-response-LastRefreshTime"></a>
The time when SageMaker AI last refreshed the usage counts in this response.
Type: Timestamp

 ** [NextToken](#API_GetCapacityReservationUsage_ResponseSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-response-NextToken"></a>
If the response is truncated, SageMaker AI returns this token. To retrieve the next set of results, use this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [SMCapacityReservationId](#API_GetCapacityReservationUsage_ResponseSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-response-SMCapacityReservationId"></a>
The ID of the SageMaker Capacity Reservation. The ID is the last part of the ARN and starts with `smcr-`.
Type: String
Pattern: `smcr-[0-9a-z]{12}`

 ** [TotalInstanceCount](#API_GetCapacityReservationUsage_ResponseSyntax) **   <a name="sagemaker-GetCapacityReservationUsage-response-TotalInstanceCount"></a>
The number of instances in the SageMaker Capacity Reservation.
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_GetCapacityReservationUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_GetCapacityReservationUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetCapacityReservationUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetCapacityReservationUsage)
