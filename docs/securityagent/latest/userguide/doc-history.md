---
source_url: https://docs.aws.amazon.com/securityagent/latest/userguide/doc-history.html
---

# Document history
<a name="doc-history"></a>

The following table describes some of the major updates and new features for the AWS Security Agents User Guide.

| Change | Description | Date |
| --- |--- |--- |
| [Private connections general availability](https://docs.aws.amazon.com/securityagent/latest/userguide/connect-private-connection.html) | Private connections are now generally available. This capability allows AWS Security Agent to connect to source control systems running in private networks using Amazon VPC Lattice, without exposing your systems to the public internet. | July 28, 2026 |
| [Private connections (preview)](https://docs.aws.amazon.com/securityagent/latest/userguide/connect-private-connection.html) | Added documentation for private connections. This new capability allows AWS Security Agent to connect to source control systems running in private networks using Amazon VPC Lattice, without exposing your systems to the public internet. | June 16, 2026 |
| [Threat modeling (preview)](https://docs.aws.amazon.com/securityagent/latest/userguide/quickstart-threat-model.html) | Added documentation for threat modeling. This new capability builds a threat model of your application from design documents (scope docs), source code (sources), or both. Scope docs are feature design documents that define the focus of the analysis, while source code provides context about your existing system. If you don’t provide scope docs, the agent generates a threat model from the source code alone. Each run produces a system overview and a set of threats classified by STRIDE category with severity ratings and recommendations. | June 8, 2026 |
| [Full repository code review (preview)](https://docs.aws.amazon.com/securityagent/latest/userguide/quickstart-code-review.html) | Added documentation for full repository code review. This new capability performs context-aware security analysis of your entire codebase and generates code remediation for findings. | May 12, 2026 |
| [Updated Region availability for finding remediation](https://docs.aws.amazon.com/securityagent/latest/userguide/remediate-finding.html) | Region availability for penetration test finding remediation in the AWS Security Agent web application has been updated. | April 16, 2026 |
| [Updated Region availability for enabling finding remediation](https://docs.aws.amazon.com/securityagent/latest/userguide/enable-remediate-findings.html) | Region availability for enabling penetration test finding remediation in the AWS Management Console has been updated. | April 16, 2026 |
| [Customer managed key support](https://docs.aws.amazon.com/securityagent/latest/userguide/customer-managed-keys.html) | Added documentation for customer managed key (CMK) support. You can now specify a customer managed KMS key when creating Agent Spaces and integrations to encrypt your data with keys you control. | March 31, 2026 |
| [AWS managed policy updates](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-awsmanpol.html) | Added AWSSecurityAgentWebAppPolicy managed policy for the new TargetDomain and DesignReviewFeedback resource types. | March 31, 2026 |
| [AWS managed policy updates](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-awsmanpol.html) | Added AWSSecurityAgentWebAppPolicy managed policy for the new AgentSpace resource type and IAM action name changes. | February 9, 2026 |
| [AWS managed policy updates](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-awsmanpol.html) | Updated SecurityAgentWebAppAPIPolicy to allow customers to delete design reviews. | January 28, 2026 |
| [AWS managed policy updates](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-awsmanpol.html) | Updated SecurityAgentWebAppAPIPolicy to allow customers to start automated code remediation for security findings. | January 20, 2026 |
| [AWS managed policy updates](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-awsmanpol.html) | Updated to SecurityAgentWebAppAPIPolicy to allow customers to view images in the console. | December 5, 2025 |
| [AWS Security Agents initial release](#doc-history) | Initial documentation for service launch | December 2, 2025 |
