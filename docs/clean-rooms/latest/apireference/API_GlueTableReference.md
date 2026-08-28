---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GlueTableReference.html
---

# GlueTableReference
<a name="API_GlueTableReference"></a>

A reference to a table within an AWS Glue data catalog.

## Contents
<a name="API_GlueTableReference_Contents"></a>

 ** databaseName **   <a name="API-Type-GlueTableReference-databaseName"></a>
The name of the database the AWS Glue table belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?`
Required: Yes

 ** tableName **   <a name="API-Type-GlueTableReference-tableName"></a>
The name of the AWS Glue table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** region **   <a name="API-Type-GlueTableReference-region"></a>
The AWS Region where the AWS Glue table is located. This parameter is required to uniquely identify and access tables across different Regions.
Type: String
Valid Values: `us-west-1 | us-west-2 | us-east-1 | us-east-2 | af-south-1 | ap-east-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-5 | ap-southeast-4 | ap-southeast-7 | ap-south-1 | ap-northeast-3 | ap-northeast-1 | ap-northeast-2 | ca-central-1 | ca-west-1 | eu-south-1 | eu-west-3 | eu-south-2 | eu-central-2 | eu-central-1 | eu-north-1 | eu-west-1 | eu-west-2 | me-south-1 | me-central-1 | il-central-1 | sa-east-1 | mx-central-1 | ap-east-2`
Required: No

## See Also
<a name="API_GlueTableReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/GlueTableReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/GlueTableReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/GlueTableReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
