---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DNSViewSummary.html
---

# DNSViewSummary
<a name="API_route53globalresolver_DNSViewSummary"></a>

Summary information about a DNS view.

## Contents
<a name="API_route53globalresolver_DNSViewSummary_Contents"></a>

 ** arn **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-arn"></a>
The Amazon Resource Name (ARN) of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** clientToken **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-clientToken"></a>
The unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-createdAt"></a>
The date and time when the DNS view was created.
Type: Timestamp
Required: Yes

 ** dnssecValidation **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-dnssecValidation"></a>
Whether DNSSEC validation is enabled for the DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** ednsClientSubnet **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-ednsClientSubnet"></a>
Whether EDNS Client Subnet injection is enabled for the DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** firewallRulesFailOpen **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-firewallRulesFailOpen"></a>
Whether firewall rules fail open when they cannot be evaluated.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** globalResolverId **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-globalResolverId"></a>
The ID of the global resolver that the DNS view is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-id"></a>
The unique identifier of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-name"></a>
The name of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-status"></a>
The current status of the DNS view.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | ENABLING | DISABLING | DISABLED | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-updatedAt"></a>
The date and time when the DNS view was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_DNSViewSummary-description"></a>
A description of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_route53globalresolver_DNSViewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/DNSViewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/DNSViewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/DNSViewSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
