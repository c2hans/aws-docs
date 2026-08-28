---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/tagging.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Tagging your AWS IoT Greengrass resources
<a name="tagging"></a>

Tags can help you organize and manage your AWS IoT Greengrass groups. You can use tags to assign metadata to groups, bulk deployments, and the cores, devices, and other resources that are added to groups. Tags can also be used in IAM policies to define conditional access to your Greengrass resources.

**Note**
Currently, Greengrass resource tags are not supported for AWS IoT billing groups or cost allocation reports.

## Tag basics
<a name="tagging-basics"></a>

Tags allow you to categorize your AWS IoT Greengrass resources, for example, by purpose, owner, and environment. When you have many resources of the same type, you can quickly identify a resource based on the tags that are attached to it. A tag consists of a key and optional value, both of which you define. We recommend that you design a set of tag keys for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. For example, you can define a set of tags for your groups that helps you track the factory location of your core devices. For more information, see [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies).

### Tagging support in the AWS IoT console
<a name="tagging-support-console"></a>

You can create, view, and manage tags for your Greengrass `Group` resources in the AWS IoT console. Before you create tags, be aware of tagging restrictions. For more information, see [Tag naming and usage conventions](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*.

**To assign tags when you create a group**
You can assign tags to a group when you create the group. Choose **Add new tag** under the **Tags** section to show the tagging input fields.

**To view and manage tags from the group configuration page**
You can view and manage tags from the group configuration page by choosing **View settings**. In the **Tags** section for the group, choose **Manage tags** to add, edit, or remove group tags.

### Tagging support in the AWS IoT Greengrass API
<a name="tagging-support-api"></a>

You can use the AWS IoT Greengrass API to create, list, and manage tags for AWS IoT Greengrass resources that support tagging. Before you create tags, be aware of tagging restrictions. For more information, see [Tag naming and usage conventions](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*.
+ To add tags during resource creation, define them in the `tags` property of the resource.
+ To add tags after a resource is created, or to update tag values, use the `TagResource` action.
+ To remove tags from a resource, use the `UntagResource` action.
+ To retrieve the tags that are associated with a resource, use the `ListTagsForResource` action or get the resource and inspect its `tags` property.

The following table lists resources you can tag in the AWS IoT Greengrass API and their corresponding `Create` and `Get` actions.

| Resource | Create | Get |
| --- | --- | --- |
| Group | [`CreateGroup`](https://docs.aws.amazon.com/greengrass/v1/apireference/creategroup-post.html) | [`GetGroup`](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html) |
| ConnectorDefinition | [`CreateConnectorDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createconnectordefinition-post.html) | [`GetConnectorDefinition `](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectordefinition-get.html) |
| CoreDefinition | [`CreateCoreDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createcoredefinition-post.html) | [`GetCoreDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/getcoredefinition-get.html) |
| DeviceDefinition | [`CreateDeviceDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createdevicedefinition-post.html) | [`GetDeviceDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/getdevicedefinition-get.html) |
| FunctionDefinition | [`CreateFunctionDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createfunctiondefinition-post.html) | [`GetFunctionDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/getfunctiondefinition-get.html) |
| LoggerDefinition | [`CreateLoggerDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createloggerdefinition-post.html) | [`GetLoggerDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/getloggerdefinition-get.html) |
| ResourceDefinition | [`CreateResourceDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createresourcedefinition-post.html) | [`GetResourceDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/getresourcedefinition-get.html) |
| SubscriptionDefinition | [`CreateSubscriptionDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/createsubscriptiondefinition-post.html) | [`GetSubscriptionDefinition`](https://docs.aws.amazon.com/greengrass/v1/apireference/getsubscriptiondefinition-get.html) |
| BulkDeployment  | [`StartBulkDeployment`](https://docs.aws.amazon.com/greengrass/v1/apireference/startbulkdeployment-post.html) | [`GetBulkDeploymentStatus`](https://docs.aws.amazon.com/greengrass/v1/apireference/getbulkdeploymentstatus-get.html) |

Use the following actions to list and manage tags for resources that support tagging:
+ [`TagResource`](https://docs.aws.amazon.com/greengrass/v1/apireference/tagresource-post.html). Adds tags to a resource. Also used to change the value of the tag's key-value pair.
+ [`ListTagsForResource`](https://docs.aws.amazon.com/greengrass/v1/apireference/listtagsforresource-get.html). Lists the tags for a resource.
+ [`UntagResource`](https://docs.aws.amazon.com/greengrass/v1/apireference/untagresource-delete.html). Removes tags from a resource.

You can add or remove tags on a resource at any time. To change the value of a tag key, add a tag to the resource that defines the same key and the new value. The new value overwrites the old value. You can set a value to an empty string, but you can't set a value to null.

When you delete a resource, tags that are associated with the resource are also deleted.

**Note**
Don't confuse resource tags with the attributes that you can assign to AWS IoT things. Although Greengrass cores are AWS IoT things, the resource tags that are described in this topic are attached to a `CoreDefinition`, not the core thing.

## Using tags with IAM policies
<a name="tagging-iam-policies"></a>

In your IAM policies, you can use resource tags to control user access and permissions. For example, policies can allow users to create only those resources that have a specific tag. Policies can also restrict users from creating or modifying resources that have certain tags. You can tag resources during creation (called *tag on create*) so you don't have to run custom tagging scripts later. When new environments are launched with tags, the corresponding IAM permissions are applied automatically.

The following condition context keys and values can be used in the `Condition` element (also called the `Condition` block) of the policy.

`greengrass:ResourceTag/{{tag-key}}: {{tag-value}}`
Allow or deny user actions on resources with specific tags.

`aws:RequestTag/{{tag-key}}: {{tag-value}}`
Require that a specific tag be used (or not used) when making API requests to create or modify tags on a taggable resource.

`aws:TagKeys: [{{tag-key}}, ...]`
Require that a specific set of tag keys be used (or not used) when making an API request to create or modify a taggable resource.

Condition context keys and values can be used only on AWS IoT Greengrass actions that act on a taggable resource. These actions take the resource as a required parameter. For example, you can set conditional access on the `GetGroupVersion`. You can't set conditional access on `AssociateServiceRoleToAccount` because no taggable resource (for example, group, core definition, or device defintion) is referenced in the request.

For more information, see [Controlling access using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) and [IAM JSON policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*. The JSON policy reference includes detailed syntax, descriptions and examples of the elements, variables, and evaluation logic of JSON policies in IAM.

### Example IAM policies
<a name="tagging-iam-policies-examples"></a>

The following example policy applies tag-based permissions that constrain a beta user to actions on beta resources only.
+ The first statement allows an IAM user to act on resources that have the *env=beta* tag only.
+ The second statement prevents an IAM user from removing the *env=beta* tag from resources. This protects the user from removing their own access.
**Note**
If you use tags to control access to resources, you should also manage the permissions that allow users to add tags or remove tags from those same resources. Otherwise, in some cases, it might be possible for users to circumvent your restrictions and gain access to a resource by modifying its tags.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "greengrass:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/env": "beta"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": "greengrass:UntagResource",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/env": "beta"
                }
            }
        }
    ]
}
```

------

To allow users to tag on create, you must give them appropriate permissions. The following example policy includes the `"aws:RequestTag/env": "beta"` condition on the `greengrass:TagResource` and `greengrass:CreateGroup` actions, which allows users to create a group only if they tag the group with *env=beta*. This effectively forces users to tag new groups.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "greengrass:TagResource",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/env": "beta"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "greengrass:CreateGroup",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/env": "beta"
                }
            }
        }
    ]
}
```

------

The following snippet shows how you can specify multiple tag values for a tag key by enclosing them in a list:

```
"StringEquals" : {
    "greengrass:ResourceTag/env" : ["dev", "test"]
}
```

## See also
<a name="tagging-see-also"></a>
+ [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
