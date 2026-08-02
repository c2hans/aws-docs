---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImagePipeline.html
---

# ImagePipeline
<a name="API_ImagePipeline"></a>

Details of an image pipeline.

## Contents
<a name="API_ImagePipeline_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-ImagePipeline-arn"></a>
The Amazon Resource Name (ARN) of the image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** consecutiveFailures **   <a name="imagebuilder-Type-ImagePipeline-consecutiveFailures"></a>
Image Builder tracks the number of consecutive failures for scheduled pipeline executions and takes one of the following actions each time it runs on a schedule:
+ If the pipeline execution is successful, the number of consecutive failures resets to zero.
+ If the pipeline execution fails, Image Builder increments the number of consecutive failures. If the failure count exceeds the limit defined in the `AutoDisablePolicy`, Image Builder disables the pipeline.
The consecutive failure count is also reset to zero under the following conditions:
+ The pipeline runs manually and succeeds.
+ The pipeline configuration is updated.
If the pipeline runs manually and fails, the count remains the same. The next scheduled run continues to increment where it left off before.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** containerRecipeArn **   <a name="imagebuilder-Type-ImagePipeline-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
Type: String
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ImagePipeline-dateCreated"></a>
The date on which this image pipeline was created.
Type: String
Required: No

 ** dateLastRun **   <a name="imagebuilder-Type-ImagePipeline-dateLastRun"></a>
This is no longer supported, and does not return a value.
Type: String
Required: No

 ** dateNextRun **   <a name="imagebuilder-Type-ImagePipeline-dateNextRun"></a>
The next date when the pipeline is scheduled to run.
Type: String
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-ImagePipeline-dateUpdated"></a>
The date on which this image pipeline was last updated.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-ImagePipeline-description"></a>
The description of the image pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** distributionConfigurationArn **   <a name="imagebuilder-Type-ImagePipeline-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
Type: String
Required: No

 ** enhancedImageMetadataEnabled **   <a name="imagebuilder-Type-ImagePipeline-enhancedImageMetadataEnabled"></a>
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
Type: Boolean
Required: No

 ** executionRole **   <a name="imagebuilder-Type-ImagePipeline-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** imageRecipeArn **   <a name="imagebuilder-Type-ImagePipeline-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.
Type: String
Required: No

 ** imageScanningConfiguration **   <a name="imagebuilder-Type-ImagePipeline-imageScanningConfiguration"></a>
Contains settings for vulnerability scans.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** imageTags **   <a name="imagebuilder-Type-ImagePipeline-imageTags"></a>
The tags to be applied to the images produced by this pipeline.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** imageTestsConfiguration **   <a name="imagebuilder-Type-ImagePipeline-imageTestsConfiguration"></a>
The image tests configuration of the image pipeline.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** infrastructureConfigurationArn **   <a name="imagebuilder-Type-ImagePipeline-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
Type: String
Required: No

 ** lastRunStatus **   <a name="imagebuilder-Type-ImagePipeline-lastRunStatus"></a>
The status of the last image that this pipeline built, such as `BUILDING`, `TESTING`, `FAILED`, or `AVAILABLE`.
Type: String
Valid Values: `PENDING | CREATING | BUILDING | TESTING | DISTRIBUTING | INTEGRATING | AVAILABLE | CANCELLED | FAILED | DEPRECATED | DELETED | DISABLED`
Required: No

 ** loggingConfiguration **   <a name="imagebuilder-Type-ImagePipeline-loggingConfiguration"></a>
Defines logging configuration for the output image.
Type: [PipelineLoggingConfiguration](API_PipelineLoggingConfiguration.md) object
Required: No

 ** name **   <a name="imagebuilder-Type-ImagePipeline-name"></a>
The name of the image pipeline.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** platform **   <a name="imagebuilder-Type-ImagePipeline-platform"></a>
The platform of the image pipeline.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** schedule **   <a name="imagebuilder-Type-ImagePipeline-schedule"></a>
The schedule of the image pipeline.
Type: [Schedule](API_Schedule.md) object
Required: No

 ** status **   <a name="imagebuilder-Type-ImagePipeline-status"></a>
The status of the image pipeline.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** tags **   <a name="imagebuilder-Type-ImagePipeline-tags"></a>
The tags of this image pipeline.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** workflows **   <a name="imagebuilder-Type-ImagePipeline-workflows"></a>
Contains the workflows that run for the image pipeline.
Type: Array of [WorkflowConfiguration](API_WorkflowConfiguration.md) objects
Required: No

## See Also
<a name="API_ImagePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImagePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImagePipeline)
