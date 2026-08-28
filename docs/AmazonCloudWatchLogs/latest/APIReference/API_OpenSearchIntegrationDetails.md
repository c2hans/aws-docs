---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_OpenSearchIntegrationDetails.html
---

# OpenSearchIntegrationDetails
<a name="API_OpenSearchIntegrationDetails"></a>

This structure contains complete information about one CloudWatch Logs integration. This structure is returned by a [GetIntegration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetIntegration.html) operation.

## Contents
<a name="API_OpenSearchIntegrationDetails_Contents"></a>

 ** accessPolicy **   <a name="CWL-Type-OpenSearchIntegrationDetails-accessPolicy"></a>
This structure contains information about the OpenSearch Service data access policy used for this integration. The access policy defines the access controls for the collection. This data access policy was automatically created as part of the integration setup. For more information about OpenSearch Service data access policies, see [Data access control for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) in the OpenSearch Service Developer Guide.
Type: [OpenSearchDataAccessPolicy](API_OpenSearchDataAccessPolicy.md) object
Required: No

 ** application **   <a name="CWL-Type-OpenSearchIntegrationDetails-application"></a>
This structure contains information about the OpenSearch Service application used for this integration. An OpenSearch Service application is the web application that was created by the integration with CloudWatch Logs. It hosts the vended logs dashboards.
Type: [OpenSearchApplication](API_OpenSearchApplication.md) object
Required: No

 ** collection **   <a name="CWL-Type-OpenSearchIntegrationDetails-collection"></a>
This structure contains information about the OpenSearch Service collection used for this integration. This collection was created as part of the integration setup. An OpenSearch Service collection is a logical grouping of one or more indexes that represent an analytics workload. For more information, see [Creating and managing OpenSearch Service Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collections.html).
Type: [OpenSearchCollection](API_OpenSearchCollection.md) object
Required: No

 ** dataSource **   <a name="CWL-Type-OpenSearchIntegrationDetails-dataSource"></a>
This structure contains information about the OpenSearch Service data source used for this integration. This data source was created as part of the integration setup. An OpenSearch Service data source defines the source and destination for OpenSearch Service queries. It includes the role required to execute queries and write to collections.
For more information about OpenSearch Service data sources , see [Creating OpenSearch Service data source integrations with Amazon S3.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html)
Type: [OpenSearchDataSource](API_OpenSearchDataSource.md) object
Required: No

 ** encryptionPolicy **   <a name="CWL-Type-OpenSearchIntegrationDetails-encryptionPolicy"></a>
This structure contains information about the OpenSearch Service encryption policy used for this integration. The encryption policy was created automatically when you created the integration. For more information, see [Encryption policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html#serverless-encryption-policies) in the OpenSearch Service Developer Guide.
Type: [OpenSearchEncryptionPolicy](API_OpenSearchEncryptionPolicy.md) object
Required: No

 ** lifecyclePolicy **   <a name="CWL-Type-OpenSearchIntegrationDetails-lifecyclePolicy"></a>
This structure contains information about the OpenSearch Service data lifecycle policy used for this integration. The lifecycle policy determines the lifespan of the data in the collection. It was automatically created as part of the integration setup.
For more information, see [Using data lifecycle policies with OpenSearch Service Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html) in the OpenSearch Service Developer Guide.
Type: [OpenSearchLifecyclePolicy](API_OpenSearchLifecyclePolicy.md) object
Required: No

 ** networkPolicy **   <a name="CWL-Type-OpenSearchIntegrationDetails-networkPolicy"></a>
This structure contains information about the OpenSearch Service network policy used for this integration. The network policy assigns network access settings to collections. For more information, see [Network policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html#serverless-network-policies) in the OpenSearch Service Developer Guide.
Type: [OpenSearchNetworkPolicy](API_OpenSearchNetworkPolicy.md) object
Required: No

 ** workspace **   <a name="CWL-Type-OpenSearchIntegrationDetails-workspace"></a>
This structure contains information about the OpenSearch Service workspace used for this integration. An OpenSearch Service workspace is the collection of dashboards along with other OpenSearch Service tools. This workspace was created automatically as part of the integration setup. For more information, see [Centralized OpenSearch user interface (Dashboards) with OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).
Type: [OpenSearchWorkspace](API_OpenSearchWorkspace.md) object
Required: No

## See Also
<a name="API_OpenSearchIntegrationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/OpenSearchIntegrationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/OpenSearchIntegrationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/OpenSearchIntegrationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
