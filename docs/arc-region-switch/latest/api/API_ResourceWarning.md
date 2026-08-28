---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ResourceWarning.html
---

# ResourceWarning
<a name="API_ResourceWarning"></a>

Represents a warning about a resource in a Region switch plan.

## Contents
<a name="API_ResourceWarning_Contents"></a>

 ** version **   <a name="regionswitch-Type-ResourceWarning-version"></a>
The version for the resource warning.
Type: String
Required: Yes

 ** warningMessage **   <a name="regionswitch-Type-ResourceWarning-warningMessage"></a>
The warning message about what needs to be corrected.
Type: String
Required: Yes

 ** warningStatus **   <a name="regionswitch-Type-ResourceWarning-warningStatus"></a>
The status of the resource warning.
Type: String
Valid Values: `active | resolved`
Required: Yes

 ** warningUpdatedTime **   <a name="regionswitch-Type-ResourceWarning-warningUpdatedTime"></a>
The timestamp when the warning was last updated.
Type: Timestamp
Required: Yes

 ** resourceArn **   <a name="regionswitch-Type-ResourceWarning-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** stepName **   <a name="regionswitch-Type-ResourceWarning-stepName"></a>
The name of the step for the resource warning.
Type: String
Required: No

 ** workflow **   <a name="regionswitch-Type-ResourceWarning-workflow"></a>
The workflow for the resource warning.
Type: [MinimalWorkflow](API_MinimalWorkflow.md) object
Required: No

## See Also
<a name="API_ResourceWarning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ResourceWarning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ResourceWarning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ResourceWarning)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
