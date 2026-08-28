---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/vpce-landing.html
---

# VPC endpoint procedures
<a name="vpce-landing"></a>

## Quotas
<a name="vpce-quotas"></a>

The primary quota differences are:
+ Lower quota for all bandwidth APIs (2 mbps):
  + PutMedia
  + GetMedia
  + GetMediaForFragmentList
+ 10 streams allowed per customer

## Create an endpoint
<a name="create-endpoint"></a>

Once you're allow listed, you will receive the VPC endpoint service name for Amazon Kinesis Video Streams. It will look like `com.amazonaws.{{region}}.kinesisvideo`.

Create an [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) for Amazon Kinesis Video Streams using either the Amazon VPC Console or the AWS Command Line Interface (AWS CLI).

In the AWS CLI, type the following:

```
aws ec2 create-vpc-endpoint \
--vpc-id {{customer-provided-vpc-id}}\
--service-name com.amazonaws.eu-west-2.kinesisvideo \
--private-dns-enabled
```

**Important**
Traffic within your VPC will use private DNS to route over the endpoint. If you don't enable this, you'll need to implement your own DNS logic. For more information about private DNS, see [AWS PrivateLink documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#private-dns-s3).

For more information on the AWS CLI option, see [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html).

## Control access to endpoints
<a name="control-access"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon Kinesis Video Streams. The policy specifies the following information:
+ the principal that can perform actions,
+ the actions that can be performed, and
+ the resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the AWS PrivateLink Guide.

The following is an example of an endpoint policy for Amazon Kinesis Video Streams. When attached to an endpoint, this policy denies access to the listed `PutMedia` actions for all principals on all resources.

```
{
"Statement":[
      {
         "Principal":"*",
         "Effect":"Deny",
         "Action":[
            "kinesisvideo:PutMedia"
         ],
         "Resource":"*"
      }
   ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
