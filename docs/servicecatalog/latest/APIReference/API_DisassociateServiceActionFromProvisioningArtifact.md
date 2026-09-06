---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociateServiceActionFromProvisioningArtifact.html
---

# DisassociateServiceActionFromProvisioningArtifact
<a name="API_DisassociateServiceActionFromProvisioningArtifact"></a>

Disassociates the specified self-service action association from the specified provisioning artifact.

## Request Syntax
<a name="API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "ProductId": "{{string}}",
   "ProvisioningArtifactId": "{{string}}",
   "ServiceActionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateServiceActionFromProvisioningArtifact_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DisassociateServiceActionFromProvisioningArtifact-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IdempotencyToken](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DisassociateServiceActionFromProvisioningArtifact-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests from the same AWS account use the same idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** [ProductId](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DisassociateServiceActionFromProvisioningArtifact-request-ProductId"></a>
The product identifier. For example, `prod-abcdzk7xy33qa`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProvisioningArtifactId](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DisassociateServiceActionFromProvisioningArtifact-request-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ServiceActionId](#API_DisassociateServiceActionFromProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-DisassociateServiceActionFromProvisioningArtifact-request-ServiceActionId"></a>
The self-service action identifier. For example, `act-fs7abcd89wxyz`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Elements
<a name="API_DisassociateServiceActionFromProvisioningArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateServiceActionFromProvisioningArtifact_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateServiceActionFromProvisioningArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateServiceActionFromProvisioningArtifact)
