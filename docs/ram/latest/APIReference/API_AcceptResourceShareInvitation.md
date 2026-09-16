---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html
---

# AcceptResourceShareInvitation
<a name="API_AcceptResourceShareInvitation"></a>

Accepts an invitation to a resource share from another AWS account. After you accept the invitation, the resources included in the resource share are available to interact with in the relevant AWS Management Consoles and tools.

## Request Syntax
<a name="API_AcceptResourceShareInvitation_RequestSyntax"></a>

```
POST /acceptresourceshareinvitation HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "resourceShareInvitationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptResourceShareInvitation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AcceptResourceShareInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceShareInvitationArn](#API_AcceptResourceShareInvitation_RequestSyntax) **   <a name="ram-AcceptResourceShareInvitation-request-resourceShareInvitationArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the invitation that you want to accept.
Type: String
Required: Yes

 ** [clientToken](#API_AcceptResourceShareInvitation_RequestSyntax) **   <a name="ram-AcceptResourceShareInvitation-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

## Response Syntax
<a name="API_AcceptResourceShareInvitation_ResponseSyntax"></a>

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
<a name="API_AcceptResourceShareInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_AcceptResourceShareInvitation_ResponseSyntax) **   <a name="ram-AcceptResourceShareInvitation-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [resourceShareInvitation](#API_AcceptResourceShareInvitation_ResponseSyntax) **   <a name="ram-AcceptResourceShareInvitation-response-resourceShareInvitation"></a>
An object that contains information about the specified invitation.
Type: [ResourceShareInvitation](API_ResourceShareInvitation.md) object

## Errors
<a name="API_AcceptResourceShareInvitation_Errors"></a>

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

## Examples
<a name="API_AcceptResourceShareInvitation_Examples"></a>

**Note**
The examples show the JSON payloads of the request and response pretty printed with white spaces and line breaks for ease for ease of reading.

###
<a name="API_AcceptResourceShareInvitation_Example_1"></a>

The following example shows the AWS account 111111111111 accepting a resource share invitation for a resource share that is in the AWS Region `us-east-1` and was from 999999999999.

#### Sample Request
<a name="API_AcceptResourceShareInvitation_Example_1_Request"></a>

```
POST /acceptresourceshareinvitation HTTP/1.1
Host: ram.us-east-1.amazonaws.com (http://ram.us-east-1.amazonaws.com/)
X-Amz-Date: 20210922T220735Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>>

{"resourceShareInvitationArn": "arn:aws:ram:us-east-1:999999999999:resource-share-invitation/1e3477be-4a95-46b4-bbe0-c400156cd8e6"}
```

#### Sample Response
<a name="API_AcceptResourceShareInvitation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 22 Sep 2021 22:07:35 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "resourceShareInvitation": {
        "invitationTimestamp": 1632348455.62,
        "receiverAccountId": "111111111111",
        "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2",
        "resourceShareInvitationArn": "arn:aws:ram:us-east-1:999999999999:resource-share-invitation/1e3477be-4a95-46b4-bbe0-c400156cd8e6",
        "resourceShareName": "MyLicenseShare",
        "senderAccountId": "999999999999",
        "status": "ACCEPTED"
    }
}
```

## See Also
<a name="API_AcceptResourceShareInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/AcceptResourceShareInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/AcceptResourceShareInvitation)
