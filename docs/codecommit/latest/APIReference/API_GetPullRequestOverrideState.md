---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetPullRequestOverrideState.html
---

# GetPullRequestOverrideState
<a name="API_GetPullRequestOverrideState"></a>

Returns information about whether approval rules have been set aside (overridden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.

## Request Syntax
<a name="API_GetPullRequestOverrideState_RequestSyntax"></a>

```
{
   "pullRequestId": "{{string}}",
   "revisionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPullRequestOverrideState_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pullRequestId](#API_GetPullRequestOverrideState_RequestSyntax) **   <a name="CodeCommit-GetPullRequestOverrideState-request-pullRequestId"></a>
The ID of the pull request for which you want to get information about whether approval rules have been set aside (overridden).
Type: String
Required: Yes

 ** [revisionId](#API_GetPullRequestOverrideState_RequestSyntax) **   <a name="CodeCommit-GetPullRequestOverrideState-request-revisionId"></a>
The system-generated ID of the revision for the pull request. To retrieve the most recent revision ID, use [GetPullRequest](API_GetPullRequest.md).
Type: String
Required: Yes

## Response Syntax
<a name="API_GetPullRequestOverrideState_ResponseSyntax"></a>

```
{
   "overridden": boolean,
   "overrider": "string"
}
```

## Response Elements
<a name="API_GetPullRequestOverrideState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [overridden](#API_GetPullRequestOverrideState_ResponseSyntax) **   <a name="CodeCommit-GetPullRequestOverrideState-response-overridden"></a>
A Boolean value that indicates whether a pull request has had its rules set aside (TRUE) or whether all approval rules still apply (FALSE).
Type: Boolean

 ** [overrider](#API_GetPullRequestOverrideState_ResponseSyntax) **   <a name="CodeCommit-GetPullRequestOverrideState-response-overrider"></a>
The Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.
Type: String

## Errors
<a name="API_GetPullRequestOverrideState_Errors"></a>

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
<a name="API_GetPullRequestOverrideState_Examples"></a>

### Example
<a name="API_GetPullRequestOverrideState_Example_1"></a>

This example illustrates one usage of GetPullRequestOverrideState.

#### Sample Request
<a name="API_GetPullRequestOverrideState_Example_1_Request"></a>

```
>>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.GetPullRequestOverrideState
X-Amz-Date: 20191021T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "34",
   "revisionId": "9f29d1673EXAMPLE"
}
```

#### Sample Response
<a name="API_GetPullRequestOverrideState_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Mon, 21 Oct 2019 20:20:13 GMT

{
    "overridden": true,
    "overrider": "arn:aws:iam::123456789012:user/Mary_Major"
}
```

## See Also
<a name="API_GetPullRequestOverrideState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetPullRequestOverrideState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetPullRequestOverrideState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
