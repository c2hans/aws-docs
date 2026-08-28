---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Dataset.html
---

# Dataset
<a name="API_Dataset"></a>

A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.

## Contents
<a name="API_Dataset_Contents"></a>

 ** CreationDate **   <a name="Cognito-Type-Dataset-CreationDate"></a>
Date on which the dataset was created.
Type: Timestamp
Required: No

 ** DatasetName **   <a name="Cognito-Type-Dataset-DatasetName"></a>
A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '\_' (underscore), '-' (dash), and '.' (dot).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.:-]+`
Required: No

 ** DataStorage **   <a name="Cognito-Type-Dataset-DataStorage"></a>
Total size in bytes of the records in this dataset.
Type: Long
Required: No

 ** IdentityId **   <a name="Cognito-Type-Dataset-IdentityId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: No

 ** LastModifiedBy **   <a name="Cognito-Type-Dataset-LastModifiedBy"></a>
The device that made the last change to this dataset.
Type: String
Required: No

 ** LastModifiedDate **   <a name="Cognito-Type-Dataset-LastModifiedDate"></a>
Date when the dataset was last modified.
Type: Timestamp
Required: No

 ** NumRecords **   <a name="Cognito-Type-Dataset-NumRecords"></a>
Number of records in this dataset.
Type: Long
Required: No

## See Also
<a name="API_Dataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/Dataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/Dataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/Dataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
