---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBInstanceStatusInfo.html
---

# DBInstanceStatusInfo
<a name="API_DBInstanceStatusInfo"></a>

Provides a list of status information for a DB instance.

## Contents
<a name="API_DBInstanceStatusInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **
Details of the error if there is an error for the instance. If the instance isn't in an error state, this value is blank.
Type: String
Required: No

 ** Normal **
Indicates whether the instance is operating normally (TRUE) or is in an error state (FALSE).
Type: Boolean
Required: No

 ** Status **
The status of the DB instance. For a StatusType of read replica, the values can be replicating, replication stop point set, replication stop point reached, error, stopped, or terminated.
Type: String
Required: No

 ** StatusType **
This value is currently "read replication."
Type: String
Required: No

## See Also
<a name="API_DBInstanceStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBInstanceStatusInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBInstanceStatusInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBInstanceStatusInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
