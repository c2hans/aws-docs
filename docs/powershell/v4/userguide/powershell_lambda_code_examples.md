---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_lambda_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Lambda examples using Tools for PowerShell V4
<a name="powershell_lambda_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Lambda.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-LMResourceTag`
<a name="lambda_TagResource_powershell_topic"></a>

The following code example shows how to use `Add-LMResourceTag`.

**Tools for PowerShell V4**
**Example 1: Adds the three tags (Washington, Oregon and California) and their associated values to the specified function identified by its ARN.**

```
Add-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction" -Tag @{ "Washington" = "Olympia"; "Oregon" = "Salem"; "California" = "Sacramento" }
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMAccountSetting`
<a name="lambda_GetAccountSettings_powershell_topic"></a>

The following code example shows how to use `Get-LMAccountSetting`.

**Tools for PowerShell V4**
**Example 1: This sample displays to compare the Account Limit and Account Usage**

```
Get-LMAccountSetting | Select-Object @{Name="TotalCodeSizeLimit";Expression={$_.AccountLimit.TotalCodeSize}}, @{Name="TotalCodeSizeUsed";Expression={$_.AccountUsage.TotalCodeSize}}
```
**Output:**

```
TotalCodeSizeLimit TotalCodeSizeUsed
------------------ -----------------
       80530636800          15078795
```
+  For API details, see [GetAccountSettings](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMAlias`
<a name="lambda_GetAlias_powershell_topic"></a>

The following code example shows how to use `Get-LMAlias`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the Routing Config weights for a specific Lambda Function Alias.**

```
Get-LMAlias -FunctionName "MylambdaFunction123" -Name "newlabel1" -Select RoutingConfig
```
**Output:**

```
AdditionalVersionWeights
------------------------
{[1, 0.6]}
```
+  For API details, see [GetAlias](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMFunctionConcurrency`
<a name="lambda_GetFunctionConcurrency_powershell_topic"></a>

The following code example shows how to use `Get-LMFunctionConcurrency`.

**Tools for PowerShell V4**
**Example 1: This examples gets the Reserved concurrency for the Lambda Function**

```
Get-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -Select *
```
**Output:**

```
ReservedConcurrentExecutions
----------------------------
100
```
+  For API details, see [GetFunctionConcurrency](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMFunctionConfiguration`
<a name="lambda_GetFunctionConfiguration_powershell_topic"></a>

The following code example shows how to use `Get-LMFunctionConfiguration`.

**Tools for PowerShell V4**
**Example 1: This example returns the version specific configuration of a Lambda Function.**

```
Get-LMFunctionConfiguration -FunctionName "MylambdaFunction123" -Qualifier "PowershellAlias"
```
**Output:**

```
CodeSha256                 : uWOW0R7z+f0VyLuUg7+/D08hkMFsq0SF4seuyUZJ/R8=
CodeSize                   : 1426
DeadLetterConfig           : Amazon.Lambda.Model.DeadLetterConfig
Description                : Verson 3 to test Aliases
Environment                : Amazon.Lambda.Model.EnvironmentResponse
FunctionArn                : arn:aws:lambda:us-east-1:123456789012:function:MylambdaFunction123
                             :PowershellAlias
FunctionName               : MylambdaFunction123
Handler                    : lambda_function.launch_instance
KMSKeyArn                  :
LastModified               : 2019-12-25T09:52:59.872+0000
LastUpdateStatus           : Successful
LastUpdateStatusReason     :
LastUpdateStatusReasonCode :
Layers                     : {}
MasterArn                  :
MemorySize                 : 128
RevisionId                 : 5d7de38b-87f2-4260-8f8a-e87280e10c33
Role                       : arn:aws:iam::123456789012:role/service-role/lambda
Runtime                    : python3.8
State                      : Active
StateReason                :
StateReasonCode            :
Timeout                    : 600
TracingConfig              : Amazon.Lambda.Model.TracingConfigResponse
Version                    : 4
VpcConfig                  : Amazon.Lambda.Model.VpcConfigDetail
```
+  For API details, see [GetFunctionConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMFunctionList`
<a name="lambda_ListFunctions_powershell_topic"></a>

The following code example shows how to use `Get-LMFunctionList`.

**Tools for PowerShell V4**
**Example 1: This sample displays all the Lambda functions with sorted code size**

```
Get-LMFunctionList | Sort-Object -Property CodeSize | Select-Object FunctionName, RunTime, Timeout, CodeSize
```
**Output:**

```
FunctionName                                                 Runtime   Timeout CodeSize
------------                                                 -------   ------- --------
test                                                         python2.7       3      243
MylambdaFunction123                                          python3.8     600      659
myfuncpython1                                                python3.8     303      675
```
+  For API details, see [ListFunctions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMPolicy`
<a name="lambda_GetPolicy_powershell_topic"></a>

The following code example shows how to use `Get-LMPolicy`.

**Tools for PowerShell V4**
**Example 1: This sample displays the Function policy of the Lambda function**

```
Get-LMPolicy -FunctionName test -Select Policy
```
**Output:**

```
{"Version":"2012-10-17",		 	 	 "Id":"default","Statement":[{"Sid":"xxxx","Effect":"Allow","Principal":{"Service":"sns.amazonaws.com"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-1:123456789102:function:test"}]}
```
+  For API details, see [GetPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMProvisionedConcurrencyConfig`
<a name="lambda_GetProvisionedConcurrencyConfig_powershell_topic"></a>

The following code example shows how to use `Get-LMProvisionedConcurrencyConfig`.

**Tools for PowerShell V4**
**Example 1: This example gets the provisioned Concurrency Configuration for the specified Alias of the Lambda Function.**

```
C:\>Get-LMProvisionedConcurrencyConfig -FunctionName "MylambdaFunction123" -Qualifier "NewAlias1"
```
**Output:**

```
AllocatedProvisionedConcurrentExecutions : 0
AvailableProvisionedConcurrentExecutions : 0
LastModified                             : 2020-01-15T03:21:26+0000
RequestedProvisionedConcurrentExecutions : 70
Status                                   : IN_PROGRESS
StatusReason                             :
```
+  For API details, see [GetProvisionedConcurrencyConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMProvisionedConcurrencyConfigList`
<a name="lambda_ListProvisionedConcurrencyConfigs_powershell_topic"></a>

The following code example shows how to use `Get-LMProvisionedConcurrencyConfigList`.

**Tools for PowerShell V4**
**Example 1: This example retrieves the list of provisioned concurrency configurations for a Lambda function.**

```
Get-LMProvisionedConcurrencyConfigList -FunctionName "MylambdaFunction123"
```
+  For API details, see [ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-LMResourceTag`
<a name="lambda_ListTags_powershell_topic"></a>

The following code example shows how to use `Get-LMResourceTag`.

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

### `Get-LMVersionsByFunction`
<a name="lambda_ListVersionsByFunction_powershell_topic"></a>

The following code example shows how to use `Get-LMVersionsByFunction`.

**Tools for PowerShell V4**
**Example 1: This example returns the list of version specific configurations for each version of the Lambda Function.**

```
Get-LMVersionsByFunction -FunctionName "MylambdaFunction123"
```
**Output:**

```
FunctionName        Runtime   MemorySize Timeout CodeSize LastModified                 RoleName
------------        -------   ---------- ------- -------- ------------                 --------
MylambdaFunction123 python3.8        128     600      659 2020-01-10T03:20:56.390+0000 lambda
MylambdaFunction123 python3.8        128       5     1426 2019-12-25T09:19:02.238+0000 lambda
MylambdaFunction123 python3.8        128       5     1426 2019-12-25T09:39:36.779+0000 lambda
MylambdaFunction123 python3.8        128     600     1426 2019-12-25T09:52:59.872+0000 lambda
```
+  For API details, see [ListVersionsByFunction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-LMAlias`
<a name="lambda_CreateAlias_powershell_topic"></a>

The following code example shows how to use `New-LMAlias`.

**Tools for PowerShell V4**
**Example 1: This example creates a New Lambda Alias for specified version and routing configuration to specify the percentage of invocation requests that it receives.**

```
New-LMAlias -FunctionName "MylambdaFunction123" -RoutingConfig_AdditionalVersionWeight @{Name="1";Value="0.6} -Description "Alias for version 4" -FunctionVersion 4 -Name "PowershellAlias"
```
+  For API details, see [CreateAlias](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Publish-LMFunction`
<a name="lambda_CreateFunction_powershell_topic"></a>

The following code example shows how to use `Publish-LMFunction`.

**Tools for PowerShell V4**
**Example 1: This example creates a new C\# (dotnetcore1.0 runtime) function named MyFunction in AWS Lambda, providing the compiled binaries for the function from a zip file on the local file system (relative or absolute paths may be used). C\# Lambda functions specify the handler for the function using the designation AssemblyName::Namespace.ClassName::MethodName. You should replace the assembly name (without .dll suffix), namespace, class name and method name parts of the handler spec appropriately. The new function will have environment variables 'envvar1' and 'envvar2' set up from the provided values.**

```
Publish-LMFunction -Description "My C# Lambda Function" `
        -FunctionName MyFunction `
        -ZipFilename .\MyFunctionBinaries.zip `
        -Handler "AssemblyName::Namespace.ClassName::MethodName" `
        -Role "arn:aws:iam::123456789012:role/LambdaFullExecRole" `
        -Runtime dotnetcore1.0 `
        -Environment_Variable @{ "envvar1"="value";"envvar2"="value" }
```
**Output:**

```
CodeSha256       : /NgBMd...gq71I=
CodeSize         : 214784
DeadLetterConfig :
Description      : My C# Lambda Function
Environment      : Amazon.Lambda.Model.EnvironmentResponse
FunctionArn      : arn:aws:lambda:us-west-2:123456789012:function:ToUpper
FunctionName     : MyFunction
Handler          : AssemblyName::Namespace.ClassName::MethodName
KMSKeyArn        :
LastModified     : 2016-12-29T23:50:14.207+0000
MemorySize       : 128
Role             : arn:aws:iam::123456789012:role/LambdaFullExecRole
Runtime          : dotnetcore1.0
Timeout          : 3
Version          : $LATEST
VpcConfig        :
```
**Example 2: This example is similar to the previous one except the function binaries are first uploaded to an Amazon S3 bucket (which must be in the same region as the intended Lambda function) and the resulting S3 object is then referenced when creating the function.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Key MyFunctionBinaries.zip -File .\MyFunctionBinaries.zip
Publish-LMFunction -Description "My C# Lambda Function" `
        -FunctionName MyFunction `
        -BucketName amzn-s3-demo-bucket `
        -Key MyFunctionBinaries.zip `
        -Handler "AssemblyName::Namespace.ClassName::MethodName" `
        -Role "arn:aws:iam::123456789012:role/LambdaFullExecRole" `
        -Runtime dotnetcore1.0 `
        -Environment_Variable @{ "envvar1"="value";"envvar2"="value" }
```
+  For API details, see [CreateFunction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Publish-LMVersion`
<a name="lambda_PublishVersion_powershell_topic"></a>

The following code example shows how to use `Publish-LMVersion`.

**Tools for PowerShell V4**
**Example 1: This example creates a version for the existing snapshot of Lambda Function Code**

```
Publish-LMVersion -FunctionName "MylambdaFunction123" -Description "Publishing Existing Snapshot of function code as a  new version through Powershell"
```
+  For API details, see [PublishVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-LMAlias`
<a name="lambda_DeleteAlias_powershell_topic"></a>

The following code example shows how to use `Remove-LMAlias`.

**Tools for PowerShell V4**
**Example 1: This example deletes the Lambda function Alias mentioned in the command.**

```
Remove-LMAlias -FunctionName "MylambdaFunction123" -Name "NewAlias"
```
+  For API details, see [DeleteAlias](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-LMFunction`
<a name="lambda_DeleteFunction_powershell_topic"></a>

The following code example shows how to use `Remove-LMFunction`.

**Tools for PowerShell V4**
**Example 1: This example deletes a specific version of a Lambda function**

```
Remove-LMFunction -FunctionName "MylambdaFunction123" -Qualifier '3'
```
+  For API details, see [DeleteFunction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-LMFunctionConcurrency`
<a name="lambda_DeleteFunctionConcurrency_powershell_topic"></a>

The following code example shows how to use `Remove-LMFunctionConcurrency`.

**Tools for PowerShell V4**
**Example 1: This examples removes the Function Concurrency of the Lambda Function.**

```
Remove-LMFunctionConcurrency -FunctionName "MylambdaFunction123"
```
+  For API details, see [DeleteFunctionConcurrency](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-LMPermission`
<a name="lambda_RemovePermission_powershell_topic"></a>

The following code example shows how to use `Remove-LMPermission`.

**Tools for PowerShell V4**
**Example 1: This example removes the function policy for the specified StatementId of a Lambda Function.**

```
$policy =  Get-LMPolicy -FunctionName "MylambdaFunction123" -Select Policy | ConvertFrom-Json| Select-Object -ExpandProperty Statement
Remove-LMPermission -FunctionName "MylambdaFunction123" -StatementId $policy[0].Sid
```
+  For API details, see [RemovePermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-LMProvisionedConcurrencyConfig`
<a name="lambda_DeleteProvisionedConcurrencyConfig_powershell_topic"></a>

The following code example shows how to use `Remove-LMProvisionedConcurrencyConfig`.

**Tools for PowerShell V4**
**Example 1: This example removes the Provisioned Concurrency Configuration for a specific Alias.**

```
Remove-LMProvisionedConcurrencyConfig -FunctionName "MylambdaFunction123" -Qualifier "NewAlias1"
```
+  For API details, see [DeleteProvisionedConcurrencyConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-LMResourceTag`
<a name="lambda_UntagResource_powershell_topic"></a>

The following code example shows how to use `Remove-LMResourceTag`.

**Tools for PowerShell V4**
**Example 1: Removes the supplied tags from a function. The cmdlet will prompt for confirmation before proceeding unless the -Force switch is specified. A single call is made to the service to remove the tags.**

```
Remove-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction" -TagKey "Washington","Oregon","California"
```
**Example 2: Removes the supplied tags from a function. The cmdlet will prompt for confirmation before proceeding unless the -Force switch is specified. Once call to the service is made per supplied tag.**

```
"Washington","Oregon","California" | Remove-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-LMAlias`
<a name="lambda_UpdateAlias_powershell_topic"></a>

The following code example shows how to use `Update-LMAlias`.

**Tools for PowerShell V4**
**Example 1: This example updates the Configuration of an existing Lambda function Alias. It updates the RoutingConfiguration value to shift 60% (0.6) of traffic to version 1**

```
Update-LMAlias -FunctionName "MylambdaFunction123" -Description " Alias for version 2" -FunctionVersion 2 -Name "newlabel1" -RoutingConfig_AdditionalVersionWeight @{Name="1";Value="0.6}
```
+  For API details, see [UpdateAlias](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-LMFunctionCode`
<a name="lambda_UpdateFunctionCode_powershell_topic"></a>

The following code example shows how to use `Update-LMFunctionCode`.

**Tools for PowerShell V4**
**Example 1: Updates the function named 'MyFunction' with new content contained in the specified zip file. For a C\# .NET Core Lambda function the zip file should contain the compiled assembly.**

```
Update-LMFunctionCode -FunctionName MyFunction -ZipFilename .\UpdatedCode.zip
```
**Example 2: This example is similar to the previous one but uses an Amazon S3 object containing the updated code to update the function.**

```
Update-LMFunctionCode -FunctionName MyFunction -BucketName amzn-s3-demo-bucket -Key UpdatedCode.zip
```
+  For API details, see [UpdateFunctionCode](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Update-LMFunctionConfiguration`
<a name="lambda_UpdateFunctionConfiguration_powershell_topic"></a>

The following code example shows how to use `Update-LMFunctionConfiguration`.

**Tools for PowerShell V4**
**Example 1: This example updates the existing Lambda Function Configuration**

```
Update-LMFunctionConfiguration -FunctionName "MylambdaFunction123" -Handler "lambda_function.launch_instance" -Timeout 600 -Environment_Variable @{ "envvar1"="value";"envvar2"="value" } -Role arn:aws:iam::123456789101:role/service-role/lambda -DeadLetterConfig_TargetArn arn:aws:sns:us-east-1: 123456789101:MyfirstTopic
```
+  For API details, see [UpdateFunctionConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-LMFunctionConcurrency`
<a name="lambda_PutFunctionConcurrency_powershell_topic"></a>

The following code example shows how to use `Write-LMFunctionConcurrency`.

**Tools for PowerShell V4**
**Example 1: This example applies the concurrency settings for the Function as a whole.**

```
Write-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -ReservedConcurrentExecution 100
```
+  For API details, see [PutFunctionConcurrency](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Write-LMProvisionedConcurrencyConfig`
<a name="lambda_PutProvisionedConcurrencyConfig_powershell_topic"></a>

The following code example shows how to use `Write-LMProvisionedConcurrencyConfig`.

**Tools for PowerShell V4**
**Example 1: This example adds a provisioned concurrency configuration to a Function's Alias**

```
Write-LMProvisionedConcurrencyConfig -FunctionName "MylambdaFunction123" -ProvisionedConcurrentExecution 20 -Qualifier "NewAlias1"
```
+  For API details, see [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
