---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListCustomerAgreements.html
---

# ListCustomerAgreements
<a name="API_ListCustomerAgreements"></a>

List active customer-agreements applicable to calling identity.

## Request Syntax
<a name="API_ListCustomerAgreements_RequestSyntax"></a>

```
GET /v1/customer-agreement/list?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCustomerAgreements_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCustomerAgreements_RequestSyntax) **   <a name="artifact-ListCustomerAgreements-request-uri-maxResults"></a>
Maximum number of resources to return in the paginated response.
Valid Range: Minimum value of 1. Maximum value of 300.

 ** [nextToken](#API_ListCustomerAgreements_RequestSyntax) **   <a name="artifact-ListCustomerAgreements-request-uri-nextToken"></a>
Pagination token to request the next page of resources.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListCustomerAgreements_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCustomerAgreements_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "customerAgreements": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomerAgreements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customerAgreements](#API_ListCustomerAgreements_ResponseSyntax) **   <a name="artifact-ListCustomerAgreements-response-customerAgreements"></a>
List of customer-agreement resources.
Type: Array of [CustomerAgreementSummary](API_CustomerAgreementSummary.md) objects

 ** [nextToken](#API_ListCustomerAgreements_ResponseSyntax) **   <a name="artifact-ListCustomerAgreements-response-nextToken"></a>
Pagination token to request the next page of resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListCustomerAgreements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unknown server exception has occurred.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

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
<a name="API_ListCustomerAgreements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/ListCustomerAgreements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ListCustomerAgreements)
