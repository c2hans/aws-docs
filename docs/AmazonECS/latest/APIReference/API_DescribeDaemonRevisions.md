---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonRevisions.html
---

# DescribeDaemonRevisions
<a name="API_DescribeDaemonRevisions"></a>

Describes one or more of your daemon revisions.

A daemon revision is a snapshot of a daemon's configuration at the time a deployment was initiated. It captures the daemon task definition, container images, tag propagation, and execute command settings. Daemon revisions are immutable.

## Request Syntax
<a name="API_DescribeDaemonRevisions_RequestSyntax"></a>

```
{
   "daemonRevisionArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeDaemonRevisions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [daemonRevisionArns](#API_DescribeDaemonRevisions_RequestSyntax) **   <a name="ECS-DescribeDaemonRevisions-request-daemonRevisionArns"></a>
The ARN of the daemon revisions to describe. You can specify up to 20 ARNs.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_DescribeDaemonRevisions_ResponseSyntax"></a>

```
{
   "daemonRevisions": [
      {
         "clusterArn": "string",
         "containerImages": [
            {
               "containerName": "string",
               "image": "string",
               "imageDigest": "string"
            }
         ],
         "createdAt": number,
         "daemonArn": "string",
         "daemonRevisionArn": "string",
         "daemonTaskDefinitionArn": "string",
         "enableECSManagedTags": boolean,
         "enableExecuteCommand": boolean,
         "propagateTags": "string"
      }
   ],
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeDaemonRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemonRevisions](#API_DescribeDaemonRevisions_ResponseSyntax) **   <a name="ECS-DescribeDaemonRevisions-response-daemonRevisions"></a>
The list of daemon revisions.
Type: Array of [DaemonRevision](API_DaemonRevision.md) objects

 ** [failures](#API_DescribeDaemonRevisions_ResponseSyntax) **   <a name="ECS-DescribeDaemonRevisions-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

## Errors
<a name="API_DescribeDaemonRevisions_Errors"></a>

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

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDaemonRevisions_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeDaemonRevisions_Example_1"></a>

This example describes a daemon revision for the my-monitoring-daemon daemon.

#### Sample Request
<a name="API_DescribeDaemonRevisions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 142
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeDaemonRevisions
X-Amz-Date: 20250320T161000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonRevisionArns": [
    "arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095"
  ]
}
```

#### Sample Response
<a name="API_DescribeDaemonRevisions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 20 Mar 2025 16:10:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 910
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemonRevisions": [
    {
      "daemonRevisionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095",
      "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
      "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
      "daemonTaskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1",
      "createdAt": "2025-03-15T12:00:00.000Z",
      "containerImages": [
        {
          "containerName": "cloudwatch-agent",
          "imageDigest": "sha256:a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
          "image": "public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest"
        }
      ],
      "propagateTags": "NONE",
      "enableECSManagedTags": false,
      "enableExecuteCommand": false
    }
  ],
  "failures": []
}
```

## See Also
<a name="API_DescribeDaemonRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeDaemonRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeDaemonRevisions)
