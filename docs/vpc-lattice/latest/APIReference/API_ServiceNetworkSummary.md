---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ServiceNetworkSummary.html
---

# ServiceNetworkSummary
<a name="API_ServiceNetworkSummary"></a>

Summary information about a service network.

## Contents
<a name="API_ServiceNetworkSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ServiceNetworkSummary-arn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ServiceNetworkSummary-createdAt"></a>
The date and time that the service network was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** id **   <a name="vpclattice-Type-ServiceNetworkSummary-id"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-ServiceNetworkSummary-lastUpdatedAt"></a>
The date and time that the service network was last updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** name **   <a name="vpclattice-Type-ServiceNetworkSummary-name"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** numberOfAssociatedResourceConfigurations **   <a name="vpclattice-Type-ServiceNetworkSummary-numberOfAssociatedResourceConfigurations"></a>
The number of resource configurations associated with a service network.
Type: Long
Required: No

 ** numberOfAssociatedServices **   <a name="vpclattice-Type-ServiceNetworkSummary-numberOfAssociatedServices"></a>
The number of services associated with the service network.
Type: Long
Required: No

 ** numberOfAssociatedVPCs **   <a name="vpclattice-Type-ServiceNetworkSummary-numberOfAssociatedVPCs"></a>
The number of VPCs associated with the service network.
Type: Long
Required: No

## See Also
<a name="API_ServiceNetworkSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ServiceNetworkSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ServiceNetworkSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ServiceNetworkSummary)
