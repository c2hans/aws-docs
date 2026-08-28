---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ActionRemoteIpDetails.html
---

# ActionRemoteIpDetails
<a name="API_ActionRemoteIpDetails"></a>

For `AwsApiAction`, `NetworkConnectionAction`, and `PortProbeAction`, `RemoteIpDetails` provides information about the remote IP address that was involved in the action.

## Contents
<a name="API_ActionRemoteIpDetails_Contents"></a>

 ** City **   <a name="securityhub-Type-ActionRemoteIpDetails-City"></a>
The city where the remote IP address is located.
Type: [City](API_City.md) object
Required: No

 ** Country **   <a name="securityhub-Type-ActionRemoteIpDetails-Country"></a>
The country where the remote IP address is located.
Type: [Country](API_Country.md) object
Required: No

 ** GeoLocation **   <a name="securityhub-Type-ActionRemoteIpDetails-GeoLocation"></a>
The coordinates of the location of the remote IP address.
Type: [GeoLocation](API_GeoLocation.md) object
Required: No

 ** IpAddressV4 **   <a name="securityhub-Type-ActionRemoteIpDetails-IpAddressV4"></a>
The IP address.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Organization **   <a name="securityhub-Type-ActionRemoteIpDetails-Organization"></a>
The internet service provider (ISP) organization associated with the remote IP address.
Type: [IpOrganizationDetails](API_IpOrganizationDetails.md) object
Required: No

## See Also
<a name="API_ActionRemoteIpDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ActionRemoteIpDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ActionRemoteIpDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ActionRemoteIpDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
