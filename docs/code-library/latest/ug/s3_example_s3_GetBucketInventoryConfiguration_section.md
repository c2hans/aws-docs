---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_GetBucketInventoryConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetBucketInventoryConfiguration` with a CLI
<a name="s3_example_s3_GetBucketInventoryConfiguration_section"></a>

The following code examples show how to use `GetBucketInventoryConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve the inventory configuration for a bucket**
The following `get-bucket-inventory-configuration` example retrieves the inventory configuration for the specified bucket with ID `1`.

```
aws s3api get-bucket-inventory-configuration \
    --bucket {{amzn-s3-demo-bucket}} \
    --id {{1}}
```
Output:

```
{
    "InventoryConfiguration": {
        "IsEnabled": true,
        "Destination": {
            "S3BucketDestination": {
                "Format": "ORC",
                "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket",
                "AccountId": "123456789012"
            }
        },
        "IncludedObjectVersions": "Current",
        "Id": "1",
        "Schedule": {
            "Frequency": "Weekly"
        }
    }
}
```
+  For API details, see [GetBucketInventoryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-inventory-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command returns the details of the inventory named 'testinventory' for the given S3 bucket.**

```
Get-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testinventory'
```
+  For API details, see [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command returns the details of the inventory named 'testinventory' for the given S3 bucket.**

```
Get-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testinventory'
```
+  For API details, see [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
