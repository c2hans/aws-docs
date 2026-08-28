---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Dataset.html
---

# Dataset
<a name="API_Dataset"></a>

Represents a dataset that can be processed by DataBrew.

## Contents
<a name="API_Dataset_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Input **   <a name="databrew-Type-Dataset-Input"></a>
Information on how DataBrew can find the dataset, in either the AWS Glue Data Catalog or Amazon S3.
Type: [Input](API_Input.md) object
Required: Yes

 ** Name **   <a name="databrew-Type-Dataset-Name"></a>
The unique name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** AccountId **   <a name="databrew-Type-Dataset-AccountId"></a>
The ID of the AWS account that owns the dataset.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="databrew-Type-Dataset-CreateDate"></a>
The date and time that the dataset was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="databrew-Type-Dataset-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the dataset.
Type: String
Required: No

 ** Format **   <a name="databrew-Type-Dataset-Format"></a>
The file format of a dataset that is created from an Amazon S3 file or folder.
Type: String
Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`
Required: No

 ** FormatOptions **   <a name="databrew-Type-Dataset-FormatOptions"></a>
A set of options that define how DataBrew interprets the data in the dataset.
Type: [FormatOptions](API_FormatOptions.md) object
Required: No

 ** LastModifiedBy **   <a name="databrew-Type-Dataset-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the dataset.
Type: String
Required: No

 ** LastModifiedDate **   <a name="databrew-Type-Dataset-LastModifiedDate"></a>
The last modification date and time of the dataset.
Type: Timestamp
Required: No

 ** PathOptions **   <a name="databrew-Type-Dataset-PathOptions"></a>
A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.
Type: [PathOptions](API_PathOptions.md) object
Required: No

 ** ResourceArn **   <a name="databrew-Type-Dataset-ResourceArn"></a>
The unique Amazon Resource Name (ARN) for the dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Source **   <a name="databrew-Type-Dataset-Source"></a>
The location of the data for the dataset, either Amazon S3 or the AWS Glue Data Catalog.
Type: String
Valid Values: `S3 | DATA-CATALOG | DATABASE`
Required: No

 ** Tags **   <a name="databrew-Type-Dataset-Tags"></a>
Metadata tags that have been applied to the dataset.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Dataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Dataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Dataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Dataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
