---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionActionIdentifier.html
---

# BatchGetSessionActionIdentifier
<a name="API_BatchGetSessionActionIdentifier"></a>

The identifiers for a session action.

## Contents
<a name="API_BatchGetSessionActionIdentifier_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchGetSessionActionIdentifier-farmId"></a>
The farm ID of the session action.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetSessionActionIdentifier-jobId"></a>
The job ID of the session action.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetSessionActionIdentifier-queueId"></a>
The queue ID of the session action.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionActionId **   <a name="deadlinecloud-Type-BatchGetSessionActionIdentifier-sessionActionId"></a>
The session action ID.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## See Also
<a name="API_BatchGetSessionActionIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionActionIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionActionIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionActionIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
