---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ReferenceInput.html
---

# ReferenceInput
<a name="API_ReferenceInput"></a>

Reference information linking a task to external systems - for input with validation

## Contents
<a name="API_ReferenceInput_Contents"></a>

 ** associationId **   <a name="devopsagent-Type-ReferenceInput-associationId"></a>
Association identifier of the external system
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** referenceId **   <a name="devopsagent-Type-ReferenceInput-referenceId"></a>
The unique identifier in the external system
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** referenceUrl **   <a name="devopsagent-Type-ReferenceInput-referenceUrl"></a>
URL to access the reference in the external system
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** system **   <a name="devopsagent-Type-ReferenceInput-system"></a>
The name of the external system
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** title **   <a name="devopsagent-Type-ReferenceInput-title"></a>
Optional title for the reference
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_ReferenceInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ReferenceInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ReferenceInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ReferenceInput)
