---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/approach-1-personal-data-copy-in-aws-cloud.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Approach 1 – personal data copy in AWS Cloud
<a name="approach-1-personal-data-copy-in-aws-cloud"></a>

 This approach allows customers to transfer, store, and read personal data in the AWS cloud while keeping primary copy on-premises.

![Transfer, store, and read personal data in the AWS Cloud](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/personal-data-external-region-on-prem.png)

 Transfer, store, and read personal data in the AWS Cloud

 With this approach, the customer can build the solutions in a way that all personal data is *written* (created, updated, deleted) in the territory of the country, whereas customers may work with copies of the data in the AWS Cloud. Customers can address the implications of this type architecture by using components from the reference architectures described in this whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
