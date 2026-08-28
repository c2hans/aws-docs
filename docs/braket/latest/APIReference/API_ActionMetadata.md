---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_ActionMetadata.html
---

# ActionMetadata
<a name="API_ActionMetadata"></a>

Contains metadata about the quantum task action, including the action type and program statistics.

## Contents
<a name="API_ActionMetadata_Contents"></a>

 ** actionType **   <a name="braket-Type-ActionMetadata-actionType"></a>
The type of action associated with the quantum task.
Type: String
Required: Yes

 ** executableCount **   <a name="braket-Type-ActionMetadata-executableCount"></a>
The number of executables in a program set. This is only available for a program set.
Type: Long
Required: No

 ** programCount **   <a name="braket-Type-ActionMetadata-programCount"></a>
The number of programs in a program set. This is only available for a program set.
Type: Long
Required: No

## See Also
<a name="API_ActionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/ActionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/ActionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/ActionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
