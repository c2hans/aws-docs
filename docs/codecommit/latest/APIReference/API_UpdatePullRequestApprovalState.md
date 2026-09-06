---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestApprovalState.html
---

# UpdatePullRequestApprovalState
<a name="API_UpdatePullRequestApprovalState"></a>

Updates the state of a user's approval on a pull request. The user is derived from the signed-in account when the request is made.

## Request Syntax
<a name="API_UpdatePullRequestApprovalState_RequestSyntax"></a>

```
{
   "approvalState": "{{string}}",
   "pullRequestId": "{{string}}",
   "revisionId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePullRequestApprovalState_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalState](#API_UpdatePullRequestApprovalState_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalState-request-approvalState"></a>
The approval state to associate with the user on the pull request.
Type: String
Valid Values: `APPROVE | REVOKE`
Required: Yes

 ** [pullRequestId](#API_UpdatePullRequestApprovalState_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalState-request-pullRequestId"></a>
The system-generated ID of the pull request.
Type: String
Required: Yes

 ** [revisionId](#API_UpdatePullRequestApprovalState_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalState-request-revisionId"></a>
The system-generated ID of the revision.
Type: String
Required: Yes

## Response Elements
<a name="API_UpdatePullRequestApprovalState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePullRequestApprovalState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalStateRequiredException **
An approval state is required, but was not specified.
HTTP Status Code: 400

 ** EncryptionIntegrityChecksFailedException **
An encryption integrity check failed.
HTTP Status Code: 500

 ** EncryptionKeyAccessDeniedException **
An encryption key could not be accessed.
HTTP Status Code: 400

 ** EncryptionKeyDisabledException **
The encryption key is disabled.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidApprovalStateException **
The state for the approval is not valid. Valid values include APPROVE and REVOKE.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidRevisionIdException **
The revision ID is not valid. Use GetPullRequest to determine the value.
HTTP Status Code: 400

 ** MaximumNumberOfApprovalsExceededException **
The number of approvals required for the approval rule exceeds the maximum number allowed.
HTTP Status Code: 400

 ** PullRequestAlreadyClosedException **
The pull request status cannot be updated because it is already closed.
HTTP Status Code: 400

 ** PullRequestCannotBeApprovedByAuthorException **
The approval cannot be applied because the user approving the pull request matches the user who created the pull request. You cannot approve a pull request that you created.
HTTP Status Code: 400

 ** PullRequestDoesNotExistException **
The pull request ID could not be found. Make sure that you have specified the correct repository name and pull request ID, and then try again.
HTTP Status Code: 400

 ** PullRequestIdRequiredException **
A pull request ID is required, but none was provided.
HTTP Status Code: 400

 ** RevisionIdRequiredException **
A revision ID is required, but was not provided.
HTTP Status Code: 400

 ** RevisionNotCurrentException **
The revision ID provided in the request does not match the current revision ID. Use GetPullRequest to retrieve the current revision ID.
HTTP Status Code: 400

## Examples
<a name="API_UpdatePullRequestApprovalState_Examples"></a>

### Example
<a name="API_UpdatePullRequestApprovalState_Example_1"></a>

This example illustrates one usage of UpdatePullRequestApprovalState.

#### Sample Request
<a name="API_UpdatePullRequestApprovalState_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdatePullRequestApprovalRuleState
X-Amz-Date: 20191025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "27",
   "revisionId": "9f29d167EXAMPLE",
   "approvalState": "APPROVE"
}
```

#### Sample Response
<a name="API_UpdatePullRequestApprovalState_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Fri, 25 Oct 2019 20:20:13 GMT
```

## See Also
<a name="API_UpdatePullRequestApprovalState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdatePullRequestApprovalState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdatePullRequestApprovalState)
