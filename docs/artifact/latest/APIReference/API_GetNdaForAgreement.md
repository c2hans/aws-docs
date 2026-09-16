---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetNdaForAgreement.html
---

# GetNdaForAgreement
<a name="API_GetNdaForAgreement"></a>

Retrieve the NDA document for an agreement.

## Request Syntax
<a name="API_GetNdaForAgreement_RequestSyntax"></a>

```
GET /v1/agreement/getNdaForAgreement?agreementId={{agreementId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNdaForAgreement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agreementId](#API_GetNdaForAgreement_RequestSyntax) **   <a name="artifact-GetNdaForAgreement-request-uri-agreementId"></a>
Agreement identifier.
Pattern: `agreement-[a-zA-Z0-9]{16}`
Required: Yes

## Request Body
<a name="API_GetNdaForAgreement_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNdaForAgreement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "acceptNdaForAgreementToken": "string",
   "agreementRevisionId": "string",
   "documentPresignedUrl": "string"
}
```

## Response Elements
<a name="API_GetNdaForAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acceptNdaForAgreementToken](#API_GetNdaForAgreement_ResponseSyntax) **   <a name="artifact-GetNdaForAgreement-response-acceptNdaForAgreementToken"></a>
NDA token that can be used to accept the NDA retrieved.
Type: String
Pattern: `nda-token-[a-zA-Z0-9]{24}`

 ** [agreementRevisionId](#API_GetNdaForAgreement_ResponseSyntax) **   <a name="artifact-GetNdaForAgreement-response-agreementRevisionId"></a>
Revision Id of the current NDA for the given agreement.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [documentPresignedUrl](#API_GetNdaForAgreement_ResponseSyntax) **   <a name="artifact-GetNdaForAgreement-response-documentPresignedUrl"></a>
Presigned S3 url to access the NDA content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Errors
<a name="API_GetNdaForAgreement_Errors"></a>

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
<a name="API_GetNdaForAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/GetNdaForAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/GetNdaForAgreement)
