---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CustomArtifactConfiguration.html
---

# CustomArtifactConfiguration
<a name="API_CustomArtifactConfiguration"></a>

Specifies dependency JARs, as well as JAR files that contain user-defined functions (UDF).

## Contents
<a name="API_CustomArtifactConfiguration_Contents"></a>

 ** ArtifactType **   <a name="APIReference-Type-CustomArtifactConfiguration-ArtifactType"></a>
 `UDF` stands for user-defined functions. This type of artifact must be in an S3 bucket. A `DEPENDENCY_JAR` can be in either Maven or an S3 bucket.
Type: String
Valid Values: `UDF | DEPENDENCY_JAR`
Required: Yes

 ** MavenReference **   <a name="APIReference-Type-CustomArtifactConfiguration-MavenReference"></a>
The parameters required to fully specify a Maven reference.
Type: [MavenReference](API_MavenReference.md) object
Required: No

 ** S3ContentLocation **   <a name="APIReference-Type-CustomArtifactConfiguration-S3ContentLocation"></a>
For a Managed Service for Apache Flink application provides a description of an Amazon S3 object, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.
Type: [S3ContentLocation](API_S3ContentLocation.md) object
Required: No

## See Also
<a name="API_CustomArtifactConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CustomArtifactConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CustomArtifactConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CustomArtifactConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
