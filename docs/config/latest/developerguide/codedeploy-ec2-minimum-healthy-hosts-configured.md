---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/codedeploy-ec2-minimum-healthy-hosts-configured.html
---

# codedeploy-ec2-minimum-healthy-hosts-configured
<a name="codedeploy-ec2-minimum-healthy-hosts-configured"></a>

Checks if the deployment group for EC2/On-Premises Compute Platform is configured with a minimum healthy hosts fleet percentage or host count greater than or equal to the input threshold. The rule is NON\_COMPLIANT if either is below the threshold.

**Identifier:** CODEDEPLOY\_EC2\_MINIMUM\_HEALTHY\_HOSTS\_CONFIGURED

**Resource Types:** AWS::CodeDeploy::DeploymentGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

minimumHealthyHostsFleetPercent (Optional)Type: intDefault: 66
Minimum percentage of healthy hosts fleet during deployment. Default value is set to 66 percent.

minimumHealthyHostsHostCount (Optional)Type: intDefault: 1
Minimum number of healthy hosts in fleet during deployment. Default value is set to 1.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d397c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
