---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationError.html
---

# DataReplicationError
<a name="API_DataReplicationError"></a>

Error in data replication.

## Contents
<a name="API_DataReplicationError_Contents"></a>

 ** error **   <a name="drs-Type-DataReplicationError-error"></a>
Error in data replication.
Type: String
Valid Values: `AGENT_NOT_SEEN | SNAPSHOTS_FAILURE | NOT_CONVERGING | UNSTABLE_NETWORK | FAILED_TO_CREATE_SECURITY_GROUP | FAILED_TO_LAUNCH_REPLICATION_SERVER | FAILED_TO_BOOT_REPLICATION_SERVER | FAILED_TO_AUTHENTICATE_WITH_SERVICE | FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE | FAILED_TO_CREATE_STAGING_DISKS | FAILED_TO_ATTACH_STAGING_DISKS | FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT | FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER | FAILED_TO_START_DATA_TRANSFER`
Required: No

 ** rawError **   <a name="drs-Type-DataReplicationError-rawError"></a>
Error in data replication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_DataReplicationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DataReplicationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DataReplicationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DataReplicationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
