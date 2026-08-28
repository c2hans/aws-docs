---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryLifeCycle.html
---

# RecoveryLifeCycle
<a name="API_RecoveryLifeCycle"></a>

An object representing the Source Network recovery Lifecycle.

## Contents
<a name="API_RecoveryLifeCycle_Contents"></a>

 ** apiCallDateTime **   <a name="drs-Type-RecoveryLifeCycle-apiCallDateTime"></a>
The date and time the last Source Network recovery was initiated.
Type: Timestamp
Required: No

 ** jobID **   <a name="drs-Type-RecoveryLifeCycle-jobID"></a>
The ID of the Job that was used to last recover the Source Network.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `drsjob-[0-9a-zA-Z]{17}`
Required: No

 ** lastRecoveryResult **   <a name="drs-Type-RecoveryLifeCycle-lastRecoveryResult"></a>
The status of the last recovery status of this Source Network.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | SUCCESS | FAIL | PARTIAL_SUCCESS | ASSOCIATE_SUCCESS | ASSOCIATE_FAIL`
Required: No

## See Also
<a name="API_RecoveryLifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryLifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryLifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryLifeCycle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
