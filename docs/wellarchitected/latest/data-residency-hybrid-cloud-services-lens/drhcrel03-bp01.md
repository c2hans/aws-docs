---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel03-bp01.html
---

# DRHCREL03-BP01 Use AWS Outposts or Local Zones for scenarios where data must reside within a country or jurisdiction without a local AWS Region
<a name="drhcrel03-bp01"></a>

 To meet data residency requirements in Regions without local AWS infrastructure, leverage AWS Outposts across multiple locations or AWS Local Zones with redundancy, while utilizing services like Amazon S3 on Outposts for resilient local data management.

 **Desired outcome:** Achieve seamless integration of AWS Cloud capabilities into local operations while maintaining strict adherence to data residency requirements even in countries with no AWS Regions.

 **Benefits of establishing this best practice:** AWS Outposts and Local Zones enable organizations to use AWS services while keeping data within specific geographical boundaries, facilitating compliance with local data sovereignty laws and regulations.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-33"></a>

 When data must remain within the country and a local AWS Region isn't available, deploy on Outposts in different physical locations with redundant power and network sources or AWS Local Zones. Use services like Amazon S3 on Outposts for backup and recovery to achieve high availability while adhering to data residency regulations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
