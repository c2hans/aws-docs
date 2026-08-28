---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionDetail.html
---

# CollectionDetail
<a name="API_CollectionDetail"></a>

Details about each OpenSearch Serverless collection, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints for federal government workloads.

## Contents
<a name="API_CollectionDetail_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-CollectionDetail-arn"></a>
The Amazon Resource Name (ARN) of the collection.
Type: String
Required: No

 ** collectionEndpoint **   <a name="opensearchserverless-Type-CollectionDetail-collectionEndpoint"></a>
Collection-specific endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection.
Type: String
Required: No

 ** collectionGroupName **   <a name="opensearchserverless-Type-CollectionDetail-collectionGroupName"></a>
The name of the collection group that contains this collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** createdDate **   <a name="opensearchserverless-Type-CollectionDetail-createdDate"></a>
The Epoch time when the collection was created.
Type: Long
Required: No

 ** dashboardEndpoint **   <a name="opensearchserverless-Type-CollectionDetail-dashboardEndpoint"></a>
Collection-specific endpoint used to access OpenSearch Dashboards.
Type: String
Required: No

 ** deletionProtection **   <a name="opensearchserverless-Type-CollectionDetail-deletionProtection"></a>
Indicates whether deletion protection is `ENABLED` or `DISABLED` for the collection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** description **   <a name="opensearchserverless-Type-CollectionDetail-description"></a>
A description of the collection.
Type: String
Required: No

 ** failureCode **   <a name="opensearchserverless-Type-CollectionDetail-failureCode"></a>
A failure code associated with the request.
Type: String
Required: No

 ** failureMessage **   <a name="opensearchserverless-Type-CollectionDetail-failureMessage"></a>
A message associated with the failure code.
Type: String
Required: No

 ** fipsEndpoints **   <a name="opensearchserverless-Type-CollectionDetail-fipsEndpoints"></a>
FIPS-compliant endpoints for the collection. These endpoints use FIPS 140-3 validated cryptographic modules and are required for federal government workloads that must comply with FedRAMP security standards.
Type: [FipsEndpoints](API_FipsEndpoints.md) object
Required: No

 ** id **   <a name="opensearchserverless-Type-CollectionDetail-id"></a>
A unique identifier for the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** kmsKeyArn **   <a name="opensearchserverless-Type-CollectionDetail-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt the collection.
Type: String
Required: No

 ** lastModifiedDate **   <a name="opensearchserverless-Type-CollectionDetail-lastModifiedDate"></a>
The date and time when the collection was last modified.
Type: Long
Required: No

 ** name **   <a name="opensearchserverless-Type-CollectionDetail-name"></a>
The name of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** standbyReplicas **   <a name="opensearchserverless-Type-CollectionDetail-standbyReplicas"></a>
Details about an OpenSearch Serverless collection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** status **   <a name="opensearchserverless-Type-CollectionDetail-status"></a>
The current status of the collection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED | UPDATE_FAILED`
Required: No

 ** type **   <a name="opensearchserverless-Type-CollectionDetail-type"></a>
The type of collection.
Type: String
Valid Values: `SEARCH | TIMESERIES | VECTORSEARCH`
Required: No

 ** vectorOptions **   <a name="opensearchserverless-Type-CollectionDetail-vectorOptions"></a>
Configuration options for vector search capabilities in the collection.
Type: [VectorOptions](API_VectorOptions.md) object
Required: No

## See Also
<a name="API_CollectionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
