---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeBatch.html
---

# ChangeBatch
<a name="API_ChangeBatch"></a>

The information for a change request.

## Contents
<a name="API_ChangeBatch_Contents"></a>

 ** Changes **   <a name="Route53-Type-ChangeBatch-Changes"></a>
Information about the changes to make to the record sets.
Type: Array of [Change](API_Change.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Comment **   <a name="Route53-Type-ChangeBatch-Comment"></a>
 *Optional:* Any comments you want to include about a change batch request.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ChangeBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
