---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_WorkspaceStatus.html
---

# WorkspaceStatus
<a name="API_WorkspaceStatus"></a>

Contains information about the current status of a workspace.

## Contents
<a name="API_WorkspaceStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-WorkspaceStatus-state"></a>
The current state of the workspace.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: Yes

 ** error **   <a name="iotsitewise-Type-WorkspaceStatus-error"></a>
Contains associated error information, if any.
Type: [WorkspaceErrorDetails](API_WorkspaceErrorDetails.md) object
Required: No

## See Also
<a name="API_WorkspaceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/WorkspaceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/WorkspaceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/WorkspaceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
