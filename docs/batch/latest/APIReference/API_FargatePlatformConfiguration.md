---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_FargatePlatformConfiguration.html
---

# FargatePlatformConfiguration
<a name="API_FargatePlatformConfiguration"></a>

The platform configuration for jobs that are running on Fargate resources. Jobs that run on Amazon EC2 resources must not specify this parameter.

## Contents
<a name="API_FargatePlatformConfiguration_Contents"></a>

 ** platformVersion **   <a name="Batch-Type-FargatePlatformConfiguration-platformVersion"></a>
The AWS Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the `LATEST` platform version is used by default. This uses a recent, approved version of the AWS Fargate platform for compute resources. For more information, see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_FargatePlatformConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FargatePlatformConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FargatePlatformConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FargatePlatformConfiguration)
