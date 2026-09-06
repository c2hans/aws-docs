---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceSizeConfig.html
---

# AudienceSizeConfig
<a name="API_AudienceSizeConfig"></a>

Returns the relevance scores at these audience sizes when used in the [GetAudienceGenerationJob](API_GetAudienceGenerationJob.md) for a specified audience generation job and configured audience model.

Specifies the list of allowed `audienceSize` values when used in the [StartAudienceExportJob](API_StartAudienceExportJob.md) for an audience generation job. You can use the `ABSOLUTE` [AudienceSize](API_AudienceSize.md) to configure out audience sizes using the count of identifiers in the output. You can use the `Percentage` [AudienceSize](API_AudienceSize.md) to configure sizes in the range 1-100 percent.

## Contents
<a name="API_AudienceSizeConfig_Contents"></a>

 ** audienceSizeBins **   <a name="API-Type-AudienceSizeConfig-audienceSizeBins"></a>
An array of the different audience output sizes.
Type: Array of integers
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Valid Range: Minimum value of 1. Maximum value of 20000000.
Required: Yes

 ** audienceSizeType **   <a name="API-Type-AudienceSizeConfig-audienceSizeType"></a>
Whether the audience output sizes are defined as an absolute number or a percentage.
Type: String
Valid Values: `ABSOLUTE | PERCENTAGE`
Required: Yes

## See Also
<a name="API_AudienceSizeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceSizeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceSizeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceSizeConfig)
