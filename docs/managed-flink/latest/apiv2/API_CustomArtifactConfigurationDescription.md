---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CustomArtifactConfigurationDescription.html
---

# CustomArtifactConfigurationDescription
<a name="API_CustomArtifactConfigurationDescription"></a>

Specifies a dependency JAR or a JAR of user-defined functions.

## Contents
<a name="API_CustomArtifactConfigurationDescription_Contents"></a>

 ** ArtifactType **   <a name="APIReference-Type-CustomArtifactConfigurationDescription-ArtifactType"></a>
 `UDF` stands for user-defined functions. This type of artifact must be in an S3 bucket. A `DEPENDENCY_JAR` can be in either Maven or an S3 bucket.
Type: String
Valid Values: `UDF | DEPENDENCY_JAR`
Required: No

 ** MavenReferenceDescription **   <a name="APIReference-Type-CustomArtifactConfigurationDescription-MavenReferenceDescription"></a>
The parameters that are required to specify a Maven dependency.
Type: [MavenReference](API_MavenReference.md) object
Required: No

 ** S3ContentLocationDescription **   <a name="APIReference-Type-CustomArtifactConfigurationDescription-S3ContentLocationDescription"></a>
For a Managed Service for Apache Flink application provides a description of an Amazon S3 object, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.
Type: [S3ContentLocation](API_S3ContentLocation.md) object
Required: No

## See Also
<a name="API_CustomArtifactConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CustomArtifactConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CustomArtifactConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CustomArtifactConfigurationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
