---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateContainerAssociation.html
---

# CreateContainerAssociation
<a name="API_CreateContainerAssociation"></a>

Creates a AWS Network Firewall container association. The association monitors container lifecycle events in your Amazon ECS or Amazon EKS clusters and resolves running container addresses for use in firewall rules.

## Request Syntax
<a name="API_CreateContainerAssociation_RequestSyntax"></a>

```
{
   "ContainerAssociationName": "{{string}}",
   "ContainerMonitoringConfigurations": [
      {
         "AttributeFilters": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "ClusterArn": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateContainerAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContainerAssociationName](#API_CreateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-CreateContainerAssociation-request-ContainerAssociationName"></a>
The descriptive name of the container association. You can't change the name of a container association after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ContainerMonitoringConfigurations](#API_CreateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-CreateContainerAssociation-request-ContainerMonitoringConfigurations"></a>
The monitoring configurations for the container association. Each configuration specifies an Amazon ECS or Amazon EKS cluster to monitor and optional attribute filters to narrow which containers are tracked.
Type: Array of [ContainerMonitoringConfiguration](API_ContainerMonitoringConfiguration.md) objects
Required: Yes

 ** [Description](#API_CreateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-CreateContainerAssociation-request-Description"></a>
A description of the container association.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`
Required: No

 ** [Tags](#API_CreateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-CreateContainerAssociation-request-Tags"></a>
The key:value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** [Type](#API_CreateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-CreateContainerAssociation-request-Type"></a>
The type of containers to monitor. You can't change the container type after creation. Valid values:
+  `ECS` - Amazon Elastic Container Service
+  `EKS` - Amazon Elastic Kubernetes Service
Type: String
Valid Values: `ECS | EKS`
Required: Yes

## Response Syntax
<a name="API_CreateContainerAssociation_ResponseSyntax"></a>

```
{
   "ContainerAssociationArn": "string",
   "ContainerAssociationName": "string",
   "ContainerMonitoringConfigurations": [
      {
         "AttributeFilters": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "ClusterArn": "string"
      }
   ],
   "Description": "string",
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "Type": "string",
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_CreateContainerAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerAssociationArn](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`

 ** [ContainerAssociationName](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-ContainerAssociationName"></a>
The descriptive name of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [ContainerMonitoringConfigurations](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-ContainerMonitoringConfigurations"></a>
The monitoring configurations for the container association.
Type: Array of [ContainerMonitoringConfiguration](API_ContainerMonitoringConfiguration.md) objects

 ** [Description](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-Description"></a>
A description of the container association.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`

 ** [Status](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-Status"></a>
The current status of the container association. For a new container association, the status is `CREATING`.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | UPDATING`

 ** [Tags](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-Tags"></a>
The key:value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [Type](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-Type"></a>
The container type. Valid values:
+  `ECS` - Amazon Elastic Container Service
+  `EKS` - Amazon Elastic Kubernetes Service
Type: String
Valid Values: `ECS | EKS`

 ** [UpdateToken](#API_CreateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateContainerAssociation-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the container association. The token marks the state of the container association resource at the time of the request.
To make changes to the container association, you provide the token in your request. Network Firewall uses the token to ensure that the container association hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the container association again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`

## Errors
<a name="API_CreateContainerAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientCapacityException **
 AWS doesn't currently have enough available capacity to fulfill your request. Try your request later.
HTTP Status Code: 500

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** LimitExceededException **
Unable to perform the operation because doing so would violate a limit setting.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_CreateContainerAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateContainerAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateContainerAssociation)
