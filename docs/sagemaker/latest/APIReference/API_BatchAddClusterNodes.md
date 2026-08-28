---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchAddClusterNodes.html
---

# BatchAddClusterNodes
<a name="API_BatchAddClusterNodes"></a>

Adds nodes to a HyperPod cluster by incrementing the target count for one or more instance groups. This operation returns a unique `NodeLogicalId` for each node being added, which can be used to track the provisioning status of the node. This API provides a safer alternative to `UpdateCluster` for scaling operations by avoiding unintended configuration changes.

**Note**
This API is only supported for clusters using `Continuous` as the `NodeProvisioningMode`.

## Request Syntax
<a name="API_BatchAddClusterNodes_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ClusterName": "{{string}}",
   "NodesToAdd": [
      {
         "AvailabilityZones": [ "{{string}}" ],
         "IncrementTargetCountBy": {{number}},
         "InstanceGroupName": "{{string}}",
         "InstanceTypes": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_BatchAddClusterNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_BatchAddClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchAddClusterNodes-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 8 hours. If you retry the request with the same client token within this timeframe and the same parameters, the API returns the same set of `NodeLogicalIds` with their latest status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [ClusterName](#API_BatchAddClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchAddClusterNodes-request-ClusterName"></a>
The name of the HyperPod cluster to which you want to add nodes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [NodesToAdd](#API_BatchAddClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchAddClusterNodes-request-NodesToAdd"></a>
A list of instance groups and the number of nodes to add to each. You can specify up to 5 instance groups in a single request, with a maximum of 50 nodes total across all instance groups.
Type: Array of [AddClusterNodeSpecification](API_AddClusterNodeSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## Response Syntax
<a name="API_BatchAddClusterNodes_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "AvailabilityZones": [ "string" ],
         "ErrorCode": "string",
         "FailedCount": number,
         "InstanceGroupName": "string",
         "InstanceTypes": [ "string" ],
         "Message": "string"
      }
   ],
   "Successful": [
      {
         "AvailabilityZones": [ "string" ],
         "InstanceGroupName": "string",
         "InstanceTypes": [ "string" ],
         "NodeLogicalId": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchAddClusterNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchAddClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchAddClusterNodes-response-Failed"></a>
A list of errors that occurred during the node addition operation. Each entry includes the instance group name, error code, number of failed additions, and an error message.
Type: Array of [BatchAddClusterNodesError](API_BatchAddClusterNodesError.md) objects

 ** [Successful](#API_BatchAddClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchAddClusterNodes-response-Successful"></a>
A list of `NodeLogicalIDs` that were successfully added to the cluster. The `NodeLogicalID` is unique per cluster and does not change between instance replacements. Each entry includes a `NodeLogicalId` that can be used to track the node's provisioning status (with `DescribeClusterNode`), the instance group name, and the current status of the node.
Type: Array of [NodeAdditionResult](API_NodeAdditionResult.md) objects

## Errors
<a name="API_BatchAddClusterNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_BatchAddClusterNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/BatchAddClusterNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchAddClusterNodes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
