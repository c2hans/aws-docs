---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkPackageInfo.html
---

# ListSolNetworkPackageInfo
<a name="API_ListSolNetworkPackageInfo"></a>

Details of a network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

## Contents
<a name="API_ListSolNetworkPackageInfo_Contents"></a>

 ** arn **   <a name="TNB-Type-ListSolNetworkPackageInfo-arn"></a>
Network package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-package/np-[a-f0-9]{17})`
Required: Yes

 ** id **   <a name="TNB-Type-ListSolNetworkPackageInfo-id"></a>
ID of the individual network package.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: Yes

 ** metadata **   <a name="TNB-Type-ListSolNetworkPackageInfo-metadata"></a>
The metadata of the network package.
Type: [ListSolNetworkPackageMetadata](API_ListSolNetworkPackageMetadata.md) object
Required: Yes

 ** nsdOnboardingState **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdOnboardingState"></a>
Onboarding state of the network service descriptor in the network package.
Type: String
Valid Values: `CREATED | ONBOARDED | ERROR`
Required: Yes

 ** nsdOperationalState **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdOperationalState"></a>
Operational state of the network service descriptor in the network package.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** nsdUsageState **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdUsageState"></a>
Usage state of the network service descriptor in the network package.
Type: String
Valid Values: `IN_USE | NOT_IN_USE`
Required: Yes

 ** nsdDesigner **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdDesigner"></a>
Designer of the onboarded network service descriptor in the network package.
Type: String
Required: No

 ** nsdId **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdId"></a>
ID of the network service descriptor on which the network package is based.
Type: String
Required: No

 ** nsdInvariantId **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdInvariantId"></a>
Identifies a network service descriptor in a version independent manner.
Type: String
Required: No

 ** nsdName **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdName"></a>
Name of the onboarded network service descriptor in the network package.
Type: String
Required: No

 ** nsdVersion **   <a name="TNB-Type-ListSolNetworkPackageInfo-nsdVersion"></a>
Version of the onboarded network service descriptor in the network package.
Type: String
Required: No

 ** vnfPkgIds **   <a name="TNB-Type-ListSolNetworkPackageInfo-vnfPkgIds"></a>
Identifies the function package for the function package descriptor referenced by the onboarded network package.
Type: Array of strings
Pattern: `fp-[a-f0-9]{17}`
Required: No

## See Also
<a name="API_ListSolNetworkPackageInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolNetworkPackageInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolNetworkPackageInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolNetworkPackageInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
