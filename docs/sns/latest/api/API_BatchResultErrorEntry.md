---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_BatchResultErrorEntry.html
---

# BatchResultErrorEntry
<a name="API_BatchResultErrorEntry"></a>

Gives a detailed description of failed messages in the batch.

## Contents
<a name="API_BatchResultErrorEntry_Contents"></a>

 ** Code **
An error code representing why the action failed on this entry.
Type: String
Required: Yes

 ** Id **
The `Id` of an entry in a batch request
Type: String
Required: Yes

 ** SenderFault **
Specifies whether the error happened due to the caller of the batch API action.
Type: Boolean
Required: Yes

 ** Message **
A message explaining why the action failed on this entry.
Type: String
Required: No

## See Also
<a name="API_BatchResultErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/BatchResultErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/BatchResultErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/BatchResultErrorEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
