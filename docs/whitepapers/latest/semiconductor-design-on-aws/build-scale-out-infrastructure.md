---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/build-scale-out-infrastructure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Build scale-out infrastructure
<a name="build-scale-out-infrastructure"></a>

 At this point in the process, engineers should have the prerequisites to start launching jobs and analyzing results. The AWS infrastructure that will be launched is a scalable, elastic environment that is capable of running full SOC design workflows.

The next step is to deploy a resource management and orchestration service that enables engineers to submit workloads into a scalable, elastic environment capable of running full SOC design workflows. The top commercial schedulers and workload management systems commonly found in silicon design environments provide options for AWS integration. This allows these tools to dynamically scale the EC2 computing resources based on demand in the queues. If your current scheduler does not support AWS integration or you are looking for a turnkey solution, AWS recommends using the official AWS Solution, [Scale-Out Computing on AWS](https://aws.amazon.com/solutions/implementations/scale-out-computing-on-aws/), to automate the process of building your environment. The solution deploys a web-based user interface (UI) and automation tools that enable you to create your own job queues, auto-scaling compute resources, shared file systems, remote desktop sessions, and other components you need to run silicon design workloads at scale in AWS. As part of launching the solution, customizations should be made to include the previously-installed tools and POC data, as these will be needed to launch jobs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
