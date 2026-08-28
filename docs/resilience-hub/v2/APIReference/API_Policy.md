---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Policy.html
---

# Policy
<a name="API_Policy"></a>

Represents a resilience policy that defines availability and disaster recovery requirements.

## Contents
<a name="API_Policy_Contents"></a>

 ** name **   <a name="ngresiliencehub-Type-Policy-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** policyArn **   <a name="ngresiliencehub-Type-Policy-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** associatedServiceCount **   <a name="ngresiliencehub-Type-Policy-associatedServiceCount"></a>
The number of services associated with this policy.
Type: Integer
Required: No

 ** availabilitySlo **   <a name="ngresiliencehub-Type-Policy-availabilitySlo"></a>
The availability SLO defined in the policy.
Type: [AvailabilitySlo](API_AvailabilitySlo.md) object
Required: No

 ** createdAt **   <a name="ngresiliencehub-Type-Policy-createdAt"></a>
The timestamp when the policy was created.
Type: Timestamp
Required: No

 ** dataRecovery **   <a name="ngresiliencehub-Type-Policy-dataRecovery"></a>
The data recovery targets defined in the policy.
Type: [DataRecoveryTargets](API_DataRecoveryTargets.md) object
Required: No

 ** description **   <a name="ngresiliencehub-Type-Policy-description"></a>
Resource description for services and policies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 615.
Required: No

 ** kmsKeyId **   <a name="ngresiliencehub-Type-Policy-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** multiAz **   <a name="ngresiliencehub-Type-Policy-multiAz"></a>
The multi-AZ disaster recovery targets defined in the policy.
Type: [MultiAzTargets](API_MultiAzTargets.md) object
Required: No

 ** multiRegion **   <a name="ngresiliencehub-Type-Policy-multiRegion"></a>
The multi-Region disaster recovery targets defined in the policy.
Type: [MultiRegionTargets](API_MultiRegionTargets.md) object
Required: No

 ** tags **   <a name="ngresiliencehub-Type-Policy-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-Policy-updatedAt"></a>
The timestamp when the policy was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Policy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Policy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Policy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Policy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
