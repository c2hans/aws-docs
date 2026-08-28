---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionSummary.html
---

# CollectionSummary
<a name="API_CollectionSummary"></a>

Details about each OpenSearch Serverless collection.

## Contents
<a name="API_CollectionSummary_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-CollectionSummary-arn"></a>
The Amazon Resource Name (ARN) of the collection.
Type: String
Required: No

 ** collectionGroupName **   <a name="opensearchserverless-Type-CollectionSummary-collectionGroupName"></a>
The name of the collection group that contains this collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** id **   <a name="opensearchserverless-Type-CollectionSummary-id"></a>
The unique identifier of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** kmsKeyArn **   <a name="opensearchserverless-Type-CollectionSummary-kmsKeyArn"></a>
The ARN of the AWS Key Management Service key used to encrypt the collection.
Type: String
Required: No

 ** name **   <a name="opensearchserverless-Type-CollectionSummary-name"></a>
The name of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-CollectionSummary-status"></a>
The current status of the collection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED | UPDATE_FAILED`
Required: No

## See Also
<a name="API_CollectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
