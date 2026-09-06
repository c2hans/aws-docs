---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/ad-setup.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Active Directory setup
<a name="ad-setup"></a>

The application that you use for the test deployment can use Microsoft Active Directory authentication against its dependencies, such as a Microsoft SQL Server database that is joined into an Active Directory domain.

Note that this allows authentication of the application in the test deployment. It does not provide single sign-on for the incoming on-premises user connections with Windows Authentication tokens in HTTP headers.

For more information, see [Join an Amazon EC2 instance to your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_join_instance.html) in the *AWS Directory Service Administration Guide*.

**Topics**
+ [Create a directory](#ad-directory)
+ [Create a user](#ad-user)
+ [Create a secret](#ad-secret)
+ [Allow the task role to read the secret](#ad-task-role)

## Create a directory
<a name="ad-directory"></a>

Create a directory in the Directory Service using the same VPC that you will use for test deployment. If you use Active Directory, you must use the **Select an Amazon VPC** option when you create the test deployment. For more information, see [Create your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html) in the *AWS Directory Service Administration Guide*.

Verify that the directory meets the following requirements:
+ The inbound rules of the security group used by your directory must allow incoming connections from the same VPC. For more information, see [Understand your directory’s AWS security group configuration](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_best_practices.html#understandsecuritygroup) in the *AWS Directory Service Administration Guide*.
+ The VPC must have a DHCP options set that lists both of the IP addresses of the directory as DNS servers. For more information, see [Create a DHCP options set](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_best_practices.html#bp_create_dhcp_options_set) in the *AWS Directory Service Administration Guide*.

## Create a user
<a name="ad-user"></a>

Create a user in the directory. Remember the sign-in credentials.

## Create a secret
<a name="ad-secret"></a>

Create a secret to pass the username and password to your application. Create the secret with the user credentials in the AWS Secrets Manager before you run the test deployment on AWS. The user credentials must contain the following fields:
+ `Username` – The domain in the `Username` value must be uppercase: `{{user}}@{{AD_DOMAIN}}`
+ `Password`

You can also use the AWS Secrets Manager in the AWS Management Console to create the secret. Create a secret and add values in the following way:

```
Key: Username, value: {{user}}@{{AD_DOMAIN}},
Key: Password, value: {{password}}
```

You can use the JSON format option in the secret as:

```
{
    "Username": "{{user}}@{{AD_DOMAIN}}",
    "Password": "{{password}}"
}
```

You can also use the AWS CLI to create the secret. For more information, see [create-secret](https://awscli.amazonaws.com/v2/documentation/api/2.0.33/reference/secretsmanager/create-secret.html) in the *AWS CLI Command Reference*.

If you use AWS CLI, use the `--secret-string` parameter as follows:

```
‘{"Username":"{{user}}@{{AD_DOMAIN.COM}}","Password":"{{password}}"}’
```

The single quotes that enclose the JSON value allow you to pass the double quotes unchanged.

Remember the ARN of the secret for later use.

## Allow the task role to read the secret
<a name="ad-task-role"></a>

In the AWS Secrets Manager in the AWS Management Console, open the secret that you created and select the **Resource permissions** tab in the information page of the secret.

Add the policy below to the secret. The policy contains the following ARNs:
+ The ARN of the [Amazon ECS task role](roles-and-policies.md#ecs-task-role) that you created with the CloudFormation template.
+ The ARN of the secret that you just created.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement" : [
    {
        "Effect": "Allow",
        "Principal": {
            "AWS": "arn:aws:iam::{{123456789012}}:role/{{my-ecs-task-role}}"
        },
        "Action": "secretsmanager:GetSecretValue",
        "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{my-secret}}-{{XyZ9Qw}}"
    }
  ]
}
```

------
