---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteContainerAssociation.html
---

# DeleteContainerAssociation
<a name="API_DeleteContainerAssociation"></a>

Deletes a container association. The resource transitions to a `DELETING` state. Deletion is asynchronous - Network Firewall returns immediately while cleanup proceeds in the background. You can't delete a container association while a rule group references it.

## Request Syntax
<a name="API_DeleteContainerAssociation_RequestSyntax"></a>

```
{
   "ContainerAssociationArn": "{{string}}",
   "ContainerAssociationName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteContainerAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContainerAssociationArn](#API_DeleteContainerAssociation_RequestSyntax) **   <a name="networkfirewall-DeleteContainerAssociation-request-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [ContainerAssociationName](#API_DeleteContainerAssociation_RequestSyntax) **   <a name="networkfirewall-DeleteContainerAssociation-request-ContainerAssociationName"></a>
The descriptive name of the container association.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## Response Syntax
<a name="API_DeleteContainerAssociation_ResponseSyntax"></a>

```
{
   "ContainerAssociationArn": "string",
   "ContainerAssociationName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DeleteContainerAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerAssociationArn](#API_DeleteContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DeleteContainerAssociation-response-ContainerAssociationArn"></a>
The Amazon Resource Name (ARN) of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`

 ** [ContainerAssociationName](#API_DeleteContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DeleteContainerAssociation-response-ContainerAssociationName"></a>
The descriptive name of the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [Status](#API_DeleteContainerAssociation_ResponseSyntax) **   <a name="networkfirewall-DeleteContainerAssociation-response-Status"></a>
The current status of the container association. After deletion is initiated, the status is `DELETING`.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | UPDATING`

## Errors
<a name="API_DeleteContainerAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidOperationException **
The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.
HTTP Status Code: 400

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
<a name="API_DeleteContainerAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteContainerAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteContainerAssociation)
