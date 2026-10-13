---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_LinkedIssue.html
---

# LinkedIssue
<a name="API_LinkedIssue"></a>

A reference to an issue created for a finding in a third-party issue tracker.

## Contents
<a name="API_LinkedIssue_Contents"></a>

 ** integrationId **   <a name="securityagent-Type-LinkedIssue-integrationId"></a>
The integration identifier for the issue-tracker provider.
Type: String
Required: No

 ** issueId **   <a name="securityagent-Type-LinkedIssue-issueId"></a>
The stable numeric issue identifier.
Type: String
Required: No

 ** issueKey **   <a name="securityagent-Type-LinkedIssue-issueKey"></a>
The issue key.
Type: String
Required: No

 ** issueUrl **   <a name="securityagent-Type-LinkedIssue-issueUrl"></a>
The issue URL.
Type: String
Required: No

 ** projectKey **   <a name="securityagent-Type-LinkedIssue-projectKey"></a>
The key of the project the issue belongs to.
Type: String
Required: No

 ** provider **   <a name="securityagent-Type-LinkedIssue-provider"></a>
The issue-tracker provider.
Type: String
Valid Values: `GITHUB | GITLAB | BITBUCKET | CONFLUENCE | AZURE_DEVOPS | JIRA`
Required: No

 ** siteUrl **   <a name="securityagent-Type-LinkedIssue-siteUrl"></a>
The Atlassian Cloud site URL.
Type: String
Required: No

## See Also
<a name="API_LinkedIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/LinkedIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/LinkedIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/LinkedIssue)
