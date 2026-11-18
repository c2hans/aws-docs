---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalCodingDatasetConfig.html
---

# MedicalCodingDatasetConfig
<a name="API_MedicalCodingDatasetConfig"></a>

The configuration of a medical coding dataset. Amazon Connect Health uses the coded examples that are in the input location when you create the dataset, and writes evaluation scores to the output location, with your permissions. Later changes to the input location don't change the dataset.

## Contents
<a name="API_MedicalCodingDatasetConfig_Contents"></a>

 ** s3InputPath **   <a name="connecthealth-Type-MedicalCodingDatasetConfig-s3InputPath"></a>
The Amazon S3 location of your coded examples. You need s3:GetObject and s3:ListBucket permissions for it, and kms:Decrypt if you encrypt it with an AWS KMS key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** s3OutputPath **   <a name="connecthealth-Type-MedicalCodingDatasetConfig-s3OutputPath"></a>
The Amazon S3 location where Amazon Connect Health writes the evaluation scores for the dataset. You need s3:PutObject permission for it, and kms:GenerateDataKey if you encrypt it with an AWS KMS key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_MedicalCodingDatasetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalCodingDatasetConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalCodingDatasetConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalCodingDatasetConfig)
