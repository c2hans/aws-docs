---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageLoggingConfiguration.html
---

# ImageLoggingConfiguration
<a name="API_ImageLoggingConfiguration"></a>

The logging configuration that's defined for the image. Image Builder uses the defined settings to direct execution log output during image creation.

## Contents
<a name="API_ImageLoggingConfiguration_Contents"></a>

 ** logGroupName **   <a name="imagebuilder-Type-ImageLoggingConfiguration-logGroupName"></a>
The log group name that Image Builder uses for image creation. If not specified, the log group name defaults to `/aws/imagebuilder/image-name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-_/\.]{1,512}$`
Required: No

## See Also
<a name="API_ImageLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageLoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
