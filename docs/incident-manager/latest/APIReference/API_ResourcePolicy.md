---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ResourcePolicy.html
---

# ResourcePolicy
<a name="API_ResourcePolicy"></a>

The resource policy that allows Incident Manager to perform actions on resources on your behalf.

## Contents
<a name="API_ResourcePolicy_Contents"></a>

 ** policyDocument **   <a name="IncidentManager-Type-ResourcePolicy-policyDocument"></a>
The JSON blob that describes the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: Yes

 ** policyId **   <a name="IncidentManager-Type-ResourcePolicy-policyId"></a>
The ID of the resource policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** ramResourceShareRegion **   <a name="IncidentManager-Type-ResourcePolicy-ramResourceShareRegion"></a>
The AWS Region that policy allows resources to be used in.
Type: String
Required: Yes

## See Also
<a name="API_ResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ResourcePolicy)
