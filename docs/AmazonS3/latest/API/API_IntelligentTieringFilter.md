---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_IntelligentTieringFilter.html
---

# IntelligentTieringFilter
<a name="API_IntelligentTieringFilter"></a>

The `Filter` is used to identify objects that the S3 Intelligent-Tiering configuration applies to.

## Contents
<a name="API_IntelligentTieringFilter_Contents"></a>

 ** And **   <a name="AmazonS3-Type-IntelligentTieringFilter-And"></a>
A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
Type: [IntelligentTieringAndOperator](API_IntelligentTieringAndOperator.md) data type
Required: No

 ** Prefix **   <a name="AmazonS3-Type-IntelligentTieringFilter-Prefix"></a>
An object key name prefix that identifies the subset of objects to which the rule applies.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Required: No

 ** Tag **   <a name="AmazonS3-Type-IntelligentTieringFilter-Tag"></a>
A container of a key value name pair.
Type: [Tag](API_Tag.md) data type
Required: No

## See Also
<a name="API_IntelligentTieringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IntelligentTieringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IntelligentTieringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IntelligentTieringFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
