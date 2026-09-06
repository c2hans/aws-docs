---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_PortalSummary.html
---

# PortalSummary
<a name="API_PortalSummary"></a>

The summary of the portal.

## Contents
<a name="API_PortalSummary_Contents"></a>

 ** portalArn **   <a name="workspacesweb-Type-PortalSummary-portalArn"></a>
The ARN of the web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** authenticationType **   <a name="workspacesweb-Type-PortalSummary-authenticationType"></a>
The type of authentication integration points used when signing into the web portal. Defaults to `Standard`.
 `Standard` web portals are authenticated directly through your identity provider. You need to call `CreateIdentityProvider` to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.
 `IAM Identity Center` web portals are authenticated through AWS IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.
Type: String
Valid Values: `Standard | IAM_Identity_Center`
Required: No

 ** browserSettingsArn **   <a name="workspacesweb-Type-PortalSummary-browserSettingsArn"></a>
The ARN of the browser settings that is associated with the web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** browserType **   <a name="workspacesweb-Type-PortalSummary-browserType"></a>
The browser type of the web portal.
Type: String
Valid Values: `Chrome`
Required: No

 ** creationDate **   <a name="workspacesweb-Type-PortalSummary-creationDate"></a>
The creation date of the web portal.
Type: Timestamp
Required: No

 ** dataProtectionSettingsArn **   <a name="workspacesweb-Type-PortalSummary-dataProtectionSettingsArn"></a>
The ARN of the data protection settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** displayName **   <a name="workspacesweb-Type-PortalSummary-displayName"></a>
The name of the web portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.+`
Required: No

 ** instanceType **   <a name="workspacesweb-Type-PortalSummary-instanceType"></a>
The type and resources of the underlying instance.
Type: String
Valid Values: `standard.regular | standard.large | standard.xlarge`
Required: No

 ** ipAccessSettingsArn **   <a name="workspacesweb-Type-PortalSummary-ipAccessSettingsArn"></a>
The ARN of the IP access settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** maxConcurrentSessions **   <a name="workspacesweb-Type-PortalSummary-maxConcurrentSessions"></a>
The maximum number of concurrent sessions for the portal.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** networkSettingsArn **   <a name="workspacesweb-Type-PortalSummary-networkSettingsArn"></a>
The ARN of the network settings that is associated with the web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** portalCustomDomain **   <a name="workspacesweb-Type-PortalSummary-portalCustomDomain"></a>
The custom domain of the web portal that users access in order to start streaming sessions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(|[a-zA-Z0-9]?((?!-)([A-Za-z0-9-]*[A-Za-z0-9])\.)+[a-zA-Z0-9]+)`
Required: No

 ** portalEndpoint **   <a name="workspacesweb-Type-PortalSummary-portalEndpoint"></a>
The endpoint URL of the web portal that users access in order to start streaming sessions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
Required: No

 ** portalStatus **   <a name="workspacesweb-Type-PortalSummary-portalStatus"></a>
The status of the web portal.
Type: String
Valid Values: `Incomplete | Pending | Active`
Required: No

 ** rendererType **   <a name="workspacesweb-Type-PortalSummary-rendererType"></a>
The renderer that is used in streaming sessions.
Type: String
Valid Values: `AppStream`
Required: No

 ** sessionLoggerArn **   <a name="workspacesweb-Type-PortalSummary-sessionLoggerArn"></a>
The ARN of the session logger that is assocaited with the portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** trustStoreArn **   <a name="workspacesweb-Type-PortalSummary-trustStoreArn"></a>
The ARN of the trust that is associated with this web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** userAccessLoggingSettingsArn **   <a name="workspacesweb-Type-PortalSummary-userAccessLoggingSettingsArn"></a>
The ARN of the user access logging settings that is associated with the web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** userSettingsArn **   <a name="workspacesweb-Type-PortalSummary-userSettingsArn"></a>
The ARN of the user settings that is associated with the web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

## See Also
<a name="API_PortalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/PortalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/PortalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/PortalSummary)
