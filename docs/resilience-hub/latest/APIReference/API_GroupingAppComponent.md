---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_GroupingAppComponent.html
---

# GroupingAppComponent
<a name="API_GroupingAppComponent"></a>

Creates a new recommended Application Component (AppComponent).

## Contents
<a name="API_GroupingAppComponent_Contents"></a>

 ** appComponentId **   <a name="resiliencehub-Type-GroupingAppComponent-appComponentId"></a>
Indicates the identifier of an AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: Yes

 ** appComponentName **   <a name="resiliencehub-Type-GroupingAppComponent-appComponentName"></a>
Indicates the name of an AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: Yes

 ** appComponentType **   <a name="resiliencehub-Type-GroupingAppComponent-appComponentType"></a>
Indicates the type of an AppComponent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_GroupingAppComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/GroupingAppComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/GroupingAppComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/GroupingAppComponent)
