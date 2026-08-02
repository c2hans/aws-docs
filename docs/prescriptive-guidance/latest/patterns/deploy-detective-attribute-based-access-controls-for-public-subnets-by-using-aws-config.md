---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html
---

# Deploy detective attribute-based access controls for public subnets by using AWS Config
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config"></a>

*Alberto Menendez, Amazon Web Services*

## Summary
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-summary"></a>

Distributed edge network architectures rely on network edge security that runs alongside the workloads in their virtual private clouds (VPCs). This provides unprecedented scalability in comparison to the more common, centralized approach. Although deploying public subnets in workload accounts can provide benefits, it also introduces new security risks because it increases the attack surface. We recommend that you deploy only Elastic Load Balancing resources, such as Application Load Balancers, or NAT gateways in the public subnets of these VPCs. Using load balancers and NAT gateways in dedicated public subnets helps you implement fine-grained control for inbound and outbound traffic.

We recommend that you implement both preventative and detective controls to limit the types of resources that can be deployed in public subnets. For more information about using attribute-based access control (ABAC) to deploy preventative controls for public subnets, see [Deploy preventative attribute-based access controls for public subnets](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-preventative-attribute-based-access-controls-for-public-subnets.html). Although effective for most situations, these preventative controls might not address all possible use cases. Therefore, this pattern builds on the ABAC approach and helps you configure alerts about noncompliant resources that are deployed in public subnets. The solution checks whether elastic network interfaces belong to a resource that is not allowed in public subnets.

To achieve this, this pattern uses [AWS Config custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) and [ABAC](https://aws.amazon.com/identity/attribute-based-access-control/). The custom rule processes the configuration of an elastic network interface whenever it is created or modified. At a high level, this rule performs two actions to determine whether the network interface is compliant:

1. To determine whether the network interface is in scope of the rule, the rule checks whether the subnet has specific [AWS tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) that indicate it is a public subnet. For example, this tag might be `IsPublicFacing=True`.

1. If the network interface is deployed in a public subnet, the rule checks which AWS service created this resource. If the resource is not an Elastic Load Balancing resource or NAT gateway, it marks the resource as noncompliant.

## Prerequisites and limitations
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Config, [set up](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) in the workload account
+ Permissions to deploy the required resources in the workload account
+ A VPC with public subnets
+ Tags properly applied to identify the target public subnets
+ (Optional) An organization in AWS Organizations
+ (Optional) A central security account that is the delegated administrator for AWS Config and AWS Security Hub CSPM

## Architecture
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-architecture"></a>

**Target architecture**

![Using an AWS Config custom rule to detect noncompliant resources in public subnets](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/85d54ead-7f00-4381-89fb-cffe307c4cfc/images/a8c19913-d260-4b70-96ba-732bb1b9881f.png)

The diagram illustrates the following:

1. When an elastic network interface resource (`AWS::EC2::NetworkInterface`) is deployed or modified, AWS Config captures the event and the configuration.

1. AWS Config matches this event against the custom rule used to evaluate the configuration.

1. The AWS Lambda function associated with this custom rule is invoked. The function evaluates the resource and applies the specified logic to determine if the resource configuration is `COMPLIANT`, `NON_COMPLIANT` or `NOT_APPLICABLE`.

1. If a resource is determined to be `NON_COMPLIANT`, AWS Config sends an alert through Amazon Simple Notification Service (Amazon SNS).
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html)

**Lambda function evaluation logic**

The following diagram shows the logic applied by the Lambda function to evaluate the compliance of the elastic network interface.

![Diagram of Lambda function logic](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/85d54ead-7f00-4381-89fb-cffe307c4cfc/images/9575e20f-142b-4eba-b34d-3b9bda163144.png)

**Automation and scale**

This pattern is a detective solution. You can also complement it with a remediation rule to automatically resolve any noncompliant resources. For more information, see [Remediating Noncompliant Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html).

You can scale this solution by:
+ Enforcing application of the corresponding AWS tags that you establish to identify public-facing subnets. For more information, see [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the AWS Organizations documentation.
+ Configuring a central security account that applies the AWS Config custom rule to every workload account in the organization. For more information, see [Automate configuration compliance at scale in AWS](https://aws.amazon.com/blogs/mt/automate-configuration-compliance-at-scale-in-aws/) (AWS blog post).
+ Integrating AWS Config with AWS Security Hub CSPM in order to capture, centralize, and notify at scale. For more information, see [Configuring AWS Config](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-prereq-config.html) in the AWS Security Hub CSPM documentation.

## Tools
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-tools"></a>
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Best practices
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-best-practices"></a>

For more examples and best practices for developing custom AWS Config rules, see the official [AWS Config Rules Repository](https://github.com/awslabs/aws-config-rules) on GitHub.

## Epics
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-epics"></a>

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |
| Add permissions to the Lambda function's execution role. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |
| Retrieve the Lambda function Amazon Resource Name (ARN). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |
| Create the AWS Config custom rule. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |
| Configure notifications. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a compliant resource. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |
| Create a noncompliant resource. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |
| Create a resource that is not applicable. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config.html) | General AWS |

## Related resources
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-resources"></a>

**AWS documentation**
+ [Setting up AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
+ [AWS Config custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html)
+ [ABAC for AWS](https://aws.amazon.com/identity/attribute-based-access-control/)
+ [Deploy preventative attribute-based access controls for public subnets](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-preventative-attribute-based-access-controls-for-public-subnets.html)

**Other AWS resources**
+ [Automate configuration compliance at scale in AWS](https://aws.amazon.com/blogs/mt/automate-configuration-compliance-at-scale-in-aws/)
+ [Distributed Inspection Architectures with Gateway Load Balancer](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/distributed-inspection-architectures-gwlb-ra.pdf)

## Additional information
<a name="deploy-detective-attribute-based-access-controls-for-public-subnets-by-using-aws-config-additional"></a>

The following is a sample Lambda function that is provided for demonstration purposes.

```
import boto3
import json
import os

# Init clients
config_client = boto3.client('config')
ec2_client = boto3.client('ec2')

def lambda_handler(event, context):

    # Init values
    compliance_value = 'NOT_APPLICABLE'
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']

    status = configuration_item['configurationItemStatus']
    eventLeftScope = event['eventLeftScope']

    # First check if the event configuration applies. Ex. resource event is not delete
    if (status == 'OK' or status == 'ResourceDiscovered') and not eventLeftScope:
        compliance_value = evaluate_change_notification_compliance(configuration_item)

    config_client.put_evaluations(
       Evaluations=[
           {
               'ComplianceResourceType': invoking_event['configurationItem']['resourceType'],
               'ComplianceResourceId': invoking_event['configurationItem']['resourceId'],
               'ComplianceType': compliance_value,
               'OrderingTimestamp': invoking_event['configurationItem']['configurationItemCaptureTime']
           },
       ],
       ResultToken=event['resultToken'])

# Function with the logs to evaluate the resource
def evaluate_change_notification_compliance(configuration_item):
    is_in_scope = is_in_scope_subnet(configuration_item['configuration']['subnetId'])

    if (configuration_item['resourceType'] != 'AWS::EC2::NetworkInterface') or not is_in_scope:
        return 'NOT_APPLICABLE'

    else:
        alb_condition = configuration_item['configuration']['requesterId'] in ['amazon-elb']
        nlb_condition = configuration_item['configuration']['interfaceType'] in ['network_load_balancer']
        nat_gateway_condition = configuration_item['configuration']['interfaceType'] in ['nat_gateway']

        if alb_condition or nlb_condition or nat_gateway_condition:
            return 'COMPLIANT'
    return 'NON_COMPLIANT'

# Function to check if elastic network interface is in public subnet
def is_in_scope_subnet(eni_subnet):

    subnet_description = ec2_client.describe_subnets(
        SubnetIds=[eni_subnet]
    )

    for subnet in subnet_description['Subnets']:
        for tag in subnet['Tags']:
            if tag['Key'] == os.environ.get('TAG_KEY') and tag['Value'] == os.environ.get('TAG_VALUE'):
                return True

    return False
```
