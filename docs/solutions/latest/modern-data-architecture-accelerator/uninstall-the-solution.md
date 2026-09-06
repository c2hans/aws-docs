---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

**Note**
Infrastructure resources that maintain data (for example, S3 buckets, RDS instances, DynamoDB tables) are configured with a `RETAIN` removal policy. Running `mdaa destroy` will not remove these resources, so your data is preserved.
However, some non-retained resources (for example, Security Groups) may depend on retained resources like RDS or OpenSearch instances. In these cases, the destroy can fail or take a long time to complete. To avoid this, delete the retained resources first before running `mdaa destroy`.

Follow these steps to uninstall the solution:

1. Run `mdaa destroy` using the same configuration file (`mdaa.yaml`) that was used for deployment. This tears down all remaining MDAA-managed stacks in the correct dependency order.

   ```
   mdaa destroy -c ./mdaa.yaml
   ```

1. Delete any retained data resources (for example, S3 buckets, RDS instances, DynamoDB tables, OpenSearch domains) that are no longer needed. These resources will have the organization name as a prefix.

## Additional notes
<a name="additional-notes"></a>

For more information on AWS CDK, refer to the [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/v2/guide/home.html).
