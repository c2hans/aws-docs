---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost02-bp03.html
---

# SCCOST02-BP03 Only store useful data and discard the rest
<a name="sccost02-bp03"></a>

 A well-designed supply chain data management architecture incorporates a data lake to store processed and normalized useful data, while raw data is either discarded or archived in cost-effective storage for potential future needs.

 **Desired outcome:** Data lifecycle is well defined as per business and regulatory requirements.

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-50"></a>

 Implement data sanitization to identify, clean, and validate critical information before cloud transfer, while pre-processing data to improve bandwidth efficiency, reduce storage costs, and support high-quality, secure cloud data.

 Use edge computing for local analytics and decision-making, prioritizing critical data for immediate cloud transmission.

### Implementation steps
<a name="implementation-steps-51"></a>

1.  Establish data classification and retention policies that define what data should be kept, archived, or discarded based on business and regulatory requirements.

1.  Implement automated data sanitization processes to clean and validate data before storage, removing unnecessary or redundant information.

1.  Deploy edge computing solutions for local data processing and filtering, transmitting only essential data to the cloud.

1.  Configure automated data lifecycle management to archive or delete data according to established retention policies.

1.  Implement data quality monitoring to make sure only valuable, accurate data is retained in storage systems.

1.  Regularly review and optimize data retention policies based on changing business needs and regulatory requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
