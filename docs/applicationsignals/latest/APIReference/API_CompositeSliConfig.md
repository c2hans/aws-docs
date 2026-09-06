---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CompositeSliConfig.html
---

# CompositeSliConfig
<a name="API_CompositeSliConfig"></a>

This structure contains the configuration for a composite service level indicator (SLI) that aggregates metrics across multiple operations of a service for service-level SLOs.

## Contents
<a name="API_CompositeSliConfig_Contents"></a>

 ** SelectionConfig **   <a name="applicationsignals-Type-CompositeSliConfig-SelectionConfig"></a>
Specifies how operations are selected for this service-level SLO. Operations can be selected explicitly by listing them, by specifying a prefix to match operation names, or by providing a regular expression pattern.
Type: [SelectionConfig](API_SelectionConfig.md) object
Required: Yes

 ** Components **   <a name="applicationsignals-Type-CompositeSliConfig-Components"></a>
The list of operations included in this composite SLI. You must specify between 2 and 20 components. Each component is a `CompositeSliComponent` that identifies a single operation by its `OperationName`.
Type: Array of [CompositeSliComponent](API_CompositeSliComponent.md) objects
Array Members: Minimum number of 2 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_CompositeSliConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CompositeSliConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CompositeSliConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CompositeSliConfig)
