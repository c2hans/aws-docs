---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_RejectInvitation.html
---

# RejectInvitation
<a name="API_RejectInvitation"></a>

Rejects an invitation to contribute the account data to a behavior graph. This operation must be called by an invited member account that has the `INVITED` status.

 `RejectInvitation` cannot be called by an organization account in the organization behavior graph. In the organization behavior graph, organization accounts do not receive an invitation.

## Request Syntax
<a name="API_RejectInvitation_RequestSyntax"></a>

```
POST /invitation/removal HTTP/1.1
Content-type: application/json

{
   "GraphArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RejectInvitation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RejectInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GraphArn](#API_RejectInvitation_RequestSyntax) **   <a name="detective-RejectInvitation-request-GraphArn"></a>
The ARN of the behavior graph to reject the invitation to.
The member account's current member status in the behavior graph must be `INVITED`.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

## Response Syntax
<a name="API_RejectInvitation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RejectInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RejectInvitation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request attempted an invalid action.
HTTP Status Code: 409

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_RejectInvitation_Examples"></a>

### Example
<a name="API_RejectInvitation_Example_1"></a>

This example illustrates one usage of RejectInvitation.

#### Sample Request
<a name="API_RejectInvitation_Example_1_Request"></a>

```
POST /invitation/removal HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 94
Authorization: AUTHPARAMS
X-Amz-Date: 20200124T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
 "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
}
```

### Example
<a name="API_RejectInvitation_Example_2"></a>

This example illustrates one usage of RejectInvitation.

#### Sample Response
<a name="API_RejectInvitation_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Date: Fri, 24 Jan 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive
```

## See Also
<a name="API_RejectInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/RejectInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/RejectInvitation)
