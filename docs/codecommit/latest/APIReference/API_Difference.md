---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Difference.html
---

# Difference
<a name="API_Difference"></a>

Returns information about a set of differences for a commit specifier.

## Contents
<a name="API_Difference_Contents"></a>

 ** afterBlob **   <a name="CodeCommit-Type-Difference-afterBlob"></a>
Information about an `afterBlob` data type object, including the ID, the file mode permission code, and the path.
Type: [BlobMetadata](API_BlobMetadata.md) object
Required: No

 ** beforeBlob **   <a name="CodeCommit-Type-Difference-beforeBlob"></a>
Information about a `beforeBlob` data type object, including the ID, the file mode permission code, and the path.
Type: [BlobMetadata](API_BlobMetadata.md) object
Required: No

 ** changeType **   <a name="CodeCommit-Type-Difference-changeType"></a>
Whether the change type of the difference is an addition (A), deletion (D), or modification (M).
Type: String
Valid Values: `A | M | D`
Required: No

## See Also
<a name="API_Difference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Difference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Difference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Difference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
