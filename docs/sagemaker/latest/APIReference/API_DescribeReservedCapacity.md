---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeReservedCapacity.html
---

# DescribeReservedCapacity
<a name="API_DescribeReservedCapacity"></a>

Retrieves details about a reserved capacity.

## Request Syntax
<a name="API_DescribeReservedCapacity_RequestSyntax"></a>

```
{
   "ReservedCapacityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReservedCapacity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReservedCapacityArn](#API_DescribeReservedCapacity_RequestSyntax) **   <a name="sagemaker-DescribeReservedCapacity-request-ReservedCapacityArn"></a>
ARN of the reserved capacity to describe.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:reserved-capacity/.*`
Required: Yes

## Response Syntax
<a name="API_DescribeReservedCapacity_ResponseSyntax"></a>

```
{
   "AvailabilityZone": "string",
   "AvailableInstanceCount": number,
   "DurationHours": number,
   "DurationMinutes": number,
   "InstanceType": "string",
   "InUseInstanceCount": number,
   "ReservedCapacityArn": "string",
   "ReservedCapacityType": "string",
   "Status": "string",
   "TotalInstanceCount": number,
   "UltraServerSummary": {
      "AvailableSpareInstanceCount": number,
      "InstanceType": "string",
      "UltraServerCount": number,
      "UltraServerType": "string",
      "UnhealthyInstanceCount": number
   }
}
```

## Response Elements
<a name="API_DescribeReservedCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailabilityZone](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-AvailabilityZone"></a>
The Availability Zone where the reserved capacity is provisioned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-z]+\-[0-9a-z\-]+`

 ** [AvailableInstanceCount](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-AvailableInstanceCount"></a>
The number of instances currently available for use in this reserved capacity.
Type: Integer
Valid Range: Minimum value of 0.

 ** [DurationHours](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-DurationHours"></a>
The total duration of the reserved capacity in hours.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 87600.

 ** [DurationMinutes](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-DurationMinutes"></a>
The number of minutes for the duration of the reserved capacity. For example, if a reserved capacity starts at 08:55 and ends at 11:30, the minutes field would be 35.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.

 ** [InstanceType](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-InstanceType"></a>
The Amazon EC2 instance type used in the reserved capacity.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.trn1.32xlarge | ml.trn2.48xlarge | ml.p6-b200.48xlarge | ml.p4de.24xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge`

 ** [InUseInstanceCount](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-InUseInstanceCount"></a>
The number of instances currently in use from this reserved capacity.
Type: Integer
Valid Range: Minimum value of 0.

 ** [ReservedCapacityArn](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-ReservedCapacityArn"></a>
ARN of the reserved capacity.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:reserved-capacity/.*`

 ** [ReservedCapacityType](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-ReservedCapacityType"></a>
The type of reserved capacity.
Type: String
Valid Values: `UltraServer | Instance`

 ** [Status](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-Status"></a>
The current status of the reserved capacity.
Type: String
Valid Values: `Pending | Active | Scheduled | Expired | Failed`

 ** [TotalInstanceCount](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-TotalInstanceCount"></a>
The total number of instances allocated to this reserved capacity.
Type: Integer
Valid Range: Minimum value of 0.

 ** [UltraServerSummary](#API_DescribeReservedCapacity_ResponseSyntax) **   <a name="sagemaker-DescribeReservedCapacity-response-UltraServerSummary"></a>
A summary of the UltraServer associated with this reserved capacity.
Type: [UltraServerSummary](API_UltraServerSummary.md) object

## Errors
<a name="API_DescribeReservedCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReservedCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeReservedCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeReservedCapacity)
