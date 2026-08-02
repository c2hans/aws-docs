---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateContainerAssociation.html
---

# UpdateContainerAssociation
<a name="API_UpdateContainerAssociation"></a>

Updates the monitoring configurations and description of a container association. You can't change the container type after creation. Provide an update token to enable optimistic concurrency control.

## Request Syntax
<a name="API_UpdateContainerAssociation_RequestSyntax"></a>

```
{
   "ContainerAssociationArn": "{{string}}",
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
   "Type": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateContainerAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContainerAssociationArn](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [ContainerAssociationName](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-ContainerAssociationName"></a>
The descriptive name of the container association.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [ContainerMonitoringConfigurations](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-ContainerMonitoringConfigurations"></a>
The updated monitoring configurations for the container association. Each configuration specifies an Amazon ECS or Amazon EKS cluster to monitor and optional attribute filters.
Type: Array of [ContainerMonitoringConfiguration](API_ContainerMonitoringConfiguration.md) objects
Required: Yes

 ** [Description](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-Description"></a>
A description of the container association. When omitted, the existing description remains unchanged. To clear the description, pass an empty string.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`
Required: No

 ** [Tags](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-Tags"></a>
The key:value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** [Type](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-Type"></a>
The container type. This value must match the existing type and can't be changed. Valid values:
+  `ECS` - Amazon Elastic Container Service
+  `EKS` - Amazon Elastic Kubernetes Service
Type: String
Valid Values: `ECS | EKS`
Required: Yes

 ** [UpdateToken](#API_UpdateContainerAssociation_RequestSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the container association. The token marks the state of the container association resource at the time of the request.
To make changes to the container association, you provide the token in your request. Network Firewall uses the token to ensure that the container association hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the container association again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`
Required: Yes

## Response Syntax
<a name="API_UpdateContainerAssociation_ResponseSyntax"></a>

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
<a name="API_UpdateContainerAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerAssociationArn](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`

 ** [ContainerAssociationName](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-ContainerAssociationName"></a>
The descriptive name of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [ContainerMonitoringConfigurations](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-ContainerMonitoringConfigurations"></a>
The monitoring configurations for the container association.
Type: Array of [ContainerMonitoringConfiguration](API_ContainerMonitoringConfiguration.md) objects

 ** [Description](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-Description"></a>
A description of the container association.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`

 ** [Status](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-Status"></a>
The current status of the container association.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING`

 ** [Tags](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-Tags"></a>
The key:value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [Type](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-Type"></a>
The container type. Valid values:
+  `ECS` - Amazon Elastic Container Service
+  `EKS` - Amazon Elastic Kubernetes Service
Type: String
Valid Values: `ECS | EKS`

 ** [UpdateToken](#API_UpdateContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-UpdateContainerAssociation-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the container association. The token marks the state of the container association resource at the time of the request.
To make changes to the container association, you provide the token in your request. Network Firewall uses the token to ensure that the container association hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the container association again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`

## Errors
<a name="API_UpdateContainerAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** InvalidTokenException **
The token you provided is stale or isn't valid for the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_UpdateContainerAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateContainerAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateContainerAssociation)
