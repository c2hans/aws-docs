---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_Dataset.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# Dataset
<a name="API_Dataset"></a>

The structure for a Dataset.

## Contents
<a name="API_Dataset_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** alias **   <a name="finspace-Type-Dataset-alias"></a>
The unique resource identifier for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^alias\/\S+`
Required: No

 ** createTime **   <a name="finspace-Type-Dataset-createTime"></a>
The timestamp at which the Dataset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** datasetArn **   <a name="finspace-Type-Dataset-datasetArn"></a>
The ARN identifier of the Dataset.
Type: String
Required: No

 ** datasetDescription **   <a name="finspace-Type-Dataset-datasetDescription"></a>
Description for a Dataset.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\s\S]*`
Required: No

 ** datasetId **   <a name="finspace-Type-Dataset-datasetId"></a>
An identifier for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** datasetTitle **   <a name="finspace-Type-Dataset-datasetTitle"></a>
Display title for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

 ** kind **   <a name="finspace-Type-Dataset-kind"></a>
The format in which Dataset data is structured.
+  `TABULAR` – Data is structured in a tabular format.
+  `NON_TABULAR` – Data is structured in a non-tabular format.
Type: String
Valid Values: `TABULAR | NON_TABULAR`
Required: No

 ** lastModifiedTime **   <a name="finspace-Type-Dataset-lastModifiedTime"></a>
The last time that the Dataset was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** ownerInfo **   <a name="finspace-Type-Dataset-ownerInfo"></a>
Contact information for a Dataset owner.
Type: [DatasetOwnerInfo](API_DatasetOwnerInfo.md) object
Required: No

 ** schemaDefinition **   <a name="finspace-Type-Dataset-schemaDefinition"></a>
Definition for a schema on a tabular Dataset.
Type: [SchemaUnion](API_SchemaUnion.md) object
Required: No

## See Also
<a name="API_Dataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/Dataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/Dataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/Dataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
