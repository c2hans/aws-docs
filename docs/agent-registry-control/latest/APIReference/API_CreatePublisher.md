---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CreatePublisher.html
---

# CreatePublisher

Creates a publisher for a domain that you control. A publisher lets you assign public identifiers under your domain to registry records. The publisher starts in `ACTION_REQUIRED`, and the response includes a `domainChallenge`. To verify that you control the domain, create a Domain Name System (DNS) TXT record with the challenge's `recordName` and `recordValue`. When the registry finds the record, the publisher becomes `ACTIVE` and you can associate registry records with it by calling `AssociatePublisher`.

Your account can have one publisher for each domain. Creating a second publisher for the same domain fails with `ConflictException`, unless the request repeats the original `clientToken`, which returns the existing publisher. The request also fails with `ConflictException` if another account has already verified the domain. If your account has reached its publisher quota, the request fails with `ServiceQuotaExceededException`. Delete an unused publisher or request a quota increase.

## Request Syntax
<a name="API_CreatePublisher_RequestSyntax"></a>

```
POST /publishers HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "value": { ... }
}
```

## URI Request Parameters
<a name="API_CreatePublisher_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePublisher_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-CreatePublisher-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the operation returns the original publisher instead of creating another one.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [tags](#API_CreatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-CreatePublisher-request-tags"></a>
The tags to attach to the publisher. Each tag is a key-value pair. You can attach up to 50 tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Required: No

 ** [value](#API_CreatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-CreatePublisher-request-value"></a>
The domain that the publisher represents.
Type: [Identifier](API_Identifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreatePublisher_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": number,
   "domainChallenge": {
      "recordName": "string",
      "recordValue": "string"
   },
   "identifierType": "string",
   "publisherArn": "string",
   "status": "string",
   "statusReason": "string",
   "tags": {
      "string" : "string"
   },
   "updatedAt": number,
   "value": { ... }
}
```

## Response Elements
<a name="API_CreatePublisher_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-createdAt"></a>
The date and time that the publisher was created.
Type: Timestamp

 ** [domainChallenge](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-domainChallenge"></a>
The DNS TXT record to create to verify that you control the publisher's domain.
Type: [DomainChallenge](API_DomainChallenge.md) object

 ** [identifierType](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-identifierType"></a>
The type of the publisher's identifier. `DOMAIN` is the only supported value.
Type: String
Valid Values: `DOMAIN`

 ** [publisherArn](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-publisherArn"></a>
The Amazon Resource Name (ARN) of the publisher.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`

 ** [status](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-status"></a>
The domain verification status of the publisher. A newly created publisher is `ACTION_REQUIRED`. A retry with the original `clientToken` returns the publisher's current status.
Type: String
Valid Values: `ACTION_REQUIRED | ACTIVE | FAILED | SUSPENDED | DELETING`

 ** [statusReason](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-statusReason"></a>
The reason for the publisher's current status. Present only when a reason is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\P{C}\t\r\n]*`

 ** [tags](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-tags"></a>
The tags attached to the publisher.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`

 ** [updatedAt](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-updatedAt"></a>
The date and time that the publisher was last updated.
Type: Timestamp

 ** [value](#API_CreatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-CreatePublisher-response-value"></a>
The domain that the publisher represents.
Type: [Identifier](API_Identifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_CreatePublisher_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would exceed a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreatePublisher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/CreatePublisher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CreatePublisher)
