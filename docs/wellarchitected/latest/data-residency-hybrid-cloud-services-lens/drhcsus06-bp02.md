---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus06-bp02.html
---

# DRHCSUS06-BP02 Track AWS Outposts roadmaps, and structure contracts to enable timely upgrades to the latest EC2 instances
<a name="drhcsus06-bp02"></a>

 When new more powerful and efficient AWS Outposts offerings are on the near-term roadmap you should consider refreshing at the end of your current AWS Outposts term, or consider using a shorter term with the existing generation if current needs must be met before the next generation is available.

 **Desired outcome:** You have option to refresh your Outposts deployment with the latest, most efficient, and performant hardware.

 **Benefits of establishing this best practice:** You will be able to leverage the latest, most efficient and powerful AWS Outposts offerings as early as possible for your data-residency workloads.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-63"></a>

 Unlike with AWS Local Zones, AWS Outposts EC2 families and instances remain fixed over the life of a deployment contract term (typically one, three, or five years). This can present a challenge for customers wishing to adopt the newest Amazon EC2 instances.

 When there is a need or desire to take advantage of the latest AWS Outposts and EC2 instance offerings, consult with your AWS account team and Outposts hybrid specialists to review roadmaps and timelines. Consider using shorter contract terms to pursue AWS Outposts upgrades and meet future data residency compute requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
