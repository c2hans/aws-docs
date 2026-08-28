---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html
---

# What are tags?
<a name="what-are-tags"></a>

A tag is a [*key-value pair*](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) applied to a resource to hold metadata about that resource. Each tag is a label consisting of a key and an optional value. Not all services and resource types currently support tags (see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html)). Other services may support tags via their own APIs. It should be noted that tags are not encrypted and should not be used to store sensitive data, such as personally identifiable information (PII).

Tags that a user creates and applies to AWS resources using the AWS CLI, API, or the AWS Management Console are known as *user-defined* tags. Several AWS services, such as AWS CloudFormation, Elastic Beanstalk, and Auto Scaling, automatically assign tags to resources that they create and manage. These keys are known as *AWS generated* tags and are typically prefixed with `aws`. This prefix cannot be used in user-defined tag keys.

 There are usage requirements and limits on the number of user-defined tags that can be added to an AWS resource. For more information, refer to [*Tag naming limits and requirements*](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-conventions) in the *AWS General Reference guide*. AWS generated tags do not count against these user-defined tag limits.

*Table 1 – Examples of user-defined tag keys and values *

|  Instance ID  |  Tag Key  |  Tag Value  |
| --- | --- | --- |
| i-01234567abcdef89a  | CostCenter  | 98765  |
|   | Stack  | Test  |
| i-12345678abcdef90b  | CostCenter  | 98765  |
|   | Stack  | Production  |

*Table 2 – Examples of AWS generated tags *

|  AWS Generated Tag Keys  |  Rationale  |
| --- | --- |
| aws:ec2spot:fleet-request-id | Identifies the Amazon EC2 Spot Instance request that launched the instance  |
| aws:cloudformation:stack-name | Identifies the AWS CloudFormation stack that created the resource  |
| lambda-console:blueprint | Identifies blueprint used as a template for an AWS Lambda function  |
| elasticbeanstalk:environment-name  | Identifies the application that created the resource  |
| aws:servicecatalog:provisionedProductArn | The provisioned product Amazon Resource Name (ARN)  |
| aws:servicecatalog:productArn | The ARN of the product from which the provisioned product was launched  |

 AWS generated tags form a namespace. For example, in a CloudFormation template, you define a set of resources to be deployed together in a `stack`, where `stack-name` is a descriptive name that you assign to identify it. If you examine a key such as `aws:cloudformation:stack-name`, you can see the namespace that is used to scope the parameter uses three elements: **aws** the *organization,* **cloudformation** the *service, and* **stack-name** the *parameter.*

 User-defined tags can also use namespaces and using an organizational identifier as a prefix is recommended. This helps you quickly identify whether a tag is something from your managed schema, or something defined by a service or tool that you are using in your environment.

 In the [Establishing Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html) whitepaper, we recommend a set of tags that should be implemented. It’s highly likely that different businesses will have different allowed patterns and different lists for a given tag. Looking at the example in Table 3:

*Table 3 – Same tag key, different value validation rules *

|   Organization   |  Tag Key  |  Tag Values Validation  |  Tag Value Example  |
| --- | --- | --- | --- |
|  Company A  | CostCenter  | 5432, 5422, 5499  | 5432  |
|  Company B  | CostCenter  | ABC\*  | ABC123  |

 If these two schemas are in separate organizations, then there is no issue with tag conflicts. However, should these two environments merge, then the namespaces can conflict and validation becomes more complex. This scenario might seem unlikely, but businesses are acquired or merged, and there are other scenarios, such as clients working with a managed service provider, game publisher, or venture capital business, where accounts from different organizations are part of a shared AWS Organization. By using the business name as a prefix to define a unique namespace, these challenges can be avoided, as shown in Table 4:

*Table 4 – Use of namespaces in tag keys *

|   Organization   |  Tag Key  |  Tag Values Validation  |  Tag Value Example  |
| --- | --- | --- | --- |
| Company A | company-a:CostCenter  | 5432, 5422, 5499  | 5432  |
| Company B | company-b:CostCenter  | ABC\*  | ABC123  |

 In large and complex organizations where businesses are acquired and divested regularly, this situation will occur more frequently. As the new acquisition’s processes and practices are harmonized across the wider group, the situation is resolved. Having distinct namespaces helps because the use of the older tags can be reported on and the relevant teams contacted to adopt the new schema. A namespace can also be used to indicate a scope or represent a use case or an area of responsibility that is aligned to organizational owners.

*Table 5 – Example of scope or use case scope within tag keys *

|  Use Case  |  Tag Key  |  Rationale  |  Allowed Values  |
| --- | --- | --- | --- |
| Data Classification  | example-inc:info-sec:data-classification | Information security defined set of data classification  | sensitive, company-confidential, customer-identifiable  |
| Operations  | example-inc:dev-ops:environment | Implement scheduling of test and development environments  | development, staging, quality-assurance, production  |
| Disaster Recovery  | example-inc:disaster-recovery:rpo | Define the recovery point objective (RPO) for a resource  | 6h, 24h  |
| Cost Allocation  | example-inc:cost-allocation:business-unit | Finance teams need cost reporting on each team's usage and spend  | corporate, recruitment, support, engineering  |

 Tags are simple and ﬂexible. Both the key and the value of the tag are variable-length strings and can support a wide character set. For more information on lengths and character sets, see [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *AWS General Reference*. Tags are case sensitive, meaning that `costCenter` and `costcenter` are different tag keys. In different countries, the spelling of a word might differ, which might affect your keys. For example, in the United States, one might define a key as `costcenter`, but in the United Kingdom, `costcentre` might be preferred. These are different keys from the resource-tagging perspective. Define spelling, case, and punctuation as part of your tagging strategy. Use these definitions as a reference for anyone creating or managing resources. This topic is discussed in more detail in the next section, [Building your tagging strategy](building-your-tagging-strategy.md).

**Note**
Although tag keys are case sensitive, IAM has additional validations for IAM resources to prevent the application of tag keys that only differ in casing. We recommend not using keys that only differ in casing. Refer to [Tags for IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules) for more details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
