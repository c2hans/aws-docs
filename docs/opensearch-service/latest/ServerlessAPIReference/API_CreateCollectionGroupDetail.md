---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionGroupDetail.html
---

# CreateCollectionGroupDetail
<a name="API_CreateCollectionGroupDetail"></a>

Details about the created collection group.

## Contents
<a name="API_CreateCollectionGroupDetail_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-arn"></a>
The Amazon Resource Name (ARN) of the collection group.
Type: String
Required: No

 ** capacityLimits **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-capacityLimits"></a>
The capacity limits for the collection group, in OpenSearch Compute Units (OCUs).
Type: [CollectionGroupCapacityLimits](API_CollectionGroupCapacityLimits.md) object
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-createdDate"></a>
The Epoch time when the collection group was created.
Type: Long
Required: No

 ** description **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-description"></a>
The description of the collection group.
Type: String
Required: No

 ** generation **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-generation"></a>
The generation of Amazon OpenSearch Serverless for the collection group.
Type: String
Valid Values: `CLASSIC | NEXTGEN`
Required: No

 ** id **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-id"></a>
The unique identifier of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** name **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-name"></a>
The name of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** standbyReplicas **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-standbyReplicas"></a>
Indicates whether standby replicas are used for the collection group.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** tags **   <a name="opensearchserverless-Type-CreateCollectionGroupDetail-tags"></a>
A map of key-value pairs associated with the collection group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_CreateCollectionGroupDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateCollectionGroupDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateCollectionGroupDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateCollectionGroupDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
