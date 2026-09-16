---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterEvent.html
---

# DescribeClusterEvent
<a name="API_DescribeClusterEvent"></a>

Retrieves detailed information about a specific event for a given HyperPod cluster. This functionality is only supported when the `NodeProvisioningMode` is set to `Continuous`.

## Request Syntax
<a name="API_DescribeClusterEvent_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "EventId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClusterEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DescribeClusterEvent_RequestSyntax) **   <a name="sagemaker-DescribeClusterEvent-request-ClusterName"></a>
The name or Amazon Resource Name (ARN) of the HyperPod cluster associated with the event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [EventId](#API_DescribeClusterEvent_RequestSyntax) **   <a name="sagemaker-DescribeClusterEvent-request-EventId"></a>
The unique identifier (UUID) of the event to describe. This ID can be obtained from the `ListClusterEvents` operation.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeClusterEvent_ResponseSyntax"></a>

```
{
   "EventDetails": {
      "ClusterArn": "string",
      "ClusterName": "string",
      "Description": "string",
      "EventDetails": {
         "EventMetadata": { ... }
      },
      "EventId": "string",
      "EventLevel": "string",
      "InstanceGroupName": "string",
      "InstanceId": "string",
      "ResourceType": "string"
   }
}
```

## Response Elements
<a name="API_DescribeClusterEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventDetails](#API_DescribeClusterEvent_ResponseSyntax) **   <a name="sagemaker-DescribeClusterEvent-response-EventDetails"></a>
Detailed information about the requested cluster event, including event metadata for various resource types such as `Cluster`, `InstanceGroup`, `Instance`, and their associated attributes.
Type: [ClusterEventDetail](API_ClusterEventDetail.md) object

## Errors
<a name="API_DescribeClusterEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClusterEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeClusterEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeClusterEvent)
