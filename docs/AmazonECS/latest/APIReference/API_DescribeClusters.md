---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html
---

# DescribeClusters
<a name="API_DescribeClusters"></a>

Describes one or more of your clusters.

 For AWS CLI examples, see [describe-clusters.rst](https://github.com/aws/aws-cli/blob/develop/awscli/examples/ecs/describe-clusters.rst) on GitHub.

## Request Syntax
<a name="API_DescribeClusters_RequestSyntax"></a>

```
{
   "clusters": [ "{{string}}" ],
   "include": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clusters](#API_DescribeClusters_RequestSyntax) **   <a name="ECS-DescribeClusters-request-clusters"></a>
A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.
Type: Array of strings
Required: No

 ** [include](#API_DescribeClusters_RequestSyntax) **   <a name="ECS-DescribeClusters-request-include"></a>
Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isn't included.
If `ATTACHMENTS` is specified, the attachments for the container instances or tasks within the cluster are included, for example the capacity providers.
If `SETTINGS` is specified, the settings for the cluster are included.
If `CONFIGURATIONS` is specified, the configuration for the cluster is included.
If `STATISTICS` is specified, the task and service count is included, separated by launch type.
If `TAGS` is specified, the metadata tags associated with the cluster are included.
Type: Array of strings
Valid Values: `ATTACHMENTS | CONFIGURATIONS | SETTINGS | STATISTICS | TAGS`
Required: No

## Response Syntax
<a name="API_DescribeClusters_ResponseSyntax"></a>

```
{
   "clusters": [
      {
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
<a name="API_DescribeClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusters](#API_DescribeClusters_ResponseSyntax) **   <a name="ECS-DescribeClusters-response-clusters"></a>
The list of clusters.
Type: Array of [Cluster](API_Cluster.md) objects

 ** [failures](#API_DescribeClusters_ResponseSyntax) **   <a name="ECS-DescribeClusters-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

## Errors
<a name="API_DescribeClusters_Errors"></a>

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

## Examples
<a name="API_DescribeClusters_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_DescribeClusters_Example_1"></a>

This example request provides descriptive information about the default cluster.

#### Sample Request
<a name="API_DescribeClusters_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 25
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeClusters
X-Amz-Date: 20150429T185014Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "clusters": [
    "default"
  ]
}
```

#### Sample Response
<a name="API_DescribeClusters_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 18:50:14 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "clusters": [
    {
      "activeServicesCount": 1,
      "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/default",
      "clusterName": "default",
      "pendingTasksCount": 0,
      "registeredContainerInstancesCount": 0,
      "runningTasksCount": 0,
      "status": "ACTIVE"
    }
  ],
  "failures": []
}
```

### Example
<a name="API_DescribeClusters_Example_2"></a>

This example request provides descriptive information about a cluster that has an associated capacity provider with managed scaling turned on. The capacity provider and the scaling policy that Amazon ECS creates on your behalf are included as attachments in the response.

#### Sample Request
<a name="API_DescribeClusters_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 25
X-Amz-Target: AmazonEC2ContainerServiceV20141113.DescribeClusters
X-Amz-Date: 20220429T185014Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "clusters": [
    "cluster-with-capacity-provider",
    "include": ["ATTACHMENTS"]
  ]
}
```

#### Sample Response
<a name="API_DescribeClusters_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2022 18:50:14 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "clusters": [
        {
            "clusterArn": "arn:aws:ecs:us-west-2:012345678910:cluster/cluster-with-capacity-provider",
            "clusterName": "cluster-with-capacity-provider",
            "status": "ACTIVE",
            "registeredContainerInstancesCount": 0,
            "runningTasksCount": 0,
            "pendingTasksCount": 0,
            "activeServicesCount": 0,
            "statistics": [],
            "tags": [],
            "settings": [],
            "capacityProviders": [
                "FARGATE",
                "FARGATE_SPOT",
                "Infra-ECS-Cluster-45ff394c-615f-4496-a336-8019a3b38d7a-EC2CapacityProvider-EXAMPLE"
            ],
            "defaultCapacityProviderStrategy": [],
            "attachments": [
                {
                    "id": "bf5ecfe0-f813-4356-b862-1dbe6025c57f",
                    "type": "as_policy",
                    "status": "CREATED",
                    "details": [
                        {
                            "name": "capacityProviderName",
                            "value": "Infra-ECS-Cluster-45ff394c-615f-4496-a336-8019a3b38d7a-EC2CapacityProvider-EXAMPLE"
                        },
                        {
                            "name": "scalingPolicyName",
                            "value": "ECSManagedAutoScalingPolicy-55c67464-7691-4310-a725-EXAMPLE"
                        }
                    ]
                }
            ],
            "attachmentsStatus": "UPDATE_COMPLETE"
        }
    ],
    "failures": []
}
```

## See Also
<a name="API_DescribeClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeClusters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
