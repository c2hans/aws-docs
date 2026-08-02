---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/playbooks.html
---

# Playbooks
<a name="playbooks"></a>

A set of remediations is grouped into a package called a *playbook*. Playbooks are installed, updated, and removed using this solution’s templates. For information about supported remediations in each playbook, refer to [Developer Guide → Playbooks](https://docs.aws.amazon.com/en_us/solutions/latest/automated-security-response-on-aws/playbooks-1.html). This solution currently supports the following playbooks:
+ Security Control, a playbook aligned with the Consolidated control findings feature of AWS Security Hub, published February 23, 2023.
**Important**
When [Consolidated control findings](deciding-where-to-deploy-each-stack.md#consolidated-controls-findings) are enabled in Security Hub, this is the only playbook that should be enabled in the solution.
+  [Center for Internet Security (CIS) Amazon Web Services Foundations benchmarks, version 1.2.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis1v2-standard), published May 18, 2018.
+  [Center for Internet Security (CIS) Amazon Web Services Foundations benchmarks, version 1.4.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis1v4-standard), published November 9, 2022.
+  [Center for Internet Security (CIS) Amazon Web Services Foundations benchmarks, version 3.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis3v0-standard), published May 13, 2024.
+  [AWS Foundational Security Best Practices (FSBP) version 1.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html), published March 2021.
+  [Payment Card Industry Data Security Standards (PCI-DSS) version 3.2.1](https://docs.aws.amazon.com/securityhub/latest/userguide/pci-standard.html), published May 2018.
+  [National Institute of Standards and Technology (NIST) version 5.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/nist-standard.html), published November 2023.

After deploying the solution’s CloudFormation stacks, the playbooks are ready to use immediately—no additional configuration is required to enable remediations for the Security Standards listed above.

## Centralized logging
<a name="centralized-logging"></a>

Automated Security Response on AWS logs to a single CloudWatch Logs group, SO0111-ASR. These logs contain detailed logging from the solution for troubleshooting and management of the solution.
