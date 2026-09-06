---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_resource-groups-tagging-api_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Resource Groups Tagging API examples using Tools for PowerShell V5
<a name="powershell_resource-groups-tagging-api_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Resource Groups Tagging API.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-RGTResourceTag`
<a name="resource-groups-tagging-api_TagResources_powershell_topic"></a>

The following code example shows how to use `Add-RGTResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example adds the tag keys "stage" and "version" with values "beta" and "preprod\_test" to an Amazon S3 bucket and an Amazon DynamoDB table. A single call is made to the service to apply the tags.**

```
$arn1 = "arn:aws:s3:::amzn-s3-demo-bucket"
$arn2 = "arn:aws:dynamodb:us-west-2:123456789012:table/mytable"

Add-RGTResourceTag -ResourceARNList $arn1,$arn2 -Tag @{ "stage"="beta"; "version"="preprod_test" }
```
**Example 2: This example adds the specified tags and values to an Amazon S3 bucket and an Amazon DynamoDB table. Two calls are made to the service, one for each resource ARN piped into the cmdlet.**

```
$arn1 = "arn:aws:s3:::amzn-s3-demo-bucket"
$arn2 = "arn:aws:dynamodb:us-west-2:123456789012:table/mytable"

$arn1,$arn2 | Add-RGTResourceTag -Tag @{ "stage"="beta"; "version"="preprod_test" }
```
+  For API details, see [TagResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGTResource`
<a name="resource-groups-tagging-api_GetResources_powershell_topic"></a>

The following code example shows how to use `Get-RGTResource`.

**Tools for PowerShell V5**
**Example 1: Returns all the tagged resources in a region and the tag keys associated with the resource. If no -Region parameter is supplied to the cmdlet it will attempt to infer region from the shell or EC2 instance metadata.**

```
Get-RGTResource
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 2: Returns all the tagged resources of the specified type in a region. The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).**

```
Get-RGTResource -ResourceType "s3"
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 3: Returns all the tagged resources of the specified type in a region. Note that when the resource types are piped into the cmdlet, one call to the service is made for each supplied resource type.**

```
"dynamodb","s3" | Get-RGTResource
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 4: Returns all the tagged resources that match the specified filter.**

```
Get-RGTResource -TagFilter @{ Key="stage" }
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 5: Returns all the tagged resources that match the specified filter and resource type.**

```
Get-RGTResource -TagFilter @{ Key="stage" } -ResourceType "dynamodb"
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
```
**Example 6: Returns all the tagged resources that match the specified filter.**

```
Get-RGTResource -TagFilter @{ Key="stage"; Values=@("beta","gamma") }
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
```
+  For API details, see [GetResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGTTagKey`
<a name="resource-groups-tagging-api_GetTagKeys_powershell_topic"></a>

The following code example shows how to use `Get-RGTTagKey`.

**Tools for PowerShell V5**
**Example 1: Returns all tag keys in the specified region. If the -Region parameter is not specified the cmdlet will attempt to infer the region from the default shell region or EC2 instance metadata. Note that the tag keys are not returned in any specific order.**

```
Get-RGTTagKey -region us-west-2
```
**Output:**

```
version
stage
```
+  For API details, see [GetTagKeys](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-RGTTagValue`
<a name="resource-groups-tagging-api_GetTagValues_powershell_topic"></a>

The following code example shows how to use `Get-RGTTagValue`.

**Tools for PowerShell V5**
**Example 1: Returns the value for the specified tag in a region. If the -Region parameter is not specified the cmdlet will attempt to infer the region from the default shell region or EC2 instance metadata.**

```
Get-RGTTagValue -Key "stage" -Region us-west-2
```
**Output:**

```
beta
```
+  For API details, see [GetTagValues](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-RGTResourceTag`
<a name="resource-groups-tagging-api_UntagResources_powershell_topic"></a>

The following code example shows how to use `Remove-RGTResourceTag`.

**Tools for PowerShell V5**
**Example 1: Removes the tag keys "stage" and "version", and the associated values, from an Amazon S3 bucket and an Amazon DynamoDB table. A single call is made to the service to remove the tags. Before the tags are removed the cmdlet will prompt for confirmation. To bypass confirmation add the -Force parameter.**

```
$arn1 = "arn:aws:s3:::amzn-s3-demo-bucket"
$arn2 = "arn:aws:dynamodb:us-west-2:123456789012:table/mytable"

Remove-RGTResourceTag -ResourceARNList $arn1,$arn2 -TagKey "stage","version"
```
**Example 2: Removes the tag keys "stage" and "version", and the associated values, from an Amazon S3 bucket and an Amazon DynamoDB table. Two calls are made to the service, one for each resource ARN piped into the cmdlet. Before each call the cmdlet will prompt for confirmation. To bypass confirmation add the -Force parameter.**

```
$arn1 = "arn:aws:s3:::amzn-s3-demo-bucket"
$arn2 = "arn:aws:dynamodb:us-west-2:123456789012:table/mytable"

$arn1,$arn2 | Remove-RGTResourceTag -TagKey "stage","version"
```
+  For API details, see [UntagResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
