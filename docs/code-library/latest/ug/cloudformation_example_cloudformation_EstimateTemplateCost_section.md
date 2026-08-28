---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_EstimateTemplateCost_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `EstimateTemplateCost` with a CLI
<a name="cloudformation_example_cloudformation_EstimateTemplateCost_section"></a>

The following code examples show how to use `EstimateTemplateCost`.

------
#### [ CLI ]

**AWS CLI**
**To estimate template cost**
The following `estimate-template-cost` example generates a cost estimate for a template named `template.yaml` in the current folder.

```
aws cloudformation estimate-template-cost \
    --template-body {{file://template.yaml}}
```
Output:

```
{
    "Url": "http://calculator.s3.amazonaws.com/calc5.html?key=cloudformation/7870825a-xmpl-4def-92e7-c4f8dd360cca"
}
```
+  For API details, see [EstimateTemplateCost](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/estimate-template-cost.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is obtained from the specified Amazon S3 URL and the single customization parameter applied. The parameter can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Measure-CFNTemplateCost -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
                        -Region us-west-1 `
                        -Parameter @{ ParameterKey="KeyName"; ParameterValue="myKeyPairName" }
```
**Example 2: Returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is parsed from the supplied content and the customization parameters applied (this example assumes the template content would have declared two parameters, 'KeyName' and 'InstanceType'). The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Measure-CFNTemplateCost -TemplateBody "{TEMPLATE CONTENT HERE}" `
                        -Parameter @( @{ ParameterKey="KeyName"; ParameterValue="myKeyPairName" },`
                                      @{ ParameterKey="InstanceType"; ParameterValue="m1.large" })
```
**Example 3: Uses New-Object to build the set of template parameters and returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is parsed from the supplied content, with customization parameters (this example assumes the template content would have declared two parameters, 'KeyName' and 'InstanceType').**

```
$p1 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p1.ParameterKey = "KeyName"
$p1.ParameterValue = "myKeyPairName"

$p2 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p2.ParameterKey = "InstanceType"
$p2.ParameterValue = "m1.large"

Measure-CFNTemplateCost -TemplateBody "{TEMPLATE CONTENT HERE}" -Parameter @( $p1, $p2 )
```
+  For API details, see [EstimateTemplateCost](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is obtained from the specified Amazon S3 URL and the single customization parameter applied. The parameter can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Measure-CFNTemplateCost -TemplateURL https://s3.amazonaws.com/amzn-s3-demo-bucket/templatefile.template `
                        -Region us-west-1 `
                        -Parameter @{ ParameterKey="KeyName"; ParameterValue="myKeyPairName" }
```
**Example 2: Returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is parsed from the supplied content and the customization parameters applied (this example assumes the template content would have declared two parameters, 'KeyName' and 'InstanceType'). The customization parameters can also be specified using 'Key' and 'Value' instead of 'ParameterKey' and 'ParameterValue'.**

```
Measure-CFNTemplateCost -TemplateBody "{TEMPLATE CONTENT HERE}" `
                        -Parameter @( @{ ParameterKey="KeyName"; ParameterValue="myKeyPairName" },`
                                      @{ ParameterKey="InstanceType"; ParameterValue="m1.large" })
```
**Example 3: Uses New-Object to build the set of template parameters and returns an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template. The template is parsed from the supplied content, with customization parameters (this example assumes the template content would have declared two parameters, 'KeyName' and 'InstanceType').**

```
$p1 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p1.ParameterKey = "KeyName"
$p1.ParameterValue = "myKeyPairName"

$p2 = New-Object -Type Amazon.CloudFormation.Model.Parameter
$p2.ParameterKey = "InstanceType"
$p2.ParameterValue = "m1.large"

Measure-CFNTemplateCost -TemplateBody "{TEMPLATE CONTENT HERE}" -Parameter @( $p1, $p2 )
```
+  For API details, see [EstimateTemplateCost](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
