---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_DisassociateCollector.html
---

# DisassociateCollector
<a name="API_DisassociateCollector"></a>

Removes one Collector association from this Environment, preserving its other associations. The stored Collector data-access role is cleared when no Collector associations remain. The Environment owner must have permission to disassociate. A current Collector access grant is not required, and the Collector does not need to remain active or present, so stale or revoked associations can be cleaned up.

## Request Syntax
<a name="API_DisassociateCollector_RequestSyntax"></a>

```
POST /environments/{{environmentId}}/collectors/disassociate HTTP/1.1
Content-type: application/json

{
   "collectorArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateCollector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_DisassociateCollector_RequestSyntax) **   <a name="continuum-DisassociateCollector-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_DisassociateCollector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [collectorArn](#API_DisassociateCollector_RequestSyntax) **   <a name="continuum-DisassociateCollector-request-collectorArn"></a>
The Amazon Resource Name (ARN) of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:collectors/[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DisassociateCollector_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DisassociateCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DisassociateCollector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/DisassociateCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/DisassociateCollector)
