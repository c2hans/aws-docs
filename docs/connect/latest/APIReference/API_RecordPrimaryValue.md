---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RecordPrimaryValue.html
---

# RecordPrimaryValue
<a name="API_RecordPrimaryValue"></a>

A record primary value.

## Contents
<a name="API_RecordPrimaryValue_Contents"></a>

 ** LastModifiedRegion **   <a name="connect-Type-RecordPrimaryValue-LastModifiedRegion"></a>
The value's last modified region.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-RecordPrimaryValue-LastModifiedTime"></a>
The value's last modified time.
Type: Timestamp
Required: No

 ** PrimaryValues **   <a name="connect-Type-RecordPrimaryValue-PrimaryValues"></a>
The value's primary values.
Type: Array of [PrimaryValueResponse](API_PrimaryValueResponse.md) objects
Required: No

 ** RecordId **   <a name="connect-Type-RecordPrimaryValue-RecordId"></a>
The value's record ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_RecordPrimaryValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RecordPrimaryValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RecordPrimaryValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RecordPrimaryValue)
