---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_wafv2_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS WAFV2 examples using Tools for PowerShell V5
<a name="powershell_5_wafv2_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with AWS WAFV2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `New-WAF2WebACL`
<a name="wafv2_CreateWebAcl_powershell_5_topic"></a>

The following code example shows how to use `New-WAF2WebACL`.

**Tools for PowerShell V5**
**Example 1: This command creates a new web ACL named "waf-test". Kindly note that as per service API documentation, 'DefaultAction' is a required property. Hence, value for either '-DefaultAction\_Allow' and/or '-DefaultAction\_Block' should be specified. Since '-DefaultAction\_Allow' and '-DefaultAction\_Block' are not the required properties, value '@{}' could be used as placeholder as shown in above example.**

```
New-WAF2WebACL -Name "waf-test" -Scope REGIONAL -Region eu-west-1 -VisibilityConfig_CloudWatchMetricsEnabled $true -VisibilityConfig_SampledRequestsEnabled $true -VisibilityConfig_MetricName "waf-test" -Description "Test" -DefaultAction_Allow @{}
```
**Output:**

```
ARN         : arn:aws:wafv2:eu-west-1:139480602983:regional/webacl/waf-test/19460b3f-db14-4b9a-8e23-a417e1eb007f
Description : Test
Id          : 19460b3f-db14-4b9a-8e23-a417e1eb007f
LockToken   : 5a0cd5eb-d911-4341-b313-b429e6d6b6ab
Name        : waf-test
```
+  For API details, see [CreateWebAcl](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
