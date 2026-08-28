---
source_url: https://docs.aws.amazon.com/cloud9/latest/APIReference/API_EnvironmentLifecycle.html
---

# EnvironmentLifecycle
<a name="API_EnvironmentLifecycle"></a>

Information about the current creation or deletion lifecycle state of an AWS Cloud9 development environment.

## Contents
<a name="API_EnvironmentLifecycle_Contents"></a>

 ** failureResource **   <a name="cloud9-Type-EnvironmentLifecycle-failureResource"></a>
If the environment failed to delete, the Amazon Resource Name (ARN) of the related AWS resource.
Type: String
Required: No

 ** reason **   <a name="cloud9-Type-EnvironmentLifecycle-reason"></a>
Any informational message about the lifecycle state of the environment.
Type: String
Required: No

 ** status **   <a name="cloud9-Type-EnvironmentLifecycle-status"></a>
The current creation or deletion lifecycle state of the environment.
+  `CREATING`: The environment is in the process of being created.
+  `CREATED`: The environment was successfully created.
+  `CREATE_FAILED`: The environment failed to be created.
+  `DELETING`: The environment is in the process of being deleted.
+  `DELETE_FAILED`: The environment failed to delete.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | DELETING | DELETE_FAILED`
Required: No

## See Also
<a name="API_EnvironmentLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/EnvironmentLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/EnvironmentLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/EnvironmentLifecycle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud9. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud9` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
