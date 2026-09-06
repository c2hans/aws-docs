---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SubscriptionPrincipal.html
---

# SubscriptionPrincipal
<a name="API_SubscriptionPrincipal"></a>

A user or group in the IAM Identity Center instance connected to the Amazon Q Business application.

## Contents
<a name="API_SubscriptionPrincipal_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="qbusiness-Type-SubscriptionPrincipal-group"></a>
The identifier of a group in the IAM Identity Center instance connected to the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** user **   <a name="qbusiness-Type-SubscriptionPrincipal-user"></a>
The identifier of a user in the IAM Identity Center instance connected to the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

## See Also
<a name="API_SubscriptionPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/SubscriptionPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/SubscriptionPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/SubscriptionPrincipal)
