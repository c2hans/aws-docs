---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBProxyTargetGroup.html
---

# DBProxyTargetGroup
<a name="API_DBProxyTargetGroup"></a>

Represents a set of RDS DB instances, Aurora DB clusters, or both that a proxy can connect to. Currently, each target group is associated with exactly one RDS DB instance or Aurora DB cluster.

This data type is used as a response element in the `DescribeDBProxyTargetGroups` action.

## Contents
<a name="API_DBProxyTargetGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConnectionPoolConfig **
The settings that determine the size and behavior of the connection pool for the target group.
Type: [ConnectionPoolConfigurationInfo](API_ConnectionPoolConfigurationInfo.md) object
Required: No

 ** CreatedDate **
The date and time when the target group was first created.
Type: Timestamp
Required: No

 ** DBProxyName **
The identifier for the RDS proxy associated with this target group.
Type: String
Required: No

 ** IsDefault **
Indicates whether this target group is the first one used for connection requests by the associated proxy. Because each proxy is currently associated with a single target group, currently this setting is always `true`.
Type: Boolean
Required: No

 ** Status **
The current status of this target group. A status of `available` means the target group is correctly associated with a database. Other values indicate that you must wait for the target group to be ready, or take some action to resolve an issue.
Type: String
Required: No

 ** TargetGroupArn **
The Amazon Resource Name (ARN) representing the target group.
Type: String
Required: No

 ** TargetGroupName **
The identifier for the target group. This name must be unique for all target groups owned by your AWS account in the specified AWS Region.
Type: String
Required: No

 ** UpdatedDate **
The date and time when the target group was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DBProxyTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBProxyTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBProxyTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBProxyTargetGroup)
