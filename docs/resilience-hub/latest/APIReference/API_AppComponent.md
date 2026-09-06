---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppComponent.html
---

# AppComponent
<a name="API_AppComponent"></a>

Defines an AppComponent.

## Contents
<a name="API_AppComponent_Contents"></a>

 ** name **   <a name="resiliencehub-Type-AppComponent-name"></a>
Name of the AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: Yes

 ** type **   <a name="resiliencehub-Type-AppComponent-type"></a>
The type of AppComponent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** additionalInfo **   <a name="resiliencehub-Type-AppComponent-additionalInfo"></a>
Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
Type: String to array of strings map
Key Pattern: `\S{1,128}`
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** id **   <a name="resiliencehub-Type-AppComponent-id"></a>
Identifier of the AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: No

## See Also
<a name="API_AppComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppComponent)
