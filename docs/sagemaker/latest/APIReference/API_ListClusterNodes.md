---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterNodes.html
---

# ListClusterNodes
<a name="API_ListClusterNodes"></a>

Retrieves the list of instances (also called *nodes* interchangeably) in a SageMaker HyperPod cluster.

## Request Syntax
<a name="API_ListClusterNodes_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "IncludeNodeLogicalIds": {{boolean}},
   "InstanceGroupNameContains": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-ClusterName"></a>
The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster in which you want to retrieve the list of nodes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [IncludeNodeLogicalIds](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-IncludeNodeLogicalIds"></a>
Specifies whether to include nodes that are still being provisioned in the response. When set to true, the response includes all nodes regardless of their provisioning status. When set to `False` (default), only nodes with assigned `InstanceIds` are returned.
Type: Boolean
Required: No

 ** [InstanceGroupNameContains](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-InstanceGroupNameContains"></a>
A filter that returns the instance groups whose name contain a specified string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [MaxResults](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-MaxResults"></a>
The maximum number of nodes to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-NextToken"></a>
If the result of the previous `ListClusterNodes` request was truncated, the response includes a `NextToken`. To retrieve the next set of cluster nodes, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-SortBy"></a>
The field by which to sort results. The default value is `CREATION_TIME`.
Type: String
Valid Values: `CREATION_TIME | NAME`
Required: No

 ** [SortOrder](#API_ListClusterNodes_RequestSyntax) **   <a name="sagemaker-ListClusterNodes-request-SortOrder"></a>
The sort order for results. The default value is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListClusterNodes_ResponseSyntax"></a>

```
{
   "ClusterNodeSummaries": [
      {
         "CurrentImageReleaseVersion": "string",
         "ImageVersionStatus": "string",
         "InstanceGroupName": "string",
         "InstanceId": "string",
         "InstanceStatus": {
            "Message": "string",
            "Status": "string"
         },
         "InstanceType": "string",
         "NodeLogicalId": "string",
         "PrivateDnsHostname": "string",
         "UltraServerInfo": {
            "Id": "string",
            "Type": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterNodeSummaries](#API_ListClusterNodes_ResponseSyntax) **   <a name="sagemaker-ListClusterNodes-response-ClusterNodeSummaries"></a>
The summaries of listed instances in a SageMaker HyperPod cluster
Type: Array of [ClusterNodeSummary](API_ClusterNodeSummary.md) objects

 ** [NextToken](#API_ListClusterNodes_ResponseSyntax) **   <a name="sagemaker-ListClusterNodes-response-NextToken"></a>
The next token specified for listing instances in a SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusterNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListClusterNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusterNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusterNodes)
