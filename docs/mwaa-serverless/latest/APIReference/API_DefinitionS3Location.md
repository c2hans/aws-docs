---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_DefinitionS3Location.html
---

# DefinitionS3Location
<a name="API_DefinitionS3Location"></a>

Specifies the Amazon S3 location of a workflow definition file. This structure contains the bucket name, object key, and optional version ID for the workflow definition. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition file at the time of workflow creation or update, ensuring that the workflow behavior remains consistent even if the source file is modified. The definition must be a valid YAML file that uses supported AWS operators and Amazon Managed Workflows for Apache Airflow Serverless syntax.

## Contents
<a name="API_DefinitionS3Location_Contents"></a>

 ** Bucket **   <a name="mwaaserverless-Type-DefinitionS3Location-Bucket"></a>
The name of the Amazon S3 bucket that contains the workflow definition file.
Type: String
Required: Yes

 ** ObjectKey **   <a name="mwaaserverless-Type-DefinitionS3Location-ObjectKey"></a>
The key (name) of the workflow definition file within the S3 bucket.
Type: String
Required: Yes

 ** VersionId **   <a name="mwaaserverless-Type-DefinitionS3Location-VersionId"></a>
Optional. The version ID of the workflow definition file in Amazon S3. If not specified, the latest version is used.
Type: String
Required: No

## See Also
<a name="API_DefinitionS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/DefinitionS3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/DefinitionS3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/DefinitionS3Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
