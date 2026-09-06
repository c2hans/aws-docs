---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_device-farm_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Device Farm examples using Tools for PowerShell V4
<a name="powershell_device-farm_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Device Farm.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `New-DFUpload`
<a name="device-farm_CreateUpload_powershell_topic"></a>

The following code example shows how to use `New-DFUpload`.

**Tools for PowerShell V4**
**Example 1: This example creates an AWS Device Farm upload for an Android app. You can get the project ARN from the output of New-DFProject or Get-DFProjectList. Use the signed URL in the New-DFUpload output to upload a file to Device Farm.**

```
New-DFUpload -ContentType "application/octet-stream" -ProjectArn "arn:aws:devicefarm:us-west-2:123456789012:project:EXAMPLEa-7ec1-4741-9c1f-d3e04EXAMPLE" -Name "app.apk" -Type ANDROID_APP
```
+  For API details, see [CreateUpload](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
