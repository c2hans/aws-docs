---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchAttachPolicy.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchAttachPolicy
<a name="API_BatchAttachPolicy"></a>

Attaches a policy object to a regular object inside a [BatchRead](API_BatchRead.md) operation. For more information, see [AttachPolicy](API_AttachPolicy.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchAttachPolicy_Contents"></a>

 ** ObjectReference **   <a name="amazoncds-Type-BatchAttachPolicy-ObjectReference"></a>
The reference that identifies the object to which the policy will be attached.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** PolicyReference **   <a name="amazoncds-Type-BatchAttachPolicy-PolicyReference"></a>
The reference that is associated with the policy object.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## See Also
<a name="API_BatchAttachPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
