---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteCluster.html
---

# DeleteCluster
<a name="API_DeleteCluster"></a>

Deletes the specified cluster. The cluster transitions to the `INACTIVE` state. Clusters with an `INACTIVE` status might remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on `INACTIVE` clusters persisting.

You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with [ListContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html) and deregister them with [DeregisterContainerInstance](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html).

## Request Syntax
<a name="API_DeleteCluster_RequestSyntax"></a>

```
{
   "cluster": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DeleteCluster_RequestSyntax) **   <a name="ECS-DeleteCluster-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteCluster_ResponseSyntax"></a>

```
{
   "cluster": {
      "activeServicesCount": number,
      "attachments": [
         {
            "details": [
               {
                  "name": "string",
                  "value": "string"
               }
            ],
            "id": "string",
            "status": "string",
            "type": "string"
         }
      ],
      "attachmentsStatus": "string",
      "capacityProviders": [ "string" ],
      "clusterArn": "string",
      "clusterName": "string",
      "configuration": {
         "executeCommandConfiguration": {
            "kmsKeyId": "string",
            "logConfiguration": {
               "cloudWatchEncryptionEnabled": boolean,
               "cloudWatchLogGroupName": "string",
               "s3BucketName": "string",
               "s3EncryptionEnabled": boolean,
               "s3KeyPrefix": "string"
            },
            "logging": "string"
         },
         "managedStorageConfiguration": {
            "fargateEphemeralStorageKmsKeyId": "string",
            "kmsKeyId": "string"
         }
      },
      "defaultCapacityProviderStrategy": [
         {
            "base": number,
            "capacityProvider": "string",
            "weight": number
         }
      ],
      "pendingTasksCount": number,
      "registeredContainerInstancesCount": number,
      "runningTasksCount": number,
      "serviceConnectDefaults": {
         "namespace": "string"
      },
      "settings": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "statistics": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DeleteCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_DeleteCluster_ResponseSyntax) **   <a name="ECS-DeleteCluster-response-cluster"></a>
The full description of the deleted cluster.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DeleteCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterContainsCapacityProviderException **
The cluster contains one or more capacity providers that prevent the requested operation. This exception occurs when you try to delete a cluster that still has active capacity providers, including Amazon ECS Managed Instances capacity providers. You must first delete all capacity providers from the cluster before you can delete the cluster itself.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterContainsContainerInstancesException **
You can't delete a cluster that has registered container instances. First, deregister the container instances before you can delete the cluster. For more information, see [DeregisterContainerInstance](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterContainsServicesException **
You can't delete a cluster that contains services. First, update the service to reduce its desired task count to 0, and then delete the service. For more information, see [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) and [DeleteService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterContainsTasksException **
You can't delete a cluster that has active tasks.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UpdateInProgressException **
There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as `PENDING` or `STAGING`, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_DeleteCluster_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DeleteCluster_Example_1"></a>

This example request deletes the cluster called `My-cluster`.

#### Sample Request
<a name="API_DeleteCluster_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 25
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DeleteCluster
X-Amz-Date: 20150429T170952Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "cluster": "My-cluster"
}
```

#### Sample Response
<a name="API_DeleteCluster_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 17:09:54 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 211
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "cluster": {
    "activeServicesCount": 0,
    "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/My-cluster",
    "clusterName": "My-cluster",
    "pendingTasksCount": 0,
    "registeredContainerInstancesCount": 0,
    "runningTasksCount": 0,
    "status": "INACTIVE"
  }
}
```

## See Also
<a name="API_DeleteCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeleteCluster)
