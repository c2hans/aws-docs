---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessEndpoint.html
---

# VerifiedAccessEndpoint
<a name="API_VerifiedAccessEndpoint"></a>

An AWS Verified Access endpoint specifies the application that AWS Verified Access provides access to. It must be attached to an AWS Verified Access group. An AWS Verified Access endpoint must also have an attached access policy before you attached it to a group.

## Contents
<a name="API_VerifiedAccessEndpoint_Contents"></a>

 ** applicationDomain **
The DNS name for users to reach your application.
Type: String
Required: No

 ** attachmentType **
The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
Type: String
Valid Values: `vpc`
Required: No

 ** cidrOptions **
The options for a CIDR endpoint.
Type: [VerifiedAccessEndpointCidrOptions](API_VerifiedAccessEndpointCidrOptions.md) object
Required: No

 ** creationTime **
The creation time.
Type: String
Required: No

 ** deletionTime **
The deletion time.
Type: String
Required: No

 ** description **
A description for the AWS Verified Access endpoint.
Type: String
Required: No

 ** deviceValidationDomain **
Returned if endpoint has a device trust provider attached.
Type: String
Required: No

 ** domainCertificateArn **
The ARN of a public TLS/SSL certificate imported into or created with ACM.
Type: String
Required: No

 ** endpointDomain **
A DNS name that is generated for the endpoint.
Type: String
Required: No

 ** endpointType **
The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
Type: String
Valid Values: `load-balancer | network-interface | rds | cidr`
Required: No

 ** lastUpdatedTime **
The last updated time.
Type: String
Required: No

 ** loadBalancerOptions **
The load balancer details if creating the AWS Verified Access endpoint as `load-balancer`type.
Type: [VerifiedAccessEndpointLoadBalancerOptions](API_VerifiedAccessEndpointLoadBalancerOptions.md) object
Required: No

 ** networkInterfaceOptions **
The options for network-interface type endpoint.
Type: [VerifiedAccessEndpointEniOptions](API_VerifiedAccessEndpointEniOptions.md) object
Required: No

 ** rdsOptions **
The options for an RDS endpoint.
Type: [VerifiedAccessEndpointRdsOptions](API_VerifiedAccessEndpointRdsOptions.md) object
Required: No

 ** SecurityGroupIdSet.N **
The IDs of the security groups for the endpoint.
Type: Array of strings
Required: No

 ** sseSpecification **
The options in use for server side encryption.
Type: [VerifiedAccessSseSpecificationResponse](API_VerifiedAccessSseSpecificationResponse.md) object
Required: No

 ** status **
The endpoint status.
Type: [VerifiedAccessEndpointStatus](API_VerifiedAccessEndpointStatus.md) object
Required: No

 ** TagSet.N **
The tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** verifiedAccessEndpointId **
The ID of the AWS Verified Access endpoint.
Type: String
Required: No

 ** verifiedAccessGroupId **
The ID of the AWS Verified Access group.
Type: String
Required: No

 ** verifiedAccessInstanceId **
The ID of the AWS Verified Access instance.
Type: String
Required: No

## See Also
<a name="API_VerifiedAccessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
