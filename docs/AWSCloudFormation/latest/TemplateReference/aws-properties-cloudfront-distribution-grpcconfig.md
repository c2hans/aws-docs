---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-grpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution GrpcConfig
<a name="aws-properties-cloudfront-distribution-grpcconfig"></a>

Amazon CloudFront supports gRPC, an open-source remote procedure call (RPC) framework built on HTTP/2. gRPC offers bi-directional streaming and binary protocol that buffers payloads, making it suitable for applications that require low latency communications.

To enable your distribution to handle gRPC requests, you must include HTTP/2 as one of the supported `HTTP` versions and allow `HTTP` methods, including `POST`.

For more information, see [Using gRPC with CloudFront distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-using-grpc.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-properties-cloudfront-distribution-grpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-grpcconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-cloudfront-distribution-grpcconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-grpcconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-cloudfront-distribution-grpcconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-grpcconfig-properties"></a>

`Enabled`  <a name="cfn-cloudfront-distribution-grpcconfig-enabled"></a>
Enables your CloudFront distribution to receive gRPC requests and to proxy them directly to your origins.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
