---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/permissions-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Permissions management
<a name="permissions-management"></a>

This section discusses the best practices for setting up commonly used IAM roles, policies, and guardrails for provisioning and operating the SageMaker AI Studio domain.

## IAM roles and policies
<a name="iam-roles-and-policies"></a>

 As a best practice, you may want to first identify the relevant people and applications, known as principals involved in the ML lifecycle, and what AWS permissions you need to grant them. As SageMaker AI is a managed service, you also need to consider service principals which are AWS services that can make API calls on a user’s behalf. The following diagram illustrates the different IAM roles you may want to create, corresponding to the different personas in the organization.

![A diagram depicting SageMaker AI IAM roles.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/sagemaker-iam-roles.png)

These roles are described in detail, along with some examples of specific IAMpermissions they will need.
+  **ML Admin user role** — This is a principal who provisions the environment for data scientists by creating studio domains and user profiles (`sagemaker:CreateDomain`, `sagemaker:CreateUserProfile`), creating AWS Key Management Service (AWS KMS) keys for users, creating S3 buckets for data scientists, and creating Amazon ECR repositories to house containers. They can also set default configurations and lifecycle scripts for users, build and attach custom images to the SageMaker AI Studio domain, and provide Service Catalog products such as custom projects, Amazon EMR templates.

   Because this principal will not run training jobs, for example, they don’t need permissions to launch SageMaker AI training or processing jobs. If they’re using infrastructure as code templates, such as CloudFormation or Terraform, to provision domains and users, this role would be assumed by the provisioning service to create the resources on the admin’s behalf. This role may have read-only access to SageMaker AI using the AWS Management Console.

   This user role will also need certain EC2 permissions to launch the domain inside a private VPC, KMS permissions to encrypt the EFS volume, as well as permissions to create a service linked role for Studio (`iam:CreateServiceLinkedRole`). We will describe those granular permissions later in the document.
+  **Data Scientist user role** — This principal is the user logging in to SageMaker AI Studio, exploring the data, creating processing and training jobs and pipelines, and so on. The primary permission the user needs is permission to launch SageMaker AI Studio, and the rest of the policies can be managed by the SageMaker AI execution service role.
+  **SageMaker AI execution service role** — Because SageMaker AI is a managed service, it launches jobs on a user’s behalf. This role is often the broadest in terms of the allowed permissions, because many customers choose to use a single execution role to run training jobs, processing jobs, or model hosting jobs. While this is an easy way to get started, because customers mature in their journey, they often split the notebook execution role into separate roles for different API actions, especially when running those jobs in deployed environments.

  You associate a role with the SageMaker AI Studio domain upon creation. However, as customers may require the flexibility of having different roles associated with the different user profiles in the domain (for example, based on their job function), you can also associate a separate IAM role with each user profile. We recommend that you map a single physical user to a single user profile. If you don’t attach a role to a user profile on creation, the default behavior is to associate the SageMaker AIStudio domain execution role with the user profile as well.

   In cases where multiple data scientists and ML engineers work together on a project and need a shared permission model for accessing resources, we recommend you create a team-level SageMaker AI service execution role for sharing the IAM permissions across your team members. In the instances where you need to lock down permissions at each user level, you can create an individual user-level SageMaker AI service execution role; however, you need to be mindful of your service limits.

## SageMaker AI Studio Notebook authorization workflow
<a name="sagemaker-studio-notebook-authorization-workflow"></a>

This section, discusses how SageMaker AI Studio Notebook authorization works for various activities that the Data Scientist needs to perform for building and training the model right from the SageMaker AI Studio Notebook. The SageMaker AI domain supports two authorization modes:
+ IAM federation
+ IAM Identity Center

Next, this paper walks you through the Data Scientist authorization workflow for each of those modes.

![A diagram depicting authentication and authorization workflow for Studio users.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/authentication-authorization-workflow.png)

### IAM Federation: SageMaker Studio Notebook workflows
<a name="iam-federation-studio-notebook-workflow"></a>

1. A Data Scientist authenticates into their corporate identity provider and assumes the Data Scientist user role (the user federation role) in the SageMaker AI console. This federation role has `iam:PassRole` API permission on the SageMaker AI execution role to pass the role Amazon Resource Name (ARN) to SageMaker Studio.

1. The Data Scientist selects the **Open Studio** link from their Studio IAM user profile that is associated with the SageMaker AI execution role

1. The SageMaker Studio IDE service is launched, assuming the user profile’s SageMaker execution role permissions. This role has `iam:PassRole` API permission on the SageMaker AI execution role to pass the role ARN to the SageMaker AI training service.

1. When Data Scientist launches the training job in the remote compute node(s), the SageMaker AI execution role ARN is passed to the SageMaker AI training service. This creates a new role session with this ARN and runs the training job. If you need to scope down the permission further for training job, you can create a training specific role and pass that role ARN when calling training API.

#### IAM Identity Center: SageMaker AI Studio Notebook workflow
<a name="idc-sagemaker-studio-notebook-sagemaker-workflow"></a>

1. The Data Scientist authenticates into their corporate identity provider and clicks on AWS IAM Identity Center. The Data Scientist is presented with Identity Center Portal for the user.

1. The Data Scientist clicks on the SageMaker AI Studio App link that was created from their IdC user profile, which is associated with the SageMaker AI execution role.

1. The SageMaker AI Studio IDE service is launched, assuming the user profile’s SageMaker AI execution role permissions. This role has `iam:PassRole` API permission on the SageMaker AI execution role to pass the role ARN to the SageMaker AI training service.

1. When the Data Scientist launches the training job in remote compute node(s), the SageMaker AI execution role ARN is passed to the SageMaker AI training service. The execution role ARN creates new role session with this ARN, and runs the training job. If you need to scope down the permission further for training jobs, you can create a training-specific role and pass that role ARN when calling the training API.

### Deployed environment: SageMaker AI training workflow
<a name="deployed-environment-sagemaker-training-workflow"></a>

In deployed environments such as system testing and production, jobs are run through automated scheduler and event triggers, and human access to those environments are restricted from SageMaker AI Studio Notebooks. This section discusses how IAM roles work with the SageMaker AI training pipeline in the deployed environment.

![A diagram depicting a SageMaker AI training workflow in a managed production environment.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/sagemaker-training-workflow-prod.png)

1. [Amazon EventBridge](https://aws.amazon.com/eventbridge/) scheduler triggers the SageMaker AI training pipeline job.

1. The SageMaker AI training pipeline job assumes the SageMaker AI training pipeline role to train the model.

1. The trained SageMaker AI model is registered into the SageMaker AI Model Registry.

1. An ML engineer assumes the ML engineer user role to manage the training pipeline and SageMaker AI model.

## Data permissions
<a name="data-permissions"></a>

The ability for SageMaker AI Studio users to access any data source is governed by the permissions associated with their SageMaker AI IAM execution role. The policies attached can authorize them to read, write or delete from certain Amazon S3 buckets or prefixes, and connect to Amazon RDS databases.

### Accessing AWS Lake Formation data
<a name="accessing-aws-lake-formation-data"></a>

Many enterprises have begun using data lakes governed by [AWS Lake Formation](https://aws.amazon.com/lake-formation/) to enable fine grained data access for their users. As an example of such governed data, administrators can mask sensitive columns for some users while still enabling queries of the same underlying table.

To utilize Lake Formation from SageMaker AI Studio, administrators can register SageMaker AI IAM execution roles as `DataLakePrincipals`. For more information, refer to [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html). Once authorized, there are three primary methods for accessing and writing governed data from SageMaker AI Studio:

1. From a SageMaker AI Studio Notebook, users can utilize query engines such as [Amazon Athena](https://aws.amazon.com/athena/) or libraries that build on top of boto3 to pull data directly to the notebook. The [AWS SDK for Pandas](https://github.com/aws/aws-sdk-pandas) (previously known as awswrangler) is a popular library. Following is a code example to show how seamless this can be:

   ```
   transaction_id = wr.lakeformation.start_transaction(read_only=True)
   df = wr.lakeformation.read_sql_query(
       sql=f"SELECT * FROM {table};",
       database=database,
       transaction_id=transaction_id
   )
   ```

1. Use the SageMaker AI Studio native connectivity to Amazon EMR to read and write data at scale. Through use of Apache Livy and Amazon EMR runtime roles, SageMaker AI Studio has built native connectivity which allows you to pass your SageMaker AI execution IAM role (or other authorized role) to an Amazon EMR cluster for data access and processing. Refer to [Connect to an Amazon EMR Cluster from Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-cluster-connect.html) for up-to-date instructions.
![A diagram depicting an architecture for accessing data managed by Lake Formation from SageMaker Studio.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/access-lf-data.png)

1. Use the SageMaker AI Studio native connectivity to [AWS Glue interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions.html) to read and write data at scale. SageMaker AI Studio Notebooks have built-in kernels that allow users to interactively run commands on [AWS Glue](https://aws.amazon.com/glue/). This enables the scalable use of Python, Spark, or Ray backends which can seamlessly read and write data at scale from governed data sources. The kernels allow users to pass their SageMaker execution or other authorized IAM roles. Refer to [Prepare Data using AWS Glue Interactive Sessions](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-glue.html) for more information.

## Common guardrails
<a name="common-guardrails"></a>

This section discusses the most commonly-used guardrails for applying governance on your ML resources using IAM policies, resource policies, VPC endpoint policies, and service control policies (SCPs).

### Limit notebook access to specific instances
<a name="limit-notebook-access-to-specific-instances"></a>

 This service control policy can be used to limit the instance types that data scientists have access to, while creating Studio notebooks. Note that any user will need the “system” instance allowed to create the default Jupyter Server app that hosts SageMaker AI Studio.

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "LimitInstanceTypesforNotebooks",
             "Effect": "Deny",
             "Action": [
                 "sagemaker:CreateApp"
             ],
             "Resource": "*",
             "Condition": {
                 "ForAnyValue:StringNotLike": {
                     "sagemaker:InstanceTypes": [
                         "ml.c5.large",
                         "ml.m5.large",
                         "ml.t3.medium",
                         "system"
                     ]
                 }
             }
         }
     ]
 }
```

------

### Limit non-compliant SageMaker AI Studio domains
<a name="limit-non-compliant-sagemaker-studio-domains"></a>

 For SageMaker AI Studio domains, the following service control policy may be used to enforce traffic to access customer resources so they do not go over the public internet, but rather through a customer’s VPC:

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {   "Sid": "LockDownStudioDomain",
             "Effect": "Deny",
             "Action": [
                 "sagemaker:CreateDomain"
             ],
             "Resource": "*",
             "Condition": {
                          "StringNotEquals": {"sagemaker:AppNetworkAccessType": "VpcOnly"
                 },
                 "Null": {
                         "sagemaker:VpcSubnets": "true",
                         "sagemaker:VpcSecurityGroupIds": "true"
                 }
             }
         }
     ]
 }
```

------

### Limit launching unauthorized SageMaker AI images
<a name="limit-launching-unauthorized-sagemaker-images"></a>

 The following policy prevents a user from launching an unauthorized SageMaker AI image within their domain:f

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Action": [
                 "sagemaker:CreateApp"
              ],
             "Effect": "Allow",
             "Resource": "*",
             "Condition": {
                 "ForAllValues:ArnNotLike": {
                     "sagemaker:ImageArns":
                         [
                         "arn:aws:sagemaker:*:*:image/{ImageName}"
                         ]
                 }
             }
         }
     ]
 }
```

------

### Launch notebooks only via SageMaker AI VPC endpoints
<a name="launch-notebooks-only-via-sagemaker-vpc-endpoints"></a>

 In addition to VPC endpoints for the SageMaker AI control plane, SageMaker AI supports VPC endpoints for users to connect to [SageMaker AI Studio notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-interface-endpoint.html) or [SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-interface-endpoint.html). If you have already set up a VPC endpoint for a SageMaker AI Studio/notebook instance, the following IAM condition key will only allow connections to SageMaker AI Studio notebooks if they are made via the SageMaker AI Studio VPC endpoint or via the SageMaker AI API endpoint.

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "EnableSageMakerStudioAccessviaVPCEndpoint",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:CreatePresignedDomainUrl",
                 "sagemaker:DescribeUserProfile"
             ],
             "Resource": "*",
             "Condition": {
                 "ForAnyValue:StringEquals": {
                     "aws:sourceVpce": [
                         "vpce-111bbccc",
                         "vpce-111bbddd"
                     ]
                 }
             }
         }
     ]
 }
```

------

### Limit SageMaker AI Studio notebook access to a limited IP range
<a name="limit-sagemaker-studio-notebook-access-to-a-limited-ip-range"></a>

 Corporations will often limit SageMaker AI Studio access to certain allowed corporate IP ranges. The following IAM policy with the `SourceIP` condition key can limit this.

------
#### [ JSON ]

****

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "EnableSageMakerStudioAccess",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:CreatePresignedDomainUrl",
                 "sagemaker:DescribeUserProfile"
             ],
             "Resource": "*",
             "Condition": {
                 "IpAddress": {
                     "aws:SourceIp": [
                         "192.0.2.0/24",
                         "203.0.113.0/24"
                     ]
                 }
             }
         }
     ]
 }
```

------

### Prevent SageMaker AI Studio users from accessing other user profiles
<a name="prevent-sagemaker-studio-users-from-accessing-other-user-profiles"></a>

As an administrator, when you create the user profile, ensure the profile is tagged with the SageMaker AI Studio user name with the tag key `studiouserid`. The principal (user or role attached to the user) should also have a tag with the key `studiouserid` (this tag can be named anything, and is not restricted to `studiouserid`)*.*

 Next, attach the following policy to the role the user will assume when launching SageMaker AI Studio.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AmazonSageMakerPresignedUrlPolicy",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePresignedDomainUrl"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sagemaker:ResourceTag/studiouserid": "${aws:PrincipalTag/studiouserid}"
                }
            }
        }
    ]
}
```

------

### Enforce tagging
<a name="enforce-tagging"></a>

 Data scientists need to use SageMaker AI Studio notebooks to explore data, and build and train models. Applying tags to notebooks helps with monitoring usage and controlling costs, as well as ensuring ownership and auditability.

 For SageMaker AI Studio apps, ensure the user profile is tagged. Tags are automatically propagated to apps from the user profile. To enforce user profile creation with tags (supported through CLI and SDK), consider adding this policy to the admin role:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceUserProfileTags",
            "Effect": "Allow",
            "Action": "sagemaker:CreateUserProfile",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:TagKeys": [
                        "studiouserid"
                    ]
                }
            }
        }
    ]
}
```

------

 For other resources, such as training jobs and processing jobs, you can make tags mandatory using the following policy:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceTagsForJobs",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateTrainingJob",
                "sagemaker:CreateProcessingJob"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:TagKeys": [
                        "studiouserid"
                    ]
                }
            }
        }
    ]
}
```

------

### Root access in SageMaker AI Studio
<a name="root-access-in-sagemaker-studio"></a>

 In SageMaker AI Studio, the notebook runs in a Docker container which, by default, does not have root access to the host instance. Similarly, other than the default run-as user, all other user ID ranges inside the container are re-mapped as non-privileged user-IDs on the host instance itself. As a result, the threat of privilege escalation is limited to the notebook container itself.

 When creating custom images, you might want to provide your user with non-root permissions for stricter controls; for example, avoiding running undesirable processes as root, or installing publicly-available packages. In such cases, you can create the image to run as a non-root user within the Dockerfile. Whether you create the user as root or non-root, you need to ensure that the UID/GID of the user is identical to the UID/GID in the [AppImageConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html) for the custom app, which creates the configuration for SageMaker AI to run an app using the custom image. For example, if your Dockerfile is built for a non-root user such as the following:

```
ARG NB_UID="1000"
ARG NB_GID="100"
...
USER $NB_UID
```

 The `AppImageConfig` file needs to mention the same UID and GID in its `KernelGatewayConfig`:

```
{
    "KernelGatewayImageConfig": {
        "FileSystemConfig": {
            "DefaultUid": 1000,
            "DefaultGid": 100
        }
    }
}
```

 The acceptable UID/GID values for custom images are 0/0 and 1000/100 for Studio images. For examples of building custom images and the associated `AppImageConfig` settings, refer to this [Github repository](https://github.com/aws-samples/sagemaker-studio-custom-image-samples).

 To avoid users tampering with this, do not grant the `CreateAppImageConfig`, `UpdateAppImageConfig`, or `DeleteAppImageConfig` permissions to SageMaker AI Studio notebook users.
