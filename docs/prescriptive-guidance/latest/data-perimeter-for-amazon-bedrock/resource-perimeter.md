---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/resource-perimeter.html
---

# Resource perimeter
<a name="resource-perimeter"></a>

The resource perimeter for Amazon Bedrock extends beyond the service itself to encompass all resources that store, process, or transmit AI-related data. This includes Amazon S3 buckets containing training datasets, OpenSearchclusters powering knowledge bases, and even CloudWatch logs that might contain sensitive prompts or responses.

This diagram is a high level illustration of a resource perimeter.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/images/guide-img/4f7d8782-326c-45ca-95dd-0c4e97e42271/images/2ca1c068-49f1-458f-8d84-7616872a1d88.png)

Figure 3.2 High level illustration of resource perimeter

1. Service control policies (SCPs) allow only approved Amazon Bedrock models in approved regions.

1. SCP denies all access to untrusted external Resources

1. Amazon VPC endpoint policies deny access to external resources outside organizational boundaries

1. Amazon VPC endpoint policy allows access only to approved resources with with required tags

This section covers the comprehensive resource protection strategies for Amazon Bedrock:
+ **Model access controls** - Implementing fine-grained IAM policies for different Amazon Bedrock models
+ **Service principals** - Managing automated access patterns and service-to-service authentication
+ **Cross-service integration controls** - Managing resource access across integrated AWS services
+ **Resource tagging strategy** - Implementing consistent tagging for resource-based access controls
+ **Identity tagging controls** - IAM policies for attribute-based resource access control
+ **Network resource access controls** - Network-based resource access restrictions
+ **Monitoring violations** - Detecting and responding to resource perimeter breaches
+ **Best practices** - Resource perimeter implementation recommendations and guidelines

Each subsection provides detailed implementation guidance and security controls specific to protecting AI-related resources.

**Note**
These resource protection examples demonstrate common patterns but may not address all data types, integration scenarios, or regulatory requirements in your environment. Conduct a thorough data classification and risk assessment for your specific AI workloads. Consult AWS service documentation for the latest encryption options, policy syntax, and integration patterns with your existing security controls.
