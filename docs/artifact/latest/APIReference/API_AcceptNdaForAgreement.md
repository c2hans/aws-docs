---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptNdaForAgreement.html
---

# AcceptNdaForAgreement
<a name="API_AcceptNdaForAgreement"></a>

Accept the NDA document for an agreement.

## Request Syntax
<a name="API_AcceptNdaForAgreement_RequestSyntax"></a>

```
POST /v1/agreement/acceptNdaForAgreement HTTP/1.1
Content-type: application/json

{
   "agreementId": "{{string}}",
   "agreementRevisionId": "{{string}}",
   "ndaToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptNdaForAgreement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AcceptNdaForAgreement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agreementId](#API_AcceptNdaForAgreement_RequestSyntax) **   <a name="artifact-AcceptNdaForAgreement-request-agreementId"></a>
Agreement identifier.
Type: String
Pattern: `agreement-[a-zA-Z0-9]{16}`
Required: Yes

 ** [agreementRevisionId](#API_AcceptNdaForAgreement_RequestSyntax) **   <a name="artifact-AcceptNdaForAgreement-request-agreementRevisionId"></a>
Revision Id received when calling GetNdaForAgreement.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [ndaToken](#API_AcceptNdaForAgreement_RequestSyntax) **   <a name="artifact-AcceptNdaForAgreement-request-ndaToken"></a>
NDA token received when calling GetNdaForAgreement.
Type: String
Pattern: `nda-token-[a-zA-Z0-9]{24}`
Required: Yes

## Response Syntax
<a name="API_AcceptNdaForAgreement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "getAgreementToken": "string"
}
```

## Response Elements
<a name="API_AcceptNdaForAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [getAgreementToken](#API_AcceptNdaForAgreement_ResponseSyntax) **   <a name="artifact-AcceptNdaForAgreement-response-getAgreementToken"></a>
NDA token that can be used to Get the agreement document.
Type: String
Pattern: `nda-token-[a-zA-Z0-9]{24}`

## Errors
<a name="API_AcceptNdaForAgreement_Errors"></a>

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
<a name="API_AcceptNdaForAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/AcceptNdaForAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/AcceptNdaForAgreement)
