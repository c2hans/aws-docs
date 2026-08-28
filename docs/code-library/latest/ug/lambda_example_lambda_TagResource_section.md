---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_lambda_TagResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `TagResource` with a CLI
<a name="lambda_example_lambda_TagResource_section"></a>

The following code examples show how to use `TagResource`.

------
#### [ CLI ]

**AWS CLI**
**To add tags to an existing Lambda function**
The following `tag-resource` example adds a tag with the key name `DEPARTMENT` and a value of `Department A` to the specified Lambda function.

```
aws lambda tag-resource \
    --resource {{arn:aws:lambda:us-west-2:123456789012:function:my-function}} \
    --tags {{"DEPARTMENT=Department A"}}
```
This command produces no output.
For more information, see [Tagging Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the *AWS Lambda Developer Guide*.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/tag-resource.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Adds the three tags (Washington, Oregon and California) and their associated values to the specified function identified by its ARN.**

```
Add-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction" -Tag @{ "Washington" = "Olympia"; "Oregon" = "Salem"; "California" = "Sacramento" }
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Adds the three tags (Washington, Oregon and California) and their associated values to the specified function identified by its ARN.**

```
Add-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction" -Tag @{ "Washington" = "Olympia"; "Oregon" = "Salem"; "California" = "Sacramento" }
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
