---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunPolicySnapshot.html
---

# TestRunPolicySnapshot
<a name="API_TestRunPolicySnapshot"></a>

A snapshot of the resilience policy captured onto a test run from the service when the run was started.

## Contents
<a name="API_TestRunPolicySnapshot_Contents"></a>

 ** availabilitySlo **   <a name="ngresiliencehub-Type-TestRunPolicySnapshot-availabilitySlo"></a>
The availability SLO targets.
Type: [AvailabilitySlo](API_AvailabilitySlo.md) object
Required: No

 ** dataRecovery **   <a name="ngresiliencehub-Type-TestRunPolicySnapshot-dataRecovery"></a>
The data recovery targets.
Type: [DataRecoveryTargets](API_DataRecoveryTargets.md) object
Required: No

 ** multiAz **   <a name="ngresiliencehub-Type-TestRunPolicySnapshot-multiAz"></a>
The multi-AZ resilience targets.
Type: [MultiAzTargets](API_MultiAzTargets.md) object
Required: No

 ** multiRegion **   <a name="ngresiliencehub-Type-TestRunPolicySnapshot-multiRegion"></a>
The multi-Region resilience targets.
Type: [MultiRegionTargets](API_MultiRegionTargets.md) object
Required: No

 ** name **   <a name="ngresiliencehub-Type-TestRunPolicySnapshot-name"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** policyArn **   <a name="ngresiliencehub-Type-TestRunPolicySnapshot-policyArn"></a>
The ARN of the policy.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

## See Also
<a name="API_TestRunPolicySnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunPolicySnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunPolicySnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunPolicySnapshot)
