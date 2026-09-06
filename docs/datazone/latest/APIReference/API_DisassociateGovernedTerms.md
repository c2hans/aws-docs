---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DisassociateGovernedTerms.html
---

# DisassociateGovernedTerms
<a name="API_DisassociateGovernedTerms"></a>

Disassociates restricted terms from an asset.

## Request Syntax
<a name="API_DisassociateGovernedTerms_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/disassociate-governed-terms HTTP/1.1
Content-type: application/json

{
   "governedGlossaryTerms": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DisassociateGovernedTerms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DisassociateGovernedTerms_RequestSyntax) **   <a name="datazone-DisassociateGovernedTerms-request-uri-domainIdentifier"></a>
The ID of the domain where you want to disassociate restricted terms from an asset.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_DisassociateGovernedTerms_RequestSyntax) **   <a name="datazone-DisassociateGovernedTerms-request-uri-entityIdentifier"></a>
The ID of an asset from which you want to disassociate restricted terms.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityType](#API_DisassociateGovernedTerms_RequestSyntax) **   <a name="datazone-DisassociateGovernedTerms-request-uri-entityType"></a>
The type of the asset from which you want to disassociate restricted terms.
Valid Values: `ASSET`
Required: Yes

## Request Body
<a name="API_DisassociateGovernedTerms_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [governedGlossaryTerms](#API_DisassociateGovernedTerms_RequestSyntax) **   <a name="datazone-DisassociateGovernedTerms-request-governedGlossaryTerms"></a>
The restricted glossary terms that you want to disassociate from an asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Response Syntax
<a name="API_DisassociateGovernedTerms_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateGovernedTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateGovernedTerms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateGovernedTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DisassociateGovernedTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DisassociateGovernedTerms)
