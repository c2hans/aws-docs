---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentBlueprintSummary.html
---

# EnvironmentBlueprintSummary
<a name="API_EnvironmentBlueprintSummary"></a>

The details of an environment blueprint summary.

## Contents
<a name="API_EnvironmentBlueprintSummary_Contents"></a>

 ** id **   <a name="datazone-Type-EnvironmentBlueprintSummary-id"></a>
The identifier of the blueprint.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-EnvironmentBlueprintSummary-name"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** provider **   <a name="datazone-Type-EnvironmentBlueprintSummary-provider"></a>
The provider of the blueprint.
Type: String
Required: Yes

 ** provisioningProperties **   <a name="datazone-Type-EnvironmentBlueprintSummary-provisioningProperties"></a>
The provisioning properties of the blueprint.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="datazone-Type-EnvironmentBlueprintSummary-createdAt"></a>
The timestamp of when an environment blueprint was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-EnvironmentBlueprintSummary-description"></a>
The description of a blueprint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** updatedAt **   <a name="datazone-Type-EnvironmentBlueprintSummary-updatedAt"></a>
The timestamp of when the blueprint was enabled.
Type: Timestamp
Required: No

## See Also
<a name="API_EnvironmentBlueprintSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentBlueprintSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentBlueprintSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentBlueprintSummary)
