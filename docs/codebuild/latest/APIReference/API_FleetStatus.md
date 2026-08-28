---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_FleetStatus.html
---

# FleetStatus
<a name="API_FleetStatus"></a>

The status of the compute fleet.

## Contents
<a name="API_FleetStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** context **   <a name="CodeBuild-Type-FleetStatus-context"></a>
Additional information about a compute fleet. Valid values include:
+  `CREATE_FAILED`: The compute fleet has failed to create.
+  `UPDATE_FAILED`: The compute fleet has failed to update.
Type: String
Valid Values: `CREATE_FAILED | UPDATE_FAILED | ACTION_REQUIRED | PENDING_DELETION | INSUFFICIENT_CAPACITY`
Required: No

 ** message **   <a name="CodeBuild-Type-FleetStatus-message"></a>
A message associated with the status of a compute fleet.
Type: String
Required: No

 ** statusCode **   <a name="CodeBuild-Type-FleetStatus-statusCode"></a>
The status code of the compute fleet. Valid values include:
+  `CREATING`: The compute fleet is being created.
+  `UPDATING`: The compute fleet is being updated.
+  `ROTATING`: The compute fleet is being rotated.
+  `PENDING_DELETION`: The compute fleet is pending deletion.
+  `DELETING`: The compute fleet is being deleted.
+  `CREATE_FAILED`: The compute fleet has failed to create.
+  `UPDATE_ROLLBACK_FAILED`: The compute fleet has failed to update and could not rollback to previous state.
+  `ACTIVE`: The compute fleet has succeeded and is active.
Type: String
Valid Values: `CREATING | UPDATING | ROTATING | PENDING_DELETION | DELETING | CREATE_FAILED | UPDATE_ROLLBACK_FAILED | ACTIVE`
Required: No

## See Also
<a name="API_FleetStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/FleetStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/FleetStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/FleetStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
