---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainedModelExportsConfigurationPolicy.html
---

# TrainedModelExportsConfigurationPolicy
<a name="API_TrainedModelExportsConfigurationPolicy"></a>

Information about how the trained model exports are configured.

## Contents
<a name="API_TrainedModelExportsConfigurationPolicy_Contents"></a>

 ** filesToExport **   <a name="API-Type-TrainedModelExportsConfigurationPolicy-filesToExport"></a>
The files that are exported during the trained model export job.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `MODEL | OUTPUT`
Required: Yes

 ** maxSize **   <a name="API-Type-TrainedModelExportsConfigurationPolicy-maxSize"></a>
The maximum size of the data that can be exported.
Type: [TrainedModelExportsMaxSize](API_TrainedModelExportsMaxSize.md) object
Required: Yes

## See Also
<a name="API_TrainedModelExportsConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainedModelExportsConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainedModelExportsConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainedModelExportsConfigurationPolicy)
