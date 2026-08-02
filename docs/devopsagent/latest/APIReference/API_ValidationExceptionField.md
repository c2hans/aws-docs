---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Describes one specific validation failure for an input member.

## Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** message **   <a name="devopsagent-Type-ValidationExceptionField-message"></a>
A detailed description of the validation failure.
Type: String
Required: Yes

 ** path **   <a name="devopsagent-Type-ValidationExceptionField-path"></a>
A JSONPointer expression to the structure member whose value failed to satisfy the modeled constraints.
Type: String
Required: Yes

## See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ValidationExceptionField)
