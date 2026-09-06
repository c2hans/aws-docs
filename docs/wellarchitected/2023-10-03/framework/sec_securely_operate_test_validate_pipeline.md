---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_securely_operate_test_validate_pipeline.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC01-BP06 Automate testing and validation of security controls in pipelines
<a name="sec_securely_operate_test_validate_pipeline"></a>

 Establish secure baselines and templates for security mechanisms that are tested and validated as part of your build, pipelines, and processes. Use tools and automation to test and validate all security controls continuously. For example, scan items such as machine images and infrastructure-as-code templates for security vulnerabilities, irregularities, and drift from an established baseline at each stage. AWS CloudFormation Guard can help you verify that CloudFormation templates are safe, save you time, and reduce the risk of configuration error.

Reducing the number of security misconfigurations introduced into a production environment is critical—the more quality control and reduction of defects you can perform in the build process, the better. Design continuous integration and continuous deployment (CI/CD) pipelines to test for security issues whenever possible. CI/CD pipelines offer the opportunity to enhance security at each stage of build and delivery. CI/CD security tooling must also be kept updated to mitigate evolving threats.

Track changes to your workload configuration to help with compliance auditing, change management, and investigations that may apply to you. You can use AWS Config to record and evaluate your AWS and third-party resources. It allows you to continuously audit and assess the overall compliance with rules and conformance packs, which are collections of rules with remediation actions.

Change tracking should include planned changes, which are part of your organization’s change control process (sometimes referred to as MACD—Move, Add, Change, Delete), unplanned changes, and unexpected changes, such as incidents. Changes might occur on the infrastructure, but they might also be related to other categories, such as changes in code repositories, machine images and application inventory changes, process and policy changes, or documentation changes.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate configuration management: Enforce and validate secure configurations automatically by using a configuration management service or tool.
  +  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
  +  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
  +  [Set Up a CI/CD Pipeline on AWS](https://aws.amazon.com/getting-started/projects/set-up-ci-cd-pipeline/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [How to use service control policies to set permission guardrails across accounts in your AWS Organization](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/)

 **Related videos:**
+  [Managing Multi-Account AWS Environments Using AWS Organizations](https://youtu.be/fxo67UeeN1A)
+  [Security Best Practices the Well-Architected Way](https://youtu.be/u6BCVkXkPnM)
