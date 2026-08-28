---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBInstanceStatusInfo.html
---

# DBInstanceStatusInfo
<a name="API_DBInstanceStatusInfo"></a>

Provides a list of status information for a DB instance.

## Contents
<a name="API_DBInstanceStatusInfo_Contents"></a>

 ** Message **
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.
Type: String
Required: No

 ** Normal **
Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.
Type: Boolean
Required: No

 ** Status **
Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.
Type: String
Required: No

 ** StatusType **
This value is currently "read replication."
Type: String
Required: No

## See Also
<a name="API_DBInstanceStatusInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBInstanceStatusInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBInstanceStatusInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBInstanceStatusInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
