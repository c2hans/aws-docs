---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_RegisterComputeNodeGroupInstance.html
---

# RegisterComputeNodeGroupInstance
<a name="API_RegisterComputeNodeGroupInstance"></a>

**Important**
This API action isn't intended for you to use.

 AWS PCS uses this API action to register the compute nodes it launches in your account.

## Request Syntax
<a name="API_RegisterComputeNodeGroupInstance_RequestSyntax"></a>

```
{
   "bootstrapId": "{{string}}",
   "clusterIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterComputeNodeGroupInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bootstrapId](#API_RegisterComputeNodeGroupInstance_RequestSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-request-bootstrapId"></a>
The client-generated token to allow for retries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\S]+`
Required: Yes

 ** [clusterIdentifier](#API_RegisterComputeNodeGroupInstance_RequestSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-request-clusterIdentifier"></a>
The name or ID of the cluster to register the compute node group instance in.
Type: String
Pattern: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{2,40})`
Required: Yes

## Response Syntax
<a name="API_RegisterComputeNodeGroupInstance_ResponseSyntax"></a>

```
{
   "clusterName": "string",
   "computeNodeGroupId": "string",
   "computeNodeGroupName": "string",
   "endpoints": [
      {
         "ipv6Address": "string",
         "port": "string",
         "privateIpAddress": "string",
         "publicIpAddress": "string",
         "type": "string"
      }
   ],
   "nodeID": "string",
   "nodeLifecycleActions": {
      "scriptCachingPolicy": "string",
      "stages": {
         "nodeBootstrapped": [
            {
               "arguments": [ "string" ],
               "executionPolicy": "string",
               "name": "string",
               "onError": "string",
               "scriptSource": {
                  "checksum": "string",
                  "s3VersionId": "string",
                  "scriptLocation": "string"
               }
            }
         ],
         "nodeReady": [
            {
               "arguments": [ "string" ],
               "executionPolicy": "string",
               "name": "string",
               "onError": "string",
               "scriptSource": {
                  "checksum": "string",
                  "s3VersionId": "string",
                  "scriptLocation": "string"
               }
            }
         ]
      }
   },
   "sharedSecret": "string"
}
```

## Response Elements
<a name="API_RegisterComputeNodeGroupInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusterName](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-clusterName"></a>
The name of the cluster that the compute node registered into.
Type: String

 ** [computeNodeGroupId](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-computeNodeGroupId"></a>
The ID of the compute node group that the compute node registered into.
Type: String

 ** [computeNodeGroupName](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-computeNodeGroupName"></a>
The name of the compute node group that the compute node registered into.
Type: String

 ** [endpoints](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-endpoints"></a>
The list of endpoints available for interaction with the scheduler.
Type: Array of [Endpoint](API_Endpoint.md) objects

 ** [nodeID](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-nodeID"></a>
The scheduler node ID for this instance.
Type: String

 ** [nodeLifecycleActions](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-nodeLifecycleActions"></a>
The node lifecycle actions configured for the node group, including scripts to run when a compute node finishes bootstrapping or becomes ready to accept jobs.
Type: [NodeLifecycleActions](API_NodeLifecycleActions.md) object

 ** [sharedSecret](#API_RegisterComputeNodeGroupInstance_ResponseSyntax) **   <a name="PCS-RegisterComputeNodeGroupInstance-response-sharedSecret"></a>
For the Slurm scheduler, this is the shared Munge key the scheduler uses to authenticate compute node group instances.
Type: String

## Errors
<a name="API_RegisterComputeNodeGroupInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 *Examples*
+ The launch template instance profile doesn't pass `iam:PassRole` verification.
+ There is a mismatch between the account ID and cluster ID.
+ The cluster ID doesn't exist.
+ The EC2 instance isn't present.
HTTP Status Code: 400

 ** InternalServerException **
 AWS PCS can't process your request right now. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_RegisterComputeNodeGroupInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/RegisterComputeNodeGroupInstance)
