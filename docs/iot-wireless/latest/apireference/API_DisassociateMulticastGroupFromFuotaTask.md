---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateMulticastGroupFromFuotaTask.html
---

# DisassociateMulticastGroupFromFuotaTask
<a name="API_DisassociateMulticastGroupFromFuotaTask"></a>

Disassociates a multicast group from a FUOTA task.

## Request Syntax
<a name="API_DisassociateMulticastGroupFromFuotaTask_RequestSyntax"></a>

```
DELETE /fuota-tasks/{{Id}}/multicast-groups/{{MulticastGroupId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateMulticastGroupFromFuotaTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DisassociateMulticastGroupFromFuotaTask_RequestSyntax) **   <a name="iotwireless-DisassociateMulticastGroupFromFuotaTask-request-uri-Id"></a>
The ID of a FUOTA task.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [MulticastGroupId](#API_DisassociateMulticastGroupFromFuotaTask_RequestSyntax) **   <a name="iotwireless-DisassociateMulticastGroupFromFuotaTask-request-uri-MulticastGroupId"></a>
The ID of the multicast group.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_DisassociateMulticastGroupFromFuotaTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateMulticastGroupFromFuotaTask_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DisassociateMulticastGroupFromFuotaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DisassociateMulticastGroupFromFuotaTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateMulticastGroupFromFuotaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/DisassociateMulticastGroupFromFuotaTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
