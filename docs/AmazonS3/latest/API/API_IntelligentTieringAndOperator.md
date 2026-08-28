---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_IntelligentTieringAndOperator.html
---

# IntelligentTieringAndOperator
<a name="API_IntelligentTieringAndOperator"></a>

A container for specifying S3 Intelligent-Tiering filters. The filters determine the subset of objects to which the rule applies.

## Contents
<a name="API_IntelligentTieringAndOperator_Contents"></a>

 ** Prefix **   <a name="AmazonS3-Type-IntelligentTieringAndOperator-Prefix"></a>
An object key name prefix that identifies the subset of objects to which the configuration applies.
Type: String
Required: No

 ** Tags **   <a name="AmazonS3-Type-IntelligentTieringAndOperator-Tags"></a>
All of these tags must exist in the object's tag set in order for the configuration to apply.
Type: Array of [Tag](API_Tag.md) data types
Required: No

## See Also
<a name="API_IntelligentTieringAndOperator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringAndOperator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringAndOperator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringAndOperator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
