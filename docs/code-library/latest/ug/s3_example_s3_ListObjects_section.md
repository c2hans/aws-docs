---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_ListObjects_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListObjects` with a CLI
<a name="s3_example_s3_ListObjects_section"></a>

The following code examples show how to use `ListObjects`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Create a web page that lists Amazon S3 objects](s3_example_s3_Scenario_ListObjectsWeb_section.md)

------
#### [ CLI ]

**AWS CLI**
The following example uses the `list-objects` command to display the names of all the objects in the specified bucket:

```
aws s3api list-objects --bucket {{text-content}} --query '{{Contents[].{Key: Key, Size: Size}}}'
```
The example uses the `--query` argument to filter the output of `list-objects` down to the key value and size for each object
For more information about objects, see Working with Amazon S3 Objects in the *Amazon S3 Developer Guide*.
+  For API details, see [ListObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command retrieves the information about all of the items in the bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket
```
**Example 2: This command retrieves the information about the item "sample.txt" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt
```
**Example 3: This command retrieves the information about all items with the prefix "sample" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix sample
```
+  For API details, see [ListObjects](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command retrieves the information about all of the items in the bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket
```
**Example 2: This command retrieves the information about the item "sample.txt" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt
```
**Example 3: This command retrieves the information about all items with the prefix "sample" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix sample
```
+  For API details, see [ListObjects](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
