---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorization.html
---

# AppAuthorization
<a name="API_AppAuthorization"></a>

Contains information about an app authorization.

## Contents
<a name="API_AppAuthorization_Contents"></a>

 ** app **   <a name="appfabric-Type-AppAuthorization-app"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** appAuthorizationArn **   <a name="appfabric-Type-AppAuthorization-appAuthorizationArn"></a>
The Amazon Resource Name (ARN) of the app authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** appBundleArn **   <a name="appfabric-Type-AppAuthorization-appBundleArn"></a>
The Amazon Resource Name (ARN) of the app bundle for the app authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** authType **   <a name="appfabric-Type-AppAuthorization-authType"></a>
The authorization type.
Type: String
Valid Values: `oauth2 | apiKey`
Required: Yes

 ** createdAt **   <a name="appfabric-Type-AppAuthorization-createdAt"></a>
The timestamp of when the app authorization was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="appfabric-Type-AppAuthorization-status"></a>
The state of the app authorization.
The following states are possible:
+  `PendingConnect`: The initial state of the app authorization. The app authorization is created but not yet connected.
+  `Connected`: The app authorization is connected to the application, and is ready to be used.
+  `ConnectionValidationFailed`: The app authorization received a validation exception when trying to connect to the application. If the app authorization is in this state, you should verify the configured credentials and try to connect the app authorization again.
+  `TokenAutoRotationFailed`: AppFabric failed to refresh the access token. If the app authorization is in this state, you should try to reconnect the app authorization.
Type: String
Valid Values: `PendingConnect | Connected | ConnectionValidationFailed | TokenAutoRotationFailed`
Required: Yes

 ** tenant **   <a name="appfabric-Type-AppAuthorization-tenant"></a>
Contains information about an application tenant, such as the application display name and identifier.
Type: [Tenant](API_Tenant.md) object
Required: Yes

 ** updatedAt **   <a name="appfabric-Type-AppAuthorization-updatedAt"></a>
The timestamp of when the app authorization was last updated.
Type: Timestamp
Required: Yes

 ** authUrl **   <a name="appfabric-Type-AppAuthorization-authUrl"></a>
The application URL for the OAuth flow.
Type: String
Required: No

 ** persona **   <a name="appfabric-Type-AppAuthorization-persona"></a>
The user persona of the app authorization.
This field should always be `admin`.
Type: String
Valid Values: `admin | endUser`
Required: No

## See Also
<a name="API_AppAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/AppAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/AppAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/AppAuthorization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
