---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_RejectResourceShareInvitation.html
---

# RejectResourceShareInvitation
<a name="API_RejectResourceShareInvitation"></a>

Rejects an invitation to a resource share from another AWS account.

## Request Syntax
<a name="API_RejectResourceShareInvitation_RequestSyntax"></a>

```
POST /rejectresourceshareinvitation HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "resourceShareInvitationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RejectResourceShareInvitation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RejectResourceShareInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceShareInvitationArn](#API_RejectResourceShareInvitation_RequestSyntax) **   <a name="ram-RejectResourceShareInvitation-request-resourceShareInvitationArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the invitation that you want to reject.
Type: String
Required: Yes

 ** [clientToken](#API_RejectResourceShareInvitation_RequestSyntax) **   <a name="ram-RejectResourceShareInvitation-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

## Response Syntax
<a name="API_RejectResourceShareInvitation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "resourceShareInvitation": {
      "invitationTimestamp": number,
      "receiverAccountId": "string",
      "receiverArn": "string",
      "resourceShareArn": "string",
      "resourceShareAssociations": [
         {
            "associatedEntity": "string",
            "associationType": "string",
            "creationTime": number,
            "external": boolean,
            "lastUpdatedTime": number,
            "resourceShareArn": "string",
            "resourceShareName": "string",
            "status": "string",
            "statusMessage": "string"
         }
      ],
      "resourceShareInvitationArn": "string",
      "resourceShareName": "string",
      "senderAccountId": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_RejectResourceShareInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_RejectResourceShareInvitation_ResponseSyntax) **   <a name="ram-RejectResourceShareInvitation-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [resourceShareInvitation](#API_RejectResourceShareInvitation_ResponseSyntax) **   <a name="ram-RejectResourceShareInvitation-response-resourceShareInvitation"></a>
An object that contains the details about the rejected invitation.
Type: [ResourceShareInvitation](API_ResourceShareInvitation.md) object

## Errors
<a name="API_RejectResourceShareInvitation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.
HTTP Status Code: 400

 ** InvalidClientTokenException **
The operation failed because the specified client token isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ResourceShareInvitationAlreadyAcceptedException **
The operation failed because the specified invitation was already accepted.
HTTP Status Code: 400

 ** ResourceShareInvitationAlreadyRejectedException **
The operation failed because the specified invitation was already rejected.
HTTP Status Code: 400

 ** ResourceShareInvitationArnNotFoundException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for an invitation was not found.
HTTP Status Code: 400

 ** ResourceShareInvitationExpiredException **
The operation failed because the specified invitation is past its expiration date and time.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

## See Also
<a name="API_RejectResourceShareInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/RejectResourceShareInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/RejectResourceShareInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
