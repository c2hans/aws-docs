---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_EvaluatePullRequestApprovalRules.html
---

# EvaluatePullRequestApprovalRules
<a name="API_EvaluatePullRequestApprovalRules"></a>

Evaluates whether a pull request has met all the conditions specified in its associated approval rules.

## Request Syntax
<a name="API_EvaluatePullRequestApprovalRules_RequestSyntax"></a>

```
{
   "pullRequestId": "{{string}}",
   "revisionId": "{{string}}"
}
```

## Request Parameters
<a name="API_EvaluatePullRequestApprovalRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pullRequestId](#API_EvaluatePullRequestApprovalRules_RequestSyntax) **   <a name="CodeCommit-EvaluatePullRequestApprovalRules-request-pullRequestId"></a>
The system-generated ID of the pull request you want to evaluate.
Type: String
Required: Yes

 ** [revisionId](#API_EvaluatePullRequestApprovalRules_RequestSyntax) **   <a name="CodeCommit-EvaluatePullRequestApprovalRules-request-revisionId"></a>
The system-generated ID for the pull request revision. To retrieve the most recent revision ID for a pull request, use [GetPullRequest](API_GetPullRequest.md).
Type: String
Required: Yes

## Response Syntax
<a name="API_EvaluatePullRequestApprovalRules_ResponseSyntax"></a>

```
{
   "evaluation": {
      "approvalRulesNotSatisfied": [ "string" ],
      "approvalRulesSatisfied": [ "string" ],
      "approved": boolean,
      "overridden": boolean
   }
}
```

## Response Elements
<a name="API_EvaluatePullRequestApprovalRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evaluation](#API_EvaluatePullRequestApprovalRules_ResponseSyntax) **   <a name="CodeCommit-EvaluatePullRequestApprovalRules-response-evaluation"></a>
The result of the evaluation, including the names of the rules whose conditions have been met (if any), the names of the rules whose conditions have not been met (if any), whether the pull request is in the approved state, and whether the pull request approval rule has been set aside by an override.
Type: [Evaluation](API_Evaluation.md) object

## Errors
<a name="API_EvaluatePullRequestApprovalRules_Errors"></a>

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

 ** RevisionNotCurrentException **
The revision ID provided in the request does not match the current revision ID. Use GetPullRequest to retrieve the current revision ID.
HTTP Status Code: 400

## Examples
<a name="API_EvaluatePullRequestApprovalRules_Examples"></a>

### Example
<a name="API_EvaluatePullRequestApprovalRules_Example_1"></a>

This example illustrates one usage of EvaluatePullRequestApprovalRules.

#### Sample Request
<a name="API_EvaluatePullRequestApprovalRules_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 124
    X-Amz-Target: CodeCommit_20150413.EvaluatePullRequestApprovalRules
    X-Amz-Date: 20191021T223055Z
    User-Agent: aws-cli/1.15.9 Python/2.7.11 Darwin/16.7.0 botocore/1.10.9
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature==8d9b5998EXAMPLE
{
   "pullRequestId": "27",
   "revisionId": "9f29d167EXAMPLE"
}
```

#### Sample Response
<a name="API_EvaluatePullRequestApprovalRules_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: d8ad1d21-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 2267
    Date: Mon, 21 Oct 2019 22:30:56 GMT
    Connection: keep-alive

{
    "evaluation": {
        "approved": false,
        "approvalRulesNotSatisfied": [
            "Require two approved approvers"
        ],
        "overridden": false,
        "approvalRulesSatisfied": []
    }
}
```

## See Also
<a name="API_EvaluatePullRequestApprovalRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/EvaluatePullRequestApprovalRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
