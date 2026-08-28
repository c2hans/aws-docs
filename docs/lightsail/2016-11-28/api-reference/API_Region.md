---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Region.html
---

# Region
<a name="API_Region"></a>

Describes the AWS Region.

## Contents
<a name="API_Region_Contents"></a>

 ** availabilityZones **   <a name="Lightsail-Type-Region-availabilityZones"></a>
The Availability Zones. Follows the format `us-east-2a` (case-sensitive).
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects
Required: No

 ** continentCode **   <a name="Lightsail-Type-Region-continentCode"></a>
The continent code (`NA`, meaning North America).
Type: String
Required: No

 ** description **   <a name="Lightsail-Type-Region-description"></a>
The description of the AWS Region (`This region is recommended to serve users in the eastern United States and eastern Canada`).
Type: String
Required: No

 ** displayName **   <a name="Lightsail-Type-Region-displayName"></a>
The display name (`Ohio`).
Type: String
Required: No

 ** name **   <a name="Lightsail-Type-Region-name"></a>
The region name (`us-east-2`).
Type: String
Valid Values: `us-east-1 | us-east-2 | us-west-1 | us-west-2 | eu-west-1 | eu-west-2 | eu-west-3 | eu-central-1 | eu-north-1 | ca-central-1 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | ap-northeast-2 | ap-southeast-3 | ap-southeast-5`
Required: No

 ** relationalDatabaseAvailabilityZones **   <a name="Lightsail-Type-Region-relationalDatabaseAvailabilityZones"></a>
The Availability Zones for databases. Follows the format `us-east-2a` (case-sensitive).
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects
Required: No

## See Also
<a name="API_Region_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Region)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Region)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Region)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
