---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetPullRequestApprovalStates.html
---

# GetPullRequestApprovalStates
<a name="API_GetPullRequestApprovalStates"></a>

Gets information about the approval states for a specified pull request. Approval states only apply to pull requests that have one or more approval rules applied to them.

## Request Syntax
<a name="API_GetPullRequestApprovalStates_RequestSyntax"></a>

```
{
   "pullRequestId": "{{string}}",
   "revisionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPullRequestApprovalStates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pullRequestId](#API_GetPullRequestApprovalStates_RequestSyntax) **   <a name="CodeCommit-GetPullRequestApprovalStates-request-pullRequestId"></a>
The system-generated ID for the pull request.
Type: String
Required: Yes

 ** [revisionId](#API_GetPullRequestApprovalStates_RequestSyntax) **   <a name="CodeCommit-GetPullRequestApprovalStates-request-revisionId"></a>
The system-generated ID for the pull request revision.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetPullRequestApprovalStates_ResponseSyntax"></a>

```
{
   "approvals": [
      {
         "approvalState": "string",
         "userArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetPullRequestApprovalStates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvals](#API_GetPullRequestApprovalStates_ResponseSyntax) **   <a name="CodeCommit-GetPullRequestApprovalStates-response-approvals"></a>
Information about users who have approved the pull request.
Type: Array of [Approval](API_Approval.md) objects

## Errors
<a name="API_GetPullRequestApprovalStates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidRevisionIdException **
The revision ID is not valid. Use GetPullRequest to determine the value.
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

## Examples
<a name="API_GetPullRequestApprovalStates_Examples"></a>

### Example
<a name="API_GetPullRequestApprovalStates_Example_1"></a>

This example illustrates one usage of GetPullRequestApprovalStates.

#### Sample Request
<a name="API_GetPullRequestApprovalStates_Example_1_Request"></a>

```
>>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.GetPullRequestApprovalStates
X-Amz-Date: 20191021T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "8",
   "revisionId": "9f29d1673EXAMPLE"
}
```

#### Sample Response
<a name="API_GetPullRequestApprovalStates_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Mon, 21 Oct 2019 20:20:13 GMT

{
    "approvals": [
        {
            "userArn": "arn:aws:iam::123456789012:user/Mary_Major",
            "approvalState": "APPROVE"
        }
    ]
}
```

## See Also
<a name="API_GetPullRequestApprovalStates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetPullRequestApprovalStates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetPullRequestApprovalStates)
