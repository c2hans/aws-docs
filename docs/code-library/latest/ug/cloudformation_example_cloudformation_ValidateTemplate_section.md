---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_ValidateTemplate_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ValidateTemplate` with a CLI
<a name="cloudformation_example_cloudformation_ValidateTemplate_section"></a>

The following code examples show how to use `ValidateTemplate`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Creating your first infrastructure stack](cloudformation_example_cloudformation_GettingStarted_021_section.md)

------
#### [ CLI ]

**AWS CLI**
**To validate an AWS CloudFormation template**
The following `validate-template` command validates the `sampletemplate.json` template:

```
aws cloudformation validate-template --template-body {{file://sampletemplate.json}}
```
Output:

```
{
    "Description": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.",
    "Parameters": [],
    "Capabilities": []
}
```
For more information, see Working with AWS CloudFormation Templates in the *AWS CloudFormation User Guide*.
+  For API details, see [ValidateTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/validate-template.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Validates the specified template content. The output details the capabilities, description and parameters of the template.**

```
Test-CFNTemplate -TemplateBody "{TEMPLATE CONTENT HERE}"
```
**Example 2: Validates the specified template accessed via an Amazon S3 URL. The output details the capabilities, description and parameters of the template.**

```
Test-CFNTemplate -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template
```
+  For API details, see [ValidateTemplate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Validates the specified template content. The output details the capabilities, description and parameters of the template.**

```
Test-CFNTemplate -TemplateBody "{TEMPLATE CONTENT HERE}"
```
**Example 2: Validates the specified template accessed via an Amazon S3 URL. The output details the capabilities, description and parameters of the template.**

```
Test-CFNTemplate -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template
```
+  For API details, see [ValidateTemplate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
