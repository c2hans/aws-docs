---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-6-personnel-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 6: Personnel security
<a name="principle-6-personnel-security"></a>

 *Where service provider personnel have access to your data and systems you need a high degree of confidence in their trustworthiness. Thorough screening, supported by adequate training, reduces the likelihood of accidental or malicious compromise by service provider personnel.*

****
 The Service User should ensure IT admin staff are strongly authenticated.

 **Applicable risk classes:** III-V

 The [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) service offers flexible user authentication options, including password policies covering aspects such as required length and complexity, expiry, reuse restrictions, and so on, and the option to use multiple factors. This service is described in more detail under Principle 9.

****
 The Service User should have a suitable auditing solution is in place to record all IT admin access to data and hosting environments.

 **Applicable risk classes:** III-V

 The AWS CloudTrail service, described in greater detail in Principle 13, provides the basis for an auditing solution to record such access. It may be configured to capture AWS sign-in and API call events, and access to data stored in Amazon S3 buckets. In addition, the CloudWatch Logs service can be used to log instance-level data access, such as configuration files, etc. Finally, partner products from the AWS Marketplace can fulfil more specialised requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
