---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Hypervisor.html
---

# Hypervisor
<a name="API_Hypervisor"></a>

Represents the hypervisor's permissions to which the gateway will connect.

A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.

## Contents
<a name="API_Hypervisor_Contents"></a>

 ** Host **   <a name="bgw-Type-Hypervisor-Host"></a>
The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `.+`
Required: No

 ** HypervisorArn **   <a name="bgw-Type-Hypervisor-HypervisorArn"></a>
The Amazon Resource Name (ARN) of the hypervisor.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: No

 ** KmsKeyArn **   <a name="bgw-Type-Hypervisor-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service used to encrypt the hypervisor.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `(^arn:(aws|aws-cn|aws-us-gov):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`
Required: No

 ** Name **   <a name="bgw-Type-Hypervisor-Name"></a>
The name of the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** State **   <a name="bgw-Type-Hypervisor-State"></a>
The state of the hypervisor.
Type: String
Valid Values: `PENDING | ONLINE | OFFLINE | ERROR`
Required: No

## See Also
<a name="API_Hypervisor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/Hypervisor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/Hypervisor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/Hypervisor)
