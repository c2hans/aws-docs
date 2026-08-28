---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchAttachToIndex.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchAttachToIndex
<a name="API_BatchAttachToIndex"></a>

Attaches the specified object to the specified index inside a [BatchRead](API_BatchRead.md) operation. For more information, see [AttachToIndex](API_AttachToIndex.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchAttachToIndex_Contents"></a>

 ** IndexReference **   <a name="amazoncds-Type-BatchAttachToIndex-IndexReference"></a>
A reference to the index that you are attaching the object to.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** TargetReference **   <a name="amazoncds-Type-BatchAttachToIndex-TargetReference"></a>
A reference to the object that you are attaching to the index.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## See Also
<a name="API_BatchAttachToIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachToIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachToIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachToIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
