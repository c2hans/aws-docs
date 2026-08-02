---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

## Gather deployment parameter details
<a name="gather-deployment-parameter-details"></a>

Before deploying Workload Discovery on AWS, review your configuration details for the Amazon OpenSearch Service [service-linked role](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/slr-es.html) and AWS Config.

### Verify whether you have an AWSServiceRoleForAmazonOpenSearchService role
<a name="verify-whether-you-have-an-awsserviceroleforamazonopensearchservice-role"></a>

The deployment creates an Amazon OpenSearch Service cluster inside an Amazon Virtual Private Cloud (Amazon VPC). The template uses a service-linked role to create the OpenSearch Service cluster. However, if you already have the role created in your account, use the existing role.

To check if you already have this role:

1. Sign in to the [Identity and Access Management (IAM) console](https://console.aws.amazon.com/iam/) for the account you plan to deploy this solution to.

1. In the **Search** box, enter `AWSServiceRoleForAmazonOpenSearchService`.

1. If your search returns a role, select `No` for the **CreateOpensearchServiceRole** parameter when you launch the stack.

### Verify AWS Config is set up
<a name="verify-aws-config-is-set-up"></a>

Workload Discovery on AWS uses AWS Config to gather the majority of resource configurations. When deploying the solution or importing a new Region, you must confirm whether AWS Config is already set up and working as expected. The **AlreadyHaveConfigSetup** CloudFormation parameter informs Workload Discovery on AWS of whether to set up AWS Config.

The following snippet is taken from the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-status.html). Run the command in the Region you intend to deploy Workload Discovery on AWS or import into Workload Discovery on AWS.

Enter the following command:

```
aws configservice get-status
```

If you receive a response similar to the output, then there is a Configuration Recorder and Delivery Channel running in that Region. Select `Yes` for the **AlreadyHaveConfigSetup** CloudFormation parameter.

Output:

```
Configuration Recorders:

name: default
recorder: ON
last status: SUCCESS

Delivery Channels:

name: default
last stream delivery status: SUCCESS
last history delivery status: SUCCESS
last snapshot delivery status: SUCCESS
```

If you are configuring AWS CloudFormation StackSets, then you must include this Region in the batch of Regions that already have AWS Config configured.

### Verify your AWS Config details in your account
<a name="verify-your-aws-config-details-in-your-account"></a>

The deployment will attempt to set up AWS Config. If you already use AWS Config in the account that you plan to either deploy to or make discoverable by Workload Discovery on AWS, select the relevant parameters when you deploy this solution. Furthermore, for successful deployment, ensure that you haven’t restricted the resources that AWS Config scans.

To check your current AWS Config configuration:

1. Sign in to the [AWS Config](https://console.aws.amazon.com/config/) console.

1. Choose **Settings** and ensure the **Record all resources supported in this Region** and **Include global resources** boxes are selected.

### Verify AWS Config aggregator type
<a name="verify-aggregator-type"></a>

If supplying an existing AWS Config aggregator (only supported in `AWS_ORGANIZATIONS` mode), ensure that the aggregator is an AWS Organization wide aggregator. Run the following command and verify the presence of the `OrganizationAggregationSource` field:

```
aws configservice describe-configuration-aggregators
```

Output:

```
{
    "ConfigurationAggregators": [
        {
            "ConfigurationAggregatorName": "aggregator-name",
            "ConfigurationAggregatorArn": "arn:aws:config:eu-west-1:123456789012:config-aggregator/config-aggregator-5jfoefab",
            "OrganizationAggregationSource": {
                "RoleArn": "arn:aws:iam::123456789012:role/service-role/ConfigAggregator-ConfigOrganizationsRole",
                "AllAwsRegions": true
            },
            "CreationTime": "2024-11-19T15:13:22.979000+00:00",
            "LastUpdatedTime": "2024-11-19T15:13:22.990000+00:00"
        }
    ]
}
```

### Verify your VPC configuration
<a name="verify-your-vpc-configuration"></a>

If deploying to an existing VPC, [verify your private subnets can route requests to AWS services](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html).

If you choose the option to deploy the solution in an existing VPC, you must ensure that the Workload Discovery on AWS Lambda functions and the Amazon ECS tasks running in the private subnets of your VPC can connect to other AWS services. The standard way to enable this is with [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html). You can list the NAT gateways in your account as shown in the following code sample.

```
aws ec2 describe-route-tables --filters Name=association.subnet-id,Values=<private-subnet-id1>,<private-subnet-id2> --query 'RouteTables[].Routes[].NatGatewayId'
```

Output:

```
[
    "nat-1111111111111111",
    "nat-2222222222222222"
]
```

**Note**
If less than two results return, the subnets do not have the correct number of NAT gateways.

If your VPC doesn’t have NAT gateways, then you must either provision them or ensure that you have [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) for all the AWS services listed in the [AWS APIs](aws-apis.md) section.
