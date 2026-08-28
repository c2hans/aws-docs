---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Describes one specific validation failure for an input member.

## Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** message **   <a name="securityagent-Type-ValidationExceptionField-message"></a>
A detailed description of the validation failure.
Type: String
Required: Yes

 ** path **   <a name="securityagent-Type-ValidationExceptionField-path"></a>
A JSONPointer expression to the structure member whose value failed to satisfy the modeled constraint.
Type: String
Required: Yes

## See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ValidationExceptionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
