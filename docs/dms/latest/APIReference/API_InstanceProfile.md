---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_InstanceProfile.html
---

# InstanceProfile
<a name="API_InstanceProfile"></a>

Provides information that defines an instance profile.

## Contents
<a name="API_InstanceProfile_Contents"></a>

 ** AvailabilityZone **   <a name="DMS-Type-InstanceProfile-AvailabilityZone"></a>
The Availability Zone where the instance profile runs.
Type: String
Required: No

 ** Description **   <a name="DMS-Type-InstanceProfile-Description"></a>
A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
Type: String
Required: No

 ** InstanceProfileArn **   <a name="DMS-Type-InstanceProfile-InstanceProfileArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the instance profile.
Type: String
Required: No

 ** InstanceProfileCreationTime **   <a name="DMS-Type-InstanceProfile-InstanceProfileCreationTime"></a>
The time the instance profile was created.
Type: Timestamp
Required: No

 ** InstanceProfileName **   <a name="DMS-Type-InstanceProfile-InstanceProfileName"></a>
The user-friendly name for the instance profile.
Type: String
Required: No

 ** KmsKeyArn **   <a name="DMS-Type-InstanceProfile-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile.
If you don't specify a value for the `KmsKeyArn` parameter, then AWS DMS uses an AWS owned encryption key to encrypt your resources.
Type: String
Required: No

 ** NetworkType **   <a name="DMS-Type-InstanceProfile-NetworkType"></a>
Specifies the network type for the instance profile. A value of `IPV4` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of `IPV6` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of `DUAL` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.
Type: String
Required: No

 ** PubliclyAccessible **   <a name="DMS-Type-InstanceProfile-PubliclyAccessible"></a>
Specifies the accessibility options for the instance profile. A value of `true` represents an instance profile with a public IP address. A value of `false` represents an instance profile with a private IP address. The default value is `true`.
Type: Boolean
Required: No

 ** SubnetGroupIdentifier **   <a name="DMS-Type-InstanceProfile-SubnetGroupIdentifier"></a>
The identifier of the subnet group that is associated with the instance profile.
Type: String
Required: No

 ** VpcSecurityGroups **   <a name="DMS-Type-InstanceProfile-VpcSecurityGroups"></a>
The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.
Type: Array of strings
Required: No

## See Also
<a name="API_InstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/InstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/InstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/InstanceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
