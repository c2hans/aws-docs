---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/encrypt-persistent-data-at-rest.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 5. Encrypt persistent data at rest
<a name="encrypt-persistent-data-at-rest"></a>

 For devices such as sensors or cameras, information stored on deployed devices may seem innocuous, but when physical control of a device is not guaranteed that information can be a target for unauthorized actors. Whether in the consumer space like cached videos on cameras, industrial application with proprietary machine learning (ML) models, or even some configuration data for operational environments, the best course of action is to encrypt all data (even transitive data) stored at rest when possible. Some additional considerations include:
+  Identify and classify data collected throughout your IoT ecosystem and learn their corresponding business use case.
+  Categorize data based on the earlier risk analysis, including impact to other stakeholders.
+  Identify opportunities to stop collecting unused data or reducing granularity and retention time, then implement improvements.
+  Ensure integrity of data used to operate devices through cryptographic mechanisms.
+  Apply access controls using least privilege principle to encryption keys, and monitor and audit data access.
+  When necessary, follow least privilege and need-to-know principles when granting access to third parties.
+  Consider privacy and transparency expectations of your customers and corresponding legal requirements.

## Supporting AWS resources
<a name="resources-5"></a>

 AWS provides the following assets and services to help you secure IoT data at the edge and cloud:
+  [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) – For security and compliance.
+  [AWS Data Privacy](https://aws.amazon.com/compliance/data-privacy/)
+  [AWS Privacy Notice](https://aws.amazon.com/privacy/)
+  [AWS Compliance programs and offerings](https://aws.amazon.com/compliance/data-privacy/)
+  [AWS Compliance Solutions Guide](https://aws.amazon.com/compliance/solutions-guide/)
+  [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) – Can be used to create and control the keys used for cryptographic operations in the cloud.
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
