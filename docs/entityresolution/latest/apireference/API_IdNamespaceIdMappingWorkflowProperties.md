---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdNamespaceIdMappingWorkflowProperties.html
---

# IdNamespaceIdMappingWorkflowProperties
<a name="API_IdNamespaceIdMappingWorkflowProperties"></a>

An object containing `idMappingType`, `providerProperties`, and `ruleBasedProperties`.

## Contents
<a name="API_IdNamespaceIdMappingWorkflowProperties_Contents"></a>

 ** idMappingType **   <a name="API-Type-IdNamespaceIdMappingWorkflowProperties-idMappingType"></a>
The type of ID mapping.
Type: String
Valid Values: `PROVIDER | RULE_BASED`
Required: Yes

 ** providerProperties **   <a name="API-Type-IdNamespaceIdMappingWorkflowProperties-providerProperties"></a>
An object which defines any additional configurations required by the provider service.
Type: [NamespaceProviderProperties](API_NamespaceProviderProperties.md) object
Required: No

 ** ruleBasedProperties **   <a name="API-Type-IdNamespaceIdMappingWorkflowProperties-ruleBasedProperties"></a>
 An object which defines any additional configurations required by rule-based matching.
Type: [NamespaceRuleBasedProperties](API_NamespaceRuleBasedProperties.md) object
Required: No

## See Also
<a name="API_IdNamespaceIdMappingWorkflowProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdNamespaceIdMappingWorkflowProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdNamespaceIdMappingWorkflowProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdNamespaceIdMappingWorkflowProperties)
