---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/Sample-CPack-Template-for-Creating-Process-Check-Rule.html
---

# Sample Conformance Pack Template for Creating Process Checks
<a name="Sample-CPack-Template-for-Creating-Process-Check-Rule"></a>

```
################################################################################
#
#  Conformance Pack template for process check
#
################################################################################
Resources:
  AWSConfigProcessCheck:
    Properties:
      ConfigRuleName: RuleName
      Description: Description of Rule
      Source:
        Owner: AWS
        SourceIdentifier: AWS_CONFIG_PROCESS_CHECK
    Type: AWS::Config::ConfigRule
```

See two sample templates, the [Operational Best Practices for CIS AWS Foundations Benchmark v1.4 Level 1](operational-best-practices-for-cis_aws_benchmark_level_1.md) template and the [Operational Best Practices for CIS AWS Foundations Benchmark v1.4 Level 2](operational-best-practices-for-cis_aws_benchmark_level_2.md) template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
