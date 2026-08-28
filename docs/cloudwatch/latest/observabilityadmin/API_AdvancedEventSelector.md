---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_AdvancedEventSelector.html
---

# AdvancedEventSelector
<a name="API_AdvancedEventSelector"></a>

Advanced event selectors let you create fine-grained selectors for management, data, and network activity events.

## Contents
<a name="API_AdvancedEventSelector_Contents"></a>

 ** FieldSelectors **   <a name="cwoa-Type-AdvancedEventSelector-FieldSelectors"></a>
Contains all selector statements in an advanced event selector.
Type: Array of [AdvancedFieldSelector](API_AdvancedFieldSelector.md) objects
Required: Yes

 ** Name **   <a name="cwoa-Type-AdvancedEventSelector-Name"></a>
An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
Type: String
Required: No

## See Also
<a name="API_AdvancedEventSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AdvancedEventSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AdvancedEventSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AdvancedEventSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
