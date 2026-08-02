---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetCustomerAgreement.html
---

# GetCustomerAgreement
<a name="API_GetCustomerAgreement"></a>

Retrieve a customer-agreement document.

## Request Syntax
<a name="API_GetCustomerAgreement_RequestSyntax"></a>

```
GET /v1/customer-agreement/get?customerAgreementId={{customerAgreementId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCustomerAgreement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [customerAgreementId](#API_GetCustomerAgreement_RequestSyntax) **   <a name="artifact-GetCustomerAgreement-request-uri-customerAgreementId"></a>
customer-agreement identifier.
Pattern: `customer-agreement-[a-zA-Z0-9]{16}`
Required: Yes

## Request Body
<a name="API_GetCustomerAgreement_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCustomerAgreement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentPresignedUrl": "string",
   "terminateAgreementToken": "string",
   "terminateTerms": [ "string" ]
}
```

## Response Elements
<a name="API_GetCustomerAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentPresignedUrl](#API_GetCustomerAgreement_ResponseSyntax) **   <a name="artifact-GetCustomerAgreement-response-documentPresignedUrl"></a>
Presigned S3 url to access the customer-agreement content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [terminateAgreementToken](#API_GetCustomerAgreement_ResponseSyntax) **   <a name="artifact-GetCustomerAgreement-response-terminateAgreementToken"></a>
Agreement token that can be used to terminate this customer-agreement.
Type: String
Pattern: `agreement-token-[a-zA-Z0-9]{24}`

 ** [terminateTerms](#API_GetCustomerAgreement_ResponseSyntax) **   <a name="artifact-GetCustomerAgreement-response-terminateTerms"></a>
Terms that must be acknowledged in order to terminate the given agreement.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`

## Errors
<a name="API_GetCustomerAgreement_Errors"></a>

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
<a name="API_GetCustomerAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/GetCustomerAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/GetCustomerAgreement)
