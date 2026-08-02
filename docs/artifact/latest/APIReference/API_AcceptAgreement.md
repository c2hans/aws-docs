---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptAgreement.html
---

# AcceptAgreement
<a name="API_AcceptAgreement"></a>

Accept an agreement.

## Request Syntax
<a name="API_AcceptAgreement_RequestSyntax"></a>

```
POST /v1/agreement/accept HTTP/1.1
Content-type: application/json

{
   "acceptanceTermsToken": "{{string}}",
   "agreementId": "{{string}}",
   "agreementRevisionId": "{{string}}",
   "executeAgreementToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptAgreement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AcceptAgreement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [acceptanceTermsToken](#API_AcceptAgreement_RequestSyntax) **   <a name="artifact-AcceptAgreement-request-acceptanceTermsToken"></a>
Agreement token for acknowledging acceptance terms of the agreement, received when calling GetAgreement.
Type: String
Pattern: `agreement-token-[a-zA-Z0-9]{24}`
Required: Yes

 ** [agreementId](#API_AcceptAgreement_RequestSyntax) **   <a name="artifact-AcceptAgreement-request-agreementId"></a>
Agreement identifier.
Type: String
Pattern: `agreement-[a-zA-Z0-9]{16}`
Required: Yes

 ** [agreementRevisionId](#API_AcceptAgreement_RequestSyntax) **   <a name="artifact-AcceptAgreement-request-agreementRevisionId"></a>
Revision Id received when calling GetAgreement.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [executeAgreementToken](#API_AcceptAgreement_RequestSyntax) **   <a name="artifact-AcceptAgreement-request-executeAgreementToken"></a>
Agreement token for executing an agreement, received when calling GetAgreement.
Type: String
Pattern: `agreement-token-[a-zA-Z0-9]{24}`
Required: Yes

## Response Syntax
<a name="API_AcceptAgreement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "customerAgreement": {
      "acceptanceTerms": [ "string" ],
      "agreementArn": "string",
      "arn": "string",
      "awsAccountId": "string",
      "description": "string",
      "effectiveEnd": "string",
      "effectiveStart": "string",
      "id": "string",
      "name": "string",
      "organizationArn": "string",
      "state": "string",
      "terminateTerms": [ "string" ],
      "type": "string"
   }
}
```

## Response Elements
<a name="API_AcceptAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customerAgreement](#API_AcceptAgreement_ResponseSyntax) **   <a name="artifact-AcceptAgreement-response-customerAgreement"></a>
customer-agreement summary details.
Type: [CustomerAgreementSummary](API_CustomerAgreementSummary.md) object

## Errors
<a name="API_AcceptAgreement_Errors"></a>

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
<a name="API_AcceptAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/AcceptAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/AcceptAgreement)
