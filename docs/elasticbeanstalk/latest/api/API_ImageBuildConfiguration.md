---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ImageBuildConfiguration.html
---

# ImageBuildConfiguration
<a name="API_ImageBuildConfiguration"></a>

Settings that Elastic Beanstalk uses to build a container image from the source bundle of an application version.

## Contents
<a name="API_ImageBuildConfiguration_Contents"></a>

 ** Architecture **
The processor architecture that Elastic Beanstalk builds the container image for. The architecture must match the architecture of the instances in the environment that you deploy the application version to.
Valid values:
+  `amd64` – x86-64 instances. This is the default.
+  `arm64` – AWS Graviton instances.
Type: String
Valid Values: `amd64 | arm64`
Required: No

 ** Buildpack **
The Cloud Native Buildpacks builder image that Elastic Beanstalk uses to build the container image. For example, `paketobuildpacks/builder-jammy-base`.
This member is required when `Type` is `buildpack`. Elastic Beanstalk doesn't provide a default builder.
Type: String
Required: No

 ** CodeBuildServiceRole **
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that AWS CodeBuild assumes to run the build in your AWS account. Elastic Beanstalk rejects a `Build` that doesn't specify this role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ComputeType **
The size of the compute resources that run the build. If you don't specify it, Elastic Beanstalk uses `BUILD_GENERAL1_MEDIUM`.
Valid values:
+  `BUILD_GENERAL1_SMALL` – Use up to 3 GB memory and 2 vCPUs for builds.
+  `BUILD_GENERAL1_MEDIUM` – Use up to 7 GB memory and 4 vCPUs for builds.
+  `BUILD_GENERAL1_LARGE` – Use up to 15 GB memory and 8 vCPUs for builds.
Type: String
Valid Values: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE`
Required: No

 ** DockerfileLocation **
The path to the Dockerfile within the source bundle, relative to the root of the source bundle. For example, `backend/Dockerfile`.
Elastic Beanstalk uses this member only when `Type` is `docker`. If you don't specify it, Elastic Beanstalk uses the Dockerfile at the root of the source bundle.
Type: String
Required: No

 ** TimeoutInMinutes **
How long, in minutes from 5 to 480 (8 hours), Elastic Beanstalk waits before stopping a build that hasn't completed. The default is 60 minutes.
Type: Integer
Required: No

 ** Type **
How Elastic Beanstalk builds the container image. Elastic Beanstalk rejects a `Build` that doesn't specify it.
Valid values:
+  `docker` – Elastic Beanstalk builds the image from a Dockerfile in your source bundle. Specify the Dockerfile with `DockerfileLocation`.
+  `buildpack` – Elastic Beanstalk builds the image with a Cloud Native Buildpacks builder. Specify the builder with `Buildpack`.
Type: String
Valid Values: `docker | buildpack`
Required: No

## See Also
<a name="API_ImageBuildConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ImageBuildConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ImageBuildConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ImageBuildConfiguration)
