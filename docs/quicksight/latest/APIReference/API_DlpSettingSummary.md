---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DlpSettingSummary.html
---

# DlpSettingSummary
<a name="API_DlpSettingSummary"></a>

A summary of a DLP setting returned by list operations.

## Contents
<a name="API_DlpSettingSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DlpSettingSummary-Arn"></a>
The Amazon Resource Name (ARN) of the DLP setting.
Type: String
Required: Yes

 ** CreatedAt **   <a name="QS-Type-DlpSettingSummary-CreatedAt"></a>
The date and time that the DLP setting was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** DlpSettingId **   <a name="QS-Type-DlpSettingSummary-DlpSettingId"></a>
The ID of the DLP setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

 ** Name **   <a name="QS-Type-DlpSettingSummary-Name"></a>
The display name of the DLP setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9](?:[\w- &]*[A-Za-z0-9])?`
Required: Yes

 ** ProviderType **   <a name="QS-Type-DlpSettingSummary-ProviderType"></a>
The type of external DLP provider used for sensitivity label classification.
Type: String
Valid Values: `MICROSOFT_PURVIEW`
Required: Yes

 ** Status **   <a name="QS-Type-DlpSettingSummary-Status"></a>
The status of the DLP setting. Valid values are `ACTIVE` and `INACTIVE`.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** UpdatedAt **   <a name="QS-Type-DlpSettingSummary-UpdatedAt"></a>
The date and time that the DLP setting was most recently updated, in ISO 8601 format.
Type: Timestamp
Required: Yes

## See Also
<a name="API_DlpSettingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DlpSettingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DlpSettingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DlpSettingSummary)
