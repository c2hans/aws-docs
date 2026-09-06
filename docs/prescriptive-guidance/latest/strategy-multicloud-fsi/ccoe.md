---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/ccoe.html
---

# Establish a multicloud-enabled CCoE
<a name="ccoe"></a>

If you have decided to adopt a multicloud strategy, we recommend that you centralize your cloud leadership efforts through a transformation office or a [Cloud Center of Excellence (CCoE)](https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/building-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise.html). A CCoE develops and evangelizes an approach for implementing cloud technology at scale across an organization. For successful cloud adoption, design your CCoE to include representatives who can speak for the teams and departments involved. Start small and incrementally grow the CCoE to meet your needs as you progress through your cloud transformation. Your cloud provider representatives, such as your AWS account manager and solutions architect, can provide resources to guide you through the creation of your CCoE.

A CCoE speeds up your ability to establish subject matter expertise, achieve agreement, earn trust across your organization, and establish effective guidelines for meeting your mission requirements. There is no single organizational structure that works for every FI, but the following guidance will help you design your own CCoE. For more information, see [Building your Cloud Operating Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/) on the AWS Prescriptive Guidance website.

**We recommend that you build a single CCoE and then specialize within it for each cloud provider.** Teams have favorite products, suppliers, software, architectural patterns, programming languages, and CSPs. Aligning your organization around these preferences can accelerate cloud adoption. When you add more providers, maintain a single CCoE that includes specialized teams. Creating separate CcoEs for each provider leads to competing engineering priorities and fragmented approaches across your IT organization.

## What does a multicloud-enabled CCoE look like?
<a name="ccoe-definition"></a>

When a CCoE is fully operational, it reflects your business and represents a microcosm of your current IT and business functions. You might have dedicated architecture teams for each CSP or create shared teams that support multiple CSPs. The shape of your CCoE must be appropriate for your business model. The following diagram provides an example of organizational structure that's derived from the best experiences of AWS FSI multicloud customers.

![Multicloud-enabled CCoE for FSIs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/images/guide-img/79fe34d7-841b-4bd6-a6da-96f5401c6a67/images/d02accfa-7066-43ba-81cb-fa19793dfcda.png)

## Best practices for multicloud CCoEs
<a name="ccoe-best-practices"></a>
+ **Ensure critical capabilities in cross-cutting functions.** This includes security, governance, compliance, cloud financial management, and risk management. Your critical capabilities must not be unique to any one cloud provider, but driven from your business needs, which might exceed the capabilities of a single CSP.
+ **Rotate staff between providers periodically.** Your engineering team will typically have uneven expertise across your CSPs. Rotating your staff between platforms to provide them with experience and exposure to new design patterns is an excellent way to speed up innovation. Ideally, rotate no more than 50% of your staff, and then rotate them back after some time, so they can share their learnings with the broader team.
+ **Prioritize and reward certification programs.** Each CSP has its own certification program to improve and validate skills. Make sure that your staff has gained certifications across your CSPs and across multiple specialties. Create an incentive program for team members who earn multiple specialty certifications from multiple CSPs.
+ **Embed security into your CCoE's inputs and outputs.** Your CCoE can create technical guardrails against future security threats because it authors your internal blueprints and provides guidance that shapes future projects. Create output goals for your CCoE, such as security escalations seen over time, and then measure changes to your workload security metrics from projects that use your CCoE's guidance. Compare security metrics between similar workloads across different CSPs.
+ **Reward collaboration through cross-team metrics. **One approach to encourage solid engineering practices is to measure your operations teams on the number of code defects found in production, and measure your developers on workload uptime. Apply the same approach to workloads in different CSPs: Ask your AWS teams to track performance metrics for workloads in another cloud, and vice versa. This cross-accountability encourages your teams to share successful strategies.
