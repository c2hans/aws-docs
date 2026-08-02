---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

In a security context, a perimeter provides a clear boundary of trust and ownership. For AWS environments, the perimeter is typically represented as a collection of resources in a group of AWSaccounts managed by AWS Organizations. This architecture establishes preventive controls that work together to protect your AI workloads from unauthorized access and data exfiltration.

**Identity layer architecture** - This layer controls which principals can perform AI operations. Unlike traditional applications where users directly access resources, Amazon Bedrock workloads often involve service-to-service communication, cross-account model sharing, and automated AI pipelines.

The identity perimeter must account for human users invoking models through applications, automated systems processing data through AI workflows, and cross-account scenarios where different AWSaccounts share custom models or knowledge bases.

**Resource layer architecture** - AI workloads interact with numerous AWSresources beyond Amazon Bedrock itself. Custom model training requires Amazon S3 buckets for datasets, knowledge bases use Amazon OpenSearch or vector databases, and model artifacts are stored across multiple services.

The resource perimeter ensures your AI identities only access trusted resources within your organization while preventing external resources from accessing your AI data.

**Network layer architecture** - Amazon Bedrock API calls carry prompts and responses that benefit from private connectivity. The network perimeter establishes private connectivity through VPC endpoints and ensures AI traffic flows through your designated network paths. This is particularly important for real-time model invocations where you want to maintain consistent network routing and security posture.

**Amazon Bedrock-specific policy implementation: **The AI data perimeter can be applied using three primary types of AWSsecurity features.
+ **Service control policies for AI resources** - Restrict access to Amazon Bedrock models, knowledge bases, and custom model endpoints using `bedrock:*` actions combined with` aws:ResourceOrgID` conditions to prevent unauthorized model access
+ **Resource control policies for AI data** - Protect Amazon S3 buckets containing training datasets, Amazon OpenSearch clusters powering knowledge bases, and model artifact storage using `aws:PrincipalOrgID` to ensure only trusted AI applications can access your data
+ **VPC endpoint policies for AI traffic** - Secure Amazon Bedrock API calls carrying sensitive prompts and responses through private connectivity, with policies that validate both the calling application and target model are within your trust boundary

These policies addressAmazon Bedrock's unique service integrations, such as when the service automatically accesses your Amazon S3 buckets for model training or when knowledge bases query your Amazon OpenSearch clusters during inference.
