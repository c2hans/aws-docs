---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_ListTrustStoreCertificates.html
---

# ListTrustStoreCertificates
<a name="API_ListTrustStoreCertificates"></a>

Retrieves a list of trust store certificates.

## Request Syntax
<a name="API_ListTrustStoreCertificates_RequestSyntax"></a>

```
GET /trustStores/{{trustStoreArn+}}/certificates?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrustStoreCertificates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTrustStoreCertificates_RequestSyntax) **   <a name="workspacesweb-ListTrustStoreCertificates-request-uri-maxResults"></a>
The maximum number of results to be included in the next page.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_ListTrustStoreCertificates_RequestSyntax) **   <a name="workspacesweb-ListTrustStoreCertificates-request-uri-nextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [trustStoreArn](#API_ListTrustStoreCertificates_RequestSyntax) **   <a name="workspacesweb-ListTrustStoreCertificates-request-uri-trustStoreArn"></a>
The ARN of the trust store
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

## Request Body
<a name="API_ListTrustStoreCertificates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrustStoreCertificates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateList": [
      {
         "issuer": "string",
         "notValidAfter": number,
         "notValidBefore": number,
         "subject": "string",
         "thumbprint": "string"
      }
   ],
   "nextToken": "string",
   "trustStoreArn": "string"
}
```

## Response Elements
<a name="API_ListTrustStoreCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateList](#API_ListTrustStoreCertificates_ResponseSyntax) **   <a name="workspacesweb-ListTrustStoreCertificates-response-certificateList"></a>
The certificate list.
Type: Array of [CertificateSummary](API_CertificateSummary.md) objects

 ** [nextToken](#API_ListTrustStoreCertificates_ResponseSyntax) **   <a name="workspacesweb-ListTrustStoreCertificates-response-nextToken"></a>
The pagination token used to retrieve the next page of results for this operation.>
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [trustStoreArn](#API_ListTrustStoreCertificates_ResponseSyntax) **   <a name="workspacesweb-ListTrustStoreCertificates-response-trustStoreArn"></a>
The ARN of the trust store.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`

## Errors
<a name="API_ListTrustStoreCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
There is an internal server error.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource cannot be found.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
There is a throttling error.
 ** quotaCode **
The originating quota.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
 ** serviceCode **
The originating service.
HTTP Status Code: 429

 ** ValidationException **
There is a validation error.
 ** fieldList **
The field that caused the error.
 ** reason **
Reason the request failed validation
HTTP Status Code: 400

## See Also
<a name="API_ListTrustStoreCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/ListTrustStoreCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/ListTrustStoreCertificates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
