---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/graviton-instances.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Graviton instances
<a name="graviton-instances"></a>

 There are many performance benefits of [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/). AWS Graviton processors are custom built by AWS using 64-bit Arm Neoverse cores. Since the first A1 Graviton instance launched in 2019, AWS has launched three additional generations including the latest: Graviton4. Each generation has brought improvements in performance and efficiency, offering better price performance over comparable current generation x86-based instances for a wide variety of workloads, including application servers, microservices, high performance computing, electronic design automation, gaming, open-source databases, and in-memory caches. The latest Graviton instances support DDR5 memory providing 50% more memory bandwidth compared to DDR4.

One of the Amazon EC2 instances powered by AWS Graviton is the Hpc7g, which offers up to 20% higher performance compared to Hpc6a. The Hpc7g offers high-memory bandwidth and 200 Gbps of Elastic Fabric Adapter (EFA) network bandwidth, and can be used with AWS ParallelCluster. If higher network bandwidth is required for more loosely coupled applications, consider the C7gn instances which offer up to 200 Gbps of network bandwidth.

 AWS Graviton has no simultaneous multithreading (SMT) or hyper threading. There is no sharing of execution units or interference between threads and sharing of L1 or L2 caches, as every vCPU is a physical core. Therefore, on AWS Graviton, well-optimized HPC applications that may have competed for resources on other instances, can push the CPUs to a higher threshold and limit extending execution time when gaps in execution stream cannot be filled.

 Interpreted and bytecode-compiled languages such as Python, Java, Node.js and .NET Core on Linux may run on AWS Graviton without modification. Support for Arm architectures is also increasingly common in third-party numerical libraries, aiding the path to adoption. For certain bytecode-compiled language, extensions modules written in lower-level languages like C or C\+\+ need to be compiled to arm64. Code changes will also be required for lower-level languages if they use to hardware specific features like single instruction, multiple data (SIMD) instructions.

 Recommended flags to compile applications for AWS Graviton based instances can be found in the [AWS Graviton Technical Guide on Github](https://github.com/aws/aws-graviton-getting-started). Additionally, AWS offers the [Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton), a command line tool that analyzes source code and generates a report with any discovered incompatibilities with Graviton CPUs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
