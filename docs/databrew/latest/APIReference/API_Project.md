---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Project.html
---

# Project
<a name="API_Project"></a>

Represents all of the attributes of a DataBrew project.

## Contents
<a name="API_Project_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-Project-Name"></a>
The unique name of a project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** RecipeName **   <a name="databrew-Type-Project-RecipeName"></a>
The name of a recipe that will be developed during a project session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** AccountId **   <a name="databrew-Type-Project-AccountId"></a>
The ID of the AWS account that owns the project.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="databrew-Type-Project-CreateDate"></a>
The date and time that the project was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="databrew-Type-Project-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who crated the project.
Type: String
Required: No

 ** DatasetName **   <a name="databrew-Type-Project-DatasetName"></a>
The dataset that the project is to act upon.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** LastModifiedBy **   <a name="databrew-Type-Project-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the project.
Type: String
Required: No

 ** LastModifiedDate **   <a name="databrew-Type-Project-LastModifiedDate"></a>
The last modification date and time for the project.
Type: Timestamp
Required: No

 ** OpenDate **   <a name="databrew-Type-Project-OpenDate"></a>
The date and time when the project was opened.
Type: Timestamp
Required: No

 ** OpenedBy **   <a name="databrew-Type-Project-OpenedBy"></a>
The Amazon Resource Name (ARN) of the user that opened the project for use.
Type: String
Required: No

 ** ResourceArn **   <a name="databrew-Type-Project-ResourceArn"></a>
The Amazon Resource Name (ARN) for the project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** RoleArn **   <a name="databrew-Type-Project-RoleArn"></a>
The Amazon Resource Name (ARN) of the role that will be assumed for this project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Sample **   <a name="databrew-Type-Project-Sample"></a>
The sample size and sampling type to apply to the data. If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset.
Type: [Sample](API_Sample.md) object
Required: No

 ** Tags **   <a name="databrew-Type-Project-Tags"></a>
Metadata tags that have been applied to the project.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Project_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Project)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Project)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Project)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
