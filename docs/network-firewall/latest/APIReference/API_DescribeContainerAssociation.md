---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeContainerAssociation.html
---

# DescribeContainerAssociation
<a name="API_DescribeContainerAssociation"></a>

Retrieves the configuration and status of a container association.

## Request Syntax
<a name="API_DescribeContainerAssociation_RequestSyntax"></a>

```
{
   "ContainerAssociationArn": "{{string}}",
   "ContainerAssociationName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeContainerAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContainerAssociationArn](#API_DescribeContainerAssociation_RequestSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-request-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [ContainerAssociationName](#API_DescribeContainerAssociation_RequestSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-request-ContainerAssociationName"></a>
The descriptive name of the container association.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## Response Syntax
<a name="API_DescribeContainerAssociation_ResponseSyntax"></a>

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
   "LastUpdatedTime": number,
   "ResolvedCidrCount": number,
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
<a name="API_DescribeContainerAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerAssociationArn](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`

 ** [ContainerAssociationName](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-ContainerAssociationName"></a>
The descriptive name of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [ContainerMonitoringConfigurations](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-ContainerMonitoringConfigurations"></a>
The monitoring configurations for the container association.
Type: Array of [ContainerMonitoringConfiguration](API_ContainerMonitoringConfiguration.md) objects

 ** [Description](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-Description"></a>
A description of the container association.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`

 ** [LastUpdatedTime](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-LastUpdatedTime"></a>
The most recent time that Network Firewall updated the container association.
Type: Timestamp

 ** [ResolvedCidrCount](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-ResolvedCidrCount"></a>
The number of CIDR blocks resolved from the monitored containers.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.

 ** [Status](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-Status"></a>
The current status of the container association.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | UPDATING`

 ** [Tags](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-Tags"></a>
The key:value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [Type](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-Type"></a>
The container type. Valid values:
+  `ECS` - Amazon Elastic Container Service
+  `EKS` - Amazon Elastic Kubernetes Service
Type: String
Valid Values: `ECS | EKS`

 ** [UpdateToken](#API_DescribeContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeContainerAssociation-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the container association. The token marks the state of the container association resource at the time of the request.
To make changes to the container association, you provide the token in your request. Network Firewall uses the token to ensure that the container association hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the container association again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`

## Errors
<a name="API_DescribeContainerAssociation_Errors"></a>

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

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_DescribeContainerAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeContainerAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeContainerAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
