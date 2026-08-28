---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneConfig.html
---

# HostedZoneConfig
<a name="API_HostedZoneConfig"></a>

A complex type that contains an optional comment about your hosted zone. If you don't want to specify a comment, omit both the `HostedZoneConfig` and `Comment` elements.

## Contents
<a name="API_HostedZoneConfig_Contents"></a>

 ** Comment **   <a name="Route53-Type-HostedZoneConfig-Comment"></a>
Any comments that you want to include about the hosted zone.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** PrivateZone **   <a name="Route53-Type-HostedZoneConfig-PrivateZone"></a>
A value that indicates whether this is a private hosted zone.
Type: Boolean
Required: No

## See Also
<a name="API_HostedZoneConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
