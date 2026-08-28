---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageTestsConfiguration.html
---

# ImageTestsConfiguration
<a name="API_ImageTestsConfiguration"></a>

Configure image tests for your pipeline build. Tests run after building the image, to verify that the AMI or container image is valid before distributing it.

## Contents
<a name="API_ImageTestsConfiguration_Contents"></a>

 ** imageTestsEnabled **   <a name="imagebuilder-Type-ImageTestsConfiguration-imageTestsEnabled"></a>
Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.
Type: Boolean
Required: No

 ** timeoutMinutes **   <a name="imagebuilder-Type-ImageTestsConfiguration-timeoutMinutes"></a>
The maximum time in minutes that tests are permitted to run.
The timeout property is not currently active. This value is ignored.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 1440.
Required: No

## See Also
<a name="API_ImageTestsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageTestsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageTestsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageTestsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
