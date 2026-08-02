---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_TerminateAgreement.html
---

# TerminateAgreement
<a name="API_TerminateAgreement"></a>

Terminate an existing customer-agreement.

## Request Syntax
<a name="API_TerminateAgreement_RequestSyntax"></a>

```
POST /v1/customer-agreement/terminate HTTP/1.1
Content-type: application/json

{
   "customerAgreementId": "{{string}}",
   "terminateAgreementToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TerminateAgreement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TerminateAgreement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [customerAgreementId](#API_TerminateAgreement_RequestSyntax) **   <a name="artifact-TerminateAgreement-request-customerAgreementId"></a>
customer-agreement identifier.
Type: String
Pattern: `customer-agreement-[a-zA-Z0-9]{16}`
Required: Yes

 ** [terminateAgreementToken](#API_TerminateAgreement_RequestSyntax) **   <a name="artifact-TerminateAgreement-request-terminateAgreementToken"></a>
Agreement token for terminating an agreement, received when calling GetCustomerAgreement.
Type: String
Pattern: `agreement-token-[a-zA-Z0-9]{24}`
Required: Yes

## Response Syntax
<a name="API_TerminateAgreement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "customerAgreement": {
      "agreementArn": "string",
      "arn": "string",
      "effectiveEnd": "string",
      "effectiveStart": "string",
      "id": "string",
      "name": "string",
      "state": "string"
   }
}
```

## Response Elements
<a name="API_TerminateAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customerAgreement](#API_TerminateAgreement_ResponseSyntax) **   <a name="artifact-TerminateAgreement-response-customerAgreement"></a>
customer-agreement summary details.
Type: [TerminateCustomerAgreementSummary](API_TerminateCustomerAgreementSummary.md) object

## Errors
<a name="API_TerminateAgreement_Errors"></a>

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
<a name="API_TerminateAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/TerminateAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/TerminateAgreement)
