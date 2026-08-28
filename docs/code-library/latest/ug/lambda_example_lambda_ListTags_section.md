---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_lambda_ListTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListTags` with a CLI
<a name="lambda_example_lambda_ListTags_section"></a>

The following code examples show how to use `ListTags`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve the list of tags for a Lambda function**
The following `list-tags` example displays the tags attached to the `my-function` Lambda function.

```
aws lambda list-tags \
    --resource {{arn:aws:lambda:us-west-2:123456789012:function:my-function}}
```
Output:

```
{
    "Tags": {
        "Category": "Web Tools",
        "Department": "Sales"
    }
}
```
For more information, see [Tagging Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) in the *AWS Lambda Developer Guide*.
+  For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Retrieves the tags and their values currently set on the specified function.**

```
Get-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
```
**Output:**

```
Key        Value
---        -----
California Sacramento
Oregon     Salem
Washington Olympia
```
+  For API details, see [ListTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Retrieves the tags and their values currently set on the specified function.**

```
Get-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
```
**Output:**

```
Key        Value
---        -----
California Sacramento
Oregon     Salem
Washington Olympia
```
+  For API details, see [ListTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
