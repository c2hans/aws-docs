---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_Subscription.html
---

# Subscription
<a name="API_connect-app-integrations_Subscription"></a>

The configuration of an event that the application subscribes.

## Contents
<a name="API_connect-app-integrations_Subscription_Contents"></a>

 ** Event **   <a name="connect-Type-connect-app-integrations_Subscription-Event"></a>
The name of the subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+::[a-zA-Z0-9\/\._\-]+(?:\*)?$`
Required: Yes

 ** Description **   <a name="connect-Type-connect-app-integrations_Subscription-Description"></a>
The description of the subscription.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

## See Also
<a name="API_connect-app-integrations_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/Subscription)
