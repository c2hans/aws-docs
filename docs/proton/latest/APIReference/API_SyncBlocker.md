---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_SyncBlocker.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# SyncBlocker
<a name="API_SyncBlocker"></a>

Detailed data of the sync blocker.

## Contents
<a name="API_SyncBlocker_Contents"></a>

 ** createdAt **   <a name="proton-Type-SyncBlocker-createdAt"></a>
The time when the sync blocker was created.
Type: Timestamp
Required: Yes

 ** createdReason **   <a name="proton-Type-SyncBlocker-createdReason"></a>
The reason why the sync blocker was created.
Type: String
Required: Yes

 ** id **   <a name="proton-Type-SyncBlocker-id"></a>
The ID of the sync blocker.
Type: String
Required: Yes

 ** status **   <a name="proton-Type-SyncBlocker-status"></a>
The status of the sync blocker.
Type: String
Valid Values: `ACTIVE | RESOLVED`
Required: Yes

 ** type **   <a name="proton-Type-SyncBlocker-type"></a>
The type of the sync blocker.
Type: String
Valid Values: `AUTOMATED`
Required: Yes

 ** contexts **   <a name="proton-Type-SyncBlocker-contexts"></a>
The contexts for the sync blocker.
Type: Array of [SyncBlockerContext](API_SyncBlockerContext.md) objects
Required: No

 ** resolvedAt **   <a name="proton-Type-SyncBlocker-resolvedAt"></a>
The time the sync blocker was resolved.
Type: Timestamp
Required: No

 ** resolvedReason **   <a name="proton-Type-SyncBlocker-resolvedReason"></a>
The reason the sync blocker was resolved.
Type: String
Required: No

## See Also
<a name="API_SyncBlocker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/SyncBlocker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/SyncBlocker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/SyncBlocker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
