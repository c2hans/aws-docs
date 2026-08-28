---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/no-unrestricted-route-to-igw.html
---

# no-unrestricted-route-to-igw
<a name="no-unrestricted-route-to-igw"></a>

Checks if there are public routes in the route table to an Internet gateway (IGW). The rule is NON\_COMPLIANT if a route to an IGW has a destination CIDR block of '0.0.0.0/0' or '::/0' or if a destination CIDR block does not match the rule parameter.

**Identifier:** NO\_UNRESTRICTED\_ROUTE\_TO\_IGW

**Resource Types:** AWS::EC2::RouteTable

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

routeTableIds (Optional)Type: CSV
Comma-separated list of route table IDs that can have routes to an Internet Gateway with a destination CIDR block of '0.0.0.0/0' or '::/0'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1185c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
