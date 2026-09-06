---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_Wave.html
---

# Wave
<a name="API_Wave"></a>

## Contents
<a name="API_Wave_Contents"></a>

 ** arn **   <a name="mgn-Type-Wave-arn"></a>
Wave ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** creationDateTime **   <a name="mgn-Type-Wave-creationDateTime"></a>
Wave creation dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** description **   <a name="mgn-Type-Wave-description"></a>
Wave description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`
Required: No

 ** isArchived **   <a name="mgn-Type-Wave-isArchived"></a>
Wave archival status.
Type: Boolean
Required: No

 ** lastModifiedDateTime **   <a name="mgn-Type-Wave-lastModifiedDateTime"></a>
Wave last modified dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** name **   <a name="mgn-Type-Wave-name"></a>
Wave name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** tags **   <a name="mgn-Type-Wave-tags"></a>
Wave tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** waveAggregatedStatus **   <a name="mgn-Type-Wave-waveAggregatedStatus"></a>
Wave aggregated status.
Type: [WaveAggregatedStatus](API_WaveAggregatedStatus.md) object
Required: No

 ** waveID **   <a name="mgn-Type-Wave-waveID"></a>
Wave ID.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_Wave_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/Wave)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/Wave)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/Wave)
