---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PIIDetection.html
---

# PIIDetection
<a name="API_PIIDetection"></a>

Specifies a transform that identifies, removes or masks PII data.

## Contents
<a name="API_PIIDetection_Contents"></a>

 ** EntityTypesToDetect **   <a name="Glue-Type-PIIDetection-EntityTypesToDetect"></a>
Indicates the types of entities the PIIDetection transform will identify as PII data.
 PII type entities include: PERSON\_NAME, DATE, USA\_SNN, EMAIL, USA\_ITIN, USA\_PASSPORT\_NUMBER, PHONE\_NUMBER, BANK\_ACCOUNT, IP\_ADDRESS, MAC\_ADDRESS, USA\_CPT\_CODE, USA\_HCPCS\_CODE, USA\_NATIONAL\_DRUG\_CODE, USA\_MEDICARE\_BENEFICIARY\_IDENTIFIER, USA\_HEALTH\_INSURANCE\_CLAIM\_NUMBER,CREDIT\_CARD,USA\_NATIONAL\_PROVIDER\_IDENTIFIER,USA\_DEA\_NUMBER,USA\_DRIVING\_LICENSE
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-PIIDetection-Inputs"></a>
The node ID inputs to the transform.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-PIIDetection-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** PiiType **   <a name="Glue-Type-PIIDetection-PiiType"></a>
Indicates the type of PIIDetection transform.
Type: String
Valid Values: `RowAudit | RowHashing | RowMasking | RowPartialMasking | ColumnAudit | ColumnHashing | ColumnMasking`
Required: Yes

 ** DetectionParameters **   <a name="Glue-Type-PIIDetection-DetectionParameters"></a>
Additional parameters for configuring PII detection behavior and sensitivity settings.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DetectionSensitivity **   <a name="Glue-Type-PIIDetection-DetectionSensitivity"></a>
The sensitivity level for PII detection. Higher sensitivity levels detect more potential PII but may result in more false positives.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** MaskValue **   <a name="Glue-Type-PIIDetection-MaskValue"></a>
Indicates the value that will replace the detected entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[*A-Za-z0-9_-]*`
Required: No

 ** MatchPattern **   <a name="Glue-Type-PIIDetection-MatchPattern"></a>
A regular expression pattern used to identify additional PII content beyond the standard detection algorithms.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** NumLeftCharsToExclude **   <a name="Glue-Type-PIIDetection-NumLeftCharsToExclude"></a>
The number of characters to exclude from redaction on the left side of detected PII content. This allows preserving context around the sensitive data.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NumRightCharsToExclude **   <a name="Glue-Type-PIIDetection-NumRightCharsToExclude"></a>
The number of characters to exclude from redaction on the right side of detected PII content. This allows preserving context around the sensitive data.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** OutputColumnName **   <a name="Glue-Type-PIIDetection-OutputColumnName"></a>
Indicates the output column name that will contain any entity type detected in that row.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** RedactChar **   <a name="Glue-Type-PIIDetection-RedactChar"></a>
The character used to replace detected PII content when redaction is enabled. The default redaction character is `*`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** RedactText **   <a name="Glue-Type-PIIDetection-RedactText"></a>
Specifies whether to redact the detected PII text. When set to `true`, PII content is replaced with redaction characters.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SampleFraction **   <a name="Glue-Type-PIIDetection-SampleFraction"></a>
Indicates the fraction of the data to sample when scanning for PII entities.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** ThresholdFraction **   <a name="Glue-Type-PIIDetection-ThresholdFraction"></a>
Indicates the fraction of the data that must be met in order for a column to be identified as PII data.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_PIIDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PIIDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PIIDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PIIDetection)
