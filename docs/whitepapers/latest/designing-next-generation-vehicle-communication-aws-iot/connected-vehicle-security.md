---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/connected-vehicle-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connected vehicle security
<a name="connected-vehicle-security"></a>

## Vehicle to cloud network connectivity
<a name="vehicle-to-cloud-network-connectivity"></a>

 Customers have several choices when connecting their vehicles to AWS. Each option presents trade-offs in areas like scalability and cost. Below we will illustrate the options with diagrams. In each diagram, we will assume traffic is flowing through a Mobile Network Operator (MNO).

 **Connectivity over the internet**

 With this option, each vehicle's Electric Control Unit (ECU) uses AWS IoT Core's public endpoint for communication. IoT Core's public endpoint will resolve to an AWS owned public IP address. With this deployment model, the bandwidth from each ECU is limited by the internet performance. Additionally, we recommend using an application-level encryption mechanism like TLS to encrypt your data in transit. You can also encrypt highly sensitive data client side, which we will illustrate below.

 **Connectivity via VPN over the internet**

 With this option, the ECU of each vehicle must establish a VPN connection into AWS. The VPN connection will allow applications running on ECUs to consume resources within Amazon Virtual Private Clouds (VPCs).

 The ECUs can then communicate with IoT Core over VPC Endpoints. The VPC Endpoints will create elastic network interfaces within the VPCs.

 With this deployment model, the throughput from each ECU is limited by internet performance, and the maximum available bandwidth for each IPSec tunnel.

 There are additional [charges for accessing data over interface endpoints](https://aws.amazon.com/privatelink/pricing/).

 **Private connectivity over Direct Connect**

 This deployment model leverages both VPC endpoints and Direct Connect for providing access to AWS IoT Core. Traffic from all ECUs is first redirected to an on-premises data center.

 Direct Connect is used to transfer data from on-premises data-centers into AWS. You can either use a private virtual interface (VIF) or a Transit VIF. With the Private VIF option, you can connect up to a maximum of 500 VPCs, and with Transit VIF you can connect to up to 5,000 Regional VPCs. However, with the Transit VIF option, you'll incur [Transit Gateway data processing charges](https://aws.amazon.com/transit-gateway/pricing/) by the GB. Since Private VIF option doesn't use a Transit Gateway, there are no Transit Gateway data processing charges with the Private VIF option.

 Since the AWS IoT Core endpoints will be deployed in only a few VPCs, we recommend using the Private VIF option as it's more cost effective.

 There are additional [charges for accessing data over interface endpoints](https://aws.amazon.com/privatelink/pricing/).

## Identity best practices on AWS IoT Core
<a name="identity-best-practices-on-aws-iot-core"></a>

 AWS IoT allows client authentication with different types of [device credentials](https://docs.aws.amazon.com/iot/latest/developerguide/client-authentication.html). In most use cases, X.509 certificates are the recommended method of authenticating your ECU. Another method, custom authentication, should only be used in migration scenarios where none of the above options are available. You should **only** use IAM-user; credentials during research and development. If you need to make direct AWS API calls from the device, it is recommended you use the [IoT Core Credential Provider](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html). The credential provider authenticates a caller using an X.509 certificate and issues a temporary, limited permissions security token. The token can be used to sign and authenticate any AWS request.

 Each device should have a unique X.509 certificate, and identities should not be shared across ECUs. ECUs must use TLS version 1.3 when connecting to AWS IoT Core for enhanced security and performance. Customers can use [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) [Audit Checks](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html) for a list of comprehensive device security posture checks.

 A vehicle has several connected ECUs, and an ECU may have more than one identity depending on back-end interaction requirements. It is important to tie these identities together using an asset store mapped to different ECUs using something like an ECU ID. You can use [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/) which provides a built-in [registry for Things](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) and their [registered X.509 certificates](https://docs.aws.amazon.com/iot/latest/developerguide/register-device-cert.html). The registry allows you to define attributes (three per thing) which are name-value pairs you can use to store information about the thing, such as ECU ID. Each certificate registered in AWS IoT Core can be associated with an [AWS IoT Core Policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) (either directly or via [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)) that authorizes actions that the ECU can perform on the AWS IoT Core service such as allowing connections, publishing or subscribing to certain [MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html). IoT Core also allows you to register certificates the first time an ECU connects using [Just-in-time-Registration](https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html) by registering the Certificate Authority (CA) that issued the certificate.

 Least privilege is the practice of only granting access that identities, in this case ECUs need to perform the intended function. It is important to discuss some anti-patterns and best practice guidance for granting least privilege to ECUs in AWS IoT Core. Common anti-patterns include:
+  Granting broad permission by assigning "`*`" to actions or resources. A "`*`" on action will allow the device any data plane operation. A "`*`" on resources will authorize any resource to conduct the policy action.
+  Avoid using hardcoded values like client ID, and instead use characteristics of things such as `ThingName`, `ThingNameType`, `Thing Attributes`, or certificate attributes such as `Subject`, `Issuer`, and `Subject Alternate Name`.

 Continuous monitoring of your policies is an important mechanism to ensure that overly permissive policies are addressed. It is recommended to review your AWS IoT Device Defender Audit checks related to overly permissive and misconfigured ECUs, and create a response/remediation strategy when these ECUs are detected. You can send your AWS IoT Device Defender Audit findings to [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), which is a cloud security posture management service that performs security best practice checks, aggregates alerts, and enables automated remediation.

 For more information, see the [Identity checklist](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens-checklist/design-principle-1.html) in the AWS Well-Architected IoT Lens.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
