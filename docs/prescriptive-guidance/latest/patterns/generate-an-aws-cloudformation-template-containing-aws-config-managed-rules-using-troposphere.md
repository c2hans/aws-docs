---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-an-aws-cloudformation-template-containing-aws-config-managed-rules-using-troposphere.html
---

# Generate an AWS CloudFormation template containing AWS Config managed rules using Troposphere
<a name="generate-an-aws-cloudformation-template-containing-aws-config-managed-rules-using-troposphere"></a>

*Lucas Nation and Freddie Wilson, Amazon Web Services*

## Summary
<a name="generate-an-aws-cloudformation-template-containing-aws-config-managed-rules-using-troposphere-summary"></a>

Many organizations use [AWS Config managed](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) rules to evaluate the compliance of their Amazon Web Services (AWS) resources against common best practices. However, these rules can be time consuming to maintain and this pattern helps you leverage [Troposphere](https://troposphere.readthedocs.io/en/latest/quick_start.html), a Python library, to generate and manage AWS Config managed rules.

The pattern helps you to manage your AWS Config managed rules by using a Python script to convert a Microsoft Excel spreadsheet containing AWS managed rules into an AWS CloudFormation template. Troposphere acts as the infrastructure as code (IaC) and this means that you can update the Excel spreadsheet with managed rules, instead of using a JSON or YAML-formatted file. You then use the template to launch an AWS CloudFormation stack that creates and updates the managed rules in your AWS account.

The AWS CloudFormation template defines each AWS Config managed rule by using the Excel spreadsheet and helps you to avoid manually creating individual rules in the AWS Management Console. The script defaults each managed rule's parameters to an empty dictionary and the scope's `ComplianceResourceTypes` defaults from `THE_RULE_IDENTIFIER.template file`*. *For more information about the rule identifier, see [Creating AWS Config managed rules with AWS CloudFormation templates](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-managed-rules-cloudformation-templates.html) in the AWS Config documentation.

## Prerequisites and limitations
<a name="generate-an-aws-cloudformation-template-containing-aws-config-managed-rules-using-troposphere-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Familiarity with using AWS CloudFormation templates to create AWS Config managed rules. For more information about this, see [Creating AWS Config managed rules with AWS CloudFormation templates](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-managed-rules-cloudformation-templates.html) in the AWS Config documentation.
+ Python 3, installed and configured. For more information about this, see the [Python documentation](https://www.python.org/).
+ An existing integrated development environment (IDE).
+ Identify your organizational units (OUs) in a column in the sample `excel_config_rules.xlsx` Excel spreadsheet (attached).

## Epics
<a name="generate-an-aws-cloudformation-template-containing-aws-config-managed-rules-using-troposphere-epics"></a>

### Customize and configure the AWS Config managed rules
<a name="customize-and-configure-the-aws-config-managed-rules"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the sample Excel spreadsheet. | Download the sample `excel_config_rules.xlsx` Excel spreadsheet (attached) and label as `Implemented` the AWS Config managed rules that you want to use. <br />Rules marked as `Implemented` will be added to the AWS CloudFormation template. | Developer |
| (Optional) Update the config\_rules\_params.json file with AWS Config rule parameters. | Some AWS Config managed rules require parameters and should be passed to the Python script as a JSON file by using the `--param-file` option. For example, the `access-keys-rotated` managed rule uses the following `maxAccessKeyAge` parameter:<pre>{<br />         "access-keys-rotated": {<br />             "InputParameters": {<br />                 "maxAccessKeyAge": 90<br />             }<br />         }<br />     }</pre><br />In this sample parameter, the `maxAccessKeyAge` is set to 90 days. The script reads the parameter file and adds any `InputParameters` that it finds. | Developer |
| (Optional) Update the config\_rules\_params.json file with AWS Config ComplianceResourceTypes. | By default, the Python script retrieves the `ComplianceResourceTypes` from AWS defined templates. If you want to override the scope of a specific AWS Config managed rule, then you need to pass it to the Python script as a JSON file using the `--param-file` option.<br />For example, the following sample code shows how the `ComplianceResourceTypes` for `ec2-volume-inuse-check` is set to the `["AWS::EC2::Volume"]` list:<pre>{<br />         "ec2-volume-inuse-check": {<br />             "Scope": {<br />                 "ComplianceResourceTypes": [<br />                     "AWS::EC2::Volume"<br />                 ]<br />             }<br />         }<br />     }</pre> | Developer |

### Run the Python script
<a name="run-the-python-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the pip packages from the requirements.txt file.  | Download the `requirements.txt` file (attached) and run the following command in your IDE to install the Python packages:<br />`pip3 install -r requirements.txt` | Developer |
| Run the Python script.  | 1. Download the `aws_config_rules.py`  file (attached) to your local machine.<br />2. Run the `- python3 aws_config_rules.py --ou <OU_NAME>` command. : `--ou` defines which OU column to choose in the Excel spreadsheet.You can also add the following optional parameters:+ `--config-rule-option` ** **– Defines the rules to choose from the Excel spreadsheet. The default is the `Implemented` parameter.<br />+ `--excel-file` ** **– The path for the Excel spreadsheet. The default is `aws_config_rules.xlsx`.<br />+ `--param-file` ** **– The path of the parameter JSON file. The default is `config_rules_params.json`.<br />+ `--max-execution-frequency` ** **– Defines how often the AWS Config managed rules are evaluated. The choices are `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`. The default is `TwentyFour_Hours`. | Developer |

### Deploy the AWS Config managed rules
<a name="deploy-the-aws-config-managed-rules"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the AWS CloudFormation stack. | 1. Sign in to the AWS Management Console, open the AWS CloudFormation console, and then choose **Create stack. **<br />2. On the **Specify template** page, choose **Upload a template file** and then upload your AWS CloudFormation template. <br />3. Specify a stack name and then choose **Next**.<br />4. Specify tags and then choose **Next**.<br />5. Choose **Create stack**. | Developer |

## Attachments
<a name="attachments-07c1cfff-fc9e-4a1f-bd36-48f025808bd8"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/07c1cfff-fc9e-4a1f-bd36-48f025808bd8/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
