---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModificationState.html
---

# ModificationState
<a name="API_ModificationState"></a>

Describes a WorkSpace modification.

## Contents
<a name="API_ModificationState_Contents"></a>

 ** Resource **   <a name="WorkSpaces-Type-ModificationState-Resource"></a>
The WorkSpace property being modified.
Type: String
Valid Values: `ROOT_VOLUME | USER_VOLUME | COMPUTE_TYPE | PROTOCOL | NESTED_VIRTUALIZATION`
Required: No

 ** State **   <a name="WorkSpaces-Type-ModificationState-State"></a>
The modification state.
Type: String
Valid Values: `UPDATE_INITIATED | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: No

## See Also
<a name="API_ModificationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModificationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModificationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModificationState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
