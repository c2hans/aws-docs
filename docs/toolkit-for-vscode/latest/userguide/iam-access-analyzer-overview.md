---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/iam-access-analyzer-overview.html
---

# Working with AWS IAM Access Analyzer
<a name="iam-access-analyzer-overview"></a>

The following sections describe how to perform IAM policy validation and custom policy checks in the AWS Toolkit for Visual Studio Code. For additional details, see the following topics in the AWS Identity and Access Management User Guide: [IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) and [IAM Access Analyzer custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html).

## Prerequisites
<a name="w2aac17c39c13b5"></a>

The following prerequisites must be met before you can work with IAM Access Analyzer policy checks from the Toolkit.
+ Install Python version 3.6 or later.
+ Install either the [IAM Policy Validator for CloudFormation](https://github.com/awslabs/aws-cloudformation-iam-policy-validator) or the [IAM Policy Validator for Terraform](https://github.com/awslabs/terraform-iam-policy-validator) that is required by Python CLI tools and specified in the IAM Policy Checks window.
+ Configure your AWS Role credentials.

## IAM Access Analyzer policy checks
<a name="w2aac17c39c13b7"></a>

You can perform policy checks for CloudFormation templates, Terraform plans, and JSON Policy documents, using the AWS Toolkit for Visual Studio Code. Your check findings are viewable in the VS Code **Problems Panel**. The following image shows the VS Code **Problems Panel**.

![VS Code Problems Panel displaying security warnings and missing version warnings for CloudFormation resources.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/vscproblemspanel2024.png)

IAM Access Analyzer provides 4 types of checks:
+ Validate Policy
+ CheckAccessNotGranted
+ CheckNoNewAccess
+ CheckNoPublicAccess

The following sections describe how to run each type of check.

**Note**
Configure your AWS Role credentials prior to running any type of check. Supported files include the following document types: CloudFormation templates, Terraform plans, and JSON Policy documents
File path references are typically provided by your administrator or security team, and can be a system file path or an Amazon S3 bucket URI. To use an Amazon S3 bucket URI, your current role must have access to the Amazon S3 bucket.
A charge is associated with each custom policy check. For details about custom policy check pricing, see the [AWS IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing/) guide.

### Running Validate Policy
<a name="w2aac17c39c13b7c15"></a>

The Validate Policy check, also known as policy validation, validates your policy against IAM policy grammar and AWS best practices. For additional information, see the [Grammar of the IAM JSON policy language](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html) and AWS [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) topics, located in the *AWS Identity and Access Management* User Guide.

1. From VS Code, open a supported file that contains AWS IAM Policies, in the VS Code editor.

1. To open IAM Access Analyzer policy checks, open the VS Code Command Pallete by pressing **CRTL\+Shift\+P**, search for **IAM Policy Checks**, then click to open the **IAM Policy Checks** pane in the VS Code editor.

1. From the **IAM Policy Checks** pane, select your document type from the drop-down menu.

1. From the **Validate Policies** section, choose the **Run Policy Validation** button to run the Validate Policy check.

1. From the **Problems Panel** in VS Code, review your policy check findings.

1. Update your policy and repeat this procedure, re-running the Validate Policy check until your policy check findings no longer display security warnings or errors.

### Running CheckAccessNotGranted
<a name="w2aac17c39c13b7c17"></a>

CheckAccessNotGranted is a custom policy check to verify that specific IAM actions are not allowed by your policy.

**Note**
File path references are typically provided by your administrator or security team, and can be a system file path or an Amazon S3 bucket URI. To use an Amazon S3 bucket URI, your current role must have access to the Amazon S3 bucket. At least one action or resource must be specified and the file should be structured after the following example:

```
              {"actions": ["action1", "action2", "action3"], "resources": ["resource1", "resource2", "resource3"]}
```

1. From VS Code, open a supported file that contains AWS IAM Policies, in the VS Code editor.

1. To open IAM Access Analyzer policy checks, open the VS Code Command Pallete by pressing **CRTL\+Shift\+P**, search for **IAM Policy Checks**, then click to open the **IAM Policy Checks** pane in the VS Code editor.

1. From the **IAM Policy Checks** pane, select your document type from the drop-down menu.

1. From the **Custom Policy Checks** section, select **CheckAccessNotGranted**.

1. In the text-input field, you can enter a comma-separated list that contains actions and resource ARNs. At least one action or resource must be provided.

1. Choose the **Run Custom Policy Check** button.

1. From the **Problems Panel** in VS Code, review your policy check findings. Custom policy checks return a `PASS` or `FAIL` result.

1. Update your policy and repeat this procedure, re-running the CheckAccessNotGranted check until it returns `PASS`.

### Running CheckNoNewAccess
<a name="w2aac17c39c13b7c19"></a>

CheckNoNewAccess is a custom policy check to verify whether your policy grants new access compared to a reference policy.

1. From VS Code, open a supported file that contains AWS IAM Policies, in the VS Code editor.

1. To open IAM Access Analyzer policy checks, open the VS Code Command Pallete by pressing **CRTL\+Shift\+P**, search for **IAM Policy Checks**, then click to open the **IAM Policy Checks** pane in the VS Code editor.

1. From the **IAM Policy Checks** pane, select your document type from the drop-down menu.

1. From the **Custom Policy Checks** section, select **CheckNoNewAccess**.

1. Input a reference JSON policy document. Alternatively, you can provide a file path that references a JSON policy document.

1. Select the **Reference Policy Type** that matches the type of your reference document.

1. Choose the **Run Custom Policy Check** button.

1. From the **Problems Panel** in VS Code, review your policy check findings. Custom policy checks return a `PASS` or `FAIL` result.

1. Update your policy and repeat this procedure, re-running the CheckNoNewAccess check until it returns `PASS`.

### Running CheckNoPublicAccess
<a name="w2aac17c39c13b7c21"></a>

CheckNoPublicAccess is a custom policy check to verify whether your policy grants public access to supported resource types within your template.

For specific information about supported resource types, see the [cloudformation-iam-policy-validator](https://github.com/awslabs/aws-cloudformation-iam-policy-validator?tab=readme-ov-file#supported-resource-based-policies) and [terraform-iam-policy-validator](https://github.com/awslabs/terraform-iam-policy-validator) GitHub repositories.

1. From VS Code, open a supported file that contains AWS IAM Policies, in the VS Code editor.

1. To open IAM Access Analyzer policy checks, open the VS Code Command Pallete by pressing **CRTL\+Shift\+P**, search for **IAM Policy Checks**, then click to open the **IAM Policy Checks** pane in the VS Code editor.

1. From the **IAM Policy Checks** pane, select your document type from the drop-down menu.

1. From the **Custom Policy Checks** section, select **CheckNoPublicAccess**.

1. Choose the **Run Custom Policy Check** button.

1. From the **Problems Panel** in VS Code, review your policy check findings. Custom policy checks return a `PASS` or `FAIL` result.

1. Update your policy and repeat this procedure, re-running the CheckNoNewAccess check until it returns `PASS`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
