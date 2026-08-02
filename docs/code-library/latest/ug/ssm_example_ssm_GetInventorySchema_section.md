---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_GetInventorySchema_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetInventorySchema` with a CLI
<a name="ssm_example_ssm_GetInventorySchema_section"></a>

The following code examples show how to use `GetInventorySchema`.

------
#### [ CLI ]

**AWS CLI**
**To view your inventory schema**
This example returns a list of inventory type names for the account.
Command:

```
aws ssm get-inventory-schema
```
Output:

```
{
  "Schemas": [
      {
          "TypeName": "AWS:AWSComponent",
          "Version": "1.0",
          "Attributes": [
              {
                  "Name": "Name",
                  "DataType": "STRING"
              },
              {
                  "Name": "ApplicationType",
                  "DataType": "STRING"
              },
              {
                  "Name": "Publisher",
                  "DataType": "STRING"
              },
              {
                  "Name": "Version",
                  "DataType": "STRING"
              },
              {
                  "Name": "InstalledTime",
                  "DataType": "STRING"
              },
              {
                  "Name": "Architecture",
                  "DataType": "STRING"
              },
              {
                  "Name": "URL",
                  "DataType": "STRING"
              }
          ]
      },
      ...
  ],
  "NextToken": "--token string truncated--"
}
```
**To view the inventory schema for a specific inventory type**
This example return the inventory schema for a the AWS:AWSComponent inventory type.
Command:

```
aws ssm get-inventory-schema --type-name {{"AWS:AWSComponent"}}
```
+  For API details, see [GetInventorySchema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory-schema.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example returns a list of inventory type names for the account.**

```
Get-SSMInventorySchema
```
+  For API details, see [GetInventorySchema](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example returns a list of inventory type names for the account.**

```
Get-SSMInventorySchema
```
+  For API details, see [GetInventorySchema](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
