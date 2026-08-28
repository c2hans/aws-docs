---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_GitHubDocumentCrawlProperties.html
---

# GitHubDocumentCrawlProperties
<a name="API_GitHubDocumentCrawlProperties"></a>

Provides the configuration information to include certain types of GitHub content. You can configure to index repository files only, or also include issues and pull requests, comments, and comment attachments.

## Contents
<a name="API_GitHubDocumentCrawlProperties_Contents"></a>

 ** CrawlIssue **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlIssue"></a>
 `TRUE` to index all issues within a repository.
Type: Boolean
Required: No

 ** CrawlIssueComment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlIssueComment"></a>
 `TRUE` to index all comments on issues.
Type: Boolean
Required: No

 ** CrawlIssueCommentAttachment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlIssueCommentAttachment"></a>
 `TRUE` to include all comment attachments for issues.
Type: Boolean
Required: No

 ** CrawlPullRequest **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlPullRequest"></a>
 `TRUE` to index all pull requests within a repository.
Type: Boolean
Required: No

 ** CrawlPullRequestComment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlPullRequestComment"></a>
 `TRUE` to index all comments on pull requests.
Type: Boolean
Required: No

 ** CrawlPullRequestCommentAttachment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlPullRequestCommentAttachment"></a>
 `TRUE` to include all comment attachments for pull requests.
Type: Boolean
Required: No

 ** CrawlRepositoryDocuments **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlRepositoryDocuments"></a>
 `TRUE` to index all files with a repository.
Type: Boolean
Required: No

## See Also
<a name="API_GitHubDocumentCrawlProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/GitHubDocumentCrawlProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/GitHubDocumentCrawlProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/GitHubDocumentCrawlProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
