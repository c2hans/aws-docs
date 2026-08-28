---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/why-cfd-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Why CFD on AWS?
<a name="why-cfd-on-aws"></a>

 AWS is a great place to run CFD cases. CFD workloads are typically tightly coupled workloads using a Message Passing Interface (MPI) implementation and relying on a large number of cores across many nodes. Many of the AWS instance types, such as the compute family instance types, are designed to include support for this type of workload. AWS has network options that support extreme scalability and short turn-around time as necessary.

 CFD workloads typically scale well on the cloud. Most codes rely on domain decomposition to distribute portions of the calculation to the compute nodes. A case can be run highly parallel to receive results in minutes. Additionally, large numbers of cases can run simultaneously as efficiently and cheaply as possible to allow the timely completion of all cases.

 The cloud offers a quick way to deploy and turn around CFD workloads at any scale without the need to own your own infrastructure. You can run jobs that once were in the realm of national labs or large industry. In just an hour or two, you can deploy CFD software, upload input files, launch compute nodes, and complete jobs on a large number of cores. When your job completes, results can be visualized and downloaded, and then all resources can be ended – so you only pay for what you use. If preferred, your results can be securely archived on AWS using a storage service, such as [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3). Due to cloud scalability, you have the option to run multiple cases simultaneously with a dedicated cluster for each case.

 The cloud accommodates the variable demand of CFD. Often, there is a need to run a large number of cases as quickly as possible. Situations can require a sudden burst of tens, hundreds, or thousands of calculations immediately, and then perhaps no runs until the next cycle. The need to run a large number of cases could be for a preliminary design review, or perhaps a sweep of cases for the creation of a solution database. On the cloud, the cost is the same to run many jobs simultaneously, in parallel, as it is to run them serially, so you can get your data more quickly and at no extra cost. The cost savings in engineering time is an often-forgotten part of cost analysis. Running in parallel can be an ideal solution for design optimization.

 Cloud computing is a strong choice for other CFD steps. You can easily change the underlying hardware configuration to handle the geometry, meshing, and post-processing. With remote visualization software available to handle the display, you can manage the GPU instance running your post-processing visualization from any screen (laptop, desktop, web browser) as though you were working on a large workstation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
