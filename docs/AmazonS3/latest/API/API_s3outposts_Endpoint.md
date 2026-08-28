---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_Endpoint.html
---

# Endpoint
<a name="API_s3outposts_Endpoint"></a>

Amazon S3 on Outposts Access Points simplify managing data access at scale for shared datasets in S3 on Outposts. S3 on Outposts uses endpoints to connect to AWS Outposts buckets so that you can perform actions within your virtual private cloud (VPC). For more information, see [ Accessing S3 on Outposts using VPC-only access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WorkingWithS3Outposts.html) in the *Amazon Simple Storage Service User Guide*.

## Contents
<a name="API_s3outposts_Endpoint_Contents"></a>

 ** AccessType **   <a name="AmazonS3-Type-s3outposts_Endpoint-AccessType"></a>
The type of connectivity used to access the Amazon S3 on Outposts endpoint.
Type: String
Valid Values: `Private | CustomerOwnedIp`
Required: No

 ** CidrBlock **   <a name="AmazonS3-Type-s3outposts_Endpoint-CidrBlock"></a>
The VPC CIDR committed by this endpoint.
Type: String
Required: No

 ** CreationTime **   <a name="AmazonS3-Type-s3outposts_Endpoint-CreationTime"></a>
The time the endpoint was created.
Type: Timestamp
Required: No

 ** CustomerOwnedIpv4Pool **   <a name="AmazonS3-Type-s3outposts_Endpoint-CustomerOwnedIpv4Pool"></a>
The ID of the customer-owned IPv4 address pool used for the endpoint.
Type: String
Pattern: `^ipv4pool-coip-([0-9a-f]{17})$`
Required: No

 ** EndpointArn **   <a name="AmazonS3-Type-s3outposts_Endpoint-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)/endpoint/[a-zA-Z0-9]{19}$`
Required: No

 ** FailedReason **   <a name="AmazonS3-Type-s3outposts_Endpoint-FailedReason"></a>
The failure reason, if any, for a create or delete endpoint operation.
Type: [FailedReason](API_s3outposts_FailedReason.md) object
Required: No

 ** NetworkInterfaces **   <a name="AmazonS3-Type-s3outposts_Endpoint-NetworkInterfaces"></a>
The network interface of the endpoint.
Type: Array of [NetworkInterface](API_s3outposts_NetworkInterface.md) objects
Required: No

 ** OutpostsId **   <a name="AmazonS3-Type-s3outposts_Endpoint-OutpostsId"></a>
The ID of the AWS Outposts.
Type: String
Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`
Required: No

 ** SecurityGroupId **   <a name="AmazonS3-Type-s3outposts_Endpoint-SecurityGroupId"></a>
The ID of the security group used for the endpoint.
Type: String
Pattern: `^sg-([0-9a-f]{8}|[0-9a-f]{17})$`
Required: No

 ** Status **   <a name="AmazonS3-Type-s3outposts_Endpoint-Status"></a>
The status of the endpoint.
Type: String
Valid Values: `Pending | Available | Deleting | Create_Failed | Delete_Failed`
Required: No

 ** SubnetId **   <a name="AmazonS3-Type-s3outposts_Endpoint-SubnetId"></a>
The ID of the subnet used for the endpoint.
Type: String
Pattern: `^subnet-([0-9a-f]{8}|[0-9a-f]{17})$`
Required: No

 ** VpcId **   <a name="AmazonS3-Type-s3outposts_Endpoint-VpcId"></a>
The ID of the VPC used for the endpoint.
Type: String
Required: No

## See Also
<a name="API_s3outposts_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/Endpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
