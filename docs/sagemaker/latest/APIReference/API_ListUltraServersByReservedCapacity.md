---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListUltraServersByReservedCapacity.html
---

# ListUltraServersByReservedCapacity
<a name="API_ListUltraServersByReservedCapacity"></a>

Lists all UltraServers that are part of a specified reserved capacity.

## Request Syntax
<a name="API_ListUltraServersByReservedCapacity_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ReservedCapacityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUltraServersByReservedCapacity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListUltraServersByReservedCapacity_RequestSyntax) **   <a name="sagemaker-ListUltraServersByReservedCapacity-request-MaxResults"></a>
The maximum number of UltraServers to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListUltraServersByReservedCapacity_RequestSyntax) **   <a name="sagemaker-ListUltraServersByReservedCapacity-request-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [ReservedCapacityArn](#API_ListUltraServersByReservedCapacity_RequestSyntax) **   <a name="sagemaker-ListUltraServersByReservedCapacity-request-ReservedCapacityArn"></a>
The ARN of the reserved capacity to list UltraServers for.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:reserved-capacity/.*`
Required: Yes

## Response Syntax
<a name="API_ListUltraServersByReservedCapacity_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UltraServers": [
      {
         "AvailabilityZone": "string",
         "AvailableInstanceCount": number,
         "AvailableSpareInstanceCount": number,
         "ConfiguredSpareInstanceCount": number,
         "HealthStatus": "string",
         "InstanceType": "string",
         "InUseInstanceCount": number,
         "TotalInstanceCount": number,
         "UltraServerId": "string",
         "UltraServerType": "string",
         "UnhealthyInstanceCount": number
      }
   ]
}
```

## Response Elements
<a name="API_ListUltraServersByReservedCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUltraServersByReservedCapacity_ResponseSyntax) **   <a name="sagemaker-ListUltraServersByReservedCapacity-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. Use it in the next request to retrieve the next set of UltraServers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [UltraServers](#API_ListUltraServersByReservedCapacity_ResponseSyntax) **   <a name="sagemaker-ListUltraServersByReservedCapacity-response-UltraServers"></a>
A list of UltraServers that are part of the specified reserved capacity.
Type: Array of [UltraServer](API_UltraServer.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListUltraServersByReservedCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListUltraServersByReservedCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListUltraServersByReservedCapacity)
