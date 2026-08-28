---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceAccessProperties.html
---

# WorkspaceAccessProperties
<a name="API_WorkspaceAccessProperties"></a>

The device types and operating systems that can be used to access a WorkSpace. For more information, see [Amazon WorkSpaces Client Network Requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-network-requirements.html).

## Contents
<a name="API_WorkspaceAccessProperties_Contents"></a>

 ** AccessEndpointConfig **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-AccessEndpointConfig"></a>
Specifies the configuration for accessing the WorkSpace.
Type: [AccessEndpointConfig](API_AccessEndpointConfig.md) object
Required: No

 ** DeviceTypeAndroid **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeAndroid"></a>
Indicates whether users can use Android and Android-compatible Chrome OS devices to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeChromeOs **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeChromeOs"></a>
Indicates whether users can use Chromebooks to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeIos **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeIos"></a>
Indicates whether users can use iOS devices to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeLinux **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeLinux"></a>
Indicates whether users can use Linux clients to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeOsx **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeOsx"></a>
Indicates whether users can use macOS clients to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeWeb **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeWeb"></a>
Indicates whether users can access their WorkSpaces through a web browser.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeWindows **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeWindows"></a>
Indicates whether users can use Windows clients to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeWorkSpacesThinClient **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeWorkSpacesThinClient"></a>
Indicates whether users can access their WorkSpaces through a WorkSpaces Thin Client.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** DeviceTypeZeroClient **   <a name="WorkSpaces-Type-WorkspaceAccessProperties-DeviceTypeZeroClient"></a>
Indicates whether users can use zero client devices to access their WorkSpaces.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

## See Also
<a name="API_WorkspaceAccessProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceAccessProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceAccessProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceAccessProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
