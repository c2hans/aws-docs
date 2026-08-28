---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateInboundExternalLink.html
---

# CreateInboundExternalLink
<a name="API_CreateInboundExternalLink"></a>

Creates an inbound external link.

## Request Syntax
<a name="API_CreateInboundExternalLink_RequestSyntax"></a>

```
POST /responder-gateway/{{gatewayId}}/inbound-external-link HTTP/1.1
Content-type: application/json

{
   "attributes": {
      "customerProvidedId": "{{string}}",
      "responderErrorMasking": [
         {
            "action": "{{string}}",
            "httpCode": "{{string}}",
            "loggingTypes": [ "{{string}}" ],
            "responseLoggingPercentage": {{number}}
         }
      ]
   },
   "clientToken": "{{string}}",
   "logSettings": {
      "applicationLogs": {
         "sampling": {
            "errorLog": {{number}},
            "filterLog": {{number}}
         }
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateInboundExternalLink_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_CreateInboundExternalLink_RequestSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_CreateInboundExternalLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_CreateInboundExternalLink_RequestSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-request-attributes"></a>
Attributes of the link.
Type: [LinkAttributes](API_LinkAttributes.md) object
Required: No

 ** [clientToken](#API_CreateInboundExternalLink_RequestSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `clientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: Yes

 ** [logSettings](#API_CreateInboundExternalLink_RequestSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-request-logSettings"></a>
Settings for the application logs.
Type: [LinkLogSettings](API_LinkLogSettings.md) object
Required: Yes

 ** [tags](#API_CreateInboundExternalLink_RequestSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-request-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.
Required: No

## Response Syntax
<a name="API_CreateInboundExternalLink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainName": "string",
   "gatewayId": "string",
   "linkId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateInboundExternalLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainName](#API_CreateInboundExternalLink_ResponseSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-response-domainName"></a>
The domain name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`

 ** [gatewayId](#API_CreateInboundExternalLink_ResponseSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [linkId](#API_CreateInboundExternalLink_ResponseSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-response-linkId"></a>
The unique identifier of the link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`

 ** [status](#API_CreateInboundExternalLink_ResponseSyntax) **   <a name="rtbfabric-CreateInboundExternalLink-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | PENDING_REQUEST | REQUESTED | ACCEPTED | ACTIVE | REJECTED | FAILED | PENDING_DELETION | DELETED | PENDING_UPDATE | PENDING_ISOLATION | ISOLATED | PENDING_RESTORATION`

## Errors
<a name="API_CreateInboundExternalLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request could not be completed because you exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_CreateInboundExternalLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/CreateInboundExternalLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/CreateInboundExternalLink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
