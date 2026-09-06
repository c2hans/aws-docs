---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_SessionSummary.html
---

# SessionSummary
<a name="API_SessionSummary"></a>

Summary information about a secure browser session.

## Contents
<a name="API_SessionSummary_Contents"></a>

 ** endTime **   <a name="workspacesweb-Type-SessionSummary-endTime"></a>
The end time of the session.
Type: Timestamp
Required: No

 ** portalArn **   <a name="workspacesweb-Type-SessionSummary-portalArn"></a>
The ARN of the web portal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** sessionId **   <a name="workspacesweb-Type-SessionSummary-sessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[\s\S]*`
Required: No

 ** startTime **   <a name="workspacesweb-Type-SessionSummary-startTime"></a>
The start time of the session.
Type: Timestamp
Required: No

 ** status **   <a name="workspacesweb-Type-SessionSummary-status"></a>
The status of the session.
Type: String
Valid Values: `Active | Terminated`
Required: No

 ** username **   <a name="workspacesweb-Type-SessionSummary-username"></a>
The username of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/SessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/SessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/SessionSummary)
