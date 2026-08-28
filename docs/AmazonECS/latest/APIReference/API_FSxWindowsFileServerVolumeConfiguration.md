---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_FSxWindowsFileServerVolumeConfiguration.html
---

# FSxWindowsFileServerVolumeConfiguration
<a name="API_FSxWindowsFileServerVolumeConfiguration"></a>

This parameter is specified when you're using [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) file system for task storage.

For more information and the input format, see [Amazon FSx for Windows File Server volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_FSxWindowsFileServerVolumeConfiguration_Contents"></a>

 ** authorizationConfig **   <a name="ECS-Type-FSxWindowsFileServerVolumeConfiguration-authorizationConfig"></a>
The authorization configuration details for the Amazon FSx for Windows File Server file system.
Type: [FSxWindowsFileServerAuthorizationConfig](API_FSxWindowsFileServerAuthorizationConfig.md) object
Required: Yes

 ** fileSystemId **   <a name="ECS-Type-FSxWindowsFileServerVolumeConfiguration-fileSystemId"></a>
The Amazon FSx for Windows File Server file system ID to use.
Type: String
Required: Yes

 ** rootDirectory **   <a name="ECS-Type-FSxWindowsFileServerVolumeConfiguration-rootDirectory"></a>
The directory within the Amazon FSx for Windows File Server file system to mount as the root directory inside the host.
Type: String
Required: Yes

## See Also
<a name="API_FSxWindowsFileServerVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/FSxWindowsFileServerVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/FSxWindowsFileServerVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/FSxWindowsFileServerVolumeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
