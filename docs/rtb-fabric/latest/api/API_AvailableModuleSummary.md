---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AvailableModuleSummary.html
---

# AvailableModuleSummary

A module that you can attach, as ListAvailableModules returns it. ListAvailableModules and GetAvailableModule never return how a module is implemented.

## Contents
<a name="API_AvailableModuleSummary_Contents"></a>

 ** moduleArn **   <a name="rtbfabric-Type-AvailableModuleSummary-moduleArn"></a>
The module's ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `arn:aws[a-zA-Z-]*:rtbfabric:[a-z0-9-]+::modules/module-[a-zA-Z0-9]{1,25}`
Required: Yes

 ** moduleId **   <a name="rtbfabric-Type-AvailableModuleSummary-moduleId"></a>
The module's ID.
Type: String
Pattern: `module-[a-zA-Z0-9]{1,25}`
Required: Yes

 ** moduleName **   <a name="rtbfabric-Type-AvailableModuleSummary-moduleName"></a>
A label, not unique: modules can share a name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]*`
Required: Yes

 ** subscriptionStatus **   <a name="rtbfabric-Type-AvailableModuleSummary-subscriptionStatus"></a>
The status of your access to the module. ACTIVE for every module returned. A module that you no longer have access to isn't returned.
Type: String
Valid Values: `ACTIVE | EXPIRED`
Required: Yes

 ** subscriptionType **   <a name="rtbfabric-Type-AvailableModuleSummary-subscriptionType"></a>
The type of access that you have to the module.
Type: String
Valid Values: `MARKETPLACE | PRIVATE | AWS_BUILT_IN`
Required: Yes

 ** marketplaceProductId **   <a name="rtbfabric-Type-AvailableModuleSummary-marketplaceProductId"></a>
The Marketplace product the module is sold under. Present only when subscriptionType is MARKETPLACE.
Type: String
Required: No

## See Also
<a name="API_AvailableModuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/AvailableModuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/AvailableModuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/AvailableModuleSummary)
