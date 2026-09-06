---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentReviews.html
---

# DocumentReviews
<a name="API_DocumentReviews"></a>

Information about a document approval review.

## Contents
<a name="API_DocumentReviews_Contents"></a>

 ** Action **   <a name="systemsmanager-Type-DocumentReviews-Action"></a>
The action to take on a document approval review request.
Type: String
Valid Values: `SendForReview | UpdateReview | Approve | Reject`
Required: Yes

 ** Comment **   <a name="systemsmanager-Type-DocumentReviews-Comment"></a>
A comment entered by a user in your organization about the document review request.
Type: Array of [DocumentReviewCommentSource](API_DocumentReviewCommentSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_DocumentReviews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentReviews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentReviews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentReviews)
