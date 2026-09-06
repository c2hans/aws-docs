---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/InspectorPricing.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic pricing
<a name="InspectorPricing"></a>

Amazon Inspector Classic pricing is based on the number of EC2 instances included in each assessment and the rules packages used in those assessments.

## Pricing for the network reachability rules package
<a name="InspectorPricing-network-reachability-rules-package"></a>

Amazon Inspector Classic assessments with the network reachability rules packages are priced per instance per assessment (instance-assessment) per month. For example, if you run 1 assessment against 1 instance, that is 1 instance-assessment. If you run 1 assessment against 10 instances, that is 10 instance-assessments. The pricing starts at $0.15 per instance-assessment per month with volume discounting to achieve as low as $0.04 per instance-assessment per month.

### Free trial details
<a name="InspectorPricing-network-reachability-rules-package-free-trial"></a>

| **First 90-days using Amazon Inspector Classic** | **Per instance-assessment price** |
| --- |--- |
| First 250 instance-assessments | $0.00 |

### Pricing details
<a name="InspectorPricing-network-reachability-rules-package-pricing-details"></a>

| **In a given month** | **Per instance-assessment price** |
| --- |--- |
| First 250 instance-assessments | $0.15 |
| Next 750 instance-assessments | $0.13 |
| Next 4,000 instance-assessments | $0.10 |
| Next 45,000 instance-assessments | $0.07 |
| All other instance-assessments | $0.04 |

## Pricing for host assessment rules packages
<a name="InspectorPricing-host-assessment-rules-package"></a>

**For any combination of Common Vulnerabilities and Exposures (CVE), Center for Internet Security (CIS) benchmarks, Security Best Practices, and Runtime Behavior Analysis included in assessments**

Amazon Inspector Classic's host assessment rules packages use an agent deployed on the Amazon EC2 Instances running the applications you want to assess. Assessments with the host rules packages are priced per agent per assessment (agent-assessment) per month. For example, if you run 1 assessment against 1 agent, that is 1 agent-assessment. If you run 1 assessment against 10 agents, that is 10 agent-assessments. The pricing starts at $0.30 per agent-assessment per month with volume discounting to achieve as low as $0.05 per agent-assessment per month.

### Free trial details
<a name="InspectorPricing-host-assessment-rules-package-free-trial"></a>

| **First 90-days using Amazon Inspector Classic** | **Per agent-assessment price** |
| --- |--- |
| First 250 agent-assessments | $0.00 |

### Pricing details
<a name="InspectorPricing-host-assessment-rules-package-pricing-details"></a>

| **In a given month** | **Per agent-assessment price** |
| --- |--- |
| First 250 agent-assessments | $0.30 |
| Next 750 agent-assessments | $0.25 |
| Next 4,000 agent-assessments | $0.15 |
| Next 45,000 agent-assessments | $0.10 |
| All other agent-assessments | $0.05 |
