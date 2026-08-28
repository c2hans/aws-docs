---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/weakness-and-limitations-of-classic-frameworks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Weakness and limitations of classic frameworks
<a name="weakness-and-limitations-of-classic-frameworks"></a>

 Some of the ideas behind the original approach, such as its focus on network perimeter concepts as well as *advanced persistent threats*, are not fully applicable in a modern, cloud-based environment. Also, the original approach tends to assume a relatively static, traditional IT environment, which is not what customers typically build in the cloud. Advanced persistent threats (APTs) have no place to live in DevSecOps environment, where entirely new, fully scanned, and tested copies of applications are deployed on new virtual infrastructure on a daily if not almost hourly basis; “network intrusion” has no definite meaning in a modern perimeter-less network of cooperating microservices, where all hosts are network-reachable without being vulnerable to persistent takeover. Even where network perimeters remain an important defense, the cloud makes it much easier to create and maintain segmentation or micro-perimeters such that lateral movement is far more difficult, and potential attackers far more constrained.

 As a result, classic intrusion analysis frameworks suffer from a number of weaknesses and limitations when applied to modern cloud platforms. These frameworks are particularly problematic when analyzing systems developed with modern DevSecOps practices using cloud-native architectural patterns. But these framework weaknesses also apply to some extent even for more traditional applications that have been “lifted and shifted” to the cloud.

## Perimeter-less or zero-trust network architectures
<a name="perimeter-less-or-zero-trust-network-architectures"></a>

 Perimeter-less or zero-trust network architectures render large parts of the classic intrusion analysis framework flawed or pointless. Zero-trust network architectures mitigate multi-step attacks designed to move through different phases or components. These architectures force every request or operation, regardless of their origin, to prove their trustworthiness, authenticity, and integrity. Privileges in these environments are none by default, and are never granted permanently. Subsequently, unauthorized actions are tightly controlled and the entire architecture is less vulnerable to abuse, from both insider and external threat actors. For more information, see [How to think about Zero Trust architectures on AWS](https://aws.amazon.com/blogs/publicsector/how-to-think-about-zero-trust-architectures-on-aws/).

## Stronger segmentation of networks in the cloud
<a name="stronger-segmentation-of-networks-in-the-cloud"></a>

 Cloud offers stronger segmentation of networks than many on-premises IT environments. Every service or application can operate within its own virtual private cloud (VPC). Within a VPC, there are firewall and routing rules that can’t be modified by an attacker, even if they gain access to a service or instance, because the corresponding rules are managed and owned by different parts of the organization and control over those settings requires access to IAM credentials or roles that are not present in the environment to which the attacker has gained access.

## Microservices architectures
<a name="microservices-architectures"></a>

 In microservices architectures, data extraction and/or lateral movement is highly constrained. You can only see the data inside that microservice and, in terms of lateral movement, you can only call or respond to well-defined API calls or interfaces. Even if a microservice is indeed compromised, the attack surface and privileges obtained are limited to that microservice and the privileges it has to call other microservices.

## Static environments versus dynamic environments
<a name="static-environments-versus-dynamic-environments"></a>

 Cloud enables the use of dynamic environments, such as environments where deployments or installations can only occur through a well-defined continuous integration/continuous deployment (CI/CD) pipeline that enforces and verifies security controls. Dynamic environments are refreshed frequently, meaning that their configuration and services are redeployed based on an agreed secure state and can then be made immutable once deployed – such that no privileges exist to change them once deployed. Their immutability makes it extremely hard for an attacker to gain persistence, even between the time of attack and next deployment. Moreover, in such environments, changes or attempts to implement changes, are easily discoverable and, regardless, overwritten by the next healthy and secure state refresh. Newly deployed infrastructure and application code have been built and tested with the latest security patches as a normal part of the CI/CD process. All these qualities of dynamic, frequently changed and improved infrastructure and application code make the concepts of installation, persistence, and exploitation much less relevant, or even potentially meaningless, in the cloud. An environment which is frequently redeployed is an environment where even a novel Advanced Persistent Threat (APT) payload won’t be able to persist in an active state beyond the next refresh, requiring an attacker to have to re-compromise the environment after the redeployment, with the flaw that led to the original compromise very likely to have been caught and patched.

## Traditional IT environments versus the cloud
<a name="traditional-it-environments-versus-the-cloud"></a>

 The value of a classical intrusion analysis framework does not directly apply to cloud environments when those environments are architected and operated according to current recommendations and modern approaches. However, across an entire organization and the pool of applications in use, such classical frameworks remain viable. Among other reasons, it will take time for many systems or applications to be modernized to fit the more cloud-based patterns discussed in previous sections. These *lift and shift* kinds of systems, as well as systems on the journey to full immutable infrastructure modernization, still have characteristics of traditional systems, and so application of classic frameworks is still valuable. In addition, even a modern CI/CD system may be deployed with a relatively static virtual network environment, for example, and so some of these concepts can still be applied to “container” into which applications are deployed. So, let’s turn to the traditional analysis and its application in light of cloud technologies. Cloud native services, alone or used in conjunction with third-party solutions, can help mitigate intrusion methods for more traditional systems and applications as well.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
