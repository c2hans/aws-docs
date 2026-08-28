---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_DeleteMembers.html
---

# DeleteMembers
<a name="API_DeleteMembers"></a>

Removes the specified member accounts from the behavior graph. The removed accounts no longer contribute data to the behavior graph. This operation can only be called by the administrator account for the behavior graph.

For invited accounts, the removed accounts are deleted from the list of accounts in the behavior graph. To restore the account, the administrator account must send another invitation.

For organization accounts in the organization behavior graph, the Detective administrator account can always enable the organization account again. Organization accounts that are not enabled as member accounts are not included in the `ListMembers` results for the organization behavior graph.

An administrator account cannot use `DeleteMembers` to remove their own account from the behavior graph. To disable a behavior graph, the administrator account uses the `DeleteGraph` API method.

## Request Syntax
<a name="API_DeleteMembers_RequestSyntax"></a>

```
POST /graph/members/removal HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "GraphArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteMembers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_DeleteMembers_RequestSyntax) **   <a name="detective-DeleteMembers-request-AccountIds"></a>
The list of AWS account identifiers for the member accounts to remove from the behavior graph. You can remove up to 50 member accounts at a time.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: Yes

 ** [GraphArn](#API_DeleteMembers_RequestSyntax) **   <a name="detective-DeleteMembers-request-GraphArn"></a>
The ARN of the behavior graph to remove members from.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

## Response Syntax
<a name="API_DeleteMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountIds": [ "string" ],
   "UnprocessedAccounts": [
      {
         "AccountId": "string",
         "Reason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DeleteMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountIds](#API_DeleteMembers_ResponseSyntax) **   <a name="detective-DeleteMembers-response-AccountIds"></a>
The list of AWS account identifiers for the member accounts that Detective successfully removed from the behavior graph.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`

 ** [UnprocessedAccounts](#API_DeleteMembers_ResponseSyntax) **   <a name="detective-DeleteMembers-response-UnprocessedAccounts"></a>
The list of member accounts that Detective was not able to remove from the behavior graph. For each member account, provides the reason that the deletion could not be processed.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects

## Errors
<a name="API_DeleteMembers_Errors"></a>

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
<a name="API_DeleteMembers_Examples"></a>

### Example
<a name="API_DeleteMembers_Example_1"></a>

This example illustrates one usage of DeleteMembers.

#### Sample Request
<a name="API_DeleteMembers_Example_1_Request"></a>

```
POST /graph/members/removal HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 128
Authorization: AUTHPARAMS
X-Amz-Date: 20200220T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
 "AccountIds": [ "444455556666" ],
 "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
}
```

### Example
<a name="API_DeleteMembers_Example_2"></a>

This example illustrates one usage of DeleteMembers.

#### Sample Response
<a name="API_DeleteMembers_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 63
Date: Thu, 20 Feb 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572

{
 "AccountIds": [ "444455556666" ],
 "UnprocessedAccounts": [ ]
}
```

## See Also
<a name="API_DeleteMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/DeleteMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/DeleteMembers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
