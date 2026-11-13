---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesPolicyViolation.html
---

# KubernetesPolicyViolation
<a name="API_KubernetesPolicyViolation"></a>

Contains an assessment of a Kubernetes policy violation.

## Contents
<a name="API_KubernetesPolicyViolation_Contents"></a>

 ** affectedResource **   <a name="guardduty-Type-KubernetesPolicyViolation-affectedResource"></a>
The Kubernetes resource that the violation affects.
Type: String
Required: No

 ** exposureVector **   <a name="guardduty-Type-KubernetesPolicyViolation-exposureVector"></a>
How the misconfiguration exposes the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** grantedAccess **   <a name="guardduty-Type-KubernetesPolicyViolation-grantedAccess"></a>
The access that the violation grants.
Type: String
Required: No

 ** misconfigurationImpact **   <a name="guardduty-Type-KubernetesPolicyViolation-misconfigurationImpact"></a>
The potential impact of the misconfiguration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** subject **   <a name="guardduty-Type-KubernetesPolicyViolation-subject"></a>
The Kubernetes subject, such as a user, a group, or a service account, that the violation involves.
Type: String
Required: No

 ** violationType **   <a name="guardduty-Type-KubernetesPolicyViolation-violationType"></a>
The type of the violation.
Type: String
Required: No

## See Also
<a name="API_KubernetesPolicyViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesPolicyViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesPolicyViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesPolicyViolation)
