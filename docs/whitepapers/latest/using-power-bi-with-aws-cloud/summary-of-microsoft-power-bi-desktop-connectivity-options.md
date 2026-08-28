---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/summary-of-microsoft-power-bi-desktop-connectivity-options.html
---

# Summary of Microsoft Power BI Desktop connectivity options
<a name="summary-of-microsoft-power-bi-desktop-connectivity-options"></a>

For a small number of users with light dataset requirements, running Microsoft Power BI Desktop on premises and connecting securely over the internet, or using Site-to-Site VPN, might be an adequate solution. Make sure that security is configured and maintained in this model. We also recommend testing this configuration to determine if it meets users' performance expectations

As the number of users increase, we recommend that you consider connectivity through AWS Direct Connect. Direct Connect provides a better user experience when loading larger datasets. Make sure that users are aware of the cost implications of transferring large datasets.

We recommend that you evaluate running Microsoft Power BI Desktop in the AWS Cloud. This is likely to provide both the best performance experience for the end user and the best management experience for cloud administrators. Amazon WorkSpaces in particular can scale from a small number of users to thousands of users. These Services also provide significant security and management benefits.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
