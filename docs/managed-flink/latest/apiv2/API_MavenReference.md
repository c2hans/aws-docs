---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_MavenReference.html
---

# MavenReference
<a name="API_MavenReference"></a>

The information required to specify a Maven reference. You can use Maven references to specify dependency JAR files.

## Contents
<a name="API_MavenReference_Contents"></a>

 ** ArtifactId **   <a name="APIReference-Type-MavenReference-ArtifactId"></a>
The artifact ID of the Maven reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** GroupId **   <a name="APIReference-Type-MavenReference-GroupId"></a>
The group ID of the Maven reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** Version **   <a name="APIReference-Type-MavenReference-Version"></a>
The version of the Maven reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## See Also
<a name="API_MavenReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/MavenReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/MavenReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/MavenReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
