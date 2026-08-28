---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/provision-minimal-iam-policy.html
---

# Minimal IAM policy for installer to provision resources
<a name="provision-minimal-iam-policy"></a>

When you install the AWS IoT Greengrass Core software, you can provision required AWS resources, such as an AWS IoT thing and an IAM role for your device. You can also deploy local development tools to the device. The installer requires AWS credentials so that it can perform these actions in your AWS account. For more information, see [Install the AWS IoT Greengrass Core software](install-greengrass-core-v2.md).

The following example policy includes the minimum set of actions that the installer requires to provision these resources. These permissions are required if you specify the `--provision` argument for the installer. Replace {{account-id}} with your AWS account ID, and replace {{GreengrassV2TokenExchangeRole}} with the name of the token exchange role that you specify with the `--tes-role-name` [installer argument](configure-installer.md).

**Note**
The `DeployDevTools` policy statement is required only if you specify the `--deploy-dev-tools` argument for the installer.

------
#### [ Greengrass nucleus v2.5.0 and later ]

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "CreateTokenExchangeRole",
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:CreateRole",
                "iam:GetPolicy",
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::{{123456789012}}:role/{{GreengrassV2TokenExchangeRole}}",
                "arn:aws:iam::{{123456789012}}:policy/{{GreengrassV2TokenExchangeRole}}Access",
                "arn:aws:iam::aws:policy/{{GreengrassV2TokenExchangeRole}}Access"
            ]
        },
        {
            "Sid": "CreateIoTResources",
            "Effect": "Allow",
            "Action": [
                "iot:AddThingToThingGroup",
                "iot:AttachPolicy",
                "iot:AttachThingPrincipal",
                "iot:CreateKeysAndCertificate",
                "iot:CreatePolicy",
                "iot:CreateRoleAlias",
                "iot:CreateThing",
                "iot:CreateThingGroup",
                "iot:DescribeEndpoint",
                "iot:DescribeRoleAlias",
                "iot:DescribeThingGroup",
                "iot:GetPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DeployDevTools",
            "Effect": "Allow",
            "Action": [
                "greengrass:CreateDeployment",
                "iot:CancelJob",
                "iot:CreateJob",
                "iot:DeleteThingShadow",
                "iot:DescribeJob",
                "iot:DescribeThing",
                "iot:DescribeThingGroup",
                "iot:GetThingShadow",
                "iot:UpdateJob",
                "iot:UpdateThingShadow"
            ],
            "Resource": "*"
        }
    ]
}
```

------

------
#### [ Earlier than v2.5.0 ]

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "CreateTokenExchangeRole",
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:CreateRole",
                "iam:GetPolicy",
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": [
            "arn:aws:iam::{{123456789012}}:role/{{GreengrassV2TokenExchangeRole}}",
    "arn:aws:iam::{{123456789012}}:policy/{{GreengrassV2TokenExchangeRole}}Access",
                "arn:aws:iam::aws:policy/{{GreengrassV2TokenExchangeRole}}Access"
            ]
        },
        {
            "Sid": "CreateIoTResources",
            "Effect": "Allow",
            "Action": [
                "iot:AddThingToThingGroup",
                "iot:AttachPolicy",
                "iot:AttachThingPrincipal",
                "iot:CreateKeysAndCertificate",
                "iot:CreatePolicy",
                "iot:CreateRoleAlias",
                "iot:CreateThing",
                "iot:CreateThingGroup",
                "iot:DescribeEndpoint",
                "iot:DescribeRoleAlias",
                "iot:DescribeThingGroup",
                "iot:GetPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DeployDevTools",
            "Effect": "Allow",
            "Action": [
                "greengrass:CreateDeployment",
                "iot:CancelJob",
                "iot:CreateJob",
                "iot:DeleteThingShadow",
                "iot:DescribeJob",
                "iot:DescribeThing",
                "iot:DescribeThingGroup",
                "iot:GetThingShadow",
                "iot:UpdateJob",
                "iot:UpdateThingShadow"
            ],
            "Resource": "*"
        }
    ]
}
```

------

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
