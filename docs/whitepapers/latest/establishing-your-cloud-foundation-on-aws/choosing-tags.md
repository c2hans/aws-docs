---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Choosing tags for your environment
<a name="choosing-tags"></a>

Across the different kind of tags, you have to define for your environment, you need to decide what tags will be the **mandatory tags** or **discretionary tags**. Additionally, you need to define what resources need to tagged, and define detection and enforcement mechanisms to ensure all the required resources have the mandatory tags. When building an environment with multiple accounts, every account in the environment should have the mandatory tags that allow you to identify what the purpose of the account is for and who is responsible for the resources in that account.

**Note**
When building your tag strategy personally identifiable information (PII) should not be used to label your resources, as tags are not encrypted and are visible across your environment. Codify these values, so you can identify owners internally.

**Mandatory tags** are the set of tags that every resource should have, regardless of purpose. These tags will enable you to identify the necessary metadata to identify the resource.

The list of recommended **mandatory tags** includes:
+ **Owner**- This tag indicates who is the owner and main user of the resource, this can be a team or an individual.
**Note**
 The Owner is not always the user who created the resource.
+ **Business Unit** - This tag identifies the business unit the resource belongs to.
+ **SDLC Stage** - This tag indicates if the resources are being used for Production or for non-Production. (For example, development, test, or sandbox.)
+ **Cost Center** - This tag specifies the budget or account that will be used to pay for the spend associated with the tag.
+ **Financial Owner** - This tag identifies who is responsible for the costs associated with the resource tagged with a specific tag.

**Discretionary tags** are the set of tags that must be defined as part of your tagging strategy, so they are available to be assigned to resources that need them (for example, temporary elevation of permissions, or data sensitivity).

The list of recommended **discretionary tags** includes:
+ **Workload ID/Name** - This tag indicates if the resource belongs to a specific workload. The value can be the workload ID or name.
+ **Compliance Requirement** - This tag identifies the resources that are subject to a specific compliance framework (for example, PCI-DSS or HIPAA).
+ **Environment version** - This tag indicates the version of the environment, in case the same workload has more than one environment associated.
+ **Workload tier** - This tag indicates the type of workload the resources belong to. Some workload types examples are confidential, internal, or critical.
+ **Backup** - This tag indicates if the resource needs to be backed up based on the type of workload and the data that it manages.
+ **SLA level** - This tag indicates SLA requirements.
+ **Lifespan** - This tag indicates the lifetime of the resources of the workload. If exceeded, these resources should be reviewed, replaced, or isolated.
