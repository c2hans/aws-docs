---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListCodeReviews.html
---

# ListCodeReviews
<a name="API_ListCodeReviews"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Lists all the code reviews that the customer has created in the past 90 days.

## Request Syntax
<a name="API_ListCodeReviews_RequestSyntax"></a>

```
GET /codereviews?MaxResults={{MaxResults}}&NextToken={{NextToken}}&ProviderTypes={{ProviderTypes}}&RepositoryNames={{RepositoryNames}}&States={{States}}&Type={{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCodeReviews_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListCodeReviews_RequestSyntax) **   <a name="reviewer-ListCodeReviews-request-uri-MaxResults"></a>
The maximum number of results that are returned per call. The default is 100.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListCodeReviews_RequestSyntax) **   <a name="reviewer-ListCodeReviews-request-uri-NextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [ProviderTypes](#API_ListCodeReviews_RequestSyntax) **   <a name="reviewer-ListCodeReviews-request-uri-ProviderTypes"></a>
List of provider types for filtering that needs to be applied before displaying the result. For example, `providerTypes=[GitHub]` lists code reviews from GitHub.
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `CodeCommit | GitHub | Bitbucket | GitHubEnterpriseServer | S3Bucket`

 ** [RepositoryNames](#API_ListCodeReviews_RequestSyntax) **   <a name="reviewer-ListCodeReviews-request-uri-RepositoryNames"></a>
List of repository names for filtering that needs to be applied before displaying the result.
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`

 ** [States](#API_ListCodeReviews_RequestSyntax) **   <a name="reviewer-ListCodeReviews-request-uri-States"></a>
List of states for filtering that needs to be applied before displaying the result. For example, `states=[Pending]` lists code reviews in the Pending state.
The valid code review states are:
+  `Completed`: The code review is complete.
+  `Pending`: The code review started and has not completed or failed.
+  `Failed`: The code review failed.
+  `Deleting`: The code review is being deleted.
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `Completed | Pending | Failed | Deleting`

 ** [Type](#API_ListCodeReviews_RequestSyntax) **   <a name="reviewer-ListCodeReviews-request-uri-Type"></a>
The type of code reviews to list in the response.
Valid Values: `PullRequest | RepositoryAnalysis`
Required: Yes

## Request Body
<a name="API_ListCodeReviews_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCodeReviews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CodeReviewSummaries": [
      {
         "CodeReviewArn": "string",
         "CreatedTimeStamp": number,
         "LastUpdatedTimeStamp": number,
         "MetricsSummary": {
            "FindingsCount": number,
            "MeteredLinesOfCodeCount": number,
            "SuppressedLinesOfCodeCount": number
         },
         "Name": "string",
         "Owner": "string",
         "ProviderType": "string",
         "PullRequestId": "string",
         "RepositoryName": "string",
         "SourceCodeType": {
            "BranchDiff": {
               "DestinationBranchName": "string",
               "SourceBranchName": "string"
            },
            "CommitDiff": {
               "DestinationCommit": "string",
               "MergeBaseCommit": "string",
               "SourceCommit": "string"
            },
            "RepositoryHead": {
               "BranchName": "string"
            },
            "RequestMetadata": {
               "EventInfo": {
                  "Name": "string",
                  "State": "string"
               },
               "Requester": "string",
               "RequestId": "string",
               "VendorName": "string"
            },
            "S3BucketRepository": {
               "Details": {
                  "BucketName": "string",
                  "CodeArtifacts": {
                     "BuildArtifactsObjectKey": "string",
                     "SourceCodeArtifactsObjectKey": "string"
                  }
               },
               "Name": "string"
            }
         },
         "State": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeReviews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeReviewSummaries](#API_ListCodeReviews_ResponseSyntax) **   <a name="reviewer-ListCodeReviews-response-CodeReviewSummaries"></a>
A list of code reviews that meet the criteria of the request.
Type: Array of [CodeReviewSummary](API_CodeReviewSummary.md) objects

 ** [NextToken](#API_ListCodeReviews_ResponseSyntax) **   <a name="reviewer-ListCodeReviews-response-NextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_ListCodeReviews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListCodeReviews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/ListCodeReviews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ListCodeReviews)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
