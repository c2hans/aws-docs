---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationRuleFilter.html
---

# ReplicationRuleFilter
<a name="API_ReplicationRuleFilter"></a>

A filter that identifies the subset of objects to which the replication rule applies. A `Filter` must specify exactly one `Prefix`, `Tag`, or an `And` child element.

## Contents
<a name="API_ReplicationRuleFilter_Contents"></a>

 ** And **   <a name="AmazonS3-Type-ReplicationRuleFilter-And"></a>
A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example:
+ If you specify both a `Prefix` and a `Tag` filter, wrap these filters in an `And` tag.
+ If you specify a filter based on multiple tags, wrap the `Tag` elements in an `And` tag.
Type: [ReplicationRuleAndOperator](API_ReplicationRuleAndOperator.md) data type
Required: No

 ** Prefix **   <a name="AmazonS3-Type-ReplicationRuleFilter-Prefix"></a>
An object key name prefix that identifies the subset of objects to which the rule applies.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Required: No

 ** Tag **   <a name="AmazonS3-Type-ReplicationRuleFilter-Tag"></a>
A container for specifying a tag key and value.
The rule applies only to objects that have the tag in their tag set.
Type: [Tag](API_Tag.md) data type
Required: No

## See Also
<a name="API_ReplicationRuleFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicationRuleFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicationRuleFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicationRuleFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
