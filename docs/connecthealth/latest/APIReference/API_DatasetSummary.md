---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DatasetSummary.html
---

# DatasetSummary

Summary information about a Dataset.

## Contents
<a name="API_DatasetSummary_Contents"></a>

 ** arn **   <a name="connecthealth-Type-DatasetSummary-arn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Pattern: `arn:aws[a-z\-]*:[a-z0-9\-]+:[a-z0-9\-]*:[0-9]{12}:.+`
Required: Yes

 ** createdAt **   <a name="connecthealth-Type-DatasetSummary-createdAt"></a>
The date and time that the dataset was created.
Type: Timestamp
Required: Yes

 ** datasetId **   <a name="connecthealth-Type-DatasetSummary-datasetId"></a>
The unique identifier of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** name **   <a name="connecthealth-Type-DatasetSummary-name"></a>
The name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1028.
Pattern: `[\x20-\x21\x23\x24\x2A-\x3A\x3F-\x7E]*`
Required: Yes

 ** status **   <a name="connecthealth-Type-DatasetSummary-status"></a>
The status of the dataset.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | DELETE_FAILED | DELETED`
Required: Yes

 ** type **   <a name="connecthealth-Type-DatasetSummary-type"></a>
The type of the dataset.
Type: String
Valid Values: `MEDICAL_CODING`
Required: Yes

 ** updatedAt **   <a name="connecthealth-Type-DatasetSummary-updatedAt"></a>
The date and time that the dataset was last updated.
Type: Timestamp
Required: Yes

 ** statusDetails **   <a name="connecthealth-Type-DatasetSummary-statusDetails"></a>
Details about the status of the dataset, such as the reason that it failed to build or delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1028.
Pattern: `[\x20-\x21\x23\x24\x2A-\x3A\x3F-\x7E]*`
Required: No

## See Also
<a name="API_DatasetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/DatasetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/DatasetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/DatasetSummary)
