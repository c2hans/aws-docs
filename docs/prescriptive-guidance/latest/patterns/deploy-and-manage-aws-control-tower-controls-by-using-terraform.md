---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-and-manage-aws-control-tower-controls-by-using-terraform.html
---

# Deploy and manage AWS Control Tower controls by using Terraform
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform"></a>

*Iker Reina Fuente and Ivan Girardi, Amazon Web Services*

## Summary
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-summary"></a>

This pattern describes how to use AWS Control Tower controls, HashiCorp Terraform, and infrastructure as code (IaC) to implement and administer preventive, detective, and proactive security controls. A [control](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) (also known as a *guardrail*) is a high-level rule that provides ongoing governance for your overall AWS Control Tower environment. For example, you can use controls to require logging for your AWS accounts and then configure automatic notifications if specific security-related events occur.

AWS Control Tower helps you implement preventive, detective, and proactive controls that govern your AWS resources and monitor compliance across multiple AWS accounts. Each control enforces a single rule. In this pattern, you use a provided IaC template to specify which controls you want to deploy in your environment.

AWS Control Tower controls apply to an entire [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit), and the control affects every AWS account within the OU. Therefore, when users perform any action in any account in your landing zone, the action is subject to the controls that govern the OU.

Implementing AWS Control Tower controls helps establish a strong security foundation for your AWS landing zone. By using this pattern to deploy the controls as IaC through Terraform, you can standardize the controls in your landing zone and more efficiently deploy and manage them.

To deploy AWS Control Tower controls as IaC, you can also use AWS Cloud Development Kit (AWS CDK) instead of Terraform. For more information, see [Deploy and manage AWS Control Tower controls by using AWS CDK and AWS CloudFormation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-and-manage-aws-control-tower-controls-by-using-aws-cdk-and-aws-cloudformation.html).

**Intended audience**

This pattern is recommended for users who have experience with AWS Control Tower, Terraform, and AWS Organizations.

## Prerequisites and limitations
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-prereqs"></a>

**Prerequisites**
+ Active AWS accounts managed as an organization in AWS Organizations and an AWS Control Tower landing zone. For instructions, see [Getting started](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) in the AWS Control Tower documentation.
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
+ An AWS Identity and Access Management (IAM) role in the management account that has permissions to deploy this pattern. For more information about the required permissions and a sample policy, see *Least privilege permissions for the IAM role* in the [Additional information](#deploy-and-manage-aws-control-tower-controls-by-using-terraform-additional) section of this pattern.
+ Permissions to assume the IAM role in the management account.
+ Terraform CLI, [installed](https://developer.hashicorp.com/terraform/cli) (Terraform documentation).
+ Terraform AWS Provider, [configured](https://hashicorp.github.io/terraform-provider-aws/) (Terraform documentation).
+ Terraform backend, [configured](https://developer.hashicorp.com/terraform/language/backend) (Terraform documentation).

**Limitations**
+ For AWS Control Tower controls, this pattern requires the use of [global identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/all-global-identifiers.html) that are in the following format:

  ```
  arn:<PARTITION>:controlcatalog:::control/<CONTROL_CATALOG_OPAQUE_ID>
  ```

  Previous versions of this pattern used [regional identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/control-metadata-tables.html) that are no longer supported. We recommend that you migrate from Regional identifiers to global identifiers. Global identifiers help you manage controls and expand the number of controls that you can use.
**Note**
In most cases, the value for `<PARTITION>` is `aws`.

**Product versions**
+ AWS Control Tower version 3.2 or later
+ Terraform version 1.5 or later
+ Terraform AWS Provider version 4.67 or later

## Architecture
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-architecture"></a>

This section provides a high-level overview of this solution and the architecture established by the sample code. The following diagram shows controls deployed across the various accounts in the OU.

![Architecture diagram of controls deployed across all AWS accounts in the organizational unit.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6e0d6c30-a539-44b7-8415-e669fb2ad26a/images/60407c0e-852e-4d5f-9a7d-8510316063aa.png)

AWS Control Tower controls are categorized according to their *behavior* and their *guidance*.

There are three primary types of control behaviors:

1. *Preventive controls* are designed to prevent actions from occurring. These are implemented with [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) or [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in AWS Organizations. The status of a preventive control is either **enforced** or **not enabled**. Preventive controls are supported in all AWS Regions.

1. *Detective controls* are designed to detect specific events when they occur and log the action in AWS CloudTrail. These are implemented with [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html). The status of a detective control is either **clear**, **in violation**, or **not enabled**. Detective controls apply only in those AWS Regions supported by AWS Control Tower.

1. *Proactive controls* scan resources that would be provisioned by AWS CloudFormation and check whether they are compliant with your company policies and objectives. Resources that are not compliant will not be provisioned. These are implemented with [AWS CloudFormation hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks.html). The status of a proactive control is **PASS**, **FAIL**, or **SKIP**.

Control *guidance* is the recommended practice for how to apply each control to your OUs. AWS Control Tower provides three categories of guidance: *mandatory*, *strongly recommended*, and *elective*. The guidance of a control is independent of its behavior. For more information, see [Control behavior and guidance](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html#control-behavior).

## Tools
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.

**Code repository**

The code for this pattern is available in the GitHub [Deploy and manage AWS Control Tower controls by using Terraform](https://github.com/aws-samples/aws-control-tower-controls-terraform) repository.

## Best practices
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-best-practices"></a>
+ The IAM role used to deploy this solution should adhere to the [principle of least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) (IAM documentation).
+ Follow the [Best practices for AWS Control Tower administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html) (AWS Control Tower documentation).

## Epics
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-epics"></a>

### Enable controls in the management account
<a name="enable-controls-in-the-management-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | In a bash shell, enter the following command. This clones the [Deploy and manage AWS Control Tower controls by using Terraform](https://github.com/aws-samples/aws-control-tower-controls-terraform) repository from GitHub.<pre>git clone https://github.com/aws-samples/aws-control-tower-controls-terraform.git</pre> | DevOps engineer |
| Edit the Terraform backend configuration file. | 1. In the cloned repository, open the **backend.tf** file.<br />2. Edit the file to set the Terraform backend configuration. The configuration you define in this file depends on your environment. For more information, see [Backend configuration](https://developer.hashicorp.com/terraform/language/settings/backends/configuration) (Terraform documentation).  <br />3. Save and close the **backend.tf** file. | DevOps engineer, Terraform |
| Edit the Terraform provider configuration file. | 1. In the cloned repository, open the **provider.tf** file.<br />2. Edit the file to set the Terraform provider configuration. For more information, see [Provider configuration](https://developer.hashicorp.com/terraform/language/providers/configuration) (Terraform documentation). Set the AWS Region as the Region where the AWS Control Tower API is available.<br />3. Save and close the **provider.tf** file. | DevOps engineer, Terraform |
| Edit the configuration file. | 1. In the cloned repository, open the **variables.tfvars** file.<br />2. Open [All global identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/all-global-identifiers.html) in the AWS Control Tower documentation.<br />3. In the JSON-formatted list, locate the control that you want to implement, and then copy its global identifier (also known as the {CONTROL\_CATALOG\_OPAQUE\_ID} value). For example, the global identifier for the **AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED** control is `k4izcjxhukijhajp6ks5mjxk`.<br />4. In the `controls` section, in the `control_names` parameter, enter the global identifier that you copied.<br />5. In the `controls` section, in the `organizational_unit_ids` parameter, enter the ID of the organizational unit where you want to enable the control, such as `ou-1111-11111111`. Enter the ID in double quotation marks, and separate multiple IDs with commas. For more information about how to retrieve OU IDs, see [Viewing the details of an OU](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html#orgs_view_ou).<br />6. Save and close the **variables.tfvars** file. For an example of an updated **variables.tfvars** file, see the [Additional information](#deploy-and-manage-aws-control-tower-controls-by-using-terraform-additional) section of this pattern. | DevOps engineer, General AWS, Terraform |
| Assume the IAM role in the management account. | In the management account, assume the IAM role that has permissions to deploy the Terraform configuration file. For more information about the permissions required and a sample policy, see *Least privilege permissions for the IAM role* in the [Additional information](#deploy-and-manage-aws-control-tower-controls-by-using-terraform-additional) section. For more information about assuming an IAM role in the AWS CLI, see [Use an IAM role in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html). | DevOps engineer, General AWS |
| Deploy the configuration file. | 1. Enter the following command to initialize Terraform.<pre>$ terraform init -upgrade</pre><br />2. Enter the following command to preview the changes compared the current state.<pre>$ terraform plan -var-file="variables.tfvars"</pre><br />3. Review the configuration changes in the Terraform plan and confirm that you want to implement these changes in the organization.<br />4. Enter the following command to deploy the resources.<pre>$ terraform apply -var-file="variables.tfvars"</pre> | DevOps engineer, General AWS, Terraform |

### (Optional) Disable controls in the AWS Control Tower management account
<a name="optional-disable-controls-in-the-ctower-management-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the `destroy` command. | Enter the following command to remove the resources deployed by this pattern.<pre>$ terraform destroy -var-file="variables.tfvars"</pre> | DevOps engineer, General AWS, Terraform |

## Troubleshooting
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `Error: creating ControlTower Control ValidationException: Guardrail <control ID> is already enabled on organizational unit <OU ID>` error | The control you are trying to enable is already enabled in the target OU. This error can occur if a user manually enabled the control through the AWS Management Console, through AWS Control Tower or through AWS Organizations. To deploy the Terraform configuration file, you can use either of the following options.<br />**Option 1: Update the Terraform current state file**<br />You can import the resource to the Terraform current state file. When you rerun the `apply` command, Terraform will skip this resource. Do the following to import the resource to the current Terraform state:1. In the AWS Control Tower management account, enter the following command to retrieve a list of the Amazon Resource Names (ARNs) for the OUs, where `<root-ID>` is the organization root. For more information about retrieving this ID, see [Viewing the details of the root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html#orgs_view_root).<pre>aws organizations list-organizational-units-for-parent --parent-id <root-ID></pre><br />2. For each OU returned in the previous step, enter the following command, where `<OU-ARN>` is the ARN of the OU.<pre>aws controltower list-enabled-controls --target-identifier <OU-ARN></pre><br />3. Copy the ARNs and perform the Terraform import in the required module so that it is included in the Terraform state. For instructions, see [Import](https://developer.hashicorp.com/terraform/language/import) (Terraform documentation).<br />4. Repeat the steps in *Deploy the configuration* in the [Epics](#deploy-and-manage-aws-control-tower-controls-by-using-terraform-epics) section.<br />**Option 2: Disable the control**<br />If you are working in a non-production environment, you can disable the control in the console. Re-enable it by repeating the steps in *Deploy the configuration* in the [Epics](#deploy-and-manage-aws-control-tower-controls-by-using-terraform-epics) section. This approach is not recommended for production environments because there is a period of time when the control will be disabled. If you want to use this option in a production environment, you can implement temporary controls, such as temporarily applying a SCP in AWS Organizations. |

## Related resources
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-resources"></a>

**AWS documentation**
+ [About controls](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) (AWS Control Tower documentation)
+ [Controls library](https://docs.aws.amazon.com/controltower/latest/userguide/controls-reference.html) (AWS Control Tower documentation)
+ [Deploy and manage AWS Control Tower controls by using AWS CDK and AWS CloudFormation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-and-manage-aws-control-tower-controls-by-using-aws-cdk-and-aws-cloudformation.html) (AWS Prescriptive Guidance)

**Other resources**
+ [Terraform](https://www.terraform.io/)
+ [Terraform CLI documentation](https://www.terraform.io/cli)

## Additional information
<a name="deploy-and-manage-aws-control-tower-controls-by-using-terraform-additional"></a>

**Example variables.tfvars**** file**

The following is an example of an updated **variables.tfvars** file. This sample enables the **AWS-GR\_ENCRYPTED\_VOLUMES** control (global ID: `503uicglhjkokaajywfpt6ros`) and the **AWS-GR\_SUBNET\_AUTO\_ASSIGN\_PUBLIC\_IP\_DISABLED** control (global ID: `50z1ot237wl8u1lv5ufau6qqo`). For a list of global IDs, see [All global identifiers](https://docs.aws.amazon.com/controltower/latest/controlreference/all-global-identifiers.html) in the AWS Control Tower documentation.

The following example also enables controls that have parameters such as **CT.S3.PV.5** (global ID: `7mo7a2h2ebsq71l8k6uzr96ou`) and  **CT.SECRETSMANAGER.PV.1** (global ID: `dvhe47fxg5o6lryqrq9g6sxg4`). For a list of controls with parameters, see [Controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html) in the AWS Control Tower documentation.

```
controls = [
    {
        control_names = [
            "503uicglhjkokaajywfpt6ros", # AWS-GR_ENCRYPTED_VOLUMES
            ...
        ],
        organizational_unit_ids = ["ou-1111-11111111", "ou-2222-22222222"...],
    },
    {
        control_names = [
            "50z1ot237wl8u1lv5ufau6qqo", # AWS-GR_SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED
            ...
        ],
        organizational_unit_ids = ["ou-1111-11111111"...],
    },
]

controls_with_params = [
  {
    control_names = [
      { "7mo7a2h2ebsq71l8k6uzr96ou" = { # CT.S3.PV.5
        parameters = {
          "ExemptedPrincipalArns" : ["arn:aws:iam::*:role/RoleName"],
          "ExemptedResourceArns" : [],
        }
      } },
      { "dvhe47fxg5o6lryqrq9g6sxg4" = { # CT.SECRETSMANAGER.PV.1
        parameters = {
          "ExemptedPrincipalArns" : ["arn:aws:iam::*:role/RoleName"],
        }
      } },
      ...
    ],
    organizational_unit_ids = ["ou-1111-11111111"...]
  },
  {
    control_names = [
      { "dvuaav61i5cnfazfelmvn9m6k" = { # AWS-GR_DISALLOW_CROSS_REGION_NETWORKING
        parameters = {
          "ExemptedPrincipalArns" : ["arn:aws:iam::*:role/RoleName"],
        }
      } },
      { "41ngl8m5c4eb1myoz0t707n7h" = { # AWS-GR_DISALLOW_VPC_INTERNET_ACCESS
        parameters = {
          "ExemptedPrincipalArns" : ["arn:aws:iam::*:role/RoleName"],
        }
      } },
      ...
    ],
    organizational_unit_ids = ["ou-2222-22222222"...]
  }
]
```

**Least privilege permissions for the IAM role**

This pattern requires that you assume an IAM role in the management account. Best practice is to assume a role with temporary permissions and limit the permissions according to the principle of least privilege. The following sample policy allows the minimum actions required to enable or disable AWS Control Tower controls.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "controltower:EnableControl",
                "controltower:DisableControl",
                "controltower:GetControlOperation",
                "controltower:ListEnabledControls",
                "organizations:AttachPolicy",
                "organizations:CreatePolicy",
                "organizations:DeletePolicy",
                "organizations:DescribeOrganization",
                "organizations:DetachPolicy",
                "organizations:ListAccounts",
                "organizations:ListAWSServiceAccessForOrganization",
                "organizations:ListChildren",
                "organizations:ListOrganizationalUnitsForParent",
                "organizations:ListParents",
                "organizations:ListPoliciesForTarget",
                "organizations:ListRoots",
                "organizations:UpdatePolicy"
            ],
            "Resource": "*"
        }
    ]
}
```
