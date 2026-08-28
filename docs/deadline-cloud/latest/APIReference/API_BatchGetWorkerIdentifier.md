---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetWorkerIdentifier.html
---

# BatchGetWorkerIdentifier
<a name="API_BatchGetWorkerIdentifier"></a>

The identifiers for a worker.

## Contents
<a name="API_BatchGetWorkerIdentifier_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchGetWorkerIdentifier-farmId"></a>
The farm ID of the worker.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-BatchGetWorkerIdentifier-fleetId"></a>
The fleet ID of the worker.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** workerId **   <a name="deadlinecloud-Type-BatchGetWorkerIdentifier-workerId"></a>
The worker ID.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetWorkerIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetWorkerIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetWorkerIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetWorkerIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
