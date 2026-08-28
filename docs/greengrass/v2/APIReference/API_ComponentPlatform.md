---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentPlatform.html
---

# ComponentPlatform
<a name="API_ComponentPlatform"></a>

Contains information about a platform that a component supports.

## Contents
<a name="API_ComponentPlatform_Contents"></a>

 ** attributes **   <a name="greengrassv2-Type-ComponentPlatform-attributes"></a>
A dictionary of attributes for the platform. The AWS IoT Greengrass Core software defines the `os` and `architecture` by default. You can specify additional platform attributes for a core device when you deploy the Greengrass nucleus component. For more information, see the [Greengrass nucleus component](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: No

 ** name **   <a name="greengrassv2-Type-ComponentPlatform-name"></a>
The friendly name of the platform. This name helps you identify the platform.
If you omit this parameter, AWS IoT Greengrass creates a friendly name from the `os` and `architecture` of the platform.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ComponentPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentPlatform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentPlatform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentPlatform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
