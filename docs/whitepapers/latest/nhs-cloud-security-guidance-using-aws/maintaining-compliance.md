---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/maintaining-compliance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Maintaining compliance
<a name="maintaining-compliance"></a>

 Having achieved compliance with the expected controls for a given risk classification, it is essential to maintain compliance, since changes to workload requirements, operating system patches, changes to configuration, and so on, all give rise to configuration drift away from the ideal established at the implementation stage. Securing a system deployed to the cloud is not a one-off activity; it is an ongoing process. This section describes the approach and the available AWS services to help with this process.

## Secure practices
<a name="secure-practices"></a>

 Before considering the tools available to implement secure practices, it is essential to ensure that good security methodology and processes exist and are adhered to within your organization. There is useful advice on what to establish in this regard within the following resources:
+  The [Cloud Adoption Framework’s Security Perspective](https://aws.amazon.com/professional-services/CAF/#Security_Perspective);
+  [The AWS Well-Architected Framework’s Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html); and
+  Other complementary [AWS security best practices](https://aws.amazon.com/security/security-resources/).

## AWS CloudFormation drift detection
<a name="aws-cloudformation-drift-detection"></a>

 AWS resources deployed and managed through the CloudFormation service (described in [Section 5.1: Configuration and change management](principle-5-operational-security.md#section-5.1-configuration-and-change-management) in this document) can benefit from a feature called *drift detection*, which discerns configuration changes to AWS resources outside this service’s agency upon request. For more information, see [Detecting unmanaged configuration changes to stacks and resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html).

## AWS Config
<a name="aws-config"></a>

 Included within the Landing Zone solution, this service tracks configuration settings of AWS resources over time against a desired-state baseline, and raises alerts (and optionally triggers remedial action) when changes are detected.

 The service also enables configuration to be audited, in order to demonstrate compliance (or otherwise) against a baseline. See the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) for a detailed description of how to use it.

## AWS Systems Manager
<a name="aws-systems-manager"></a>

 To minimise the possibility and impact of unauthorised or erroneous configuration changes being made to the operating systems of Amazon EC2 instances and the applications on them, as well as other AWS resources, use the [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) suite of services.

## AWS Security Hub CSPM
<a name="aws-security-hub"></a>

 This service brings together the variety of security tools available within the AWS environment, providing automated compliance checks and aggregated security findings from disparate security tools in a standardised format. For more information, see [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html).

## Third-party tools
<a name="third-party-tools"></a>

 A variety of AWS Partners offer tools that complement the capabilities of AWS Config and provide configuration management for the resources in the cloud, such as software running on Amazon EC2 instances. See the [Infrastructure Configuration Management](https://d1.awsstatic.com/aws-answers/AWS_Infrastructure_Configuration_Management.pdf) Solution Brief for more information.
