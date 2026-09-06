---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/migration-methodology.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration methodology
<a name="migration-methodology"></a>

When you begin the migration of your semiconductor design workflows to AWS, you will find there are many parallels with managing traditional deployments across multiple sites within your corporate network, whether these sites are distributed engineering locations, or represent an entire data center. Larger organizations in the semiconductor industry typically have multiple data centers that are geographically dispersed because of the distributed nature of their design teams. These organizations typically choose specific workloads to run in specific locations, or replicate and synchronize data to allow for multiple sites to take the load of large-scale, global workflows.

 Geographically distributed teams may not lend itself to a simple, and straight-forward approach for migrating workflows to AWS. We encourage our customers to look at specific parts of their design flow or even a new project, when considering which workloads to migrate to AWS. Choosing the right tool or workflow will often require, for example, determining what data replication, caching, and license server management will be needed to run the flow on AWS.

 Most of the same approaches and design decisions related to multiple data centers also apply to the cloud. With AWS, you can build one or more virtual data centers that mirror your existing on-premises electronic design automation (EDA) design environment and data center infrastructure. The foundational technologies that enable compute resources, storage servers, and user workstations are available with just a few keystrokes. This ability to rapidly create new semiconductor design and verification environments in just minutes is a major benefit of deploying on cloud. However, the real power of using the AWS Cloud for semiconductor design comes from the dynamic capabilities and enormous scale provided by AWS, resulting in faster time-to-results, reduced schedule risk, and more efficient utilization of valuable EDA software licenses.
