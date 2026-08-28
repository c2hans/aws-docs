---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionPackageInfo.html
---

# ListSolFunctionPackageInfo
<a name="API_ListSolFunctionPackageInfo"></a>

Information about a function package.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

## Contents
<a name="API_ListSolFunctionPackageInfo_Contents"></a>

 ** arn **   <a name="TNB-Type-ListSolFunctionPackageInfo-arn"></a>
Function package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-package/fp-[a-f0-9]{17})`
Required: Yes

 ** id **   <a name="TNB-Type-ListSolFunctionPackageInfo-id"></a>
ID of the function package.
Type: String
Pattern: `fp-[a-f0-9]{17}`
Required: Yes

 ** onboardingState **   <a name="TNB-Type-ListSolFunctionPackageInfo-onboardingState"></a>
Onboarding state of the function package.
Type: String
Valid Values: `CREATED | ONBOARDED | ERROR`
Required: Yes

 ** operationalState **   <a name="TNB-Type-ListSolFunctionPackageInfo-operationalState"></a>
Operational state of the function package.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** usageState **   <a name="TNB-Type-ListSolFunctionPackageInfo-usageState"></a>
Usage state of the function package.
Type: String
Valid Values: `IN_USE | NOT_IN_USE`
Required: Yes

 ** metadata **   <a name="TNB-Type-ListSolFunctionPackageInfo-metadata"></a>
The metadata of the function package.
Type: [ListSolFunctionPackageMetadata](API_ListSolFunctionPackageMetadata.md) object
Required: No

 ** vnfdId **   <a name="TNB-Type-ListSolFunctionPackageInfo-vnfdId"></a>
Identifies the function package and the function package descriptor.
Type: String
Required: No

 ** vnfdVersion **   <a name="TNB-Type-ListSolFunctionPackageInfo-vnfdVersion"></a>
Identifies the version of the function package descriptor.
Type: String
Required: No

 ** vnfProductName **   <a name="TNB-Type-ListSolFunctionPackageInfo-vnfProductName"></a>
The product name for the network function.
Type: String
Required: No

 ** vnfProvider **   <a name="TNB-Type-ListSolFunctionPackageInfo-vnfProvider"></a>
Provider of the function package and the function package descriptor.
Type: String
Required: No

## See Also
<a name="API_ListSolFunctionPackageInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolFunctionPackageInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolFunctionPackageInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolFunctionPackageInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
