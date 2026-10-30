---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceAttributeUpdates.html
---

# InstanceAttributeUpdates
<a name="API_InstanceAttributeUpdates"></a>

Describes the attributes to update on a Lightsail instance when it starts.

## Contents
<a name="API_InstanceAttributeUpdates_Contents"></a>

 ** bundleId **   <a name="Lightsail-Type-InstanceAttributeUpdates-bundleId"></a>
The ID of the bundle to update the instance to.
Specify one of the following values for the bundle ID:
+  ** `auto` ** – Updates an instance that runs on a previous-generation bundle to the newer-generation equivalent of that bundle. For example, specify `auto` to update an instance that runs on `small_2_0` to `small_3_0`.
+  **Newer-generation bundle ID** – Updates an instance that runs on a previous-generation bundle to the specified bundle. For example, specify `small_3_0` to update an instance that runs on `small_2_0` to `small_3_0`.
+  **Original bundle ID** – Updates an instance to the previous-generation bundle that it ran on before an earlier update. For example, specify `small_2_0` to return an instance that runs on `small_3_0` to `small_2_0`.
The instance must be in the `stopped` state to update its bundle.
There is no additional cost to update an instance to a newer-generation bundle.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_InstanceAttributeUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceAttributeUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceAttributeUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceAttributeUpdates)
