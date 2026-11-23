---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AssociatePublisher.html
---

# AssociatePublisher

Associates a registry record with a publisher and assigns the record a public identifier under the publisher's domain. The registry record must be `APPROVED`, and the publisher must be `ACTIVE`. A registry record can have only one publisher association. The new association starts in `PENDING_APPROVAL` until a curator approves or rejects it by calling `UpdatePublisherAssociationApprovalStatus`.

The request fails with `ConflictException` in these cases:
+ The publisher isn't `ACTIVE`.
+ The registry record already has an association, unless the request repeats the original `clientToken`.
+ Another registry record already uses the same public identifier.

To retry safely, repeat the request with the same `clientToken`. A retry returns the original association. If the publisher has reached its association quota, the request fails with `ServiceQuotaExceededException`. Remove an unused association or request a quota increase. If your account doesn't own the registry record, the request fails with `AccessDeniedException`. If a service that the request depends on is temporarily unavailable, the request fails with `DependencyException`. Retry the request.

## Request Syntax
<a name="API_AssociatePublisher_RequestSyntax"></a>

```
POST /associations HTTP/1.1
Content-type: application/json

{
   "categories": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "publisherArn": "{{string}}",
   "recordArn": "{{string}}",
   "subdomain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociatePublisher_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociatePublisher_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [categories](#API_AssociatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-request-categories"></a>
An optional ordered list of categories to include in the public identifier, after the domain. You can specify up to 8 categories. Each category can be up to 64 characters long and can contain lowercase letters, digits, periods (.), underscores (\_), and hyphens (-).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9._-]+`
Required: No

 ** [clientToken](#API_AssociatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the operation returns the original association instead of creating another one.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [publisherArn](#API_AssociatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-request-publisherArn"></a>
The Amazon Resource Name (ARN) of the publisher to associate the registry record with. The publisher must be `ACTIVE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`
Required: Yes

 ** [recordArn](#API_AssociatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-request-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record to associate with the publisher. The registry record must be `APPROVED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
Required: Yes

 ** [subdomain](#API_AssociatePublisher_RequestSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-request-subdomain"></a>
An optional Domain Name System (DNS) label to place in front of the publisher's domain in the public identifier. For example, `agents` with the domain `example.com` produces the authority `agents.example.com`. If you omit it, the public identifier uses the publisher's domain. The label can contain letters, digits, and hyphens, can't start or end with a hyphen, and can be up to 63 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?`
Required: No

## Response Syntax
<a name="API_AssociatePublisher_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "publicIdentifier": "string",
   "publisher": "string",
   "recordArn": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_AssociatePublisher_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [publicIdentifier](#API_AssociatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-response-publicIdentifier"></a>
The public identifier assigned to the registry record. It has the form `urn:air:authority[:category...]:name[;kind]`:
+  `authority` - The publisher's domain, prefixed by the subdomain if you specified one.
+  `category` - The categories that you specified, if any.
+  `name` - The registry record's name.
+  `kind` - A suffix derived from the record type: `mcp`, `agent`, `skill`, or `webbot`. Gateway records have no suffix.
For example, `urn:air:agents.example.com:finance:weather;mcp`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[uU][rR][nN]:[aA][iI][rR]:([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}:([a-zA-Z0-9._~!$&'()*+,;=:@/-]|%[0-9a-fA-F]{2})+(\?\+([a-zA-Z0-9._~!$&'()*+,;=:@-]|%[0-9a-fA-F]{2})([a-zA-Z0-9._~!$&'()*+,;=:@/?-]|%[0-9a-fA-F]{2})*)?(\?=([a-zA-Z0-9._~!$&'()*+,;=:@-]|%[0-9a-fA-F]{2})([a-zA-Z0-9._~!$&'()*+,;=:@/?-]|%[0-9a-fA-F]{2})*)?(#([a-zA-Z0-9._~!$&'()*+,;=:@/?-]|%[0-9a-fA-F]{2})*)?`

 ** [publisher](#API_AssociatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-response-publisher"></a>
The Amazon Resource Name (ARN) of the publisher that the registry record is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`

 ** [recordArn](#API_AssociatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-response-recordArn"></a>
The Amazon Resource Name (ARN) of the associated registry record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`

 ** [status](#API_AssociatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-response-status"></a>
The status of the association. A newly created association is `PENDING_APPROVAL`. A retry with the original `clientToken` returns the association's current status, which is one of the following:
+  `PENDING_APPROVAL` - The association is waiting for a curator to approve or reject it.
+  `APPROVED` - A curator approved the association.
+  `REJECTED` - A curator rejected the association.
+  `SUSPENDED` - The association was approved but is suspended, for example because the publisher's domain could no longer be verified. `statusReason`, when present, describes why.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | SUSPENDED`

 ** [statusReason](#API_AssociatePublisher_ResponseSyntax) **   <a name="agentregistrycontrol-AssociatePublisher-response-statusReason"></a>
The reason for the association's current status. Present only when a reason is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\P{C}\t\r\n]*`

## Errors
<a name="API_AssociatePublisher_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

 ** DependencyException **
A service that the request depends on returned an error or was unavailable. Retry the request.
HTTP Status Code: 503

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
<a name="API_AssociatePublisher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/AssociatePublisher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AssociatePublisher)
