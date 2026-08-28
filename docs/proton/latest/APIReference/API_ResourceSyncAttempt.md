---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ResourceSyncAttempt.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ResourceSyncAttempt
<a name="API_ResourceSyncAttempt"></a>

Detail data for a resource sync attempt activated by a push to a repository.

## Contents
<a name="API_ResourceSyncAttempt_Contents"></a>

 ** events **   <a name="proton-Type-ResourceSyncAttempt-events"></a>
An array of events with detail data.
Type: Array of [ResourceSyncEvent](API_ResourceSyncEvent.md) objects
Required: Yes

 ** initialRevision **   <a name="proton-Type-ResourceSyncAttempt-initialRevision"></a>
Detail data for the initial repository commit, path and push.
Type: [Revision](API_Revision.md) object
Required: Yes

 ** startedAt **   <a name="proton-Type-ResourceSyncAttempt-startedAt"></a>
The time when the sync attempt started.
Type: Timestamp
Required: Yes

 ** status **   <a name="proton-Type-ResourceSyncAttempt-status"></a>
The status of the sync attempt.
Type: String
Valid Values: `INITIATED | IN_PROGRESS | SUCCEEDED | FAILED`
Required: Yes

 ** target **   <a name="proton-Type-ResourceSyncAttempt-target"></a>
The resource that is synced to.
Type: String
Required: Yes

 ** targetRevision **   <a name="proton-Type-ResourceSyncAttempt-targetRevision"></a>
Detail data for the target revision.
Type: [Revision](API_Revision.md) object
Required: Yes

## See Also
<a name="API_ResourceSyncAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ResourceSyncAttempt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ResourceSyncAttempt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ResourceSyncAttempt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
