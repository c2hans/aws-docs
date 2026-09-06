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
