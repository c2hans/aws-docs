---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-s3datasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource S3DataSourceConfiguration
<a name="aws-properties-kendra-datasource-s3datasourceconfiguration"></a>

Provides the configuration information to connect to an Amazon S3 bucket.

## Syntax
<a name="aws-properties-kendra-datasource-s3datasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-s3datasourceconfiguration-syntax.json"></a>

```
{
  "[AccessControlListConfiguration](#cfn-kendra-datasource-s3datasourceconfiguration-accesscontrollistconfiguration)" : {{AccessControlListConfiguration}},
  "[BucketName](#cfn-kendra-datasource-s3datasourceconfiguration-bucketname)" : {{String}},
  "[DocumentsMetadataConfiguration](#cfn-kendra-datasource-s3datasourceconfiguration-documentsmetadataconfiguration)" : {{DocumentsMetadataConfiguration}},
  "[ExclusionPatterns](#cfn-kendra-datasource-s3datasourceconfiguration-exclusionpatterns)" : {{[ String, ... ]}},
  "[InclusionPatterns](#cfn-kendra-datasource-s3datasourceconfiguration-inclusionpatterns)" : {{[ String, ... ]}},
  "[InclusionPrefixes](#cfn-kendra-datasource-s3datasourceconfiguration-inclusionprefixes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-s3datasourceconfiguration-syntax.yaml"></a>

```
  [AccessControlListConfiguration](#cfn-kendra-datasource-s3datasourceconfiguration-accesscontrollistconfiguration): {{
    AccessControlListConfiguration}}
  [BucketName](#cfn-kendra-datasource-s3datasourceconfiguration-bucketname): {{String}}
  [DocumentsMetadataConfiguration](#cfn-kendra-datasource-s3datasourceconfiguration-documentsmetadataconfiguration): {{
    DocumentsMetadataConfiguration}}
  [ExclusionPatterns](#cfn-kendra-datasource-s3datasourceconfiguration-exclusionpatterns): {{
    - String}}
  [InclusionPatterns](#cfn-kendra-datasource-s3datasourceconfiguration-inclusionpatterns): {{
    - String}}
  [InclusionPrefixes](#cfn-kendra-datasource-s3datasourceconfiguration-inclusionprefixes): {{
    - String}}
```

## Properties
<a name="aws-properties-kendra-datasource-s3datasourceconfiguration-properties"></a>

`AccessControlListConfiguration`  <a name="cfn-kendra-datasource-s3datasourceconfiguration-accesscontrollistconfiguration"></a>
Provides the path to the S3 bucket that contains the user context filtering files for the data source. For the format of the file, see [Access control for S3 data sources](https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html).
*Required*: No
*Type*: [AccessControlListConfiguration](aws-properties-kendra-datasource-accesscontrollistconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketName`  <a name="cfn-kendra-datasource-s3datasourceconfiguration-bucketname"></a>
The name of the bucket that contains the documents.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentsMetadataConfiguration`  <a name="cfn-kendra-datasource-s3datasourceconfiguration-documentsmetadataconfiguration"></a>
Specifies document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.
*Required*: No
*Type*: [DocumentsMetadataConfiguration](aws-properties-kendra-datasource-documentsmetadataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExclusionPatterns`  <a name="cfn-kendra-datasource-s3datasourceconfiguration-exclusionpatterns"></a>
A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to exclude from your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:
+ */myapp/config/\**—All files inside config directory.
+ *\*\*/\*.png*—All .png files in all directories.
+ *\*\*/\*.{png, ico, md}*—All .png, .ico or .md files in all directories.
+ */myapp/src/\*\*/\*.ts*—All .ts files inside src directory (and all its subdirectories).
+ *\*\*/\!(\*.module).ts*—All .ts files but not .module.ts
+ *\*.png , \*.jpg*—All PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
+ *\*internal\**—All files in a directory that contain 'internal' in the file name, such as 'internal', 'internal\_only', 'company\_internal'.
+ *\*\*/\*internal\**—All internal-related files in a directory and its subdirectories.
For more examples, see [Use of Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters) in the AWS CLI Command Reference.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InclusionPatterns`  <a name="cfn-kendra-datasource-s3datasourceconfiguration-inclusionpatterns"></a>
A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to include in your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:
+ */myapp/config/\**—All files inside config directory.
+ *\*\*/\*.png*—All .png files in all directories.
+ *\*\*/\*.{png, ico, md}*—All .png, .ico or .md files in all directories.
+ */myapp/src/\*\*/\*.ts*—All .ts files inside src directory (and all its subdirectories).
+ *\*\*/\!(\*.module).ts*—All .ts files but not .module.ts
+ *\*.png , \*.jpg*—All PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
+ *\*internal\**—All files in a directory that contain 'internal' in the file name, such as 'internal', 'internal\_only', 'company\_internal'.
+ *\*\*/\*internal\**—All internal-related files in a directory and its subdirectories.
For more examples, see [Use of Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters) in the AWS CLI Command Reference.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InclusionPrefixes`  <a name="cfn-kendra-datasource-s3datasourceconfiguration-inclusionprefixes"></a>
A list of S3 prefixes for the documents that should be included in the index.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
