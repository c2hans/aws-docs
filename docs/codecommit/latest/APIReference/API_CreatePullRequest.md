---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreatePullRequest.html
---

# CreatePullRequest
<a name="API_CreatePullRequest"></a>

Creates a pull request in the specified repository.

## Request Syntax
<a name="API_CreatePullRequest_RequestSyntax"></a>

```
{
   "clientRequestToken": "{{string}}",
   "description": "{{string}}",
   "targets": [
      {
         "destinationReference": "{{string}}",
         "repositoryName": "{{string}}",
         "sourceReference": "{{string}}"
      }
   ],
   "title": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePullRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreatePullRequest_RequestSyntax) **   <a name="CodeCommit-CreatePullRequest-request-clientRequestToken"></a>
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.
The AWSSDKs prepopulate client request tokens. If you are using an AWSSDK, an idempotency token is created for you.
Type: String
Required: No

 ** [description](#API_CreatePullRequest_RequestSyntax) **   <a name="CodeCommit-CreatePullRequest-request-description"></a>
A description of the pull request.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** [targets](#API_CreatePullRequest_RequestSyntax) **   <a name="CodeCommit-CreatePullRequest-request-targets"></a>
The targets for the pull request, including the source of the code to be reviewed (the source branch) and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).
Type: Array of [Target](API_Target.md) objects
Required: Yes

 ** [title](#API_CreatePullRequest_RequestSyntax) **   <a name="CodeCommit-CreatePullRequest-request-title"></a>
The title of the pull request. This title is used to identify the pull request to other users in the repository.
Type: String
Length Constraints: Maximum length of 150.
Required: Yes

## Response Syntax
<a name="API_CreatePullRequest_ResponseSyntax"></a>

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
<a name="API_CreatePullRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pullRequest](#API_CreatePullRequest_ResponseSyntax) **   <a name="CodeCommit-CreatePullRequest-response-pullRequest"></a>
Information about the newly created pull request.
Type: [PullRequest](API_PullRequest.md) object

## Errors
<a name="API_CreatePullRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientRequestTokenRequiredException **
A client request token is required. A client request token is an unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.
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

 ** IdempotencyParameterMismatchException **
The client request token is not valid. Either the token is not in a valid format, or the token has been used in a previous request and cannot be reused.
HTTP Status Code: 400

 ** InvalidClientRequestTokenException **
The client request token is not valid.
HTTP Status Code: 400

 ** InvalidDescriptionException **
The pull request description is not valid. Descriptions cannot be more than 1,000 characters.
HTTP Status Code: 400

 ** InvalidReferenceNameException **
The specified reference name format is not valid. Reference names must conform to the Git references format (for example, refs/heads/main). For more information, see [Git Internals - Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References) or consult your Git documentation.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** InvalidTargetException **
The target for the pull request is not valid. A target must contain the full values for the repository name, source branch, and destination branch for the pull request.
HTTP Status Code: 400

 ** InvalidTargetsException **
The targets for the pull request is not valid or not in a valid format. Targets are a list of target objects. Each target object must contain the full values for the repository name, source branch, and destination branch for a pull request.
HTTP Status Code: 400

 ** InvalidTitleException **
The title of the pull request is not valid. Pull request titles cannot exceed 100 characters in length.
HTTP Status Code: 400

 ** MaximumOpenPullRequestsExceededException **
You cannot create the pull request because the repository has too many open pull requests. The maximum number of open pull requests for a repository is 1,000. Close one or more open pull requests, and then try again.
HTTP Status Code: 400

 ** MultipleRepositoriesInPullRequestException **
You cannot include more than one repository in a pull request. Make sure you have specified only one repository name in your request, and then try again.
HTTP Status Code: 400

 ** ReferenceDoesNotExistException **
The specified reference does not exist. You must provide a full commit ID.
HTTP Status Code: 400

 ** ReferenceNameRequiredException **
A reference name is required, but none was provided.
HTTP Status Code: 400

 ** ReferenceTypeNotSupportedException **
The specified reference is not a supported type.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

 ** SourceAndDestinationAreSameException **
The source branch and destination branch for the pull request are the same. You must specify different branches for the source and destination.
HTTP Status Code: 400

 ** TargetRequiredException **
A pull request target is required. It cannot be empty or null. A pull request target must contain the full values for the repository name, source branch, and destination branch for the pull request.
HTTP Status Code: 400

 ** TargetsRequiredException **
An array of target objects is required. It cannot be empty or null.
HTTP Status Code: 400

 ** TitleRequiredException **
A pull request title is required. It cannot be empty or null.
HTTP Status Code: 400

## Examples
<a name="API_CreatePullRequest_Examples"></a>

### Example
<a name="API_CreatePullRequest_Example_1"></a>

This example illustrates one usage of CreatePullRequest.

#### Sample Request
<a name="API_CreatePullRequest_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.CreatePullRequest
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "clientRequestToken": "123Example",
   "description": "A code review of the new feature I just added to the service.",
   "targets": [
      {
         "destinationReference": "refs/heads/main",
         "repositoryName": "MyDemoRepo",
         "sourceReference": "refs/heads/jane-branch"
      }
   ],
   "title": "Pronunciation difficulty analyzer"
}
```

#### Sample Response
<a name="API_CreatePullRequest_Example_1_Response"></a>

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
                    "approvalRuleTemplateId": "dd8b17fe-EXAMPLE",
                    "approvalRuleTemplateName": "2-approver-rule-for-main"
                },
                "ruleContentSha256": "4711b576EXAMPLE"
            }
        ],
        "authorArn": "arn:aws:iam::123456789012:user/Jane_Doe",
        "description": "A code review of the new feature I just added to the service.",
        "title": "Pronunciation difficulty analyzer",
        "pullRequestTargets": [
            {
                "destinationCommit": "5d036259EXAMPLE",
                "destinationReference": "refs/heads/main",
                "repositoryName": "MyDemoRepo",
                "sourceCommit": "317f8570EXAMPLE",
                "sourceReference": "refs/heads/jane-branch",
                "mergeMetadata": {
                    "isMerged": false
                }
            }
        ],
        "lastActivityDate": 1508962823.285,
        "pullRequestId": "42",
        "clientRequestToken": "123Example",
        "pullRequestStatus": "OPEN",
        "creationDate": 1508962823.285
    }
}
```

## See Also
<a name="API_CreatePullRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/CreatePullRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CreatePullRequest)
