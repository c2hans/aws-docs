---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ReusableDelegationSetLimit.html
---

# ReusableDelegationSetLimit
<a name="API_ReusableDelegationSetLimit"></a>

A complex type that contains the type of limit that you specified in the request and the current value for that limit.

## Contents
<a name="API_ReusableDelegationSetLimit_Contents"></a>

 ** Type **   <a name="Route53-Type-ReusableDelegationSetLimit-Type"></a>
The limit that you requested: `MAX_ZONES_BY_REUSABLE_DELEGATION_SET`, the maximum number of hosted zones that you can associate with the specified reusable delegation set.
Type: String
Valid Values: `MAX_ZONES_BY_REUSABLE_DELEGATION_SET`
Required: Yes

 ** Value **   <a name="Route53-Type-ReusableDelegationSetLimit-Value"></a>
The current value for the `MAX_ZONES_BY_REUSABLE_DELEGATION_SET` limit.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_ReusableDelegationSetLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ReusableDelegationSetLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ReusableDelegationSetLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ReusableDelegationSetLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
