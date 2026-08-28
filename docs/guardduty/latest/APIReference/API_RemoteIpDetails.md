---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RemoteIpDetails.html
---

# RemoteIpDetails
<a name="API_RemoteIpDetails"></a>

Contains information about the remote IP address of the connection.

## Contents
<a name="API_RemoteIpDetails_Contents"></a>

 ** city **   <a name="guardduty-Type-RemoteIpDetails-city"></a>
The city information of the remote IP address.
Type: [City](API_City.md) object
Required: No

 ** country **   <a name="guardduty-Type-RemoteIpDetails-country"></a>
The country code of the remote IP address.
Type: [Country](API_Country.md) object
Required: No

 ** geoLocation **   <a name="guardduty-Type-RemoteIpDetails-geoLocation"></a>
The location information of the remote IP address.
Type: [GeoLocation](API_GeoLocation.md) object
Required: No

 ** ipAddressV4 **   <a name="guardduty-Type-RemoteIpDetails-ipAddressV4"></a>
The IPv4 remote address of the connection.
Type: String
Required: No

 ** ipAddressV6 **   <a name="guardduty-Type-RemoteIpDetails-ipAddressV6"></a>
The IPv6 remote address of the connection.
Type: String
Required: No

 ** organization **   <a name="guardduty-Type-RemoteIpDetails-organization"></a>
The ISP organization information of the remote IP address.
Type: [Organization](API_Organization.md) object
Required: No

## See Also
<a name="API_RemoteIpDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RemoteIpDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RemoteIpDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RemoteIpDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
