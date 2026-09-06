---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_BatchRunSettings.html
---

# BatchRunSettings
<a name="API_BatchRunSettings"></a>

A union type representing per-run configurations for the batch. Specify exactly one of the following members.

## Contents
<a name="API_BatchRunSettings_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inlineSettings **   <a name="omics-Type-BatchRunSettings-inlineSettings"></a>
A list of per-run configurations provided inline in the request. Each entry must include a unique `runSettingId`. Supports up to 100 entries. For batches with more than 100 runs, use `s3UriSettings`.
Type: Array of [InlineSetting](API_InlineSetting.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** s3UriSettings **   <a name="omics-Type-BatchRunSettings-s3UriSettings"></a>
An Amazon S3 URI pointing to a JSON file containing per-run configurations. The file must be a JSON array in the same format as `inlineSettings`. Supports up to 100,000 run configurations. The maximum file size is 6 GB.
The IAM service role in `roleArn` must have read access to this S3 object. HealthOmics validates access to the file during the synchronous API call and records the file's ETag. If the file is modified after submission, the batch fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_BatchRunSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/BatchRunSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/BatchRunSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/BatchRunSettings)
