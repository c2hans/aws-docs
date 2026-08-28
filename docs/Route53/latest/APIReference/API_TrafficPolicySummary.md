---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_TrafficPolicySummary.html
---

# TrafficPolicySummary
<a name="API_TrafficPolicySummary"></a>

A complex type that contains information about the latest version of one traffic policy that is associated with the current AWS account.

## Contents
<a name="API_TrafficPolicySummary_Contents"></a>

 ** Id **   <a name="Route53-Type-TrafficPolicySummary-Id"></a>
The ID that Amazon Route 53 assigned to the traffic policy when you created it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** LatestVersion **   <a name="Route53-Type-TrafficPolicySummary-LatestVersion"></a>
The version number of the latest version of the traffic policy.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** Name **   <a name="Route53-Type-TrafficPolicySummary-Name"></a>
The name that you specified for the traffic policy when you created it.
Type: String
Length Constraints: Maximum length of 512.
Required: Yes

 ** TrafficPolicyCount **   <a name="Route53-Type-TrafficPolicySummary-TrafficPolicyCount"></a>
The number of traffic policies that are associated with the current AWS account.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** Type **   <a name="Route53-Type-TrafficPolicySummary-Type"></a>
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

## See Also
<a name="API_TrafficPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/TrafficPolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/TrafficPolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/TrafficPolicySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
