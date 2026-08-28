---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestDescription.html
---

# UpdatePullRequestDescription
<a name="API_UpdatePullRequestDescription"></a>

Replaces the contents of the description of a pull request.

## Request Syntax
<a name="API_UpdatePullRequestDescription_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "pullRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePullRequestDescription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdatePullRequestDescription_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestDescription-request-description"></a>
The updated content of the description for the pull request. This content replaces the existing description.
Type: String
Length Constraints: Maximum length of 10240.
Required: Yes

 ** [pullRequestId](#API_UpdatePullRequestDescription_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestDescription-request-pullRequestId"></a>
The system-generated ID of the pull request. To get this ID, use [ListPullRequests](API_ListPullRequests.md).
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdatePullRequestDescription_ResponseSyntax"></a>

```
{
   "pullRequest": {
      "approvalRules": [
         {
            "approvalRuleContent": "string",
            "approvalRuleId": "string",
            "approvalRuleName": "string",
            "creationDate": number,
            "lastModifiedDate": number,
            "lastModifiedUser": "string",
            "originApprovalRuleTemplate": {
               "approvalRuleTemplateId": "string",
               "approvalRuleTemplateName": "string"
            },
            "ruleContentSha256": "string"
         }
      ],
      "authorArn": "string",
      "clientRequestToken": "string",
      "creationDate": number,
      "description": "string",
      "lastActivityDate": number,
      "pullRequestId": "string",
      "pullRequestStatus": "string",
      "pullRequestTargets": [
         {
            "destinationCommit": "string",
            "destinationReference": "string",
            "mergeBase": "string",
            "mergeMetadata": {
               "isMerged": boolean,
               "mergeCommitId": "string",
               "mergedBy": "string",
               "mergeOption": "string"
            },
            "repositoryName": "string",
            "sourceCommit": "string",
            "sourceReference": "string"
         }
      ],
      "revisionId": "string",
      "title": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePullRequestDescription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pullRequest](#API_UpdatePullRequestDescription_ResponseSyntax) **   <a name="CodeCommit-UpdatePullRequestDescription-response-pullRequest"></a>
Information about the updated pull request.
Type: [PullRequest](API_PullRequest.md) object

## Errors
<a name="API_UpdatePullRequestDescription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDescriptionException **
The pull request description is not valid. Descriptions cannot be more than 1,000 characters.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
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

## Examples
<a name="API_UpdatePullRequestDescription_Examples"></a>

### Example
<a name="API_UpdatePullRequestDescription_Example_1"></a>

This example illustrates one usage of UpdatePullRequestDescription.

#### Sample Request
<a name="API_UpdatePullRequestDescription_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdatePullRequestDescription
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "description": "Updated the pull request to remove unused global variable.",
   "pullRequestId": "47"
}
```

#### Sample Response
<a name="API_UpdatePullRequestDescription_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Wed, 25 Oct 2017 20:20:13 GMT

{
    "pullRequest": {
        "approvalRules": [
            {
                "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
                "approvalRuleId": "dd8b17fe-EXAMPLE",
                "approvalRuleName": "2-approver-rule-for-main",
                "creationDate": 1571356106.936,
                "lastModifiedDate": 571356106.936,
                "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
                "originApprovalRuleTemplate": {
                    "approvalRuleTemplateId": "dd8b17fe-OTHEREXAMPLE",
                    "approvalRuleTemplateName": "2-approver-rule-for-main"
                },
                "ruleContentSha256": "4711b576EXAMPLE"
            }
        ],
        "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
        "clientRequestToken": "",
        "creationDate": 1508530823.155,
        "description": "Updated the pull request to remove unused global variable.",
        "lastActivityDate": 1508372423.204,
        "pullRequestId": "47",
        "pullRequestStatus": "OPEN",
        "pullRequestTargets": [
            {
                "destinationCommit": "9f31c968EXAMPLE",
                "destinationReference": "refs/heads/main",
                "mergeMetadata": {
                    "isMerged": false,
                },
                "repositoryName": "MyDemoRepo",
                "sourceCommit": "99132ab0EXAMPLE",
                "sourceReference": "refs/heads/variables-branch"
            }
        ],
        "title": "Consolidation of global variables"
    }
}
```

## See Also
<a name="API_UpdatePullRequestDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdatePullRequestDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdatePullRequestDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
