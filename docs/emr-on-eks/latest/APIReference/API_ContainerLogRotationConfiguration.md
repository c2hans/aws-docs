---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ContainerLogRotationConfiguration.html
---

# ContainerLogRotationConfiguration
<a name="API_ContainerLogRotationConfiguration"></a>

The settings for container log rotation.

## Contents
<a name="API_ContainerLogRotationConfiguration_Contents"></a>

 ** maxFilesToKeep **   <a name="emroneks-Type-ContainerLogRotationConfiguration-maxFilesToKeep"></a>
The number of files to keep in container after rotation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: Yes

 ** rotationSize **   <a name="emroneks-Type-ContainerLogRotationConfiguration-rotationSize"></a>
The file size at which to rotate logs. Minimum of 2KB, Maximum of 2GB.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `^\d+(\.\d+)?[KMG][Bb]?$`
Required: Yes

## See Also
<a name="API_ContainerLogRotationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ContainerLogRotationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ContainerLogRotationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ContainerLogRotationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
