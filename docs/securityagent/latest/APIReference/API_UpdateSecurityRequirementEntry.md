---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateSecurityRequirementEntry.html
---

# UpdateSecurityRequirementEntry
<a name="API_UpdateSecurityRequirementEntry"></a>

Contains the details for updating an existing security requirement within a pack. The name is an immutable identifier used to locate the requirement and cannot be modified.

## Contents
<a name="API_UpdateSecurityRequirementEntry_Contents"></a>

 ** name **   <a name="securityagent-Type-UpdateSecurityRequirementEntry-name"></a>
The name of the security requirement to update. This is an immutable identifier and cannot be changed once the requirement is created.
Type: String
Required: Yes

 ** description **   <a name="securityagent-Type-UpdateSecurityRequirementEntry-description"></a>
The updated description of the security requirement.
Type: String
Required: No

 ** domain **   <a name="securityagent-Type-UpdateSecurityRequirementEntry-domain"></a>
The updated security domain the requirement belongs to.
Type: String
Required: No

 ** evaluation **   <a name="securityagent-Type-UpdateSecurityRequirementEntry-evaluation"></a>
The updated evaluation criteria used to assess compliance with this requirement.
Type: String
Required: No

 ** remediation **   <a name="securityagent-Type-UpdateSecurityRequirementEntry-remediation"></a>
The updated remediation steps when the requirement is not met.
Type: String
Required: No

## See Also
<a name="API_UpdateSecurityRequirementEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateSecurityRequirementEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateSecurityRequirementEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateSecurityRequirementEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
