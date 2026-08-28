---
source_url: https://docs.aws.amazon.com/pinpoint/latest/archguide/security-infrastructure-security.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Infrastructure security in Amazon Pinpoint
<a name="security-infrastructure-security"></a>

As a managed service, Amazon Pinpoint is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon Pinpoint through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Although you can make these API calls from any network location, Amazon Pinpoint supports resource-based access policies. These policies can include restrictions based on source IP address. To learn more about this type of policy, see [Managing access using policies](security-iam.md#security_iam_access-manage).

In addition, you can configure and use various AWS security features to control access to Amazon Pinpoint resources from any mobile or web apps that you integrate with Amazon Pinpoint. This includes restrictions on API calls for tasks such as adding endpoints, updating endpoint data, submitting event data, and reporting usage data.

To use these features, we recommend that you use the AWS Mobile SDKs or AWS Amplify JavaScript libraries to integrate mobile and web apps with Amazon Pinpoint. For Android or iOS apps, we recommend that you use the AWS Mobile SDK for Android or the AWS Mobile SDK for iOS, respectively. For JavaScript-based mobile or web apps, we recommend that you use the AWS Amplify JavaScript Library for the web or the AWS Amplify JavaScript Library for React Native. To learn more about these resources, see [Getting started with the AWS mobile SDKs](https://docs.amplify.aws/gen1/android/sdk/), and [Getting started with the AWS Amplify library for react native](https://docs.amplify.aws/gen1/react-native/start/getting-started/introduction/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
