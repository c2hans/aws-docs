---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-your-aws-landing-zone-design.html
---

# Document your AWS landing zone design
<a name="document-your-aws-landing-zone-design"></a>

*Michael Daehnert, Florian Langer, and Michael Lodemann, Amazon Web Services*

## Summary
<a name="document-your-aws-landing-zone-design-summary"></a>

A *landing zone* is a well-architected, multi-account environment that's based on security and compliance best practices. It is the enterprise-wide container that holds all of your organizational units (OUs), AWS accounts, users, and other resources. A landing zone can scale to fit the needs of an enterprise of any size. AWS has two options for creating your landing zone: a service-based landing zone using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) or a customized landing zone that you build. Each option requires a different level of AWS knowledge.

AWS created AWS Control Tower to help you save time by automating the setup of a landing zone. AWS Control Tower is managed by AWS and uses best practices and guidelines to help you create your foundational environment. AWS Control Tower uses integrated services, such as [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) and [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), to provision accounts in your landing zone and manage access to those accounts.

AWS landing zone projects vary in requirements, implementation details, and operational action items. There are customization aspects that need to be handled with every landing zone implementation. This includes (but is not limited to) how access management is handled, which technology stack is used, and what the monitoring requirements are for operational excellence. This pattern provides a template that helps you document your landing zone project. By using the template, you can document your project more quickly and help your development and operations teams understand your landing zone.

## Prerequisites and limitations
<a name="document-your-aws-landing-zone-design-prereqs"></a>

**Limitations**

This pattern does not describe what a landing zone is or how to implement one. For more information about these topics, see the [Related resources](#document-your-aws-landing-zone-design-resources) section.

## Epics
<a name="document-your-aws-landing-zone-design-epics"></a>

### Create the design document
<a name="create-the-design-document"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify key stakeholders. | Identify key service and team managers that are linked to your landing zone. | Project manager |
| Customize the template. | Download the template in the [Attachments](#attachments-9e39a05a-8f51-4fe3-8999-522feafed6ca) section, and then update the template as follows:1. Remove any sections that don't apply to your organization's landing zone or processes.<br />2. Add any sections that are unique to your organization. | Project manager |
| Complete the template. | In meetings with the stakeholders or by using a write-and-review process, complete the template as follows:1. Use the guidance and information in the blue boxes to complete each section.<br />2. Replace or remove any yellow fields with custom values for your organization.<br />3. Replace or remove any image fields with your custom architecture or flow diagrams.<br />4. Complete the *Revision history* and *Contributors *section of the template. | Project manager |
| Share the design document. | When your landing zone design documentation is complete, save it in a shared repository or central location where all stakeholders can access it. We recommend that you use standard document control processes to record and approve revisions to the design document. | Project manager |

## Related resources
<a name="document-your-aws-landing-zone-design-resources"></a>
+ [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
  + [Plan your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/planning-your-deployment.html)
  + [AWS multi-account strategy for your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html)
  + [Administrative tips for landing zone setup](https://docs.aws.amazon.com/controltower/latest/userguide/tips-for-admin-setup.html)
  + [Expectations for landing zone configuration](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-configure.html)
+ [Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) (AWS Solutions Library)
+ [Setting up a secure and scalable multi-account AWS environment](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/welcome.html) (AWS Prescriptive Guidance)

## Attachments
<a name="attachments-9e39a05a-8f51-4fe3-8999-522feafed6ca"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/9e39a05a-8f51-4fe3-8999-522feafed6ca/attachments/attachment.zip)
