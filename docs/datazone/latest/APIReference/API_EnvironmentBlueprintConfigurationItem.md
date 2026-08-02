---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentBlueprintConfigurationItem.html
---

# EnvironmentBlueprintConfigurationItem
<a name="API_EnvironmentBlueprintConfigurationItem"></a>

The configuration details of an environment blueprint.

## Contents
<a name="API_EnvironmentBlueprintConfigurationItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-domainId"></a>
The identifier of the Amazon DataZone domain in which an environment blueprint exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** environmentBlueprintId **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-environmentBlueprintId"></a>
The identifier of the environment blueprint.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** allowUserProvidedConfigurations **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-allowUserProvidedConfigurations"></a>
Specifies whether user-provided resource configurations are allowed for the environment blueprint.
Type: Boolean
Required: No

 ** createdAt **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-createdAt"></a>
The timestamp of when an environment blueprint was created.
Type: Timestamp
Required: No

 ** enabledRegions **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-enabledRegions"></a>
The enabled AWS Regions specified in a blueprint configuration.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: No

 ** environmentRolePermissionBoundary **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-environmentRolePermissionBoundary"></a>
The environment role permission boundary.
Type: String
Pattern: `arn:aws[^:]*:iam::(aws|\d{12}):policy/[\w+=,.@-]*`
Required: No

 ** manageAccessRoleArn **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-manageAccessRoleArn"></a>
The ARN of the manage access role specified in the environment blueprint configuration.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** provisioningConfigurations **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-provisioningConfigurations"></a>
The provisioning configuration of a blueprint.
Type: Array of [ProvisioningConfiguration](API_ProvisioningConfiguration.md) objects
Required: No

 ** provisioningRoleArn **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-provisioningRoleArn"></a>
The ARN of the provisioning role specified in the environment blueprint configuration.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** regionalParameters **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-regionalParameters"></a>
The regional parameters of the environment blueprint.
Type: String to string to string map map
Key Length Constraints: Minimum length of 4. Maximum length of 16.
Key Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: No

 ** resourceConfigurations **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-resourceConfigurations"></a>
The resource configurations of the environment blueprint.
Type: Array of [ResourceConfiguration](API_ResourceConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** updatedAt **   <a name="datazone-Type-EnvironmentBlueprintConfigurationItem-updatedAt"></a>
The timestamp of when the environment blueprint was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_EnvironmentBlueprintConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentBlueprintConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentBlueprintConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentBlueprintConfigurationItem)
