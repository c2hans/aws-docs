---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentReviewCommentSource.html
---

# DocumentReviewCommentSource
<a name="API_DocumentReviewCommentSource"></a>

Information about comments added to a document review request.

## Contents
<a name="API_DocumentReviewCommentSource_Contents"></a>

 ** Content **   <a name="systemsmanager-Type-DocumentReviewCommentSource-Content"></a>
The content of a comment entered by a user who requests a review of a new document version, or who reviews the new version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: No

 ** Type **   <a name="systemsmanager-Type-DocumentReviewCommentSource-Type"></a>
The type of information added to a review request. Currently, only the value `Comment` is supported.
Type: String
Valid Values: `Comment`
Required: No

## See Also
<a name="API_DocumentReviewCommentSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentReviewCommentSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentReviewCommentSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentReviewCommentSource)
