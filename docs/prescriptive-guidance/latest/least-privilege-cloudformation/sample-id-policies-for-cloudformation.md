---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/sample-id-policies-for-cloudformation.html
---

# Sample identity-based policies for CloudFormation
<a name="sample-id-policies-for-cloudformation"></a>

This section contains sample identity-based policies that demonstrate how to grant and deny permissions for CloudFormation. You can use these sample policies to start designing your own policies that adhere to the principle of least privilege.

For a list of CloudFormation specific actions and conditions, see [Actions, resources, and condition keys for AWS CloudFormation](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudformation.html) and [AWS CloudFormation conditions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions). For a list of resource types to use with conditions, see [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html).

This section contains the following example policies:
+ [Allow view access](#sample-allow-view-access)
+ [Allow stack creation based on template](#sample-allow-stack-creation-based-on-template)
+ [Deny update or deletion of a stack](#sample-deny-stack-changes)

## Allow view access
<a name="sample-allow-view-access"></a>

View access is the least-privileged type of access to CloudFormation. This kind of policy might be appropriate for those IAM principals who want to view all of the CloudFormation stacks in the AWS account. The following sample policy grants permissions to view the details of any CloudFormation stack in the account.

```
{
    "Version":"2012-10-17",
    "Statement":[{
        "Effect":"Allow",
        "Action":[
            "cloudformation:DescribeStacks",
            "cloudformation:DescribeStackEvents",
            "cloudformation:DescribeStackResource",
            "cloudformation:DescribeStackResources"
        ],
        "Resource":"*"
    }]
}
```

## Allow stack creation based on template
<a name="sample-allow-stack-creation-based-on-template"></a>

The following sample policy allows IAM principals to create stacks by using only the CloudFormation templates that are stored in a specific Amazon Simple Storage Service (Amazon S3) bucket. The bucket name is `my-CFN-templates`. You can upload approved templates to this bucket. The `cloudformation:TemplateUrl` condition key in the policy prevents the IAM principal from using any other templates to create stacks.

|
|
| Important: Allow the IAM principal to have read-only access to this S3 bucket. This helps prevent the IAM principal from adding, removing, or modifying the approved templates. |
| --- |

```
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect" : "Allow",
      "Action" : [ "cloudformation:CreateStack"],
      "Resource" : "*",
      "Condition" : {
        "StringLike" : {
          "cloudformation:TemplateUrl" : "https:// my-CFN-templates.s3.amazonaws.com/*"
        }
      }
    }
  ]
}
```

## Deny update or deletion of a stack
<a name="sample-deny-stack-changes"></a>

To help protect specific CloudFormation stacks that provision business-critical AWS resources, you can restrict update and deletion actions for that specific stack. You can allow these actions for only a few specified IAM principals and deny them for any other IAM principal in the environment. The following policy statement denies permissions to update or delete a specific CloudFormation stack in a specific AWS Region and AWS account.

```
{
    "Version": "2012-10-17",
    "Statement":[{
        "Effect":"Deny",
        "Action":[
            "cloudformation:DeleteStack",
            "cloudformation:UpdateStack"
        ],
        "Resource":"arn:aws:cloudformation:us-east-1:123456789012:stack/MyProductionStack/<stack_ID>"
    }]
}
```

This policy statement denies permissions to update or delete the `MyProductionStack` CloudFormation stack, which is in the `us-east-1` AWS Region and in the `123456789012` AWS account. You can view the stack ID in the CloudFormation console. The following are some examples of how you could modify the `Resource` element of this statement for your use case:
+ You can add multiple CloudFormation stack IDs in the `Resource` element of this policy.
+ You can use `arn:aws:cloudformation:us-east-1:123456789012:stack/*` to prevent IAM principals from updating or deleting any stack that is in the `us-east-1` AWS Region and in the `123456789012` account.

An important step is deciding which policy should contain this statement. You could add this statement to the following policies:
+ **The identity-based policy attached to the IAM principal** – Putting the statement in this policy restricts the specific IAM principal from creating or deleting a specific CloudFormation stack.
+ **A permissions boundary attached to the IAM principal** – Putting the statement in this policy creates a permission guardrail. It restricts more than one IAM principal from creating or deleting a specific CloudFormation stack, but it doesn't restrict all principals in your environment.
+ **A SCP attached to an account, organizational unit, or organization** – Putting the statement in this policy creates a permission guardrail. It restricts all IAM principals in the target account, organizational unit, or organization from creating or deleting a specific CloudFormation stack.

  However, if you don't allow at least one IAM principal, a *privileged principal*, to update or delete the CloudFormation stack, then you will not be able to make any changes, when necessary, to the resources provisioned through this stack. A user or a development pipeline (recommended) can assume this privileged principal. If you want to deploy the restriction as an SCP, then we recommend the following policy statement instead.

  ```
  {
      "Version": "2012-10-17",
      "Statement":[{
          "Effect":"Deny",
          "Action":[
              "cloudformation:DeleteStack",
              "cloudformation:UpdateStack"
          ],
          "Resource":"arn:aws:cloudformation:us-east-1:123456789012:stack/MyProductionStack/<stack_ID>",
  	  "Condition": {
          	"ArnNotLike": {
            		"aws:PrincipalARN" : [<ARN of the allowed privilege IAM principal>  ]
          }
        }
      }]
  }
  ```

  In this statement, the `Condition` element defines the IAM principal that is excluded from the SCP. This statement denies any IAM principal permissions to update or delete CloudFormation stacks unless the ARN of the IAM principal matches the ARN in the `Condition` element. The `aws:PrincipalARN` condition key accepts a list, which means that you can exclude more than one IAM principal from the restrictions, as necessary for your environment. For a similar SCP that prevents modifications to CloudFormation resources, see [SCP-CLOUDFORMATION-1](https://aws-samples.github.io/aws-iam-permissions-guardrails/guardrails/scp-guardrails.html#scp-cloudformation-1) (GitHub).
