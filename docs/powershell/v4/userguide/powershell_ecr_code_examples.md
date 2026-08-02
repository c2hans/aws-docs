---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ecr_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Amazon ECR examples using Tools for PowerShell V4
<a name="powershell_ecr_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon ECR.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-ECRLoginCommand`
<a name="ecr_Get-ECRLoginCommand_powershell_topic"></a>

The following code example shows how to use `Get-ECRLoginCommand`.

**Tools for PowerShell V4**
**Example 1: Returns a PSObject containing login information that can be used to authenticate to any Amazon ECR registry that your IAM principal has access to. The credentials and region endpoint required for the call to obtain the authorization token are obtained from the shell defaults (set up by the `Set-AWSCredential/Set-DefaultAWSRegion` or `Initialize-AWSDefaultConfiguration` cmdlets). You can use the Command property with Invoke-Expression to log in to the specified registry or use the returned credentials in other tools requiring login.**

```
Get-ECRLoginCommand
```
**Output:**

```
Username      : AWS
Password      : eyJwYXlsb2Fk...kRBVEFfS0VZIn0=
ProxyEndpoint : https://123456789012.dkr.ecr.us-west-2.amazonaws.com
Endpoint      : https://123456789012.dkr.ecr.us-west-2.amazonaws.com
ExpiresAt     : 9/26/2017 6:08:23 AM
Command       : docker login --username AWS --password eyJwYXlsb2Fk...kRBVEFfS0VZIn0= https://123456789012.dkr.ecr.us-west-2.amazonaws.com
```
**Example 2: Retrieves a PSObject containing login information that you use as an input to a docker login command. You can specify any Amazon ECR registry URI to authenticate to as long as your IAM principal has access to that registry.**

```
(Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin 012345678910.dkr.ecr.us-east-1.amazonaws.com
```
+  For API details, see [Get-ECRLoginCommand](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
