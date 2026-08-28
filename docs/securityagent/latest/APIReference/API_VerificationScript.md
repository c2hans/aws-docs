---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_VerificationScript.html
---

# VerificationScript
<a name="API_VerificationScript"></a>

Contains metadata for a verification script that can be used to reproduce a security finding.

## Contents
<a name="API_VerificationScript_Contents"></a>

 ** envVars **   <a name="securityagent-Type-VerificationScript-envVars"></a>
The list of environment variables required to run the verification script.
Type: Array of [VerificationScriptEnvVar](API_VerificationScriptEnvVar.md) objects
Required: No

 ** instructions **   <a name="securityagent-Type-VerificationScript-instructions"></a>
Instructions for running the verification script, including prerequisites and how to interpret results.
Type: String
Required: No

 ** scriptType **   <a name="securityagent-Type-VerificationScript-scriptType"></a>
The type of script. Valid values are python and bash.
Type: String
Required: No

 ** scriptUrl **   <a name="securityagent-Type-VerificationScript-scriptUrl"></a>
URL to download the verification script.
Type: String
Required: No

## See Also
<a name="API_VerificationScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/VerificationScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/VerificationScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/VerificationScript)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
