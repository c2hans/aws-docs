---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MigrationProject.html
---

# MigrationProject
<a name="API_MigrationProject"></a>

Provides information that defines a migration project.

## Contents
<a name="API_MigrationProject_Contents"></a>

 ** Description **   <a name="DMS-Type-MigrationProject-Description"></a>
A user-friendly description of the migration project.
Type: String
Required: No

 ** InstanceProfileArn **   <a name="DMS-Type-MigrationProject-InstanceProfileArn"></a>
The Amazon Resource Name (ARN) of the instance profile for your migration project.
Type: String
Required: No

 ** InstanceProfileName **   <a name="DMS-Type-MigrationProject-InstanceProfileName"></a>
The name of the associated instance profile.
Type: String
Required: No

 ** MigrationProjectArn **   <a name="DMS-Type-MigrationProject-MigrationProjectArn"></a>
The ARN string that uniquely identifies the migration project.
Type: String
Required: No

 ** MigrationProjectCreationTime **   <a name="DMS-Type-MigrationProject-MigrationProjectCreationTime"></a>
The time when the migration project was created.
Type: Timestamp
Required: No

 ** MigrationProjectName **   <a name="DMS-Type-MigrationProject-MigrationProjectName"></a>
The name of the migration project.
Type: String
Required: No

 ** SchemaConversionApplicationAttributes **   <a name="DMS-Type-MigrationProject-SchemaConversionApplicationAttributes"></a>
The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.
Type: [SCApplicationAttributes](API_SCApplicationAttributes.md) object
Required: No

 ** SourceDataProviderDescriptors **   <a name="DMS-Type-MigrationProject-SourceDataProviderDescriptors"></a>
Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.
Type: Array of [DataProviderDescriptor](API_DataProviderDescriptor.md) objects
Required: No

 ** TargetDataProviderDescriptors **   <a name="DMS-Type-MigrationProject-TargetDataProviderDescriptors"></a>
Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.
Type: Array of [DataProviderDescriptor](API_DataProviderDescriptor.md) objects
Required: No

 ** TransformationRules **   <a name="DMS-Type-MigrationProject-TransformationRules"></a>
The transformation rules for the migration project in JSON format. Transformation rules let you customize how DMS Schema Conversion converts your source database objects, including renaming, adding prefixes or suffixes, and changing data types. For the transformation rule format and examples, see [Transformation rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-transformation-rules.html).
Homogeneous data migrations do not support transformation rules.
Type: String
Required: No

## See Also
<a name="API_MigrationProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MigrationProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MigrationProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MigrationProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
