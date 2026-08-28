---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_StreamingProperties.html
---

# StreamingProperties
<a name="API_StreamingProperties"></a>

Describes the streaming properties.

## Contents
<a name="API_StreamingProperties_Contents"></a>

 ** GlobalAccelerator **   <a name="WorkSpaces-Type-StreamingProperties-GlobalAccelerator"></a>
Indicates the Global Accelerator properties.
Type: [GlobalAcceleratorForDirectory](API_GlobalAcceleratorForDirectory.md) object
Required: No

 ** StorageConnectors **   <a name="WorkSpaces-Type-StreamingProperties-StorageConnectors"></a>
Indicates the storage connector used
Type: Array of [StorageConnector](API_StorageConnector.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** StreamingExperiencePreferredProtocol **   <a name="WorkSpaces-Type-StreamingProperties-StreamingExperiencePreferredProtocol"></a>
Indicates the type of preferred protocol for the streaming experience.
Type: String
Valid Values: `TCP | UDP`
Required: No

 ** UserSettings **   <a name="WorkSpaces-Type-StreamingProperties-UserSettings"></a>
Indicates the permission settings asscoiated with the user.
Type: Array of [UserSetting](API_UserSetting.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_StreamingProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/StreamingProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/StreamingProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/StreamingProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
