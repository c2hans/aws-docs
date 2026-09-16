---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_OverridePullRequestApprovalRules.html
---

# OverridePullRequestApprovalRules
<a name="API_OverridePullRequestApprovalRules"></a>

Sets aside (overrides) all approval rule requirements for a specified pull request.

## Request Syntax
<a name="API_OverridePullRequestApprovalRules_RequestSyntax"></a>

```
{
   "overrideStatus": "{{string}}",
   "pullRequestId": "{{string}}",
   "revisionId": "{{string}}"
}
```

## Request Parameters
<a name="API_OverridePullRequestApprovalRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [overrideStatus](#API_OverridePullRequestApprovalRules_RequestSyntax) **   <a name="CodeCommit-OverridePullRequestApprovalRules-request-overrideStatus"></a>
Whether you want to set aside approval rule requirements for the pull request (OVERRIDE) or revoke a previous override and apply approval rule requirements (REVOKE). REVOKE status is not stored.
Type: String
Valid Values: `OVERRIDE | REVOKE`
Required: Yes

 ** [pullRequestId](#API_OverridePullRequestApprovalRules_RequestSyntax) **   <a name="CodeCommit-OverridePullRequestApprovalRules-request-pullRequestId"></a>
The system-generated ID of the pull request for which you want to override all approval rule requirements. To get this information, use [GetPullRequest](API_GetPullRequest.md).
Type: String
Required: Yes

 ** [revisionId](#API_OverridePullRequestApprovalRules_RequestSyntax) **   <a name="CodeCommit-OverridePullRequestApprovalRules-request-revisionId"></a>
The system-generated ID of the most recent revision of the pull request. You cannot override approval rules for anything but the most recent revision of a pull request. To get the revision ID, use GetPullRequest.
Type: String
Required: Yes

## Response Elements
<a name="API_OverridePullRequestApprovalRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_OverridePullRequestApprovalRules_Errors"></a>

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

 ** InvalidOverrideStatusException **
The override status is not valid. Valid statuses are OVERRIDE and REVOKE.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidRevisionIdException **
The revision ID is not valid. Use GetPullRequest to determine the value.
HTTP Status Code: 400

 ** OverrideAlreadySetException **
The pull request has already had its approval rules set to override.
HTTP Status Code: 400

 ** OverrideStatusRequiredException **
An override status is required, but no value was provided. Valid values include OVERRIDE and REVOKE.
HTTP Status Code: 400

 ** PullRequestAlreadyClosedException **
The pull request status cannot be updated because it is already closed.
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
<a name="API_OverridePullRequestApprovalRules_Examples"></a>

### Example
<a name="API_OverridePullRequestApprovalRules_Example_1"></a>

This example illustrates one usage of OverridePullRequestApprovalRules.

#### Sample Request
<a name="API_OverridePullRequestApprovalRules_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.OverridePullRequestApprovalRules
X-Amz-Date: 20191021T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "34",
   "revisionId": "927df8d8dEXAMPLE",
   "overrideStatus": OVERRIDE
}
```

#### Sample Response
<a name="API_OverridePullRequestApprovalRules_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Mon, 21 Oct 2019 22:43:13 GMT
```

## See Also
<a name="API_OverridePullRequestApprovalRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/OverridePullRequestApprovalRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/OverridePullRequestApprovalRules)
