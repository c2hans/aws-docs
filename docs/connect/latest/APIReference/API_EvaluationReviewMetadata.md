---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationReviewMetadata.html
---

# EvaluationReviewMetadata
<a name="API_EvaluationReviewMetadata"></a>

Metadata information about an evaluation review.

## Contents
<a name="API_EvaluationReviewMetadata_Contents"></a>

 ** ReviewRequestComments **   <a name="connect-Type-EvaluationReviewMetadata-ReviewRequestComments"></a>
Comments provided when requesting the evaluation review.
Type: Array of [EvaluationReviewRequestComment](API_EvaluationReviewRequestComment.md) objects
Array Members: Maximum number of 1 item.
Required: Yes

 ** CreatedBy **   <a name="connect-Type-EvaluationReviewMetadata-CreatedBy"></a>
 *This member has been deprecated.*
The user who created the evaluation review.
Type: String
Required: No

 ** CreatedTime **   <a name="connect-Type-EvaluationReviewMetadata-CreatedTime"></a>
 *This member has been deprecated.*
The timestamp when the evaluation review was created.
Type: Timestamp
Required: No

 ** RequestedBy **   <a name="connect-Type-EvaluationReviewMetadata-RequestedBy"></a>
The user who requested the evaluation review.
Type: String
Required: No

 ** RequestedTime **   <a name="connect-Type-EvaluationReviewMetadata-RequestedTime"></a>
The timestamp when the evaluation review was requested.
Type: Timestamp
Required: No

 ** ReviewId **   <a name="connect-Type-EvaluationReviewMetadata-ReviewId"></a>
The unique identifier for the evaluation review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_EvaluationReviewMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationReviewMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationReviewMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationReviewMetadata)
