---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/cost-optimization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost optimization
<a name="cost-optimization"></a>

 The intention of this guide is to focus on the enablement and building of your workflows on AWS. However, pricing is an important component when deciding to move production from on-premises to AWS. In a like-for-like comparison, we encourage you to first analyze the results of on-premises jobs as compared to the jobs run on AWS. That is, when using nearly the same resources, did the job runs on AWS meet or exceed your expectations of the job runs performed on-premises? The next steps are to perform workload and cost optimization on your entire workflow. These steps can mean choosing different instance types, storage options, serverless architectures, and of course leveraging the breadth of services that AWS has to offer.

## Amazon EC2 Spot Instances
<a name="amazon-ec2-spot-instances"></a>

 [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot) let you take advantage of unused EC2 capacity in the AWS Cloud. Spot Instances are available at up to a 90% discount compared to On-Demand prices. You can use Spot Instances for various stateless, fault-tolerant, or flexible applications such as big data, containerized workloads, CI/CD, web servers, high-performance computing (HPC), and test & development workloads.

 In the semiconductor industry, you can also use EC2 Spot instances to reduce cost. One specific usage is for library characterization. As the workloads run on EC2 Spot instances need to be fault-tolerant, if a library characterization job were to be interrupted, the job can be immediately restarted, and the time lost is minimal. The cost savings when using EC2 Spot instances far outweighs the time lost due to interruptions. For information, see the **Savings over On-Demand** and the **Frequency of Interruption columns in the** [Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
