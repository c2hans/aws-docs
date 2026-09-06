---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentSessionSummary.html
---

# DevEnvironmentSessionSummary
<a name="API_DevEnvironmentSessionSummary"></a>

Information about active sessions for a Dev Environment.

## Contents
<a name="API_DevEnvironmentSessionSummary_Contents"></a>

 ** devEnvironmentId **   <a name="codecatalyst-Type-DevEnvironmentSessionSummary-devEnvironmentId"></a>
The system-generated unique ID of the Dev Environment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** id **   <a name="codecatalyst-Type-DevEnvironmentSessionSummary-id"></a>
The system-generated unique ID of the Dev Environment session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.
Required: Yes

 ** projectName **   <a name="codecatalyst-Type-DevEnvironmentSessionSummary-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** spaceName **   <a name="codecatalyst-Type-DevEnvironmentSessionSummary-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** startedTime **   <a name="codecatalyst-Type-DevEnvironmentSessionSummary-startedTime"></a>
The date and time the session started, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp
Required: Yes

## See Also
<a name="API_DevEnvironmentSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/DevEnvironmentSessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/DevEnvironmentSessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/DevEnvironmentSessionSummary)
