---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZone.html
---

# HostedZone
<a name="API_HostedZone"></a>

A complex type that contains general information about the hosted zone.

## Contents
<a name="API_HostedZone_Contents"></a>

 ** CallerReference **   <a name="Route53-Type-HostedZone-CallerReference"></a>
The value that you specified for `CallerReference` when you created the hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Id **   <a name="Route53-Type-HostedZone-Id"></a>
The ID that Amazon Route 53 assigned to the hosted zone when you created it.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Name **   <a name="Route53-Type-HostedZone-Name"></a>
The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
For information about how to specify characters other than `a-z`, `0-9`, and `-` (hyphen) and how to specify internationalized domain names, see [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html).
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** Config **   <a name="Route53-Type-HostedZone-Config"></a>
A complex type that includes the `Comment` and `PrivateZone` elements. If you omitted the `HostedZoneConfig` and `Comment` elements from the request, the `Config` and `Comment` elements don't appear in the response.
Type: [HostedZoneConfig](API_HostedZoneConfig.md) object
Required: No

 ** Features **   <a name="Route53-Type-HostedZone-Features"></a>
The features configuration for the hosted zone, including accelerated recovery settings and status information.
Type: [HostedZoneFeatures](API_HostedZoneFeatures.md) object
Required: No

 ** LinkedService **   <a name="Route53-Type-HostedZone-LinkedService"></a>
If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Route 53.
Type: [LinkedService](API_LinkedService.md) object
Required: No

 ** ResourceRecordSetCount **   <a name="Route53-Type-HostedZone-ResourceRecordSetCount"></a>
The number of resource record sets in the hosted zone.
Type: Long
Required: No

## See Also
<a name="API_HostedZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZone)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
