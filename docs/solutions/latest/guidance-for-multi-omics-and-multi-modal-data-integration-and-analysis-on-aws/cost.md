---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this reference deployment. As of the date of publication, the cost for running this guidance with default settings in the US East (N. Virginia) Region is approximately **$61.00 per month**.

<table>
<thead>
  <tr><th> AWS service </th><th> Details </th><th> Cost per month [$ USD]</th></tr>
</thead>
<tbody>
  <tr><td> AWS Glue </td><td> $2.80 during setup to run the Glue jobs and crawlers </td><td> One-time cost ($2.80)</td></tr>
  <tr><td> AWS Glue </td><td> AWS Glue job runs per job: <br /> 10 DPUs * 3/60 hour at $0.44 per DPU-Hour or $0.22 per job <br /> AWS Glue crawler runs per crawler: <br /> 1 DPUs * 1/6 hour at $0.44 per DPU-Hour or $0.0748 per crawler <br /> Athena query runs: <br /> Less than 0.0005 TB scanned * 0.0005 * $5/TB = $0.0025 </td><td> One-time cost ($0.22 per job, $0.0748 per crawler, $0.0025 per TB)</td></tr>
  <tr><td> AWS KMS </td><td> One key to encrypt the Glue data catalog </td><td> $1.00 </td></tr>
  <tr><td> Amazon SageMaker AI </td><td> Notebook Instance </td><td> $36.00 ($0.05 per hour) </td></tr>
  <tr><td> Amazon S3 </td><td> Data lake data storage </td><td> $0.06 </td></tr>
  <tr><td> Amazon Athena </td><td> $0.00025 for each Athena query run for interpreting the data </td><td> Variable ( $0.00025 per query)</td></tr>
  <tr><td> Quick </td><td> Standard pricing per author </td><td> $24.00* </td></tr>
  <tr><td>Amazon Omics</td><td>One VCF is within Free Tier pricing</td><td>$0.00</td></tr>
  <tr><td colspan="2"> <b>Total: </b></td><td> <b>$61.00</b> </td></tr>
</tbody>
</table>

 \* Quick offers a free 30-day trial, after which the standard pricing per analysis author is $24 per month.

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html)  through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

 If you customize the guidance to analyze your genomics dataset, the cost factors include the storage size of the data being analyzed, the number of Extract Transform and Load (ETL) jobs and crawlers being used, compute resources required for each job, number of notebook instances provisioned and volume of data scanned when using Athena. For a more accurate estimate of cost, we recommend working with a sample dataset of your choosing as a benchmark.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
