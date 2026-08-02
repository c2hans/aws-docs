---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/using-systems-manager-parameters.html
---

# Use AWS Systems Manager parameters instead of AMI IDs in launch templates
<a name="using-systems-manager-parameters"></a>

This section shows you how to create a launch template that specifies an AWS Systems Manager parameter that references an Amazon Machine Image (AMI) ID. You can use a parameter stored in your same AWS account, a parameter shared from another AWS account, or a public parameter for a public AMI maintained by AWS.

With Systems Manager parameters, you can update your Auto Scaling groups to use new AMI IDs without needing to create new launch templates or new versions of launch templates each time an AMI ID changes. These IDs can change regularly, such as when an AMI is updated with the latest operating system or software updates.

You can create, update, or delete your own Systems Manager parameters using the [Parameter Store, a capability of AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html). You must create a Systems Manager parameter before you can use it in a launch template. To get started, create a parameter with the data type `aws:ec2:image`, and for its value, enter the ID of an AMI. The AMI ID has the form `ami-{{<identifier>}}`, for example, `ami-123example456`. The correct AMI ID depends on the instance type and AWS Region that you're launching your Auto Scaling group in.

For more information about creating a valid parameter for an AMI ID, see [Creating Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html).

## Create a launch template that specifies a parameter for the AMI
<a name="using-systems-manager-parameters-create-launch-template"></a>

To create a launch template that specifies a parameter for the AMI, use one of the following methods:

------
#### [ Console ]

**To create a launch template using an AWS Systems Manager parameter**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**, and then choose **Create launch template**.

1. For **Launch template name**, enter a descriptive name for the launch template.

1. Under **Application and OS Images (Amazon Machine Image)**, choose **Browse more AMIs**.

1. Choose the arrow button to the right of the search bar, and then choose **Specify custom value/Systems Manager parameter**.

1. In the **Specify custom value or Systems Manager parameter** dialog box, do the following:

   1. For **AMI ID or Systems Manager parameter string**, enter the Systems Manager parameter name using one of the following formats:

      To reference a public parameter:
      + **resolve:ssm:{{public-parameter}}**

      To reference a parameter stored in the same account:
      + **resolve:ssm:{{parameter-name}}**
      + **resolve:ssm:{{parameter-name}}:{{version-number}}**
      + **resolve:ssm:{{parameter-name}}:{{label}}**

      To reference a parameter shared from another AWS account:
      + **resolve:ssm:{{parameter-ARN}}**
      + **resolve:ssm:{{parameter-ARN}}:{{version-number}}**
      + **resolve:ssm:{{parameter-ARN}}:{{label}}**

   1. Choose **Save**.

1. Configure any other launch template settings as needed, and then choose **Create launch template**. For more information, see [Create a launch template for an Auto Scaling group](create-launch-template.md).

------
#### [ AWS CLI ]

To create a launch template that specifies a Systems Manager parameter, you can use one of the following example commands. Replace each {{user input placeholder}} with your own information.

**Example: Create a launch template that specifies an AWS-owned public parameter**
Use the following syntax: `resolve:ssm:{{public-parameter}}`, where `resolve:ssm` is the standard prefix and `{{public-parameter}}` is the path and name of the public parameter.

In this example, the launch template uses an AWS-provided public parameter to launch instances using the latest Amazon Linux 2 AMI in the AWS Region that is configured for your profile.

```
aws ec2 create-launch-template --launch-template-name {{my-template-for-auto-scaling}} --version-description {{version1}} \
  --launch-template-data file://config.json
```

Contents of `config.json`:

```
{
    "ImageId":"resolve:ssm:{{/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
    "InstanceType":"{{t2.micro}}"
}
```

The following is an example response.

```
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-089c023a30example",
        "LaunchTemplateName": "my-template-for-auto-scaling",
        "CreateTime": "2022-12-28T19:52:27.000Z",
        "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1
    }
}
```

**Example: Create a launch template that specifies a parameter stored in the same account**
Use the following syntax: `resolve:ssm:{{parameter-name}}`, where `resolve:ssm` is the standard prefix and `{{parameter-name}}` is the Systems Manager parameter name.

The following example creates a launch template that gets the AMI ID from an existing Systems Manager parameter named `{{golden-ami}}`.

```
aws ec2 create-launch-template --launch-template-name {{my-template-for-auto-scaling}} \
  --launch-template-data file://config.json
```

Contents of `config.json`:

```
{
    "ImageId":"resolve:ssm:{{golden-ami}}",
    "InstanceType":"{{t2.micro}}"
}
```

The default version of the parameter, if it is not specified, is the latest version.

The following example references a specific version of the {{`golden-ami`}} parameter. The example uses version {{`3`}} of the {{`golden-ami`}} parameter, but you can use any valid version number.

```
{
    "ImageId":"resolve:ssm:{{golden-ami:3}}",
    "InstanceType":"{{t2.micro}}"
}
```

The following similar example references the parameter label {{`prod`}} that maps to a specific version of the {{`golden-ami`}} parameter.

```
{
    "ImageId":"resolve:ssm:{{golden-ami:prod}}",
    "InstanceType":"{{t2.micro}}"
}
```

The following is example output.

```
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-068f72b724example",
        "LaunchTemplateName": "my-template-for-auto-scaling",
        "CreateTime": "2022-12-27T17:11:21.000Z",
        "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1
    }
}
```

**Example: Create a launch template that specifies a parameter shared from another AWS account**
Use the following syntax: `resolve:ssm:{{parameter-ARN}}`, where `resolve:ssm` is the standard prefix and `{{parameter-ARN}}` is the ARN of the Systems Manager parameter.

The following example creates a launch template that gets the AMI ID from an existing Systems Manager parameter with the ARN of `{{arn:aws:ssm:us-east-2:123456789012:parameter/MyParameter}}`.

```
aws ec2 create-launch-template --launch-template-name {{my-template-for-auto-scaling}} --version-description {{version1}} \
  --launch-template-data file://config.json
```

Contents of `config.json`:

```
{
    "ImageId":"resolve:ssm:{{arn:aws:ssm:us-east-2:123456789012:parameter/MyParameter}}",
    "InstanceType":"{{t2.micro}}"
}
```

The default version of the parameter, if it is not specified, is the latest version.

The following example references a specific version of the `{{MyParameter}}` parameter. The example uses version {{`3`}} of the `{{MyParameter}}` parameter, but you can use any valid version number.

```
{
    "ImageId":"resolve:ssm:{{arn:aws:ssm:us-east-2:123456789012:parameter/MyParameter:3}}",
    "InstanceType":"{{t2.micro}}"
}
```

The following similar example references the parameter label {{`prod`}} that maps to a specific version of the `{{MyParameter}}` parameter.

```
{
    "ImageId":"resolve:ssm:{{arn:aws:ssm:us-east-2:123456789012:parameter/MyParameter:prod}}",
    "InstanceType":"{{t2.micro}}"
}
```

The following is an example response.

```
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-00f93d4588example",
        "LaunchTemplateName": "my-template-for-auto-scaling",
        "CreateTime": "2024-01-08T12:43:21.000Z",
        "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1
    }
}
```

------

To specify a parameter from the Parameter Store in a launch template, you must have the `ssm:GetParameters` permission for the specified parameter. Anyone who uses the launch template also needs the `ssm:GetParameters` permission in order for the parameter value to be validated. For more information, see [Restricting access to Systems Manager parameters using IAM policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-access.html) in the *AWS Systems Manager User Guide*.

## Verify a launch template gets the correct AMI ID
<a name="using-systems-manager-parameters-verify-launch-template"></a>

Use the [describe-launch-template-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-template-versions.html) command and include the `--resolve-alias` option to resolve the parameter to the actual AMI ID.

```
aws ec2 describe-launch-template-versions --launch-template-name {{my-template-for-auto-scaling}} \
   --versions {{1}} --resolve-alias
```

The example returns the AMI ID for `ImageId`. When an instance is launched using this launch template, the AMI ID resolves to `ami-0ac394d6a3example`.

```
{
    "LaunchTemplateVersions": [
        {
            "LaunchTemplateId": "lt-089c023a30example",
            "LaunchTemplateName": "my-template-for-auto-scaling",
            "VersionNumber": 1,
            "CreateTime": "2022-12-28T19:52:27.000Z",
            "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
            "DefaultVersion": true,
            "LaunchTemplateData": {
                "ImageId": "ami-0ac394d6a3example",
                "InstanceType": "t2.micro",
            }
        }
    ]
}
```

## Related resources
<a name="using-systems-manager-parameters-related-resources"></a>

For more details about specifying a Systems Manager parameter in your launch template, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide*.

For more information about working with Systems Manager parameters, see the following reference materials in the Systems Manager documentation.
+ To create parameter versions and labels, see [Working with parameter versions](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-versions.html) and [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html).
+ For information about how to look up the AMI public parameters supported by Amazon EC2, see [Calling AMI public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ami.html).
+ For information about sharing parameters with other AWS accounts or through AWS Organizations, see [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html).
+ For information about monitoring whether your parameters are created successfully, see [Native parameter support for Amazon Machine Image IDs](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-ec2-aliases.html).

## Limitations
<a name="using-systems-manager-parameters-limitations"></a>

When working with Systems Manager parameters, note the following limitations:
+ Amazon EC2 Auto Scaling only supports specifying AMI IDs as parameters.
+ Creating or updating [mixed instances groups](ec2-auto-scaling-mixed-instances-groups.md) with [attribute-based instance type selection](create-mixed-instances-group-attribute-based-instance-type-selection.md) using a launch template that specifies a Systems Manager parameter is not supported.
+ If your Auto Scaling group uses a launch template that specifies a Systems Manager parameter, you will not be able to start an instance refresh with a desired configuration or using skip matching.
+ If your Auto Scaling group uses a launch template that specifies a Systems Manager parameter, warm pools are not supported.
+ On each call to create or update your Auto Scaling group, Amazon EC2 Auto Scaling will resolve the Systems Manager parameter in the launch template. If you are using advanced parameters or higher throughput limits, the frequent calls to the Parameter Store (that is, the `GetParameters` operation) can increase your costs for Systems Manager because charges are incurred per Parameter Store API interaction. For more information, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/).
