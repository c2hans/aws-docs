---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_EnvironmentConfiguration.html
---

# EnvironmentConfiguration
<a name="API_EnvironmentConfiguration"></a>

Environment-level operating policy.

## Contents
<a name="API_EnvironmentConfiguration_Contents"></a>

 ** network **   <a name="continuum-Type-EnvironmentConfiguration-network"></a>
Network policy for agent execution.
Type: [EnvironmentNetworkConfiguration](API_EnvironmentNetworkConfiguration.md) object
Required: No

 ** patchCreationPolicy **   <a name="continuum-Type-EnvironmentConfiguration-patchCreationPolicy"></a>
The patch Creation Policy.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** scanFrequency **   <a name="continuum-Type-EnvironmentConfiguration-scanFrequency"></a>
The scan Frequency.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `P([0-9]+Y([0-9]+M)?([0-9]+D)?(T([0-9]+H([0-9]+M)?([0-9]+S)?|[0-9]+M([0-9]+S)?|[0-9]+S))?|[0-9]+M([0-9]+D)?(T([0-9]+H([0-9]+M)?([0-9]+S)?|[0-9]+M([0-9]+S)?|[0-9]+S))?|[0-9]+D(T([0-9]+H([0-9]+M)?([0-9]+S)?|[0-9]+M([0-9]+S)?|[0-9]+S))?|T([0-9]+H([0-9]+M)?([0-9]+S)?|[0-9]+M([0-9]+S)?|[0-9]+S))`
Required: No

## See Also
<a name="API_EnvironmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/EnvironmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/EnvironmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/EnvironmentConfiguration)
