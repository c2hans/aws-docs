---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_KeyValueStore.html
---

# KeyValueStore
<a name="API_KeyValueStore"></a>

The key value store. Use this to separate data from function code, allowing you to update data without having to publish a new version of a function. The key value store holds keys and their corresponding values.

## Contents
<a name="API_KeyValueStore_Contents"></a>

 ** ARN **   <a name="cloudfront-Type-KeyValueStore-ARN"></a>
The Amazon Resource Name (ARN) of the key value store.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-KeyValueStore-Comment"></a>
A comment for the key value store.
Type: String
Required: Yes

 ** Id **   <a name="cloudfront-Type-KeyValueStore-Id"></a>
The unique Id for the key value store.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-KeyValueStore-LastModifiedTime"></a>
The last-modified time of the key value store.
Type: Timestamp
Required: Yes

 ** Name **   <a name="cloudfront-Type-KeyValueStore-Name"></a>
The name of the key value store.
Type: String
Required: Yes

 ** Status **   <a name="cloudfront-Type-KeyValueStore-Status"></a>
The status of the key value store.
Type: String
Required: No

## See Also
<a name="API_KeyValueStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KeyValueStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KeyValueStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KeyValueStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
