---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GatewayDetails.html
---

# GatewayDetails
<a name="API_GatewayDetails"></a>

The details of gateway.

## Contents
<a name="API_GatewayDetails_Contents"></a>

 ** DeprecationDate **   <a name="bgw-Type-GatewayDetails-DeprecationDate"></a>
Date after which this gateway will not receive software updates for new features and bug fixes.
Type: Timestamp
Required: No

 ** GatewayArn **   <a name="bgw-Type-GatewayDetails-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway. Use the `ListGateways` operation to return a list of gateways for your account and AWS Region.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: No

 ** GatewayDisplayName **   <a name="bgw-Type-GatewayDetails-GatewayDisplayName"></a>
The display name of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** GatewayType **   <a name="bgw-Type-GatewayDetails-GatewayType"></a>
The type of the gateway type.
Type: String
Valid Values: `BACKUP_VM`
Required: No

 ** HypervisorId **   <a name="bgw-Type-GatewayDetails-HypervisorId"></a>
The hypervisor ID of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** LastSeenTime **   <a name="bgw-Type-GatewayDetails-LastSeenTime"></a>
Details showing the last time AWS Backup gateway communicated with the cloud, in Unix format and UTC time.
Type: Timestamp
Required: No

 ** MaintenanceStartTime **   <a name="bgw-Type-GatewayDetails-MaintenanceStartTime"></a>
Returns your gateway's weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway's time zone. Can be weekly or monthly.
Type: [MaintenanceStartTime](API_MaintenanceStartTime.md) object
Required: No

 ** NextUpdateAvailabilityTime **   <a name="bgw-Type-GatewayDetails-NextUpdateAvailabilityTime"></a>
Details showing the next update availability time of the gateway.
Type: Timestamp
Required: No

 ** SoftwareVersion **   <a name="bgw-Type-GatewayDetails-SoftwareVersion"></a>
The version number of the software running on the gateway appliance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** VpcEndpoint **   <a name="bgw-Type-GatewayDetails-VpcEndpoint"></a>
The DNS name for the virtual private cloud (VPC) endpoint the gateway uses to connect to the cloud for backup gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_GatewayDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/GatewayDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/GatewayDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/GatewayDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
