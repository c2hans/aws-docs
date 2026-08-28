---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/appendix.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix
<a name="appendix"></a>

 **IAM roles**

```
    "Effect": "Allow",

    "Action": [

    "cloudformation:CreateStack",

    "cloudformation:DescribeStacks",

    "cloudformation:DescribeStackEvents",

    "cloudformation:DescribeStackResource",

    "cloudformation:DescribeStackResources",

    "cloudformation:GetTemplateSummary",

    "cloudformation:ListStackResources",

    "cloudformation:GetTemplate",

    "cloudformation:ListChangeSets",

    "cloudformation:GetStackPolicy"

    ],

    },

    {

    "Effect": "Allow",

    "Action": [

    "iam:CreateRole",

    "iam:CreatePolicy",

    "iam:AttachRolePolicy",

    "iam:GetRole",

    "iam:PassRole",

    "iam:PutRolePolicy",

    "lambda:CreateFunction",

    "lambda:InvokeFunction",

    "lambda:GetFunctionConfiguration",

    "cloudformation:DescribeStackResource",

    "cloudformation:DescribeStackResources"

    ],
```

 The other roles remain in your AWS account:
+ ` arn:aws:iam::aws:policy/AmazonVPCCrossAccountNetworkInterfaceOperations `
+ ` arn:aws:iam::role/vmware-sddc-formation-4c517b6f-1e2-BasicLambdaRole-SD4OX7YN3MNU `
+ ` arn:aws:iam::role/vmware-sddc-formation-4c517b6f-1e2-RemoteRolePayer-169300WFK6EYA `
+ ` arn:aws:iam::aws:policy/AmazonVPCCrossAccountNetworkInterfaceOperations `

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
