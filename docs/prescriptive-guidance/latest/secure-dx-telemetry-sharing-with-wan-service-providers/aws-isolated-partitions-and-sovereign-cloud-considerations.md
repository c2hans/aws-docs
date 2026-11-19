---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/aws-isolated-partitions-and-sovereign-cloud-considerations.html
---

# AWS Isolated Partitions and Sovereign Cloud Considerations

The framework is designed to operate across all AWS partitions without modification. However, each partition has unique characteristics that affect deployment planning, service availability, and compliance requirements. The following table summarizes the key considerations for each partition.

|
|
| Partition | ARN Prefix | Considerations |
| --- |--- |--- |
| aws (Commercial) | arn:aws: | Service availability varies by Region. Verify availability of Direct Connect, Config, CloudWatch, and EventBridge in the target Region. Broadest WSP/ESP ecosystem. |
| aws-us-gov (GovCloud) | arn:aws-us-gov: | FedRAMP High baseline. Verify DX availability in target GovCloud Region. ESP must have GovCloud account. Cross-account role assumption must occur within the aws-us-gov partition. |
| Isolated / restricted-access partitions | arn:(varies) | Coordinate with your provisioning team early; additional clearances may be required. Verify availability of Direct Connect, Config, CloudWatch and EventBridge in the target Region. Use AWS::Partition in CloudFormation to construct ARNs dynamically so the same template deploys without code changes  |

In AWS isolated or restricted-access partition environments, the tag-based metadata storage approach is particularly valuable. These partitions have limited access to external collaboration tools, making it difficult for WSPs to obtain customer contact information and circuit details through conventional channels. By storing this metadata directly on the Direct Connect resources as tags, the framework provides a self-service mechanism that works entirely within the partition boundary. The CloudFormation template uses AWS::Partition to construct all ARNs dynamically, ensuring correct ARN formatting in every partition without code changes.
