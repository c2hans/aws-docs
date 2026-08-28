---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_SystemsManagerAgent.html
---

# SystemsManagerAgent
<a name="API_SystemsManagerAgent"></a>

Contains settings for the Systems Manager agent on your build instance.

## Contents
<a name="API_SystemsManagerAgent_Contents"></a>

 ** uninstallAfterBuild **   <a name="imagebuilder-Type-SystemsManagerAgent-uninstallAfterBuild"></a>
Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. default value is false.
The default behavior of uninstallAfterBuild is to remove the SSM Agent if it was installed by EC2 Image Builder
Type: Boolean
Required: No

## See Also
<a name="API_SystemsManagerAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/SystemsManagerAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/SystemsManagerAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/SystemsManagerAgent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
