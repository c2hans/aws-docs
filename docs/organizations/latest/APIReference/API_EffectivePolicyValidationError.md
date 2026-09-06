---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_EffectivePolicyValidationError.html
---

# EffectivePolicyValidationError
<a name="API_EffectivePolicyValidationError"></a>

Contains details about the validation errors that occurred when generating or enforcing an [effective policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_effective.html), such as which policies contributed to the error and location of the error.

## Contents
<a name="API_EffectivePolicyValidationError_Contents"></a>

 ** ContributingPolicies **   <a name="organizations-Type-EffectivePolicyValidationError-ContributingPolicies"></a>
The individual policies [inherited](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html) and [attached](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html) to the account which contributed to the validation error.
Type: Array of strings
Length Constraints: Maximum length of 130.
Pattern: `^p-[0-9a-zA-Z_]{8,128}$`
Required: No

 ** ErrorCode **   <a name="organizations-Type-EffectivePolicyValidationError-ErrorCode"></a>
The error code for the validation error. For example, `ELEMENTS_TOO_MANY`.
Type: String
Required: No

 ** ErrorMessage **   <a name="organizations-Type-EffectivePolicyValidationError-ErrorMessage"></a>
The error message for the validation error.
Type: String
Required: No

 ** PathToError **   <a name="organizations-Type-EffectivePolicyValidationError-PathToError"></a>
The path within the effective policy where the validation error occurred.
Type: String
Required: No

## See Also
<a name="API_EffectivePolicyValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/EffectivePolicyValidationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/EffectivePolicyValidationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/EffectivePolicyValidationError)
