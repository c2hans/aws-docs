---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheNodeUpdateStatus.html
---

# CacheNodeUpdateStatus
<a name="API_CacheNodeUpdateStatus"></a>

The status of the service update on the cache node

## Contents
<a name="API_CacheNodeUpdateStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheNodeId **
The node ID of the cache cluster
Type: String
Required: No

 ** NodeDeletionDate **
The deletion date of the node
Type: Timestamp
Required: No

 ** NodeUpdateEndDate **
The end date of the update for a node
Type: Timestamp
Required: No

 ** NodeUpdateInitiatedBy **
Reflects whether the update was initiated by the customer or automatically applied
Type: String
Valid Values: `system | customer`
Required: No

 ** NodeUpdateInitiatedDate **
The date when the update is triggered
Type: Timestamp
Required: No

 ** NodeUpdateStartDate **
The start date of the update for a node
Type: Timestamp
Required: No

 ** NodeUpdateStatus **
The update status of the node
Type: String
Valid Values: `not-applied | waiting-to-start | in-progress | stopping | stopped | complete`
Required: No

 ** NodeUpdateStatusModifiedDate **
The date when the NodeUpdateStatus was last modified>
Type: Timestamp
Required: No

## See Also
<a name="API_CacheNodeUpdateStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheNodeUpdateStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheNodeUpdateStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheNodeUpdateStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
