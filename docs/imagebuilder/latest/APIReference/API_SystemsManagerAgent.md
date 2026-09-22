---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_SystemsManagerAgent.html
---

# SystemsManagerAgent
<a name="API_SystemsManagerAgent"></a>

Contains settings for the Systems Manager agent on your build instance. This setting applies to Linux and macOS build instances only. Requests that set it for a recipe with a Windows base image are rejected.

## Contents
<a name="API_SystemsManagerAgent_Contents"></a>

 ** uninstallAfterBuild **   <a name="imagebuilder-Type-SystemsManagerAgent-uninstallAfterBuild"></a>
Specifies whether the Systems Manager agent is removed from your final build image before Image Builder creates the new AMI. If `true`, the agent is removed. If `false`, the agent is kept, so that it's included in the AMI. If you don't set this property, Image Builder removes the agent only if Image Builder installed the agent during the build. An agent that was pre-installed on the base image is kept.
Type: Boolean
Required: No

## See Also
<a name="API_SystemsManagerAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/SystemsManagerAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/SystemsManagerAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/SystemsManagerAgent)
