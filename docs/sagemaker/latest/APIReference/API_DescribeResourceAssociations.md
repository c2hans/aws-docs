---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeResourceAssociations.html
---

# DescribeResourceAssociations

Returns the resources in your account that are associated with a SageMaker Capacity Reservation and the status of each association. Resources include SageMaker AI HyperPod clusters and SageMaker AI endpoints.

## Request Syntax
<a name="API_DescribeResourceAssociations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SMCapacityReservationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeResourceAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeResourceAssociations_RequestSyntax) **   <a name="sagemaker-DescribeResourceAssociations-request-MaxResults"></a>
The maximum number of results to return in the response. If more results are available, the response includes a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeResourceAssociations_RequestSyntax) **   <a name="sagemaker-DescribeResourceAssociations-request-NextToken"></a>
If the previous response was truncated, the response includes a `NextToken` value. To retrieve the next set of results, use that token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SMCapacityReservationArn](#API_DescribeResourceAssociations_RequestSyntax) **   <a name="sagemaker-DescribeResourceAssociations-request-SMCapacityReservationArn"></a>
The Amazon Resource Name (ARN) of the SageMaker Capacity Reservation. The ARN has the format `arn:aws:sagemaker:region:account-id:sm-capacity-reservation/smcr-id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:sm-capacity-reservation/smcr-[0-9a-z]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeResourceAssociations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceAssociations": [
      { ... }
   ],
   "SMCapacityReservationArn": "string",
   "SMCapacityReservationId": "string"
}
```

## Response Elements
<a name="API_DescribeResourceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeResourceAssociations_ResponseSyntax) **   <a name="sagemaker-DescribeResourceAssociations-response-NextToken"></a>
If the response is truncated, SageMaker AI returns this token. To retrieve the next set of results, use this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [ResourceAssociations](#API_DescribeResourceAssociations_ResponseSyntax) **   <a name="sagemaker-DescribeResourceAssociations-response-ResourceAssociations"></a>
The associations between resources in your account and the SageMaker Capacity Reservation. The list is empty when your account has no associations with the reservation.
Type: Array of [CapacityReservationResourceAssociation](API_CapacityReservationResourceAssociation.md) objects

 ** [SMCapacityReservationArn](#API_DescribeResourceAssociations_ResponseSyntax) **   <a name="sagemaker-DescribeResourceAssociations-response-SMCapacityReservationArn"></a>
The Amazon Resource Name (ARN) of the SageMaker Capacity Reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:sm-capacity-reservation/smcr-[0-9a-z]{12}`

 ** [SMCapacityReservationId](#API_DescribeResourceAssociations_ResponseSyntax) **   <a name="sagemaker-DescribeResourceAssociations-response-SMCapacityReservationId"></a>
The ID of the SageMaker Capacity Reservation. The ID is the last part of the ARN and starts with `smcr-`.
Type: String
Pattern: `smcr-[0-9a-z]{12}`

## Errors
<a name="API_DescribeResourceAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeResourceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeResourceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeResourceAssociations)
