---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_NotebookS3LocationForOutput.html
---

# NotebookS3LocationForOutput
<a name="API_NotebookS3LocationForOutput"></a>

The Amazon S3 location that stores the notebook execution input.

## Contents
<a name="API_NotebookS3LocationForOutput_Contents"></a>

 ** Bucket **   <a name="EMR-Type-NotebookS3LocationForOutput-Bucket"></a>
The Amazon S3 bucket that stores the notebook execution input.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Key **   <a name="EMR-Type-NotebookS3LocationForOutput-Key"></a>
The key to the Amazon S3 location that stores the notebook execution input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_NotebookS3LocationForOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/NotebookS3LocationForOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/NotebookS3LocationForOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/NotebookS3LocationForOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
