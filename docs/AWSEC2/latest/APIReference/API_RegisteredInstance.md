---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisteredInstance.html
---

# RegisteredInstance
<a name="API_RegisteredInstance"></a>

Describes an Amazon EC2 instance that is enabled for SQL Server High Availability standby detection monitoring.

## Contents
<a name="API_RegisteredInstance_Contents"></a>

 ** haStatus **
The SQL Server High Availability status of the instance. Valid values are:
+  `processing` - The SQL Server High Availability status for the SQL Server High Availability instance is being updated.
+  `active` - The SQL Server High Availability instance is an active node in an SQL Server High Availability cluster.
+  `standby` - The SQL Server High Availability instance is a standby failover node in an SQL Server High Availability cluster.
+  `invalid` - An error occurred due to misconfigured permissions, or unable to dertemine SQL Server High Availability status for the SQL Server High Availability instance.
Type: String
Valid Values: `processing | active | standby | invalid`
Required: No

 ** instanceId **
The ID of the SQL Server High Availability instance.
Type: String
Required: No

 ** lastUpdatedTime **
The date and time when the instance's SQL Server High Availability status was last updated, in the ISO 8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp
Required: No

 ** processingStatus **
A brief description of the SQL Server High Availability status. If the instance is in the `invalid` High Availability status, this parameter includes the error message.
Type: String
Required: No

 ** sqlServerCredentials **
The ARN of the AWS Secrets Manager secret containing the SQL Server access credentials for the SQL Server High Availability instance. If not specified, deafult local user credentials will be used by the AWS Systems Manager agent.
Type: String
Required: No

 ** sqlServerLicenseUsage **
The license type for the SQL Server license. Valid values include:
+  `full` - The SQL Server High Availability instance is using a full SQL Server license.
+  `waived` - The SQL Server High Availability instance is waived from the SQL Server license.
Type: String
Valid Values: `full | waived`
Required: No

 ** TagSet.N **
The tags assigned to the SQL Server High Availability instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RegisteredInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RegisteredInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RegisteredInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RegisteredInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
