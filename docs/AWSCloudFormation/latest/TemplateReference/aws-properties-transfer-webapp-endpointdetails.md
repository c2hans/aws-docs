---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-endpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp EndpointDetails
<a name="aws-properties-transfer-webapp-endpointdetails"></a>

The virtual private cloud (VPC) endpoint settings that are configured for your file transfer protocol-enabled server. With a VPC endpoint, you can restrict access to your server and resources only within your VPC. To control incoming internet traffic, invoke the `UpdateServer` API and attach an Elastic IP address to your server's endpoint.

**Note**
 After May 19, 2021, you won't be able to create a server using `EndpointType=VPC_ENDPOINT` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with `EndpointType=VPC_ENDPOINT` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use `EndpointType`=`VPC`.
For more information, see [Discontinuing the use of VPC\_ENDPOINT](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint).
It is recommended that you use `VPC` as the `EndpointType`. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with `EndpointType` set to `VPC_ENDPOINT`.

## Syntax
<a name="aws-properties-transfer-webapp-endpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-webapp-endpointdetails-syntax.json"></a>

```
{
  "[Vpc](#cfn-transfer-webapp-endpointdetails-vpc)" : {{Vpc}}
}
```

### YAML
<a name="aws-properties-transfer-webapp-endpointdetails-syntax.yaml"></a>

```
  [Vpc](#cfn-transfer-webapp-endpointdetails-vpc): {{
    Vpc}}
```

## Properties
<a name="aws-properties-transfer-webapp-endpointdetails-properties"></a>

`Vpc`  <a name="cfn-transfer-webapp-endpointdetails-vpc"></a>
Property description not available.
*Required*: No
*Type*: [Vpc](aws-properties-transfer-webapp-vpc.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
