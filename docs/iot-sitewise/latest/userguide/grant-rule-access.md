---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/grant-rule-access.html
---

# Grant AWS IoT the required access
<a name="grant-rule-access"></a>

You use IAM roles to control the AWS resources to which each rule has access. Before you create a rule, you must create an IAM role with a policy that allows the rule to perform actions on the required AWS resource. AWS IoT assumes this role when running a rule.

If you create the rule action in the AWS IoT console, you can choose a root asset to create a role that has access to a selected asset hierarchy. For more information about how to manually define a role for a rule, see [Granting AWS IoT the required access](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-role.html) and [Pass role permissions](https://docs.aws.amazon.com/iot/latest/developerguide/pass-role.html) in the *AWS IoT Developer Guide*.

For the AWS IoT SiteWise rule action, you must define a role that allows `iotsitewise:BatchPutAssetPropertyValue` access to the asset properties to which the rule sends data. To improve security, you can specify an AWS IoT SiteWise asset hierarchy path in the `Condition` property.

The following example trust policy allows access to a specific asset and its children.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iotsitewise:BatchPutAssetPropertyValue",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "iotsitewise:assetHierarchyPath": [
            "/{{root node asset ID}}",
            "/{{root node asset ID}}/*"
          ]
        }
      }
    }
  ]
}
```

------

Remove the `Condition` from the policy to allow access to all of your assets. The following example trust policy allows access to all of your assets in the current Region.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iotsitewise:BatchPutAssetPropertyValue",
      "Resource": "*"
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
