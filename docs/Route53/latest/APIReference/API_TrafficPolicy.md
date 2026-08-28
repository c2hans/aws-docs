---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_TrafficPolicy.html
---

# TrafficPolicy
<a name="API_TrafficPolicy"></a>

A complex type that contains settings for a traffic policy.

## Contents
<a name="API_TrafficPolicy_Contents"></a>

 ** Document **   <a name="Route53-Type-TrafficPolicy-Document"></a>
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the `CreateTrafficPolicy` request. For more information about the JSON format, see [Traffic Policy Document Format](https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html).
Type: String
Length Constraints: Maximum length of 102400.
Required: Yes

 ** Id **   <a name="Route53-Type-TrafficPolicy-Id"></a>
The ID that Amazon Route 53 assigned to a traffic policy when you created it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** Name **   <a name="Route53-Type-TrafficPolicy-Name"></a>
The name that you specified when you created the traffic policy.
Type: String
Length Constraints: Maximum length of 512.
Required: Yes

 ** Type **   <a name="Route53-Type-TrafficPolicy-Type"></a>
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

 ** Version **   <a name="Route53-Type-TrafficPolicy-Version"></a>
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of `Version` is always 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** Comment **   <a name="Route53-Type-TrafficPolicy-Comment"></a>
The comment that you specify in the `CreateTrafficPolicy` request, if any.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_TrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/TrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/TrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/TrafficPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
