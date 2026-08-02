---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AppSpecification.html
---

# AppSpecification
<a name="API_AppSpecification"></a>

Configuration to run a processing job in a specified container image.

## Contents
<a name="API_AppSpecification_Contents"></a>

 ** ImageUri **   <a name="sagemaker-Type-AppSpecification-ImageUri"></a>
The container image to be run by the processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** ContainerArguments **   <a name="sagemaker-Type-AppSpecification-ContainerArguments"></a>
The arguments for a container used to run a processing job.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** ContainerEntrypoint **   <a name="sagemaker-Type-AppSpecification-ContainerEntrypoint"></a>
The entrypoint for a container used to run a processing job.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_AppSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AppSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AppSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AppSpecification)
