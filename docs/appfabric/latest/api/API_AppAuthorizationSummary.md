---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorizationSummary.html
---

# AppAuthorizationSummary
<a name="API_AppAuthorizationSummary"></a>

Contains a summary of an app authorization.

## Contents
<a name="API_AppAuthorizationSummary_Contents"></a>

 ** app **   <a name="appfabric-Type-AppAuthorizationSummary-app"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** appAuthorizationArn **   <a name="appfabric-Type-AppAuthorizationSummary-appAuthorizationArn"></a>
The Amazon Resource Name (ARN) of the app authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** appBundleArn **   <a name="appfabric-Type-AppAuthorizationSummary-appBundleArn"></a>
The Amazon Resource Name (ARN) of the app bundle for the app authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** status **   <a name="appfabric-Type-AppAuthorizationSummary-status"></a>
The state of the app authorization.
The following states are possible:
+  `PendingConnect`: The initial state of the app authorization. The app authorization is created but not yet connected.
+  `Connected`: The app authorization is connected to the application, and is ready to be used.
+  `ConnectionValidationFailed`: The app authorization received a validation exception when trying to connect to the application. If the app authorization is in this state, you should verify the configured credentials and try to connect the app authorization again.
+  `TokenAutoRotationFailed`: AppFabric failed to refresh the access token. If the app authorization is in this state, you should try to reconnect the app authorization.
Type: String
Valid Values: `PendingConnect | Connected | ConnectionValidationFailed | TokenAutoRotationFailed`
Required: Yes

 ** tenant **   <a name="appfabric-Type-AppAuthorizationSummary-tenant"></a>
Contains information about an application tenant, such as the application display name and identifier.
Type: [Tenant](API_Tenant.md) object
Required: Yes

 ** updatedAt **   <a name="appfabric-Type-AppAuthorizationSummary-updatedAt"></a>
Timestamp for when the app authorization was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_AppAuthorizationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/AppAuthorizationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/AppAuthorizationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/AppAuthorizationSummary)
