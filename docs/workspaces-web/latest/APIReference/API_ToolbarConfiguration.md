---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_ToolbarConfiguration.html
---

# ToolbarConfiguration
<a name="API_ToolbarConfiguration"></a>

The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.

## Contents
<a name="API_ToolbarConfiguration_Contents"></a>

 ** hiddenToolbarItems **   <a name="workspacesweb-Type-ToolbarConfiguration-hiddenToolbarItems"></a>
The list of toolbar items to be hidden.
Type: Array of strings
Valid Values: `Windows | DualMonitor | FullScreen | Webcam | Microphone`
Required: No

 ** maxDisplayResolution **   <a name="workspacesweb-Type-ToolbarConfiguration-maxDisplayResolution"></a>
The maximum display resolution that is allowed for the session.
Type: String
Valid Values: `size4096X2160 | size3840X2160 | size3440X1440 | size2560X1440 | size1920X1080 | size1280X720 | size1024X768 | size800X600`
Required: No

 ** toolbarType **   <a name="workspacesweb-Type-ToolbarConfiguration-toolbarType"></a>
The type of toolbar displayed during the session.
Type: String
Valid Values: `Floating | Docked`
Required: No

 ** visualMode **   <a name="workspacesweb-Type-ToolbarConfiguration-visualMode"></a>
The visual mode of the toolbar.
Type: String
Valid Values: `Dark | Light`
Required: No

## See Also
<a name="API_ToolbarConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/ToolbarConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/ToolbarConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/ToolbarConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
