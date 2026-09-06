---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/security_iam_id-based-policy-examples.html
---

# Amazon EC2 Auto Scaling identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, a brand new user in your AWS account has no permissions to do anything. An IAM administrator must create and assign IAM policies that give an IAM identity (such as a user or role) permission to perform Amazon EC2 Auto Scaling API actions.

To learn how to create an IAM policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

The following shows an example of a permissions policy.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": [
          "autoscaling:CreateAutoScalingGroup",
          "autoscaling:UpdateAutoScalingGroup",
          "autoscaling:DeleteAutoScalingGroup"
      ],
      "Resource": "*",
      "Condition": {
          "StringEquals": { "autoscaling:ResourceTag/{{purpose}}": "{{testing}}" }
      }
   },
   {
      "Effect": "Allow",
      "Action": "autoscaling:Describe*",
      "Resource": "*"
   }]
}
```

------

This sample policy grants permissions to create, update, and delete Auto Scaling groups, but only if the group uses the tag `purpose=testing`. Because `Describe` actions do not support resource-level permissions, you must specify them in a separate statement without conditions. To launch instances with a launch template, the user must also have the `ec2:RunInstances` permission. For more information, see [Control Amazon EC2 launch template usage in Auto Scaling groups](ec2-auto-scaling-launch-template-permissions.md).

**Note**
You can create your own custom IAM policies to allow or deny permissions for IAM identities (users or roles) to perform Amazon EC2 Auto Scaling actions. You can attach these custom policies to the IAM identities that require the specified permissions. The following examples show permissions for some common use cases.
Some Amazon EC2 Auto Scaling API actions allow you to include specific Auto Scaling groups in your policy that can be created or modified by the action. You can restrict the target resources for these actions by specifying individual Auto Scaling group ARNs. As a best practice, however, we recommend that you use tag-based policies that allow (or deny) actions on Auto Scaling groups with a specific tag.

**Topics**
+ [Control the size of the Auto Scaling groups that can be created](#policy-example-min-max-size)
+ [Control which tag keys and tag values can be used](#policy-example-tags)
+ [Control which Auto Scaling groups can be deleted](#policy-example-delete-auto-scaling-group)
+ [Control which scaling policies can be deleted](#policy-example-delete-policy)
+ [Control access to instance refresh actions](#policy-example-instance-refresh-policy)
+ [Create a service-linked role](#ec2-auto-scaling-slr-permissions)
+ [Control which service-linked role can be passed (using PassRole)](#policy-example-pass-role)

## Control the size of the Auto Scaling groups that can be created
<a name="policy-example-min-max-size"></a>

The following policy grants permissions to create and update all Auto Scaling groups with the tag `environment=development`, as long as the requester doesn't specify a minimum size less than **1** or a maximum size greater than **10**. Whenever possible, use tags to help you control access to the Auto Scaling groups in your account.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": [
          "autoscaling:CreateAutoScalingGroup",
          "autoscaling:UpdateAutoScalingGroup"
      ],
      "Resource": "*",
      "Condition": {
          "StringEquals": { "autoscaling:ResourceTag/{{environment}}": "{{development}}" },
          "NumericGreaterThanEqualsIfExists": { "autoscaling:MinSize": {{1}} },
          "NumericLessThanEqualsIfExists": { "autoscaling:MaxSize": {{10}} }
      }
   }]
}
```

------

Alternatively, if you are not using tags to control access to Auto Scaling groups, you can use ARNs to identify the Auto Scaling groups that the IAM policy applies to.

An Auto Scaling group has the following ARN.

```
"Resource": "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:*:autoScalingGroupName/{{my-asg}}"
```

You can also specify multiple ARNs by enclosing them in a list. For more information about specifying the ARNs of Amazon EC2 Auto Scaling resources in the `Resource` element, see [Policy resources for Amazon EC2 Auto Scaling](control-access-using-iam.md#security_iam_service-with-iam-id-based-policies-resources).

## Control which tag keys and tag values can be used
<a name="policy-example-tags"></a>

You can also use conditions in your IAM policies to control the tag keys and tag values that can be applied to Auto Scaling groups. To grant permissions to create or tag an Auto Scaling group only if the requester specifies certain tags, use the `aws:RequestTag` condition key. To allow only specific tag keys, use the `aws:TagKeys` condition key with the `ForAllValues` modifier.

The following policy requires the requester to specify a tag with the key `environment` in the request. The `"?*"` value enforces that there is some value for the tag key. To use a wildcard, you must use the `StringLike` condition operator.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": [
          "autoscaling:CreateAutoScalingGroup",
          "autoscaling:CreateOrUpdateTags"
      ],
      "Resource": "*",
      "Condition": {
          "StringLike": { "aws:RequestTag/{{environment}}": "{{?*}}" }
      }
   }]
}
```

------

The following policy specifies that the requester can only tag Auto Scaling groups with the tags `purpose=webserver` and `cost-center=cc123`, and allows only the `purpose` and `cost-center` tags (no other tags can be specified).

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": [
          "autoscaling:CreateAutoScalingGroup",
          "autoscaling:CreateOrUpdateTags"
      ],
      "Resource": "*",
      "Condition": {
          "StringEquals": {
              "aws:RequestTag/{{purpose}}": "{{webserver}}",
              "aws:RequestTag/{{cost-center}}": "{{cc123}}"
          },
          "ForAllValues:StringEquals": { "aws:TagKeys": ["{{purpose}}", "{{cost-center}}"] }
      }
   }]
}
```

------

The following policy requires the requester to specify at least one tag in the request, and allows only the `cost-center` and `owner` keys.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": [
          "autoscaling:CreateAutoScalingGroup",
          "autoscaling:CreateOrUpdateTags"
      ],
      "Resource": "*",
      "Condition": {
          "ForAnyValue:StringEquals": { "aws:TagKeys": ["{{cost-center}}", "{{owner}}"] }
      }
   }]
}
```

------

**Note**
For conditions, the condition key is not case-sensitive and the condition value is case-sensitive. Therefore, to enforce the case-sensitivity of a tag key, use the `aws:TagKeys` condition key, where the tag key is specified as a value in the condition.

## Control which Auto Scaling groups can be deleted
<a name="policy-example-delete-auto-scaling-group"></a>

The following policy allows deletion of an Auto Scaling group only if the group has the tag `environment=development`.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": "autoscaling:DeleteAutoScalingGroup",
      "Resource": "*",
      "Condition": {
          "StringEquals": { "aws:ResourceTag/{{environment}}": "{{development}}" }
      }
   }]
}
```

------

The following policy uses the `autoscaling:ForceDelete` condition key to control access to the `DeleteAutoScalingGroup` API action. This can prevent certain users from using the force delete operation, which terminates all instances within an Auto Scaling group when deleting the group.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [{
        "Effect": "Deny",
        "Action": "autoscaling:DeleteAutoScalingGroup",
        "Resource": "*",
        "Condition": {
            "Bool": {
                "autoscaling:ForceDelete": "true"
            }
        }
    }]
}
```

------

Alternatively, if you are not using condition keys to control access to Auto Scaling groups, you can specify the ARNs of resources in the `Resource` element to control access instead.

The following policy gives users permissions to use the `DeleteAutoScalingGroup` API action, but only for Auto Scaling groups whose name begins with `devteam-`.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "autoscaling:DeleteAutoScalingGroup",
            "Resource": "arn:aws:autoscaling:{{us-east-1}}:{{111122223333}}:autoScalingGroup:*:autoScalingGroupName/{{devteam-}}*"
        }
    ]
}
```

------

You can also specify multiple ARNs by enclosing them in a list. Including the UUID ensures that access is granted to the specific Auto Scaling group. The UUID for a new group is different than the UUID for a deleted group with the same name.

```
"Resource": [
    "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{devteam-1}}",
    "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{devteam-2}}",
    "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{devteam-3}}"
]
```

## Control which scaling policies can be deleted
<a name="policy-example-delete-policy"></a>

The following policy grants permissions to use the `DeletePolicy` action to delete a scaling policy. However, it also denies the action if the Auto Scaling group being acted upon has the tag `environment=production`. Whenever possible, use tags to help you control access to the Auto Scaling groups in your account.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": "autoscaling:DeletePolicy",
      "Resource": "*"
   },
   {
      "Effect": "Deny",
      "Action": "autoscaling:DeletePolicy",
      "Resource": "*",
      "Condition": {
          "StringEquals": { "autoscaling:ResourceTag/{{environment}}": "{{production}}" }
      }
   }]
}
```

------

## Control access to instance refresh actions
<a name="policy-example-instance-refresh-policy"></a>

The following policy grants permission to start, roll back, and cancel an instance refresh only if the Auto Scaling group being acted upon has the tag `environment=testing`. Because `Describe` actions do not support resource-level permissions, you must specify them in a separate statement without conditions.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": [
          "autoscaling:StartInstanceRefresh",
          "autoscaling:CancelInstanceRefresh",
          "autoscaling:RollbackInstanceRefresh"
      ],
      "Resource": "*",
      "Condition": {
          "StringEquals": { "autoscaling:ResourceTag/{{environment}}": "{{testing}}" }
      }
   },
   {
      "Effect": "Allow",
      "Action": "autoscaling:DescribeInstanceRefreshes",
      "Resource": "*"
   }]
}
```

------

To specify a desired configuration in the `StartInstanceRefresh` call, users might need some related permissions, such as:
+ **ec2:RunInstances** – To launch EC2 instances using a launch template, the user must have the `ec2:RunInstances` permission in an IAM policy. For more information, see [Control Amazon EC2 launch template usage in Auto Scaling groups](ec2-auto-scaling-launch-template-permissions.md).
+ **ec2:CreateTags** – To launch EC2 instances from a launch template that adds tags to the instances and volumes on creation, the user must have the `ec2:CreateTags` permission in an IAM policy. For more information, see [Permissions required to tag instances and volumes](ec2-auto-scaling-launch-template-permissions.md#policy-example-launch-template-createtags).
+ **iam:PassRole** – To launch EC2 instances from a launch template that contains an instance profile (a container for an IAM role), the user must also have the `iam:PassRole` permission in an IAM policy. For more information and an example IAM policy, see [IAM role for applications that run on Amazon EC2 instances](us-iam-role.md).
+ **ssm:GetParameters** – To launch EC2 instances from a launch template that uses an AWS Systems Manager parameter, the user must also have the `ssm:GetParameters` permission in an IAM policy. For more information, see [Use AWS Systems Manager parameters instead of AMI IDs in launch templates](using-systems-manager-parameters.md).

## Create a service-linked role
<a name="ec2-auto-scaling-slr-permissions"></a>

Amazon EC2 Auto Scaling requires permissions to create a service-linked role the first time that any user in your AWS account calls Amazon EC2 Auto Scaling API actions. If the service-linked role does not exist already, Amazon EC2 Auto Scaling creates it in your account. The service-linked role gives permissions to Amazon EC2 Auto Scaling so that it can call other AWS services on your behalf.

For automatic role creation to succeed, users must have permissions for the `iam:CreateServiceLinkedRole` action.

```
"Action": "iam:CreateServiceLinkedRole"
```

The following shows an example of a permissions policy that allows a user to create an Amazon EC2 Auto Scaling service-linked role for Amazon EC2 Auto Scaling.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/autoscaling.amazonaws.com/{{AWSServiceRoleForAutoScaling}}",
      "Condition": {
          "StringLike": { "iam:AWSServiceName":"{{autoscaling.amazonaws.com}}" }
      }
   }]
}
```

------

## Control which service-linked role can be passed (using PassRole)
<a name="policy-example-pass-role"></a>

Users who create or update Auto Scaling groups and specify a custom suffix service-linked role in the request require the `iam:PassRole` permission.

You can use the `iam:PassRole` permission to protect the security of your AWS KMS customer managed keys if you give different service-linked roles access to different keys. Depending on your organization's needs, you might have a key for the development team, another for the QA team, and another for the finance team. First, create a service-linked role that has access to the required key, for example, a service-linked role named **AWSServiceRoleForAutoScaling\_devteamkeyaccess**. Then, attach the policy to an IAM identity, such as a user or role.

The following policy grants permissions to pass the ****AWSServiceRoleForAutoScaling\_devteamkeyaccess**** role to any Auto Scaling group whose name begins with `devteam-`. If the IAM identity that creates the Auto Scaling group tries to specify a different service-linked role, they receive an error. If they choose not to specify a service-linked role, the default **AWSServiceRoleForAutoScaling** role is used instead.

For more information about custom suffix service-linked roles, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md).
