---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_PolicySummary.html
---

# PolicySummary
<a name="API_PolicySummary"></a>

Contains summary information about a resilience policy.

## Contents
<a name="API_PolicySummary_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-PolicySummary-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** policyArn **   <a name="ngresiliencehub-Type-PolicySummary-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** associatedServiceCount **   <a name="ngresiliencehub-Type-PolicySummary-associatedServiceCount"></a>
The number of services associated with this policy.
Type: Integer
Required: No

 ** availabilitySlo **   <a name="ngresiliencehub-Type-PolicySummary-availabilitySlo"></a>
The availability SLO defined in the policy.
Type: [AvailabilitySlo](API_AvailabilitySlo.md) object
Required: No

 ** createdAt **   <a name="ngresiliencehub-Type-PolicySummary-createdAt"></a>
The timestamp when the policy was created.
Type: Timestamp
Required: No

 ** dataRecovery **   <a name="ngresiliencehub-Type-PolicySummary-dataRecovery"></a>
The data recovery targets defined in the policy.
Type: [DataRecoveryTargets](API_DataRecoveryTargets.md) object
Required: No

 ** multiAz **   <a name="ngresiliencehub-Type-PolicySummary-multiAz"></a>
The multi-AZ disaster recovery targets defined in the policy.
Type: [MultiAzTargets](API_MultiAzTargets.md) object
Required: No

 ** multiRegion **   <a name="ngresiliencehub-Type-PolicySummary-multiRegion"></a>
The multi-Region disaster recovery targets defined in the policy.
Type: [MultiRegionTargets](API_MultiRegionTargets.md) object
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-PolicySummary-updatedAt"></a>
The timestamp when the policy was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_PolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/PolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/PolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/PolicySummary)
