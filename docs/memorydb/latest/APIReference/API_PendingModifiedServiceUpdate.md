---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_PendingModifiedServiceUpdate.html
---

# PendingModifiedServiceUpdate
<a name="API_PendingModifiedServiceUpdate"></a>

Update action that has yet to be processed for the corresponding apply/stop request

## Contents
<a name="API_PendingModifiedServiceUpdate_Contents"></a>

 ** ServiceUpdateName **   <a name="MemoryDB-Type-PendingModifiedServiceUpdate-ServiceUpdateName"></a>
The unique ID of the service update
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-PendingModifiedServiceUpdate-Status"></a>
The status of the service update
Type: String
Valid Values: `available | in-progress | complete | scheduled`
Required: No

## See Also
<a name="API_PendingModifiedServiceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/PendingModifiedServiceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/PendingModifiedServiceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/PendingModifiedServiceUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
