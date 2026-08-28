---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneSummary.html
---

# HostedZoneSummary
<a name="API_HostedZoneSummary"></a>

In the response to a `ListHostedZonesByVPC` request, the `HostedZoneSummaries` element contains one `HostedZoneSummary` element for each hosted zone that the specified Amazon VPC is associated with. Each `HostedZoneSummary` element contains the hosted zone name and ID, and information about who owns the hosted zone.

## Contents
<a name="API_HostedZoneSummary_Contents"></a>

 ** HostedZoneId **   <a name="Route53-Type-HostedZoneSummary-HostedZoneId"></a>
The Route 53 hosted zone ID of a private hosted zone that the specified VPC is associated with.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Name **   <a name="Route53-Type-HostedZoneSummary-Name"></a>
The name of the private hosted zone, such as `example.com`.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** Owner **   <a name="Route53-Type-HostedZoneSummary-Owner"></a>
The owner of a private hosted zone that the specified VPC is associated with. The owner can be either an AWS account or an AWS service.
Type: [HostedZoneOwner](API_HostedZoneOwner.md) object
Required: Yes

## See Also
<a name="API_HostedZoneSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
