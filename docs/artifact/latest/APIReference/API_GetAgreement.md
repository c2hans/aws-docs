---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAgreement.html
---

# GetAgreement
<a name="API_GetAgreement"></a>

Retrieve an agreement document.

## Request Syntax
<a name="API_GetAgreement_RequestSyntax"></a>

```
GET /v1/agreement/get?agreementId={{agreementId}}&ndaToken={{ndaToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAgreement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agreementId](#API_GetAgreement_RequestSyntax) **   <a name="artifact-GetAgreement-request-uri-agreementId"></a>
Agreement identifier.
Pattern: `agreement-[a-zA-Z0-9]{16}`
Required: Yes

 ** [ndaToken](#API_GetAgreement_RequestSyntax) **   <a name="artifact-GetAgreement-request-uri-ndaToken"></a>
NDA token received when calling AcceptNdaForAgreement.
Pattern: `nda-token-[a-zA-Z0-9]{24}`
Required: Yes

## Request Body
<a name="API_GetAgreement_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgreement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "acceptanceTerms": [ "string" ],
   "acceptanceTermsToken": "string",
   "agreementRevisionId": "string",
   "documentPresignedUrl": "string",
   "executeAgreementToken": "string"
}
```

## Response Elements
<a name="API_GetAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acceptanceTerms](#API_GetAgreement_ResponseSyntax) **   <a name="artifact-GetAgreement-response-acceptanceTerms"></a>
Terms that must be acknowledged in order to accept the given agreement.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`

 ** [acceptanceTermsToken](#API_GetAgreement_ResponseSyntax) **   <a name="artifact-GetAgreement-response-acceptanceTermsToken"></a>
Agreement token that can be used to acknowledge acceptance terms when accepting the given agreement.
Type: String
Pattern: `agreement-token-[a-zA-Z0-9]{24}`

 ** [agreementRevisionId](#API_GetAgreement_ResponseSyntax) **   <a name="artifact-GetAgreement-response-agreementRevisionId"></a>
Revision Id of the agreement.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [documentPresignedUrl](#API_GetAgreement_ResponseSyntax) **   <a name="artifact-GetAgreement-response-documentPresignedUrl"></a>
Presigned S3 url to access the agreement content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [executeAgreementToken](#API_GetAgreement_ResponseSyntax) **   <a name="artifact-GetAgreement-response-executeAgreementToken"></a>
Agreement token that can be used to execute the given agreement.
Type: String
Pattern: `agreement-token-[a-zA-Z0-9]{24}`

## Errors
<a name="API_GetAgreement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unknown server exception has occurred.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** quotaCode **
Code for the affected quota.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
 ** serviceCode **
Code for the affected service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Code for the affected quota.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
Code for the affected service.
HTTP Status Code: 429

 ** ValidationException **
Request fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/GetAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/GetAgreement)
