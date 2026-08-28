---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_Ec2Config.html
---

# Ec2Config
<a name="API_Ec2Config"></a>

The subnet and security groups that AWS DataSync uses to connect to one of your Amazon EFS file system's [mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html).

## Contents
<a name="API_Ec2Config_Contents"></a>

 ** SecurityGroupArns **   <a name="DataSync-Type-Ec2Config-SecurityGroupArns"></a>
Specifies the Amazon Resource Names (ARNs) of the security groups associated with an Amazon EFS file system's mount target.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`
Required: Yes

 ** SubnetArn **   <a name="DataSync-Type-Ec2Config-SubnetArn"></a>
Specifies the ARN of a subnet where DataSync creates the [network interfaces](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces) for managing traffic during your transfer.
The subnet must be located:
+ In the same virtual private cloud (VPC) as the Amazon EFS file system.
+ In the same Availability Zone as at least one mount target for the Amazon EFS file system.
You don't need to specify a subnet that includes a file system mount target.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/subnet-[a-f0-9]+$`
Required: Yes

## See Also
<a name="API_Ec2Config_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/Ec2Config)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/Ec2Config)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/Ec2Config)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
