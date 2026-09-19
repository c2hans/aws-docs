---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_RedundantIngestCredential.html
---

# RedundantIngestCredential
<a name="API_RedundantIngestCredential"></a>

An object representing a redundant ingest credential.

## Contents
<a name="API_RedundantIngestCredential_Contents"></a>

 ** participantId **   <a name="ivsrealtimeeapireference-Type-RedundantIngestCredential-participantId"></a>
ID of the participant within the stage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** streamKey **   <a name="ivsrealtimeeapireference-Type-RedundantIngestCredential-streamKey"></a>
Ingest-key value.
Type: String
Pattern: `rt_[0-9]+_[a-z0-9-]+_[a-zA-Z0-9-]+_.+`
Required: No

## See Also
<a name="API_RedundantIngestCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/RedundantIngestCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/RedundantIngestCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/RedundantIngestCredential)
