---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DisassociatePublisher.html
---

# DisassociatePublisher

Removes the publisher association from a registry record and releases the record's public identifier. Disassociating a registry record that has no association succeeds. If another account created the association, the request fails with `AccessDeniedException`.

## Request Syntax
<a name="API_DisassociatePublisher_RequestSyntax"></a>

```
DELETE /associations/{{recordArn+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociatePublisher_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordArn](#API_DisassociatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-DisassociatePublisher-request-uri-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record to disassociate from its publisher.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
Required: Yes

## Request Body
<a name="API_DisassociatePublisher_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociatePublisher_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DisassociatePublisher_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DisassociatePublisher_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DisassociatePublisher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/DisassociatePublisher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DisassociatePublisher)
