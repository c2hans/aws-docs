---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemon.html
---

# DescribeDaemon
<a name="API_DescribeDaemon"></a>

Describes the specified daemon.

## Request Syntax
<a name="API_DescribeDaemon_RequestSyntax"></a>

```
{
   "daemonArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDaemon_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [daemonArn](#API_DescribeDaemon_RequestSyntax) **   <a name="ECS-DescribeDaemon-request-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon to describe.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeDaemon_ResponseSyntax"></a>

```
{
   "daemon": {
      "clusterArn": "string",
      "createdAt": number,
      "currentRevisions": [
         {
            "arn": "string",
            "capacityProviders": [
               {
                  "arn": "string",
                  "runningCount": number,
                  "withoutDaemonCount": number
               }
            ],
            "totalRunningCount": number,
            "totalWithoutDaemonCount": number
         }
      ],
      "daemonArn": "string",
      "deploymentArn": "string",
      "status": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_DescribeDaemon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [daemon](#API_DescribeDaemon_ResponseSyntax) **   <a name="ECS-DescribeDaemon-response-daemon"></a>
The full description of the daemon, including the current revisions, deployment ARN, cluster, and status information.
Type: [DaemonDetail](API_DaemonDetail.md) object

## Errors
<a name="API_DescribeDaemon_Errors"></a>

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

 ** DaemonNotFoundException **
The specified daemon wasn't found. You can view your available daemons with [ListDaemons](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html). Amazon ECS daemons are cluster specific and Region specific.
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
<a name="API_DescribeDaemon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeDaemon_Example_1"></a>

This example describes the my-monitoring-daemon daemon.

#### Sample Request
<a name="API_DescribeDaemon_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 94
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeDaemon
X-Amz-Date: 20250320T160000Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon"
}
```

#### Sample Response
<a name="API_DescribeDaemon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 20 Mar 2025 16:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 822
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "daemon": {
    "daemonArn": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon",
    "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
    "status": "ACTIVE",
    "currentRevisions": [
      {
        "arn": "arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095",
        "capacityProviders": [
          {
            "arn": "arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider",
            "runningCount": 3
          }
        ],
        "totalRunningCount": 3
      }
    ],
    "deploymentArn": "arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/aB1cD2eF3gH4iJ5k",
    "createdAt": "2025-03-15T12:00:00.000Z",
    "updatedAt": "2025-03-20T15:30:00.000Z"
  }
}
```

## See Also
<a name="API_DescribeDaemon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeDaemon)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeDaemon)
