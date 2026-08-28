---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ComputeConfig.html
---

# ComputeConfig
<a name="API_ComputeConfig"></a>

Configuration parameters for provisioning an AWS DMS Serverless replication.

## Contents
<a name="API_ComputeConfig_Contents"></a>

 ** AvailabilityZone **   <a name="DMS-Type-ComputeConfig-AvailabilityZone"></a>
The Availability Zone where the AWS DMS Serverless replication using this configuration will run. The default value is a random, system-chosen Availability Zone in the configuration's AWS Region, for example, `"us-west-2"`. You can't set this parameter if the `MultiAZ` parameter is set to `true`.
Type: String
Required: No

 ** DnsNameServers **   <a name="DMS-Type-ComputeConfig-DnsNameServers"></a>
A list of custom DNS name servers supported for the AWS DMS Serverless replication to access your source or target database. This list overrides the default name servers supported by the AWS DMS Serverless replication. You can specify a comma-separated list of internet addresses for up to four DNS name servers. For example: `"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"`
Type: String
Required: No

 ** KmsKeyId **   <a name="DMS-Type-ComputeConfig-KmsKeyId"></a>
An AWS Key Management Service (AWS KMS) key Amazon Resource Name (ARN) that is used to encrypt the data during AWS DMS Serverless replication.
If you don't specify a value for the `KmsKeyId` parameter, AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your Amazon Web Services account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** MaxCapacityUnits **   <a name="DMS-Type-ComputeConfig-MaxCapacityUnits"></a>
Specifies the maximum value of the AWS DMS capacity units (DCUs) for which a given AWS DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the maximum value that you can specify for AWS DMS Serverless is 384. The `MaxCapacityUnits` parameter is the only DCU parameter you are required to specify.
Type: Integer
Required: No

 ** MinCapacityUnits **   <a name="DMS-Type-ComputeConfig-MinCapacityUnits"></a>
Specifies the minimum value of the AWS DMS capacity units (DCUs) for which a given AWS DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the minimum DCU value that you can specify for AWS DMS Serverless is 1. If you don't set this value, AWS DMS sets this parameter to the minimum DCU value allowed, 1. If there is no current source activity, AWS DMS scales down your replication until it reaches the value specified in `MinCapacityUnits`.
Type: Integer
Required: No

 ** MultiAZ **   <a name="DMS-Type-ComputeConfig-MultiAZ"></a>
Specifies whether the AWS DMS Serverless replication is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the `MultiAZ` parameter is set to `true`.
Type: Boolean
Required: No

 ** PreferredMaintenanceWindow **   <a name="DMS-Type-ComputeConfig-PreferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur for the AWS DMS Serverless replication, in Universal Coordinated Time (UTC). The format is `ddd:hh24:mi-ddd:hh24:mi`.
The default is a 30-minute window selected at random from an 8-hour block of time per AWS Region. This maintenance occurs on a random day of the week. Valid values for days of the week include `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat`, and `Sun`.
Constraints include a minimum 30-minute window.
Type: String
Required: No

 ** ReplicationSubnetGroupId **   <a name="DMS-Type-ComputeConfig-ReplicationSubnetGroupId"></a>
Specifies a subnet group identifier to associate with the AWS DMS Serverless replication.
Type: String
Required: No

 ** VpcSecurityGroupIds **   <a name="DMS-Type-ComputeConfig-VpcSecurityGroupIds"></a>
Specifies the virtual private cloud (VPC) security group to use with the AWS DMS Serverless replication. The VPC security group must work with the VPC containing the replication.
Type: Array of strings
Required: No

## See Also
<a name="API_ComputeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ComputeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ComputeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ComputeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
