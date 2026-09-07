---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution includes one main AWS CloudFormation template and two nested templates. You can download the CloudFormation templates before deploying the solution.

## Main stack
<a name="main-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/view-template.png)](https://s3.amazonaws.com/solutions-reference/security-automations-for-aws-waf/latest/aws-waf-security-automations.template) **aws-waf-security-automations.template** - Use this template as the entry point to launch the solution in your account. The default configuration deploys an AWS WAF web ACL with preconfigured rules. You can customize the template based on your needs.

## WebACL stack
<a name="webacl-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/view-template.png)](https://s3.amazonaws.com/solutions-reference/security-automations-for-aws-waf/latest/aws-waf-security-automations-webacl.template) **aws-waf-security-automations-webacl.template** - This nested template provisions AWS WAF resources including a web ACL, IP, sets and other associated resources.

## Firehose Athena stack
<a name="firehose-athena-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/view-template.png)](https://s3.amazonaws.com/solutions-reference/security-automations-for-aws-waf/latest/aws-waf-security-automations-firehose-athena.template) **aws-waf-security-automations-firehose-athena.template** - This nested template provisions resources related to [AWS Glue](https://aws.amazon.com/glue/), Athena, and Firehose. It’s created when you choose either the **Scanner & Probe** Athena log parser or the **HTTP Flood** Lambda or Athena log parser.

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

This AWS CloudFormation template deploys the Security Automations for AWS WAF solution in the AWS Cloud.
