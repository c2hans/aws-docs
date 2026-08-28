---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus01-bp01.html
---

# DRHCSUS01-BP01 Choose the Local Zone anchored to the Region that best aligns with your sustainability goals if more than one meets your data-residency requirements
<a name="drhcsus01-bp01"></a>

 It may be possible to evaluate and choose an AWS Local Zone that is anchored to a more sustainable AWS Region when there are several which meet your data residency requirements.

 **Desired outcome:** Services are deployed to the Local Zone anchored to the most sustainable parent AWS Region.

 **Benefits of establishing this best practice:** You can choose an AWS Local Zone that is anchored to a more sustainable AWS Region to support your sustainability objectives.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-52"></a>

 AWS Local Zones are always anchored to a parent AWS Region where control plane functions and the full set of AWS services are made available for building solutions. When considering a Local Zone for data residency use cases, there may be only one that meets your requirements. However, there may be times where more than one Local Zone can be used, each anchored to different parent Regions. When this is the case, select an [AWS Region based on sustainability](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/) and deploy to the Local Zone that is anchored to that Region. For more detail on Local Zone to Region relationships, see [AWS Local Zones locations](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/?nc=sn&loc=3).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
