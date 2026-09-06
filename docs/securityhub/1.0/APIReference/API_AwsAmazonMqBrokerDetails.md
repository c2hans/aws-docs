---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAmazonMqBrokerDetails.html
---

# AwsAmazonMqBrokerDetails
<a name="API_AwsAmazonMqBrokerDetails"></a>

 Provides details about an Amazon MQ message broker. A message broker allows software applications and components to communicate using various programming languages, operating systems, and formal messaging protocols.

## Contents
<a name="API_AwsAmazonMqBrokerDetails_Contents"></a>

 ** AuthenticationStrategy **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-AuthenticationStrategy"></a>
 The authentication strategy used to secure the broker. The default is `SIMPLE`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AutoMinorVersionUpgrade **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-AutoMinorVersionUpgrade"></a>
 Whether automatically upgrade new minor versions for brokers, as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot.
Type: Boolean
Required: No

 ** BrokerArn **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-BrokerArn"></a>
 The Amazon Resource Name (ARN) of the broker.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BrokerId **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-BrokerId"></a>
 The unique ID that Amazon MQ generates for the broker.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BrokerName **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-BrokerName"></a>
The broker's name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeploymentMode **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-DeploymentMode"></a>
 The broker's deployment mode.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionOptions **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-EncryptionOptions"></a>
 Encryption options for the broker. Doesn’t apply to RabbitMQ brokers.
Type: [AwsAmazonMqBrokerEncryptionOptionsDetails](API_AwsAmazonMqBrokerEncryptionOptionsDetails.md) object
Required: No

 ** EngineType **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-EngineType"></a>
 The type of broker engine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-EngineVersion"></a>
 The version of the broker engine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostInstanceType **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-HostInstanceType"></a>
 The broker's instance type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LdapServerMetadata **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-LdapServerMetadata"></a>
 The metadata of the Lightweight Directory Access Protocol (LDAP) server used to authenticate and authorize connections to the broker. This is an optional failover server.
Type: [AwsAmazonMqBrokerLdapServerMetadataDetails](API_AwsAmazonMqBrokerLdapServerMetadataDetails.md) object
Required: No

 ** Logs **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-Logs"></a>
 Turns on Amazon CloudWatch logging for brokers.
Type: [AwsAmazonMqBrokerLogsDetails](API_AwsAmazonMqBrokerLogsDetails.md) object
Required: No

 ** MaintenanceWindowStartTime **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-MaintenanceWindowStartTime"></a>
 The scheduled time period (UTC) during which Amazon MQ begins to apply pending updates or patches to the broker.
Type: [AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails](API_AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails.md) object
Required: No

 ** PubliclyAccessible **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-PubliclyAccessible"></a>
 Permits connections from applications outside of the VPC that hosts the broker's subnets.
Type: Boolean
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-SecurityGroups"></a>
 The list of rules (one minimum, 125 maximum) that authorize connections to brokers.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** StorageType **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-StorageType"></a>
 The broker's storage type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubnetIds **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-SubnetIds"></a>
 The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Users **   <a name="securityhub-Type-AwsAmazonMqBrokerDetails-Users"></a>
 The list of all broker usernames for the specified broker. Doesn't apply to RabbitMQ brokers.
Type: Array of [AwsAmazonMqBrokerUsersDetails](API_AwsAmazonMqBrokerUsersDetails.md) objects
Required: No

## See Also
<a name="API_AwsAmazonMqBrokerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAmazonMqBrokerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAmazonMqBrokerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAmazonMqBrokerDetails)
