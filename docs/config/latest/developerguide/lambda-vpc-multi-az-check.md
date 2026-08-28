---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/lambda-vpc-multi-az-check.html
---

# lambda-vpc-multi-az-check
<a name="lambda-vpc-multi-az-check"></a>

Checks if Lambda has more than 1 availability zone associated. The rule is NON\_COMPLIANT if only 1 availability zone is associated with the Lambda or the number of availability zones associated is less than number specified in the optional parameter.

**Identifier:** LAMBDA\_VPC\_MULTI\_AZ\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), China (Ningxia) Region

**Parameters:**

availabilityZones (Optional)Type: int
Number of expected Availability zones.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1077c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
