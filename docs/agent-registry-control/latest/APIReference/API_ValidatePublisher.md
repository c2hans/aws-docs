---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ValidatePublisher.html
---

# ValidatePublisher

Restarts domain verification for a publisher that is `FAILED` or `SUSPENDED`. The publisher returns to `ACTION_REQUIRED` with a new `domainChallenge`, which the response includes. Update the Domain Name System (DNS) TXT record with the new `recordValue`. The previous value no longer verifies the domain. The request fails with `ConflictException` if the publisher is `ACTIVE`, verification is already in progress (`ACTION_REQUIRED`), or the publisher is being deleted.

## Request Syntax
<a name="API_ValidatePublisher_RequestSyntax"></a>

```
POST /publishers/{{publisherArn}}/verification HTTP/1.1
```

## URI Request Parameters
<a name="API_ValidatePublisher_RequestParameters"></a>

The request uses the following URI parameters.

 ** [publisherArn](#API_ValidatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-request-uri-publisherArn"></a>
The Amazon Resource Name (ARN) of the publisher to verify again.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`
Required: Yes

## Request Body
<a name="API_ValidatePublisher_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ValidatePublisher_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_ValidatePublisher_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-createdAt"></a>
The date and time that the publisher was created.
Type: Timestamp

 ** [domainChallenge](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-domainChallenge"></a>
The new DNS TXT record to create to verify that you control the publisher's domain.
Type: [DomainChallenge](API_DomainChallenge.md) object

 ** [identifierType](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-identifierType"></a>
The type of the publisher's identifier. `DOMAIN` is the only supported value.
Type: String
Valid Values: `DOMAIN`

 ** [publisherArn](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-publisherArn"></a>
The Amazon Resource Name (ARN) of the publisher.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`

 ** [status](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-status"></a>
The domain verification status of the publisher. After verification restarts, the status is `ACTION_REQUIRED`.
Type: String
Valid Values: `ACTION_REQUIRED | ACTIVE | FAILED | SUSPENDED | DELETING`

 ** [statusReason](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-statusReason"></a>
The reason for the publisher's current status. Present only when a reason is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\P{C}\t\r\n]*`

 ** [tags](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-tags"></a>
The tags attached to the publisher.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`

 ** [updatedAt](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-updatedAt"></a>
The date and time that the publisher was last updated.
Type: Timestamp

 ** [value](#API_ValidatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-ValidatePublisher-response-value"></a>
The domain that the publisher represents.
Type: [Identifier](API_Identifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_ValidatePublisher_Errors"></a>

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
<a name="API_ValidatePublisher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/ValidatePublisher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ValidatePublisher)
