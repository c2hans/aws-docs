---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceGenerationJobDataSource.html
---

# AudienceGenerationJobDataSource
<a name="API_AudienceGenerationJobDataSource"></a>

Defines the Amazon S3 bucket where the seed audience for the generating audience is stored.

## Contents
<a name="API_AudienceGenerationJobDataSource_Contents"></a>

 ** roleArn **   <a name="API-Type-AudienceGenerationJobDataSource-roleArn"></a>
The ARN of the IAM role that can read the Amazon S3 bucket where the seed audience is stored.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** dataSource **   <a name="API-Type-AudienceGenerationJobDataSource-dataSource"></a>
Defines the Amazon S3 bucket where the seed audience for the generating audience is stored. A valid data source is a JSON line file in the following format:
 `{"user_id": "111111"}`
 `{"user_id": "222222"}`
 `...`
Type: [S3ConfigMap](API_S3ConfigMap.md) object
Required: No

 ** sqlComputeConfiguration **   <a name="API-Type-AudienceGenerationJobDataSource-sqlComputeConfiguration"></a>
Provides configuration information for the instances that will perform the compute work.
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** sqlParameters **   <a name="API-Type-AudienceGenerationJobDataSource-sqlParameters"></a>
The protected SQL query parameters.
Type: [ProtectedQuerySQLParameters](API_ProtectedQuerySQLParameters.md) object
Required: No

## See Also
<a name="API_AudienceGenerationJobDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceGenerationJobDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceGenerationJobDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceGenerationJobDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
