---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RegisteredDomainDelegationInfo.html
---

# RegisteredDomainDelegationInfo
<a name="API_RegisteredDomainDelegationInfo"></a>

Describes the delegation state of an Amazon Route 53 registered domain to Amazon Lightsail.

When you delegate an Amazon Route 53 registered domain to Lightsail, you can manage the DNS of the domain using a Lightsail DNS zone. You no longer use the Route 53 hosted zone to manage the DNS of the domain. To delegate the domain, Lightsail automatically updates the domain's name servers in Route 53 to the name servers of the Lightsail DNS zone. Then, Lightsail automatically deletes the Route 53 hosted zone for the domain.

All of the following conditions must be true for automatic domain delegation to be successful:
+ The registered domain must be in the same AWS account as the Lightsail account making the request.
+ The user or entity making the request must have permission to manage domains in Route 53.
+ The Route 53 hosted zone for the domain must be empty. It cannot contain DNS records other than start of authority (SOA) and name server records.

If automatic domain delegation fails, or if you manage the DNS of your domain using a service other than Route 53, then you must manually add the Lightsail DNS zone name servers to your domain in order to delegate management of its DNS to Lightsail. For more information, see [Creating a DNS zone to manage your domain’s records in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-create-dns-entry) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_RegisteredDomainDelegationInfo_Contents"></a>

 ** nameServersUpdateState **   <a name="Lightsail-Type-RegisteredDomainDelegationInfo-nameServersUpdateState"></a>
An object that describes the state of the name server records that are automatically added to the Route 53 domain by Lightsail.
Type: [NameServersUpdateState](API_NameServersUpdateState.md) object
Required: No

 ** r53HostedZoneDeletionState **   <a name="Lightsail-Type-RegisteredDomainDelegationInfo-r53HostedZoneDeletionState"></a>
Describes the deletion state of an Amazon Route 53 hosted zone for a domain that is being automatically delegated to an Amazon Lightsail DNS zone.
Type: [R53HostedZoneDeletionState](API_R53HostedZoneDeletionState.md) object
Required: No

## See Also
<a name="API_RegisteredDomainDelegationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RegisteredDomainDelegationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RegisteredDomainDelegationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RegisteredDomainDelegationInfo)
