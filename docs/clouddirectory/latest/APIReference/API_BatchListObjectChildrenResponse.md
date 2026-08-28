---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListObjectChildrenResponse.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListObjectChildrenResponse
<a name="API_BatchListObjectChildrenResponse"></a>

Represents the output of a [ListObjectChildren](API_ListObjectChildren.md) response operation.

## Contents
<a name="API_BatchListObjectChildrenResponse_Contents"></a>

 ** Children **   <a name="amazoncds-Type-BatchListObjectChildrenResponse-Children"></a>
The children structure, which is a map with the key as the `LinkName` and `ObjectIdentifier` as the value.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListObjectChildrenResponse-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListObjectChildrenResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectChildrenResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectChildrenResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectChildrenResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
