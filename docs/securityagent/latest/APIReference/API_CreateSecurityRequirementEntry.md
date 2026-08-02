---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateSecurityRequirementEntry.html
---

# CreateSecurityRequirementEntry
<a name="API_CreateSecurityRequirementEntry"></a>

Contains the details for a security requirement to create within a pack.

## Contents
<a name="API_CreateSecurityRequirementEntry_Contents"></a>

 ** description **   <a name="securityagent-Type-CreateSecurityRequirementEntry-description"></a>
A description of the security requirement.
Type: String
Required: Yes

 ** domain **   <a name="securityagent-Type-CreateSecurityRequirementEntry-domain"></a>
The security domain the requirement belongs to.
Type: String
Required: Yes

 ** evaluation **   <a name="securityagent-Type-CreateSecurityRequirementEntry-evaluation"></a>
The evaluation criteria used to assess compliance with this requirement.
Type: String
Required: Yes

 ** name **   <a name="securityagent-Type-CreateSecurityRequirementEntry-name"></a>
The name of the security requirement.
Type: String
Required: Yes

 ** remediation **   <a name="securityagent-Type-CreateSecurityRequirementEntry-remediation"></a>
The recommended remediation steps when the requirement is not met.
Type: String
Required: No

## See Also
<a name="API_CreateSecurityRequirementEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateSecurityRequirementEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateSecurityRequirementEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateSecurityRequirementEntry)
