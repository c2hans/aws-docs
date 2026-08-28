---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_IteratorDescription.html
---

# IteratorDescription
<a name="API_IteratorDescription"></a>

Provides information about the current iterator.

## Contents
<a name="API_IteratorDescription_Contents"></a>

 ** iteratorPosition **   <a name="keyspaces-Type-IteratorDescription-iteratorPosition"></a>
 Indicates the current iterator's position within the shard. The possible values are:
+  `AT_TIP` - No more records are currently available.
+  `BEHIND_TIP` - Additional records may be available.
Stream progresses in absence of customer records. `BEHIND_TIP` with an empty `changeRecords` list indicates the stream is progressing but no customer records are available at this position. Continue polling normally.
Type: String
Valid Values: `AT_TIP | BEHIND_TIP`
Required: No

## See Also
<a name="API_IteratorDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/IteratorDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/IteratorDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/IteratorDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
