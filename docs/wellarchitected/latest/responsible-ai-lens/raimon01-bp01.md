---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon01-bp01.html
---

# RAIMON01-BP01 Obtain consent for monitoring production data
<a name="raimon01-bp01"></a>

 As appropriate, implement consent mechanisms that inform users about what data will be collected for monitoring purposes and obtain appropriate permissions before beginning data collection activities. This includes considering opt-in and opt-out data collection strategies while adhering to guidance from your legal counsel. When appropriate, design transparent consent processes that explain monitoring objectives, data usage, retention periods, and user rights regarding their monitored data for opting in or opt out. Establish procedures for managing consent changes over time, including mechanisms for users to withdraw consent and processes for handling data from users who have opted out.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-91"></a>

1.  As appropriate, create a consent framework defining data collection types and purposes. For example, a music recommendation system might ask for user consent to use system inputs and outputs for validating and improving system performance.

1.  Build verification mechanisms to check consent before data collection. For example, an e-commerce system might verify consent status before collecting browsing behavior for personalization.

1.  Deploy technical controls to filter data based on consent preferences. For instance, a smart home system might adjust data collection granularity based on user consent levels. Use Amazon S3 for storing data by consent levels.

1.  If appropriate and feasible, set up automated processes for consent changes.

1.  Maintain audit trails of consent activities. For example, a financial AI system might track consent changes with timestamps in an immutable ledger.

## Resources
<a name="resources-87"></a>

 **Related documents:**
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
+  [Amazon S3](https://aws.amazon.com/s3/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
