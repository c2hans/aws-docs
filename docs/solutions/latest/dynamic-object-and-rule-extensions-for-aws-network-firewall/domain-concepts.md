---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/domain-concepts.html
---

# Domain concepts
<a name="domain-concepts"></a>

## Roles
<a name="roles"></a>

 Roles represents the operator’s logical identity that is going to interact with this solution. Currently, this solution supports a single IAM role. This role represents a Security Operations (SecOps) user, or a user that would typically configure the ANFW instance.

## Rule bundle
<a name="rule-bundle"></a>

 A rule bundle in the solution is an abstraction representing the underlying resource which aggregates the firewall rules. It represents an ANFW rule group associated with an individual role or team using the solution, and a collection of rules to be applied to the firewall.

## Rule
<a name="rule"></a>

 A rule defines what kind of traffic is allowed or blocked, in respect to the objects it references. For instance, a rule could be defined to allow traffic from a static IP (an object) to a cloud resource (another object). A rule is an object abstraction which results in a Suricata rule being automatically applied to the ANFW rule group once the objects are resolved.

## Object
<a name="object"></a>

 An object is an abstraction of the resource which rules can reference. It can be a static resource, such as a fixed IP/CIDR, or dynamic cloud resource, such as an AWS ARN or tag. The solution currently supports the following types of objects:

|  **Objects**  |  **Description**  |
| --- | --- |
|  Amazon EC2 ARN  |  Resolves to the IP of the EC2 instance  |
|  Auto Scaling group ARN  |  Resolves to the IP of the EC2 instance in the ASG  |
|  Amazon Virtual Private Cloud ARN  |  Resolves to the CIDR of the VPC  |
|  Amazon Virtual Private Cloud Subnet ARN  |  Resolves to the CIDR of the subnet  |
|  Tags  |  Resolves to the EC2 instances and AWS Lambda functions which contain matching tag values  |
|  Amazon EC2 security group ARN  |  Resolves to the IP of EC2 instances to which this security group is attached  |

## Audit
<a name="audit"></a>

 An audit is a record for all mutation actions: create, update, delete (CRUD) upon rule bundle, rule, and object. It records the requestor, its action, requested content, and the result of the actions.

 For more information, refer to [API schema](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/) in the GitHub repository for supported object types.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
