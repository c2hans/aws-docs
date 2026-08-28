---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html
---

# ListRepositoryAssociations
<a name="API_ListRepositoryAssociations"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Returns a list of [RepositoryAssociationSummary](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html) objects that contain summary information about a repository association. You can filter the returned list by [ProviderType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-ProviderType), [Name](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Name), [State](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-State), and [Owner](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Owner).

## Request Syntax
<a name="API_ListRepositoryAssociations_RequestSyntax"></a>

```
GET /associations?MaxResults={{MaxResults}}&Name={{Names}}&NextToken={{NextToken}}&Owner={{Owners}}&ProviderType={{ProviderTypes}}&State={{States}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRepositoryAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListRepositoryAssociations_RequestSyntax) **   <a name="reviewer-ListRepositoryAssociations-request-uri-MaxResults"></a>
The maximum number of repository association results returned by `ListRepositoryAssociations` in paginated output. When this parameter is used, `ListRepositoryAssociations` only returns `maxResults` results in a single page with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListRepositoryAssociations` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter is not used, `ListRepositoryAssociations` returns up to 100 results and a `nextToken` value if applicable.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Names](#API_ListRepositoryAssociations_RequestSyntax) **   <a name="reviewer-ListRepositoryAssociations-request-uri-Names"></a>
List of repository names to use as a filter.
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`

 ** [NextToken](#API_ListRepositoryAssociations_RequestSyntax) **   <a name="reviewer-ListRepositoryAssociations-request-uri-NextToken"></a>
The `nextToken` value returned from a previous paginated `ListRepositoryAssociations` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.
Treat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [Owners](#API_ListRepositoryAssociations_RequestSyntax) **   <a name="reviewer-ListRepositoryAssociations-request-uri-Owners"></a>
List of owners to use as a filter. For AWS CodeCommit, it is the name of the CodeCommit account that was used to associate the repository. For other repository source providers, such as Bitbucket and GitHub Enterprise Server, this is name of the account that was used to associate the repository.
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`

 ** [ProviderTypes](#API_ListRepositoryAssociations_RequestSyntax) **   <a name="reviewer-ListRepositoryAssociations-request-uri-ProviderTypes"></a>
List of provider types to use as a filter.
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `CodeCommit | GitHub | Bitbucket | GitHubEnterpriseServer | S3Bucket`

 ** [States](#API_ListRepositoryAssociations_RequestSyntax) **   <a name="reviewer-ListRepositoryAssociations-request-uri-States"></a>
List of repository association states to use as a filter.
The valid repository association states are:
+  **Associated**: The repository association is complete.
+  **Associating**: CodeGuru Reviewer is:
  + Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.
**Note**
If your repository `ProviderType` is `GitHub`, `GitHub Enterprise Server`, or `Bitbucket`, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.
  + Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.
+  **Failed**: The repository failed to associate or disassociate.
+  **Disassociating**: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.
+  **Disassociated**: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see [Using tags to control access to associated repositories](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html) in the *Amazon CodeGuru Reviewer User Guide*.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `Associated | Associating | Failed | Disassociating | Disassociated`

## Request Body
<a name="API_ListRepositoryAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRepositoryAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RepositoryAssociationSummaries": [
      {
         "AssociationArn": "string",
         "AssociationId": "string",
         "ConnectionArn": "string",
         "LastUpdatedTimeStamp": number,
         "Name": "string",
         "Owner": "string",
         "ProviderType": "string",
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositoryAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRepositoryAssociations_ResponseSyntax) **   <a name="reviewer-ListRepositoryAssociations-response-NextToken"></a>
The `nextToken` value to include in a future `ListRecommendations` request. When the results of a `ListRecommendations` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [RepositoryAssociationSummaries](#API_ListRepositoryAssociations_ResponseSyntax) **   <a name="reviewer-ListRepositoryAssociations-response-RepositoryAssociationSummaries"></a>
A list of repository associations that meet the criteria of the request.
Type: Array of [RepositoryAssociationSummary](API_RepositoryAssociationSummary.md) objects

## Errors
<a name="API_ListRepositoryAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListRepositoryAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ListRepositoryAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
