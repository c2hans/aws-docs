---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/tagging-standards.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tagging standards
<a name="tagging-standards"></a>

As you define your tagging strategy, a naming convention needs to be established for the different tags across your environment ensuring a standard, and making it easier for the tagged resources to be identified. Tags enable you to identify resources, and having no more than 50 tags per resource will allow you to keep your tag strategy manageable in your environment. The following are examples for tag key names and values:

```
example-key:owner = SecOps
```

```
example-key:cost-center = 5432
```

```
example-key:financial-owner = Security
```

## Resources that need to be tagged
<a name="tagged-resources"></a>

There are resources that always need to be tagged in your environment, because it is critical to have the identifiable information about the resources at all times. The resources in this category are meant to be persistent, and in some occasions, they act as resource containers for other resources. These resources include, but are not limited to, accounts, critical workloads, and shared infrastructure. For these resources, you should aim to tag a hundred percent of the resources which will allow you to identify the spend, access, ownership, and permissions for the tagged resources.

However, as operational complexity increases, and the level of automation to manage tags becomes more demanding, you may choose to not tag certain types of resources that are ephemeral. These resources should run within a resource container that is properly tagged to allow you to identify and trace what happened within that environment, but enforcing the tags on these types of resources may not be necessary if they do not belong to critical workloads or applications.

## Enforcing tagging
<a name="enforcing-tagging"></a>

Because of the importance of tagging and the level of complexity, it’s recommended to automate the tagging process when possible. This will reduce the human error that can be introduced when tagging critical resources, and will minimize the number of resources that are not identifiable due to the lack of tags. When possible, creating tag policies in your organization can help you ensure that the tags assigned to resources have the correct value assigned.

Additionally, automation needs to be established in the environment to discover resources with missing tags or resources that are not compliant with the established tagging strategy. Once the resources have been identified, a report including these resources on the environment needs to be sent to the relevant stakeholders, to evaluate and make a decision to remediate the situation, if needed.

Based on the results of this report, if a situation where persistent resources that are identified as non-compliant or have missing tags is given, it should be remediated immediately, by assigning a default pre-defined tag value defined as part of your tagging strategy, or if pre-defined tag doesn’t exist deleting the non-compliant resources.

As part of your tagging strategy, it is important to implement preventative controls that ensure that disallow resource to be created without the appropriated tags on critical resources. For more information, refer to [Establish preventive controls across your environment](establish-preventive-controls-across-your-environment.md).

## Build a tagging dictionary
<a name="tagging-dictionary"></a>

As part of your tagging dictionary, you should define certain tags that can be used to access specific environments resources based on the tags attached to a role at a certain time. These tags can be used for a temporary escalation of privileges or for deploying changes through infrastructure as code that other identities may not have access otherwise.

We recommend that you define and build a tagging dictionary where all these values are available for developers, cloud architects, and environment operators. In order to add, update, or remove values for each of the tags included in the tagging dictionary, you need to establishes processes where all the relevant stakeholders can provide their inputs, when a tag becomes standard. This will ensure that all relevant stakeholders involved in the definition of the tags in your environment are aware of any changes they need to provision and deploy across their resources.

This tagging dictionary needs to be made available to builders and stakeholders, so tags can be applied consistently across the environment, and everyone is aware of requirements or errors that can be caused due to an incorrect used of tags in the environment. Including missing tags and wrong or misspelled tag keys in your resources.

## Defining tags for Attribute-based access control
<a name="define-tags"></a>

As part of your tagging dictionary, you should define certain tags that can be used to access specific environments resources based on the tags attached to a role at a certain time. These tags can be used for a temporary escalation of privileges or for deploying changes through infrastructure as code that other identities may not have access otherwise.
