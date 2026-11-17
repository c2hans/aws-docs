---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterOperation.html
---

# DescribeClusterOperation
<a name="API_DescribeClusterOperation"></a>

Retrieves detailed information about a specific operation for a given HyperPod cluster, such as a scaling operation or a deep health check. Use the `OperationId` returned by the `ListClusterOperations` operation to identify the operation to describe.

## Request Syntax
<a name="API_DescribeClusterOperation_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "OperationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClusterOperation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DescribeClusterOperation_RequestSyntax) **   <a name="sagemaker-DescribeClusterOperation-request-ClusterName"></a>
The name or Amazon Resource Name (ARN) of the HyperPod cluster associated with the operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `((arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}))`
Required: Yes

 ** [OperationId](#API_DescribeClusterOperation_RequestSyntax) **   <a name="sagemaker-DescribeClusterOperation-request-OperationId"></a>
The unique identifier (UUID) of the operation to describe. This ID can be obtained from the `ListClusterOperations` operation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeClusterOperation_ResponseSyntax"></a>

```
{
   "ClusterArn": "string",
   "CreationTime": number,
   "DeepHealthCheckDetails": [
      {
         "DeepHealthChecks": [ "string" ],
         "InstanceGroupName": "string",
         "InstanceIds": [ "string" ]
      }
   ],
   "OperationId": "string",
   "ScalingDetails": [
      {
         "Desired": {
            "CurrentCount": number,
            "MinCount": number,
            "TargetCount": number
         },
         "InstanceGroupName": "string",
         "Original": {
            "CurrentCount": number,
            "MinCount": number,
            "TargetCount": number
         },
         "Status": "string"
      }
   ],
   "Status": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_DescribeClusterOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the HyperPod cluster associated with the operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [CreationTime](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-CreationTime"></a>
The timestamp when the operation was created.
Type: Timestamp

 ** [DeepHealthCheckDetails](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-DeepHealthCheckDetails"></a>
The deep health check details for the operation. This field is populated when the operation `Type` is `DeepHealthCheck`.
Type: Array of [InstanceGroupHealthCheckConfiguration](API_InstanceGroupHealthCheckConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 99 items.

 ** [OperationId](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-OperationId"></a>
The unique identifier (UUID) of the operation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [ScalingDetails](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-ScalingDetails"></a>
The per-instance-group scaling details for the operation. This field is populated when the operation `Type` is `Scaling`.
Type: Array of [ClusterOperationScalingDetails](API_ClusterOperationScalingDetails.md) objects

 ** [Status](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-Status"></a>
The current status of the operation. Valid values are `InProgress`, `Superseded`, or `Done`.
Type: String
Valid Values: `InProgress | Superseded | Done`

 ** [Type](#API_DescribeClusterOperation_ResponseSyntax) **   <a name="sagemaker-DescribeClusterOperation-response-Type"></a>
The type of the operation. Valid values are `Scaling` or `DeepHealthCheck`.
Type: String
Valid Values: `Scaling | DeepHealthCheck`

## Errors
<a name="API_DescribeClusterOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClusterOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeClusterOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeClusterOperation)
