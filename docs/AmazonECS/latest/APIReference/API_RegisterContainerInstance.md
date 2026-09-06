---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterContainerInstance.html
---

# RegisterContainerInstance
<a name="API_RegisterContainerInstance"></a>

**Note**
This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.

## Request Syntax
<a name="API_RegisterContainerInstance_RequestSyntax"></a>

```
{
   "attributes": [
      {
         "name": "{{string}}",
         "targetId": "{{string}}",
         "targetType": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "cluster": "{{string}}",
   "containerInstanceArn": "{{string}}",
   "instanceIdentityDocument": "{{string}}",
   "instanceIdentityDocumentSignature": "{{string}}",
   "platformDevices": [
      {
         "id": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "totalResources": [
      {
         "doubleValue": {{number}},
         "integerValue": {{number}},
         "longValue": {{number}},
         "name": "{{string}}",
         "stringSetValue": [ "{{string}}" ],
         "type": "{{string}}"
      }
   ],
   "versionInfo": {
      "agentHash": "{{string}}",
      "agentVersion": "{{string}}",
      "dockerVersion": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_RegisterContainerInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attributes](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-attributes"></a>
The container instance attributes that this container instance supports.
Type: Array of [Attribute](API_Attribute.md) objects
Required: No

 ** [cluster](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [containerInstanceArn](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-containerInstanceArn"></a>
The ARN of the container instance (if it was previously registered).
Type: String
Required: No

 ** [instanceIdentityDocument](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-instanceIdentityDocument"></a>
The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: `curl http://169.254.169.254/latest/dynamic/instance-identity/document/`
Type: String
Required: No

 ** [instanceIdentityDocumentSignature](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-instanceIdentityDocumentSignature"></a>
The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: `curl http://169.254.169.254/latest/dynamic/instance-identity/signature/`
Type: String
Required: No

 ** [platformDevices](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-platformDevices"></a>
The devices that are available on the container instance. The supported device types are GPUs and Neuron devices.
Type: Array of [PlatformDevice](API_PlatformDevice.md) objects
Required: No

 ** [tags](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-tags"></a>
The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [totalResources](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-totalResources"></a>
The resources available on the instance.
Type: Array of [Resource](API_Resource.md) objects
Required: No

 ** [versionInfo](#API_RegisterContainerInstance_RequestSyntax) **   <a name="ECS-RegisterContainerInstance-request-versionInfo"></a>
The version information for the Amazon ECS container agent and Docker daemon that runs on the container instance.
Type: [VersionInfo](API_VersionInfo.md) object
Required: No

## Response Syntax
<a name="API_RegisterContainerInstance_ResponseSyntax"></a>

```
{
   "containerInstance": {
      "agentConnected": boolean,
      "agentUpdateStatus": "string",
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
      "attributes": [
         {
            "name": "string",
            "targetId": "string",
            "targetType": "string",
            "value": "string"
         }
      ],
      "capacityProviderName": "string",
      "containerInstanceArn": "string",
      "ec2InstanceId": "string",
      "healthStatus": {
         "details": [
            {
               "lastStatusChange": number,
               "lastUpdated": number,
               "status": "string",
               "statusReason": "string",
               "type": "string"
            }
         ],
         "overallStatus": "string"
      },
      "pendingTasksCount": number,
      "registeredAt": number,
      "registeredResources": [
         {
            "doubleValue": number,
            "integerValue": number,
            "longValue": number,
            "name": "string",
            "stringSetValue": [ "string" ],
            "type": "string"
         }
      ],
      "remainingResources": [
         {
            "doubleValue": number,
            "integerValue": number,
            "longValue": number,
            "name": "string",
            "stringSetValue": [ "string" ],
            "type": "string"
         }
      ],
      "runningTasksCount": number,
      "status": "string",
      "statusReason": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "version": number,
      "versionInfo": {
         "agentHash": "string",
         "agentVersion": "string",
         "dockerVersion": "string"
      }
   }
}
```

## Response Elements
<a name="API_RegisterContainerInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerInstance](#API_RegisterContainerInstance_ResponseSyntax) **   <a name="ECS-RegisterContainerInstance-response-containerInstance"></a>
The container instance that was registered.
Type: [ContainerInstance](API_ContainerInstance.md) object

## Errors
<a name="API_RegisterContainerInstance_Errors"></a>

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

## See Also
<a name="API_RegisterContainerInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RegisterContainerInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RegisterContainerInstance)
