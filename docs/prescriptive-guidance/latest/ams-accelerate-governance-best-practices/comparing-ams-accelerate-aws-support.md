---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ams-accelerate-governance-best-practices/comparing-ams-accelerate-aws-support.html
---

# Comparing AMS Accelerate and AWS Support
<a name="comparing-ams-accelerate-aws-support"></a>

## Comparing AMS Accelerate and AWS Support
<a name="key-differences"></a>

### Key differences in AMS Accelerate and AWS Support governance responsibilities
<a name="key-differences-in-ams-accelerate-and-aws-support-governance-responsibilities.005d3ef6-e764-523f-9ef6-994a29c53fac"></a>

The AWS Support and AMS Accelerate support models mainly differ in the following governance areas:
+ Network traffic protection (encryption, integrity, and identity)
+ Customer-side data encryption and data integrity authentication
+ Server-side encryption (file system and data)

In the AMS Accelerate support model, AWS is responsible for these governance areas. In the AWS Support model, you are responsible for them.

For more information about the different types of support models offered by AWS Support, see [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/) in the AWS Support documentation.

### AWS Support and AMS Accelerate responsibility matrix
<a name="aws-support-and-ams-accelerate-responsibility-matrix.3e841a78-2d57-5df4-a80f-eefd55d757cb"></a>

The following table shows the high-level governance responsibilities of you, as the customer, and AWS in both the AWS Support and AMS Accelerate support models.

|
|
| Governance area |  AWS Support: Who's responsible (AWS or you)  | AMS Accelerate: Who's responsible (AWS or you) |
| --- |--- |--- |
| AWS Regions | AWS | AWS |
| AWS Availability Zones | AWS | AWS |
| AWS Edge locations | AWS | AWS |
| AWS Global Cloud Infrastructure | AWS | AWS |
| AWS compute | AWS | AWS |
| AWS storage | AWS | AWS |
| AWS database | AWS | AWS |
| AWS networking | AWS | AWS |
| Network traffic protection (encryption, integrity, identity) | You | AWS |
| Customer-side data encryption and data integrity authentication | You | AWS |
| Server-side encryption (file system and data) | You | AWS |
| Operating system, network, and firewall configuration | You | You |
| Platform and application identity and access management | You | You |
| Customer data | You | You |

**Note**
Each operational process has its own, responsible, accountable, consulted, and informed (RACI) matrix. For more information, see [Roles and responsibilities](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#acc-sd-responsibilities) in the *AMS Accelerate User Guide*.

## Support model options
<a name="support-model-options"></a>

The following diagram shows the different support models that you can apply to each AWS account.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/ams-accelerate-governance-best-practices/images/guide-img/6036bebd-169c-4167-8ede-cf3d4823dab9/images/4d0be365-0238-45d2-98c4-d6973a01de88.png)

**Note**
An [AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/planning-your-deployment.html) that includes multiple AWS accounts can have more than one support model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
