---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCapacityReservation.html
---

# DescribeCapacityReservation

Returns details about a SageMaker Capacity Reservation, such as its instance type, instance count, Availability Zone, and start and end times.

## Request Syntax
<a name="API_DescribeCapacityReservation_RequestSyntax"></a>

```
{
   "SMCapacityReservationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCapacityReservation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SMCapacityReservationArn](#API_DescribeCapacityReservation_RequestSyntax) **   <a name="sagemaker-DescribeCapacityReservation-request-SMCapacityReservationArn"></a>
The Amazon Resource Name (ARN) of the SageMaker Capacity Reservation. The ARN has the format `arn:aws:sagemaker:region:account-id:sm-capacity-reservation/smcr-id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:sm-capacity-reservation/smcr-[0-9a-z]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeCapacityReservation_ResponseSyntax"></a>

```
{
   "CapacityReservation": {
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
}
```

## Response Elements
<a name="API_DescribeCapacityReservation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityReservation](#API_DescribeCapacityReservation_ResponseSyntax) **   <a name="sagemaker-DescribeCapacityReservation-response-CapacityReservation"></a>
Details about the SageMaker Capacity Reservation.
Type: [CapacityReservationDetail](API_CapacityReservationDetail.md) object

## Errors
<a name="API_DescribeCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeCapacityReservation)
