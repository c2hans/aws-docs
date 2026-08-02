---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_CreateCluster_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateCluster` with an AWS SDK or CLI
<a name="eks_example_eks_CreateCluster_section"></a>

The following code examples show how to use `CreateCluster`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Getting started with managed kubernetes clusters](eks_example_eks_GettingStarted_034_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create a new cluster**
This example command creates a cluster named `prod` in your default region.
Command:

```
aws eks create-cluster --name {{prod}} \
--role-arn {{arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-J7ONKE3BQ4PI}} \
--resources-vpc-config {{subnetIds=subnet-6782e71e,subnet-e7e761ac,securityGroupIds=sg-6979fe18}}
```
Output:

```
{
    "cluster": {
        "name": "prod",
        "arn": "arn:aws:eks:us-west-2:012345678910:cluster/prod",
        "createdAt": 1527808069.147,
        "version": "1.10",
        "roleArn": "arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-J7ONKE3BQ4PI",
        "resourcesVpcConfig": {
            "subnetIds": [
                "subnet-6782e71e",
                "subnet-e7e761ac"
            ],
            "securityGroupIds": [
                "sg-6979fe18"
            ],
            "vpcId": "vpc-950809ec"
        },
        "status": "CREATING",
        "certificateAuthority": {}
    }
}
```
**To create a new cluster with private endpoint access and logging enabled**
This example command creates a cluster named `example` in your default region with public endpoint access disabled, private endpoint access enabled, and all logging types enabled.
Command:

```
aws eks create-cluster --name {{example}} --kubernetes-version {{1.12}} \
--role-arn {{arn:aws:iam::012345678910:role/example-cluster-ServiceRole-1XWBQWYSFRE2Q}} \
--resources-vpc-config {{subnetIds=subnet-0a188dccd2f9a632f,subnet-09290d93da4278664,subnet-0f21dd86e0e91134a,subnet-0173dead68481a583,subnet-051f70a57ed6fcab6,subnet-01322339c5c7de9b4,securityGroupIds=sg-0c5b580845a031c10,endpointPublicAccess=false,endpointPrivateAccess=true}} \
--logging '{{{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}}}'
```
Output:

```
{
    "cluster": {
        "name": "example",
        "arn": "arn:aws:eks:us-west-2:012345678910:cluster/example",
        "createdAt": 1565804921.901,
        "version": "1.12",
        "roleArn": "arn:aws:iam::012345678910:role/example-cluster-ServiceRole-1XWBQWYSFRE2Q",
        "resourcesVpcConfig": {
            "subnetIds": [
                "subnet-0a188dccd2f9a632f",
                "subnet-09290d93da4278664",
                "subnet-0f21dd86e0e91134a",
                "subnet-0173dead68481a583",
                "subnet-051f70a57ed6fcab6",
                "subnet-01322339c5c7de9b4"
            ],
            "securityGroupIds": [
                "sg-0c5b580845a031c10"
            ],
            "vpcId": "vpc-0f622c01f68d4afec",
            "endpointPublicAccess": false,
            "endpointPrivateAccess": true
        },
        "logging": {
            "clusterLogging": [
                {
                    "types": [
                        "api",
                        "audit",
                        "authenticator",
                        "controllerManager",
                        "scheduler"
                    ],
                    "enabled": true
                }
            ]
        },
        "status": "CREATING",
        "certificateAuthority": {},
        "platformVersion": "eks.3"
    }
}
```
+  For API details, see [CreateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-cluster.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new cluster called 'prod'.**

```
New-EKSCluster -Name prod -ResourcesVpcConfig @{SubnetIds=@("subnet-0a1b2c3d","subnet-3a2b1c0d");SecurityGroupIds="sg-6979fe18"} -RoleArn "arn:aws:iam::012345678901:role/eks-service-role"
```
**Output:**

```
Arn                  : arn:aws:eks:us-west-2:012345678901:cluster/prod
CertificateAuthority : Amazon.EKS.Model.Certificate
ClientRequestToken   :
CreatedAt            : 12/10/2018 9:25:31 PM
Endpoint             :
Name                 : prod
PlatformVersion      : eks.3
ResourcesVpcConfig   : Amazon.EKS.Model.VpcConfigResponse
RoleArn              : arn:aws:iam::012345678901:role/eks-service-role
Status               : CREATING
Version              : 1.10
```
+  For API details, see [CreateCluster](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new cluster called 'prod'.**

```
New-EKSCluster -Name prod -ResourcesVpcConfig @{SubnetIds=@("subnet-0a1b2c3d","subnet-3a2b1c0d");SecurityGroupIds="sg-6979fe18"} -RoleArn "arn:aws:iam::012345678901:role/eks-service-role"
```
**Output:**

```
Arn                  : arn:aws:eks:us-west-2:012345678901:cluster/prod
CertificateAuthority : Amazon.EKS.Model.Certificate
ClientRequestToken   :
CreatedAt            : 12/10/2018 9:25:31 PM
Endpoint             :
Name                 : prod
PlatformVersion      : eks.3
ResourcesVpcConfig   : Amazon.EKS.Model.VpcConfigResponse
RoleArn              : arn:aws:iam::012345678901:role/eks-service-role
Status               : CREATING
Version              : 1.10
```
+  For API details, see [CreateCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/eks#code-examples).

```
async fn make_cluster(
    client: &aws_sdk_eks::Client,
    name: &str,
    arn: &str,
    subnet_ids: Vec<String>,
) -> Result<(), aws_sdk_eks::Error> {
    let cluster = client
        .create_cluster()
        .name(name)
        .role_arn(arn)
        .resources_vpc_config(
            VpcConfigRequest::builder()
                .set_subnet_ids(Some(subnet_ids))
                .build(),
        )
        .send()
        .await?;
    println!("cluster created: {:?}", cluster);

    Ok(())
}
```
+  For API details, see [CreateCluster](https://docs.rs/aws-sdk-eks/latest/aws_sdk_eks/client/struct.Client.html#method.create_cluster) in *AWS SDK for Rust API reference*.

------
