---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_SessionLogger.html
---

# SessionLogger
<a name="API_SessionLogger"></a>

The session logger resource.

## Contents
<a name="API_SessionLogger_Contents"></a>

 ** sessionLoggerArn **   <a name="workspacesweb-Type-SessionLogger-sessionLoggerArn"></a>
The ARN of the session logger resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** additionalEncryptionContext **   <a name="workspacesweb-Type-SessionLogger-additionalEncryptionContext"></a>
The additional encryption context of the session logger.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Pattern: `[\s\S]*`
Required: No

 ** associatedPortalArns **   <a name="workspacesweb-Type-SessionLogger-associatedPortalArns"></a>
The associated portal ARN.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** creationDate **   <a name="workspacesweb-Type-SessionLogger-creationDate"></a>
The date the session logger resource was created.
Type: Timestamp
Required: No

 ** customerManagedKey **   <a name="workspacesweb-Type-SessionLogger-customerManagedKey"></a>
The custom managed key of the session logger.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** displayName **   <a name="workspacesweb-Type-SessionLogger-displayName"></a>
The human-readable display name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[ _\-\d\w]+`
Required: No

 ** eventFilter **   <a name="workspacesweb-Type-SessionLogger-eventFilter"></a>
The filter that specifies which events to monitor.
Type: [EventFilter](API_EventFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** logConfiguration **   <a name="workspacesweb-Type-SessionLogger-logConfiguration"></a>
The configuration that specifies where logs are fowarded.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

## See Also
<a name="API_SessionLogger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/SessionLogger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/SessionLogger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/SessionLogger)
