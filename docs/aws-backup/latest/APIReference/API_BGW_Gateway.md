---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_Gateway.html
---

# Gateway
<a name="API_BGW_Gateway"></a>

A gateway is an AWS Backup Gateway appliance that runs on the customer's network to provide seamless connectivity to backup storage in the AWS Cloud.

## Contents
<a name="API_BGW_Gateway_Contents"></a>

 ** GatewayArn **   <a name="Backup-Type-BGW_Gateway-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway. Use the `ListGateways` operation to return a list of gateways for your account and AWS Region.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: No

 ** GatewayDisplayName **   <a name="Backup-Type-BGW_Gateway-GatewayDisplayName"></a>
The display name of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** GatewayType **   <a name="Backup-Type-BGW_Gateway-GatewayType"></a>
The type of the gateway.
Type: String
Valid Values: `BACKUP_VM`
Required: No

 ** HypervisorId **   <a name="Backup-Type-BGW_Gateway-HypervisorId"></a>
The hypervisor ID of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** LastSeenTime **   <a name="Backup-Type-BGW_Gateway-LastSeenTime"></a>
The last time AWS Backup gateway communicated with the gateway, in Unix format and UTC time.
Type: Timestamp
Required: No

## See Also
<a name="API_BGW_Gateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/Gateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/Gateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/Gateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
