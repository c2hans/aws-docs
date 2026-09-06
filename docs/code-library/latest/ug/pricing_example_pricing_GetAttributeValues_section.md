---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/pricing_example_pricing_GetAttributeValues_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetAttributeValues` with a CLI
<a name="pricing_example_pricing_GetAttributeValues_section"></a>

The following code examples show how to use `GetAttributeValues`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve a list of attribute values**
The following `get-attribute-values` example retrieves a list of values available for the given attribute.

```
aws pricing get-attribute-values \
    --service-code {{AmazonEC2}} \
    --attribute-name {{volumeType}} \
    --max-items {{2}}
```
Output:

```
{
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==",
    "AttributeValues": [
        {
            "Value": "Cold HDD"
        },
        {
            "Value": "General Purpose"
        }
    ]
}
```
+  For API details, see [GetAttributeValues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/get-attribute-values.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the values for the attribute 'volumeType' for Amazon EC2 in the us-east-1 region.**

```
Get-PLSAttributeValue -ServiceCode AmazonEC2 -AttributeName "volumeType" -region us-east-1
```
**Output:**

```
Value
-----
Cold HDD
General Purpose
Magnetic
Provisioned IOPS
Throughput Optimized HDD
```
+  For API details, see [GetAttributeValues](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the values for the attribute 'volumeType' for Amazon EC2 in the us-east-1 region.**

```
Get-PLSAttributeValue -ServiceCode AmazonEC2 -AttributeName "volumeType" -region us-east-1
```
**Output:**

```
Value
-----
Cold HDD
General Purpose
Magnetic
Provisioned IOPS
Throughput Optimized HDD
```
+  For API details, see [GetAttributeValues](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
