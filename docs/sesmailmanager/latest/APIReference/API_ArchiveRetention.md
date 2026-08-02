---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveRetention.html
---

# ArchiveRetention
<a name="API_ArchiveRetention"></a>

The retention policy for an email archive that specifies how long emails are kept before being automatically deleted.

## Contents
<a name="API_ArchiveRetention_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** RetentionPeriod **   <a name="sesmailmanager-Type-ArchiveRetention-RetentionPeriod"></a>
The enum value sets the period for retaining emails in an archive.
Type: String
Valid Values: `THREE_MONTHS | SIX_MONTHS | NINE_MONTHS | ONE_YEAR | EIGHTEEN_MONTHS | TWO_YEARS | THIRTY_MONTHS | THREE_YEARS | FOUR_YEARS | FIVE_YEARS | SIX_YEARS | SEVEN_YEARS | EIGHT_YEARS | NINE_YEARS | TEN_YEARS | PERMANENT`
Required: No

## See Also
<a name="API_ArchiveRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ArchiveRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ArchiveRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ArchiveRetention)
