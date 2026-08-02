---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResiliencyPolicy.html
---

# ResiliencyPolicy
<a name="API_ResiliencyPolicy"></a>

Defines a resiliency policy.

**Note**
 AWS Resilience Hub allows you to provide a value of zero for `rtoInSecs` and `rpoInSecs` of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for `rtoInSecs` and `rpoInSecs`, the estimated workload RTO and estimated workload RPO result will be near zero and the **Compliance status** for your application will be set to **Policy breached**.

## Contents
<a name="API_ResiliencyPolicy_Contents"></a>

 ** creationTime **   <a name="resiliencehub-Type-ResiliencyPolicy-creationTime"></a>
Date and time when the resiliency policy was created.
Type: Timestamp
Required: No

 ** dataLocationConstraint **   <a name="resiliencehub-Type-ResiliencyPolicy-dataLocationConstraint"></a>
Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
Type: String
Valid Values: `AnyLocation | SameContinent | SameCountry`
Required: No

 ** estimatedCostTier **   <a name="resiliencehub-Type-ResiliencyPolicy-estimatedCostTier"></a>
Specifies the estimated cost tier of the resiliency policy.
Type: String
Valid Values: `L1 | L2 | L3 | L4`
Required: No

 ** policy **   <a name="resiliencehub-Type-ResiliencyPolicy-policy"></a>
The resiliency policy.
Type: String to [FailurePolicy](API_FailurePolicy.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** policyArn **   <a name="resiliencehub-Type-ResiliencyPolicy-policyArn"></a>
Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:resiliency-policy/`policy-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** policyDescription **   <a name="resiliencehub-Type-ResiliencyPolicy-policyDescription"></a>
Description of the resiliency policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** policyName **   <a name="resiliencehub-Type-ResiliencyPolicy-policyName"></a>
The name of the policy
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** tags **   <a name="resiliencehub-Type-ResiliencyPolicy-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** tier **   <a name="resiliencehub-Type-ResiliencyPolicy-tier"></a>
The tier for this resiliency policy, ranging from the highest severity (`MissionCritical`) to lowest (`NonCritical`).
Type: String
Valid Values: `MissionCritical | Critical | Important | CoreServices | NonCritical | NotApplicable`
Required: No

## See Also
<a name="API_ResiliencyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ResiliencyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ResiliencyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ResiliencyPolicy)
