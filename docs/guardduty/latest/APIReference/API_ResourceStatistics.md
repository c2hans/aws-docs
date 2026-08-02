---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ResourceStatistics.html
---

# ResourceStatistics
<a name="API_ResourceStatistics"></a>

Information about each resource type associated with the `groupedByResource` statistics.

## Contents
<a name="API_ResourceStatistics_Contents"></a>

 ** accountId **   <a name="guardduty-Type-ResourceStatistics-accountId"></a>
The ID of the AWS account.
Type: String
Required: No

 ** lastGeneratedAt **   <a name="guardduty-Type-ResourceStatistics-lastGeneratedAt"></a>
The timestamp at which the statistics for this resource was last generated.
Type: Timestamp
Required: No

 ** resourceId **   <a name="guardduty-Type-ResourceStatistics-resourceId"></a>
ID associated with each resource. The following list provides the mapping of the resource type and resource ID.

**Mapping of resource and resource ID**
+ AccessKey - `resource.accessKeyDetails.accessKeyId`
+ Container - `resource.containerDetails.id`
+ ECSCluster - `resource.ecsClusterDetails.name`
+ EKSCluster - `resource.eksClusterDetails.name`
+ Instance - `resource.instanceDetails.instanceId`
+ KubernetesCluster - `resource.kubernetesDetails.kubernetesWorkloadDetails.name`
+ Lambda - `resource.lambdaDetails.functionName`
+ RDSDBInstance - `resource.rdsDbInstanceDetails.dbInstanceIdentifier`
+ S3Bucket - `resource.s3BucketDetails.name`
+ S3Object - `resource.s3BucketDetails.name`
Type: String
Required: No

 ** resourceType **   <a name="guardduty-Type-ResourceStatistics-resourceType"></a>
The type of resource.
Type: String
Required: No

 ** totalFindings **   <a name="guardduty-Type-ResourceStatistics-totalFindings"></a>
The total number of findings associated with this resource.
Type: Integer
Required: No

## See Also
<a name="API_ResourceStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ResourceStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ResourceStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ResourceStatistics)
