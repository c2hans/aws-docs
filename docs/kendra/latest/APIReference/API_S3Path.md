---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_S3Path.html
---

# S3Path
<a name="API_S3Path"></a>

Information required to find a specific file in an Amazon S3 bucket.

## Contents
<a name="API_S3Path_Contents"></a>

 ** Bucket **   <a name="kendra-Type-S3Path-Bucket"></a>
The name of the S3 bucket that contains the file.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** Key **   <a name="kendra-Type-S3Path-Key"></a>
The name of the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_S3Path_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/S3Path)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/S3Path)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/S3Path)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
