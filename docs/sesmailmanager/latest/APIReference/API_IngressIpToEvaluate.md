---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressIpToEvaluate.html
---

# IngressIpToEvaluate
<a name="API_IngressIpToEvaluate"></a>

The structure for an IP based condition matching on the incoming mail.

## Contents
<a name="API_IngressIpToEvaluate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Attribute **   <a name="sesmailmanager-Type-IngressIpToEvaluate-Attribute"></a>
An enum type representing the allowed attribute types for an IP condition.
Type: String
Valid Values: `SENDER_IP`
Required: No

## See Also
<a name="API_IngressIpToEvaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressIpToEvaluate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressIpToEvaluate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressIpToEvaluate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
