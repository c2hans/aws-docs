---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudtrail_example_cloudtrail_StartLogging_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `StartLogging` with a CLI
<a name="cloudtrail_example_cloudtrail_StartLogging_section"></a>

The following code examples show how to use `StartLogging`.

------
#### [ CLI ]

**AWS CLI**
**To start logging for a trail**
The following `start-logging` command turns on logging for `Trail1`:

```
aws cloudtrail start-logging --name {{Trail1}}
```
+  For API details, see [StartLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-logging.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Starts the recording of AWS API calls and log file delivery for the trail named 'myExampleTrail'. This example assumes the trail was created in the same region as the current shell default.**

```
Start-CTLogging -Name myExampleTrail
```
**Example 2: Starts the recording of AWS API calls and log file delivery for a trail that was created in a region other than the current shell default (in this case, the Frankfurt (eu-central-1) region).**

```
Start-CTLogging -Name myExampleTrail -Region eu-central-1
```
+  For API details, see [StartLogging](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Starts the recording of AWS API calls and log file delivery for the trail named 'myExampleTrail'. This example assumes the trail was created in the same region as the current shell default.**

```
Start-CTLogging -Name myExampleTrail
```
**Example 2: Starts the recording of AWS API calls and log file delivery for a trail that was created in a region other than the current shell default (in this case, the Frankfurt (eu-central-1) region).**

```
Start-CTLogging -Name myExampleTrail -Region eu-central-1
```
+  For API details, see [StartLogging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
