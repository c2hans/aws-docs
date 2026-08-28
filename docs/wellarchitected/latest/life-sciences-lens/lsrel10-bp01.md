---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp01.html
---

# LSREL10-BP01 Implement comprehensive reliability testing
<a name="lsrel10-bp01"></a>

 Develop structured protocols that test reliability aspects including load performance, failover, recovery, and long-term stability. For regulated systems, include reliability tests in the validation package with traceability to user and regulatory requirements. Use controlled chaos engineering experiments to validate resilience by safely injecting faults and failures into your applications while preserving data integrity and adherence.

 **Desired outcome:**
+  Reliability tests are systematic, repeatable, and documented.
+  Systems demonstrate resilience to failure injection and load stress.
+  Test evidence supports regulatory validation requirements.

 **Common anti-patterns:**
+  Treating reliability tests as optional instead of mandatory.
+  Running only idealized tests without simulating failures.
+  Lack of traceability between reliability test cases and regulatory or user requirements.

 **Benefits of establishing this best practice:**
+  Improves predictability of experiments and workloads under stress.
+  Builds regulator and auditor confidence in system resilience.
+  Reduces costly delays by uncovering reliability gaps early.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Define reliability acceptance criteria in line with user and regulatory requirements.

 Incorporate resilience tests into validation and qualification protocols.

 Perform controlled chaos experiments to uncover weaknesses safely.

 Automate reliability testing where possible for repeatability.

### Implementation steps
<a name="implementation-steps"></a>

1.  Run fault-injection experiments with AWS Fault Injection Service (FIS).

1.  Use AWS CodePipeline to integrate reliability tests into CI/CD.

1.  Capture test logs in Amazon CloudWatch Logs and archive evidence in Amazon S3 Object Lock for regulatory adherence.

1.  Document test execution and results in AWS Audit Manager.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
