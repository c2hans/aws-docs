---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBProxyTarget.html
---

# DBProxyTarget
<a name="API_DBProxyTarget"></a>

Contains the details for an RDS Proxy target. It represents an RDS DB instance or Aurora DB cluster that the proxy can connect to. One or more targets are associated with an RDS Proxy target group.

This data type is used as a response element in the `DescribeDBProxyTargets` action.

## Contents
<a name="API_DBProxyTarget_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Endpoint **
The writer endpoint for the RDS DB instance or Aurora DB cluster.
Type: String
Required: No

 ** Port **
The port that the RDS Proxy uses to connect to the target RDS DB instance or Aurora DB cluster.
Type: Integer
Required: No

 ** RdsResourceId **
The identifier representing the target. It can be the instance identifier for an RDS DB instance, or the cluster identifier for an Aurora DB cluster.
Type: String
Required: No

 ** Role **
A value that indicates whether the target of the proxy can be used for read/write or read-only operations.
Type: String
Valid Values: `READ_WRITE | READ_ONLY | UNKNOWN`
Required: No

 ** TargetArn **
The Amazon Resource Name (ARN) for the RDS DB instance or Aurora DB cluster.
Type: String
Required: No

 ** TargetHealth **
Information about the connection health of the RDS Proxy target.
Type: [TargetHealth](API_TargetHealth.md) object
Required: No

 ** TrackedClusterId **
The DB cluster identifier when the target represents an Aurora DB cluster. This field is blank when the target represents an RDS DB instance.
Type: String
Required: No

 ** Type **
Specifies the kind of database, such as an RDS DB instance or an Aurora DB cluster, that the target represents.
Type: String
Valid Values: `RDS_INSTANCE | RDS_SERVERLESS_ENDPOINT | TRACKED_CLUSTER`
Required: No

## See Also
<a name="API_DBProxyTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBProxyTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBProxyTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBProxyTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
