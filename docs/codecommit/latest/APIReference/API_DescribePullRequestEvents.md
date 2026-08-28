---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DescribePullRequestEvents.html
---

# DescribePullRequestEvents
<a name="API_DescribePullRequestEvents"></a>

Returns information about one or more pull request events.

## Request Syntax
<a name="API_DescribePullRequestEvents_RequestSyntax"></a>

```
{
   "actorArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pullRequestEventType": "{{string}}",
   "pullRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePullRequestEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorArn](#API_DescribePullRequestEvents_RequestSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-request-actorArn"></a>
The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.
Type: String
Required: No

 ** [maxResults](#API_DescribePullRequestEvents_RequestSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results. The default is 100 events, which is also the maximum number of events that can be returned in a result.
Type: Integer
Required: No

 ** [nextToken](#API_DescribePullRequestEvents_RequestSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [pullRequestEventType](#API_DescribePullRequestEvents_RequestSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-request-pullRequestEventType"></a>
Optional. The pull request event type about which you want to return information.
Type: String
Valid Values: `PULL_REQUEST_CREATED | PULL_REQUEST_STATUS_CHANGED | PULL_REQUEST_SOURCE_REFERENCE_UPDATED | PULL_REQUEST_MERGE_STATE_CHANGED | PULL_REQUEST_APPROVAL_RULE_CREATED | PULL_REQUEST_APPROVAL_RULE_UPDATED | PULL_REQUEST_APPROVAL_RULE_DELETED | PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN | PULL_REQUEST_APPROVAL_STATE_CHANGED`
Required: No

 ** [pullRequestId](#API_DescribePullRequestEvents_RequestSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-request-pullRequestId"></a>
The system-generated ID of the pull request. To get this ID, use [ListPullRequests](API_ListPullRequests.md).
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribePullRequestEvents_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "pullRequestEvents": [
      {
         "actorArn": "string",
         "approvalRuleEventMetadata": {
            "approvalRuleContent": "string",
            "approvalRuleId": "string",
            "approvalRuleName": "string"
         },
         "approvalRuleOverriddenEventMetadata": {
            "overrideStatus": "string",
            "revisionId": "string"
         },
         "approvalStateChangedEventMetadata": {
            "approvalStatus": "string",
            "revisionId": "string"
         },
         "eventDate": number,
         "pullRequestCreatedEventMetadata": {
            "destinationCommitId": "string",
            "mergeBase": "string",
            "repositoryName": "string",
            "sourceCommitId": "string"
         },
         "pullRequestEventType": "string",
         "pullRequestId": "string",
         "pullRequestMergedStateChangedEventMetadata": {
            "destinationReference": "string",
            "mergeMetadata": {
               "isMerged": boolean,
               "mergeCommitId": "string",
               "mergedBy": "string",
               "mergeOption": "string"
            },
            "repositoryName": "string"
         },
         "pullRequestSourceReferenceUpdatedEventMetadata": {
            "afterCommitId": "string",
            "beforeCommitId": "string",
            "mergeBase": "string",
            "repositoryName": "string"
         },
         "pullRequestStatusChangedEventMetadata": {
            "pullRequestStatus": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribePullRequestEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribePullRequestEvents_ResponseSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-response-nextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String

 ** [pullRequestEvents](#API_DescribePullRequestEvents_ResponseSyntax) **   <a name="CodeCommit-DescribePullRequestEvents-response-pullRequestEvents"></a>
Information about the pull request events.
Type: Array of [PullRequestEvent](API_PullRequestEvent.md) objects

## Errors
<a name="API_DescribePullRequestEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActorDoesNotExistException **
The specified Amazon Resource Name (ARN) does not exist in the AWS account.
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

 ** InvalidActorArnException **
The Amazon Resource Name (ARN) is not valid. Make sure that you have provided the full ARN for the user who initiated the change for the pull request, and then try again.
HTTP Status Code: 400

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxResultsException **
The specified number of maximum results is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestEventTypeException **
The pull request event type is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** PullRequestDoesNotExistException **
The pull request ID could not be found. Make sure that you have specified the correct repository name and pull request ID, and then try again.
HTTP Status Code: 400

 ** PullRequestIdRequiredException **
A pull request ID is required, but none was provided.
HTTP Status Code: 400

## Examples
<a name="API_DescribePullRequestEvents_Examples"></a>

### Example
<a name="API_DescribePullRequestEvents_Example_1"></a>

This example illustrates one usage of DescribePullRequestEvents.

#### Sample Request
<a name="API_DescribePullRequestEvents_Example_1_Request"></a>

```
>>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.DescribePullRequestEvents
X-Amz-Date: 20171110T235323Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "8"
}
```

#### Sample Response
<a name="API_DescribePullRequestEvents_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 660
Date: Fri, 10 Nov 2017 11:53:59 GMT

{
    "pullRequestEvents": [
        {
            "pullRequestId": "8",
            "pullRequestEventType": "PULL_REQUEST_CREATED",
            "eventDate": 1510341779.53,
            "actor": "arn:aws:iam::123456789012:user/Zhang_Wei"
        },
        {
            "pullRequestStatusChangedEventMetadata": {
                "pullRequestStatus": "CLOSED"
            },
            "pullRequestId": "8",
            "pullRequestEventType": "PULL_REQUEST_STATUS_CHANGED",
            "eventDate": 1510341930.72,
            "actor": "arn:aws:iam::123456789012:user/Jane_Doe"
        }
    ]
}
```

## See Also
<a name="API_DescribePullRequestEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DescribePullRequestEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DescribePullRequestEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
