---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-threat-detection.html
---

# 7. Threat detection and security posture management for agentic AI systems on AWS
<a name="best-practices-threat-detection"></a>

Active threat detection identifies security incidents and misconfigurations that could enable lateral movement or data compromise. Continuous posture management highlights security drift and identifies toxic combinations.

**This section contains the following best practices:**
+ [7.1 Establish continuous security posture management (General)](#best-practices-7-continuous-security-posture-mgmt)

## 7.1 Establish continuous security posture management (General)
<a name="best-practices-7-continuous-security-posture-mgmt"></a>

Implement continuous posture management that detects misconfigurations in resources and highlights toxic combinations that enable lateral movement. This can prevent attackers from expanding their access across systems. Deploy detection and response capabilities for cloud infrastructure and application environments to identify and respond to security threats that target agentic AI systems. Implement continuous posture management that detects misconfigurations in resources and highlights toxic combinations that enable lateral movement. This can prevent attackers from expanding their access across systems.

A *Cloud-Native Application Protection Platform (CNAPP)* can provide comprehensive security coverage across the entire agentic AI system lifecycle. It combines cloud security posture management for infrastructure configuration monitoring, cloud workload protection for runtime threat detection, and application security testing capabilities. These integrated platforms continuously monitor cloud infrastructure configurations that support agentic AI systems. For example, they can identify misconfigurations in [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) policies, network [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), and [resource permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html). They can also provide real-time behavioral analysis of agent runtime activities to detect anomalous process execution, network connections, and potential code injection attempts.

CNAPP platforms can detect combinations that individually appear benign but collectively create security vulnerabilities, such as overly permissive IAM roles combined with unrestricted network access, or internet-facing agents with compromised authentication mechanisms. These combinations typically result from suboptimal configurations or open vulnerabilities that create exploitable attack paths.

Advanced CNAPP solutions establish behavioral baselines for normal agent operations and employ anomaly detection systems that identify deviations that indicate potential compromise. Examples of deviations might include unusual API call patterns and unexpected data access requests. These platforms implement correlation engines that analyze events across multiple agents and infrastructure components to detect coordinated attacks or sophisticated threats that span multiple system layers.

Complement CNAPP with static code analysis (SCA) tools that examine application source code for hardcoded credentials and unsecure coding patterns. Ideally the SCA and CNAPP solutions should be integrated to provide a more complete dataset for vulnerability management and toxic combination detection.

While CNAPP and SCA tools provide important security capabilities, in isolation, they do not offer complete visibility into agentic AI system threats. These tools primarily focus on infrastructure and traditional application security. They do not specialize in threats that are unique to agentic AI systems (such as prompt manipulation) or emergent behaviors from multi-agent interactions that require specialized detection capabilities.
