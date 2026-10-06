---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ScopeChange.html
---

# ScopeChange
<a name="API_ScopeChange"></a>

A code change in a CI/CD pipeline run that defines what a CI/CD pentest job tests. Each scope change identifies an integrated repository and the commit range for the change.

## Contents
<a name="API_ScopeChange_Contents"></a>

 ** headCommitSha **   <a name="securityagent-Type-ScopeChange-headCommitSha"></a>
The commit SHA at the tip of the change to be tested.
Type: String
Required: Yes

 ** integrationId **   <a name="securityagent-Type-ScopeChange-integrationId"></a>
The identifier of the integration for the source-code provider that hosts the repository.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-ScopeChange-providerResourceId"></a>
The provider-specific identifier of the repository the change belongs to.
Type: String
Required: Yes

 ** baseCommitSha **   <a name="securityagent-Type-ScopeChange-baseCommitSha"></a>
The commit SHA that the change is compared against. When omitted, the change is evaluated against the head commit alone.
Type: String
Required: No

 ** triggerRunId **   <a name="securityagent-Type-ScopeChange-triggerRunId"></a>
The identifier of the CI/CD pipeline run that triggered this pentest job.
Type: String
Required: No

## See Also
<a name="API_ScopeChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ScopeChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ScopeChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ScopeChange)
