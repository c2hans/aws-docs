---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_FeedSummary.html
---

# FeedSummary
<a name="API_FeedSummary"></a>

Contains configuration information about a feed. It is used in the ListFeeds response.

## Contents
<a name="API_FeedSummary_Contents"></a>

 ** arn **   <a name="elementalinference-Type-FeedSummary-arn"></a>
The ARN of the feed.
Type: String
Required: Yes

 ** id **   <a name="elementalinference-Type-FeedSummary-id"></a>
The ID of the feed.
Type: String
Pattern: `[a-z0-9]{19}`
Required: Yes

 ** name **   <a name="elementalinference-Type-FeedSummary-name"></a>
The name of the feed
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** status **   <a name="elementalinference-Type-FeedSummary-status"></a>
The status of the feed.
Type: String
Valid Values: `CREATING | AVAILABLE | ACTIVE | UPDATING | DELETING | DELETED | ARCHIVED`
Required: Yes

 ** association **   <a name="elementalinference-Type-FeedSummary-association"></a>
The resource, if any, associated with the feed.
Type: [FeedAssociation](API_FeedAssociation.md) object
Required: No

## See Also
<a name="API_FeedSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/FeedSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/FeedSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/FeedSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
