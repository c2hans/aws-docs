---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Gateway.html
---

# Gateway
<a name="API_Gateway"></a>

A gateway is an AWS Backup Gateway appliance that runs on the customer's network to provide seamless connectivity to backup storage in the AWS Cloud.

## Contents
<a name="API_Gateway_Contents"></a>

 ** GatewayArn **   <a name="bgw-Type-Gateway-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway. Use the `ListGateways` operation to return a list of gateways for your account and AWS Region.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: No

 ** GatewayDisplayName **   <a name="bgw-Type-Gateway-GatewayDisplayName"></a>
The display name of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** GatewayType **   <a name="bgw-Type-Gateway-GatewayType"></a>
The type of the gateway.
Type: String
Valid Values: `BACKUP_VM`
Required: No

 ** HypervisorId **   <a name="bgw-Type-Gateway-HypervisorId"></a>
The hypervisor ID of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** LastSeenTime **   <a name="bgw-Type-Gateway-LastSeenTime"></a>
The last time AWS Backup gateway communicated with the gateway, in Unix format and UTC time.
Type: Timestamp
Required: No

## See Also
<a name="API_Gateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/Gateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/Gateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/Gateway)
