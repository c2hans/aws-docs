---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRoute53HostedZoneDetails.html
---

# AwsRoute53HostedZoneDetails
<a name="API_AwsRoute53HostedZoneDetails"></a>

 Provides details about a specified Amazon Route 53 hosted zone, including the four name servers assigned to the hosted zone. A hosted zone represents a collection of records that can be managed together, belonging to a single parent domain name.

## Contents
<a name="API_AwsRoute53HostedZoneDetails_Contents"></a>

 ** HostedZone **   <a name="securityhub-Type-AwsRoute53HostedZoneDetails-HostedZone"></a>
 An object that contains information about the specified hosted zone.
Type: [AwsRoute53HostedZoneObjectDetails](API_AwsRoute53HostedZoneObjectDetails.md) object
Required: No

 ** NameServers **   <a name="securityhub-Type-AwsRoute53HostedZoneDetails-NameServers"></a>
 An object that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** QueryLoggingConfig **   <a name="securityhub-Type-AwsRoute53HostedZoneDetails-QueryLoggingConfig"></a>
 An array that contains one `QueryLoggingConfig` element for each DNS query logging configuration that is associated with the current AWS account.
Type: [AwsRoute53QueryLoggingConfigDetails](API_AwsRoute53QueryLoggingConfigDetails.md) object
Required: No

 ** Vpcs **   <a name="securityhub-Type-AwsRoute53HostedZoneDetails-Vpcs"></a>
 An object that contains information about the Amazon Virtual Private Clouds (Amazon VPCs) that are associated with the specified hosted zone.
Type: Array of [AwsRoute53HostedZoneVpcDetails](API_AwsRoute53HostedZoneVpcDetails.md) objects
Required: No

## See Also
<a name="API_AwsRoute53HostedZoneDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRoute53HostedZoneDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRoute53HostedZoneDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRoute53HostedZoneDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
