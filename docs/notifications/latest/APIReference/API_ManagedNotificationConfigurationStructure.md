---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationConfigurationStructure.html
---

# ManagedNotificationConfigurationStructure
<a name="API_ManagedNotificationConfigurationStructure"></a>

Describes the basic structure and properties of a `ManagedNotificationConfiguration`.

## Contents
<a name="API_ManagedNotificationConfigurationStructure_Contents"></a>

 ** arn **   <a name="Notifications-Type-ManagedNotificationConfigurationStructure-arn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

 ** description **   <a name="Notifications-Type-ManagedNotificationConfigurationStructure-description"></a>
The description of the `ManagedNotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\u0001-\u001F\u007F-\u009F]*`
Required: Yes

 ** name **   <a name="Notifications-Type-ManagedNotificationConfigurationStructure-name"></a>
The name of the `ManagedNotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-]+`
Required: Yes

## See Also
<a name="API_ManagedNotificationConfigurationStructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationConfigurationStructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationConfigurationStructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationConfigurationStructure)
