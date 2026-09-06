---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Step.html
---

# Step
<a name="API_Step"></a>

Represents a step in the pentest job execution pipeline. Steps include preflight, static analysis, pentest, and finalizing.

## Contents
<a name="API_Step_Contents"></a>

 ** createdAt **   <a name="securityagent-Type-Step-createdAt"></a>
The date and time the step was created, in UTC format.
Type: Timestamp
Required: No

 ** name **   <a name="securityagent-Type-Step-name"></a>
The name of the step. Valid values include PREFLIGHT, STATIC\_ANALYSIS, PENTEST, VALIDATION, and FINALIZING.
Type: String
Valid Values: `PREFLIGHT | STATIC_ANALYSIS | PENTEST | FINALIZING | VALIDATION`
Required: No

 ** status **   <a name="securityagent-Type-Step-status"></a>
The current status of the step.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | FAILED | STOPPED`
Required: No

 ** updatedAt **   <a name="securityagent-Type-Step-updatedAt"></a>
The date and time the step was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_Step_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Step)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Step)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Step)
