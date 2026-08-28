---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_QopConfiguration.html
---

# QopConfiguration
<a name="API_QopConfiguration"></a>

The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS) cluster.

## Contents
<a name="API_QopConfiguration_Contents"></a>

 ** DataTransferProtection **   <a name="DataSync-Type-QopConfiguration-DataTransferProtection"></a>
The data transfer protection setting configured on the HDFS cluster. This setting corresponds to your `dfs.data.transfer.protection` setting in the `hdfs-site.xml` file on your Hadoop cluster.
Type: String
Valid Values: `DISABLED | AUTHENTICATION | INTEGRITY | PRIVACY`
Required: No

 ** RpcProtection **   <a name="DataSync-Type-QopConfiguration-RpcProtection"></a>
The RPC protection setting configured on the HDFS cluster. This setting corresponds to your `hadoop.rpc.protection` setting in your `core-site.xml` file on your Hadoop cluster.
Type: String
Valid Values: `DISABLED | AUTHENTICATION | INTEGRITY | PRIVACY`
Required: No

## See Also
<a name="API_QopConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/QopConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/QopConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/QopConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
