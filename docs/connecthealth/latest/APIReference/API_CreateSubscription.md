---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateSubscription.html
---

# CreateSubscription
<a name="API_CreateSubscription"></a>

Creates a new Subscription within a Domain for billing and user management.

## Request Syntax
<a name="API_CreateSubscription_RequestSyntax"></a>

```
POST /domains/{{domainId}}/subscriptions HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_CreateSubscription_RequestSyntax) **   <a name="connecthealth-CreateSubscription-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateSubscription_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "activatedAt": number,
   "arn": "string",
   "createdAt": number,
   "deactivatedAt": number,
   "domainId": "string",
   "lastUpdatedAt": number,
   "status": "string",
   "subscriptionId": "string"
}
```

## Response Elements
<a name="API_CreateSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [activatedAt](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-activatedAt"></a>

Type: Timestamp

 ** [arn](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-arn"></a>

Type: String
Pattern: `arn:aws:health-agent:[a-z0-9-]+:[0-9]{12}:domain/(hai-|dom-)[a-z0-9]+/subscription/sub-[a-zA-Z0-9]{21}`

 ** [createdAt](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-createdAt"></a>

Type: Timestamp

 ** [deactivatedAt](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-deactivatedAt"></a>

Type: Timestamp

 ** [domainId](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-domainId"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`

 ** [lastUpdatedAt](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-lastUpdatedAt"></a>

Type: Timestamp

 ** [status](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-status"></a>

Type: String
Valid Values: `ACTIVE | INACTIVE | DELETED`

 ** [subscriptionId](#API_CreateSubscription_ResponseSyntax) **   <a name="connecthealth-CreateSubscription-response-subscriptionId"></a>

Type: String
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`

## Errors
<a name="API_CreateSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_CreateSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/CreateSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/CreateSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
