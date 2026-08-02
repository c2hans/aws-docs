---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_WorkspaceConfigurationStatus.html
---

# WorkspaceConfigurationStatus
<a name="API_WorkspaceConfigurationStatus"></a>

This structure displays the current status of the workspace configuration, and might also contain a reason for that status.

## Contents
<a name="API_WorkspaceConfigurationStatus_Contents"></a>

 ** statusCode **   <a name="prometheus-Type-WorkspaceConfigurationStatus-statusCode"></a>
The current status of the workspace configuration.
Type: String
Valid Values: `ACTIVE | UPDATING | UPDATE_FAILED`
Required: Yes

 ** statusReason **   <a name="prometheus-Type-WorkspaceConfigurationStatus-statusReason"></a>
The reason for the current status, if a reason is available.
Type: String
Required: No

## See Also
<a name="API_WorkspaceConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/WorkspaceConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/WorkspaceConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/WorkspaceConfigurationStatus)
