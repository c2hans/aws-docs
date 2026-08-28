---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops13-bp01.html
---

# EUCOPS13-BP01 Perform regular service reviews to identify significant trends in performance, scalability, and availability
<a name="eucops13-bp01"></a>

 Perform regular reviews of service performance and capabilities to maintain visibility of key issues and focus on service improvement and readiness.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-15"></a>

 While real-time monitoring and alerting is essential in meeting business and technical SLAs with internal and external customers, performing periodic review of logfile and monitoring data can help to identify problem trends and to put in place remediation steps to avoid future outages.

 Along with incumbent monitoring tools, you can use Amazon CloudWatch and Amazon Kinesis to centrally store data to use for retrospective performance and systems health analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
