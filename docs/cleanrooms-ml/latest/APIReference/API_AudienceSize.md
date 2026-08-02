---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceSize.html
---

# AudienceSize
<a name="API_AudienceSize"></a>

The size of the generated audience. Must match one of the sizes in the configured audience model.

## Contents
<a name="API_AudienceSize_Contents"></a>

 ** type **   <a name="API-Type-AudienceSize-type"></a>
Whether the audience size is defined in absolute terms or as a percentage. You can use the `ABSOLUTE` [AudienceSize](#API_AudienceSize) to configure out audience sizes using the count of identifiers in the output. You can use the `Percentage` [AudienceSize](#API_AudienceSize) to configure sizes in the range 1-100 percent.
Type: String
Valid Values: `ABSOLUTE | PERCENTAGE`
Required: Yes

 ** value **   <a name="API-Type-AudienceSize-value"></a>
Specify an audience size value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20000000.
Required: Yes

## See Also
<a name="API_AudienceSize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceSize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceSize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceSize)
