---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_SecurityRequirementPackSummary.html
---

# SecurityRequirementPackSummary
<a name="API_SecurityRequirementPackSummary"></a>

Contains summary information about a security requirement pack.

## Contents
<a name="API_SecurityRequirementPackSummary_Contents"></a>

 ** createdAt **   <a name="securityagent-Type-SecurityRequirementPackSummary-createdAt"></a>
The date and time the security requirement pack was created, in UTC format.
Type: Timestamp
Required: Yes

 ** managementType **   <a name="securityagent-Type-SecurityRequirementPackSummary-managementType"></a>
The management type of the pack.
Type: String
Valid Values: `AWS_MANAGED | CUSTOMER_MANAGED`
Required: Yes

 ** name **   <a name="securityagent-Type-SecurityRequirementPackSummary-name"></a>
The name of the security requirement pack.
Type: String
Required: Yes

 ** packId **   <a name="securityagent-Type-SecurityRequirementPackSummary-packId"></a>
The unique identifier of the security requirement pack.
Type: String
Required: Yes

 ** status **   <a name="securityagent-Type-SecurityRequirementPackSummary-status"></a>
The status of the security requirement pack.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** updatedAt **   <a name="securityagent-Type-SecurityRequirementPackSummary-updatedAt"></a>
The date and time the security requirement pack was last updated, in UTC format.
Type: Timestamp
Required: Yes

 ** description **   <a name="securityagent-Type-SecurityRequirementPackSummary-description"></a>
A description of the security requirement pack.
Type: String
Required: No

 ** vendorName **   <a name="securityagent-Type-SecurityRequirementPackSummary-vendorName"></a>
The vendor name for AWS managed packs.
Type: String
Required: No

## See Also
<a name="API_SecurityRequirementPackSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/SecurityRequirementPackSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/SecurityRequirementPackSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/SecurityRequirementPackSummary)
