---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-target.html
---

# Viewing valid CEV upgrade targets for RDS Custom for Oracle DB instances
<a name="custom-upgrading-target"></a>

**Note**
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

You can see existing CEVs on the **Custom engine versions** page in the AWS Management Console.

You can also use the [describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html) AWS CLI command to find valid CEVs to use when you upgrade your DB instances, as shown in the following example. This example assumes that you created a DB instance using the engine version `19.my_cev1`, and that the upgrade versions `19.my_cev2` and `19.my_cev` exist.

```
aws rds describe-db-engine-versions --engine custom-oracle-ee --engine-version 19.my_cev1
```

The output resembles the following. The `ImageId` field shows the AMI ID.

```
{
    "DBEngineVersions": [
        {
            "Engine": "custom-oracle-ee",
            "EngineVersion": "19.my_cev1",
            ...
            "Image": {
                "ImageId": "ami-2345",
                "Status": "active"
            },
            "DBEngineVersionArn": "arn:aws:rds:us-west-2:123456789012:cev:custom-oracle-ee/19.my_cev1/12a34b5c-67d8-90e1-2f34-gh56ijk78lm9"
            "ValidUpgradeTarget": [
                {
                    "Engine": "custom-oracle-ee",
                    "EngineVersion": "19.my_cev2",
                    "Description": "19.my_cev2 description",
                    "AutoUpgrade": false,
                    "IsMajorVersionUpgrade": false
                },
                {
                    "Engine": "custom-oracle-ee",
                    "EngineVersion": "19.my_cev3",
                    "Description": "19.my_cev3 description",
                    "AutoUpgrade": false,
                    "IsMajorVersionUpgrade": false
                }
            ]
            ...
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
