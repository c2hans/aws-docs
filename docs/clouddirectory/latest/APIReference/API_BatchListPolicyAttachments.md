---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListPolicyAttachments.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListPolicyAttachments
<a name="API_BatchListPolicyAttachments"></a>

Returns all of the `ObjectIdentifiers` to which a given policy is attached inside a [BatchRead](API_BatchRead.md) operation. For more information, see [ListPolicyAttachments](API_ListPolicyAttachments.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchListPolicyAttachments_Contents"></a>

 ** PolicyReference **   <a name="amazoncds-Type-BatchListPolicyAttachments-PolicyReference"></a>
The reference that identifies the policy object.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** MaxResults **   <a name="amazoncds-Type-BatchListPolicyAttachments-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListPolicyAttachments-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListPolicyAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListPolicyAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListPolicyAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListPolicyAttachments)
