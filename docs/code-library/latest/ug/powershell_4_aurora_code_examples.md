---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_aurora_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Aurora examples using Tools for PowerShell V4
<a name="powershell_4_aurora_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Aurora.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-RDSOrderableDBInstanceOption`
<a name="aurora_DescribeOrderableDBInstanceOptions_powershell_4_topic"></a>

The following code example shows how to use `Get-RDSOrderableDBInstanceOption`.

**Tools for PowerShell V4**
**Example 1: This example lists the DB engine versions that support a specific DB instance class in an AWS Region.**

```
$params = @{
  Engine = 'aurora-postgresql'
  DBInstanceClass = 'db.r5.large'
  Region = 'us-east-1'
}
Get-RDSOrderableDBInstanceOption @params
```
**Example 2: This example lists the DB instance classes that are supported for a specific DB engine version in an AWS Region.**

```
$params = @{
  Engine = 'aurora-postgresql'
  EngineVersion = '13.6'
  Region = 'us-east-1'
}
Get-RDSOrderableDBInstanceOption @params
```
+  For API details, see [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
