---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_AdditionalInstanceConfiguration.html
---

# AdditionalInstanceConfiguration
<a name="API_AdditionalInstanceConfiguration"></a>

In addition to your infrastructure configuration, these settings provide an extra layer of control over your build instances. You can also specify commands to run on launch for all of your build instances.

Image Builder does not automatically install the Systems Manager agent on Windows instances. If your base image includes the Systems Manager agent, then the AMI that you create will also include the agent. For Linux instances, if the base image does not already include the Systems Manager agent, Image Builder installs it. For Linux instances where Image Builder installs the Systems Manager agent, you can choose whether to keep it for the AMI that you create.

## Contents
<a name="API_AdditionalInstanceConfiguration_Contents"></a>

 ** systemsManagerAgent **   <a name="imagebuilder-Type-AdditionalInstanceConfiguration-systemsManagerAgent"></a>
The Systems Manager agent settings for your build instance. This setting applies to Linux and macOS build instances only. Requests that set it for a recipe with a Windows base image are rejected.
Type: [SystemsManagerAgent](API_SystemsManagerAgent.md) object
Required: No

 ** userDataOverride **   <a name="imagebuilder-Type-AdditionalInstanceConfiguration-userDataOverride"></a>
Use this property to provide commands or a command script to run when you launch your build instance.
The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image.
The user data is always base 64 encoded. For example, the following commands are encoded as `IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhcg==`:
 *\#\!/bin/bash*
mkdir -p /var/bb/
touch /var
Type: String
Length Constraints: Minimum length of 1. Maximum length of 21847.
Pattern: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
Required: No

## See Also
<a name="API_AdditionalInstanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/AdditionalInstanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/AdditionalInstanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/AdditionalInstanceConfiguration)
