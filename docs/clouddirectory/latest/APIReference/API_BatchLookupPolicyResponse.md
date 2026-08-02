---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchLookupPolicyResponse.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchLookupPolicyResponse
<a name="API_BatchLookupPolicyResponse"></a>

Represents the output of a [LookupPolicy](API_LookupPolicy.md) response operation.

## Contents
<a name="API_BatchLookupPolicyResponse_Contents"></a>

 ** NextToken **   <a name="amazoncds-Type-BatchLookupPolicyResponse-NextToken"></a>
The pagination token.
Type: String
Required: No

 ** PolicyToPathList **   <a name="amazoncds-Type-BatchLookupPolicyResponse-PolicyToPathList"></a>
Provides list of path to policies. Policies contain `PolicyId`, `ObjectIdentifier`, and `PolicyType`. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies).
Type: Array of [PolicyToPath](API_PolicyToPath.md) objects
Required: No

## See Also
<a name="API_BatchLookupPolicyResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchLookupPolicyResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchLookupPolicyResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchLookupPolicyResponse)
