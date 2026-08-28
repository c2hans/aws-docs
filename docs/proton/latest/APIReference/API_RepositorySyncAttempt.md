---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_RepositorySyncAttempt.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# RepositorySyncAttempt
<a name="API_RepositorySyncAttempt"></a>

Detail data for a repository sync attempt activated by a push to a repository.

## Contents
<a name="API_RepositorySyncAttempt_Contents"></a>

 ** events **   <a name="proton-Type-RepositorySyncAttempt-events"></a>
Detail data for sync attempt events.
Type: Array of [RepositorySyncEvent](API_RepositorySyncEvent.md) objects
Required: Yes

 ** startedAt **   <a name="proton-Type-RepositorySyncAttempt-startedAt"></a>
The time when the sync attempt started.
Type: Timestamp
Required: Yes

 ** status **   <a name="proton-Type-RepositorySyncAttempt-status"></a>
The sync attempt status.
Type: String
Valid Values: `INITIATED | IN_PROGRESS | SUCCEEDED | FAILED | QUEUED`
Required: Yes

## See Also
<a name="API_RepositorySyncAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/RepositorySyncAttempt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/RepositorySyncAttempt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/RepositorySyncAttempt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
