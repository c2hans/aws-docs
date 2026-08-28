---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/strategies.html
---

# Installation strategies
<a name="strategies"></a>

If you have specific customization requirements in networking, security, and other areas, see the following table for guidance. For more information, see [Installing on AWS](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html/installing/installing-on-aws) in the Red Hat OpenShift documentation.

|
|
| Installation scenario | IPI | UPI | Notes |
| --- |--- |--- |--- |
| **Fast cluster installation** |  |   | You can use Red Hat OpenShift on AWS.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-aws-default) |
| **Customized cluster** |  |  | You can install with some of the customization options provided by the installer (such as rosa-cli). This scenario is suitable for both IPI and UPI. Use UPI if you need further customizations.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-aws-customizations) |
| **Cluster with network customizations** |  |  | By using IPI, you have the flexibility to specify an existing IP range in the install-config.yaml file.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-aws-network-customizations) |
| **Cluster in in an existing VPC** |   |  | You can provision the cluster in an existing VPC and network infrastructure. For better flexibility, use UPI.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-aws-vpc) |
| **Private cluster in an existing VPC** |   |  | If you have a security requirement to host the cluster on a private network, with no access to the internet, you might have to set up private hosted zones and configure route tables carefully. For this scenario, UPI provides better flexibility.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-aws-private) |
| **AWS infrastructure that you provision** |   |  | Use UPI to create the underlying infrastructure components and resources by using AWS CloudFormation templates.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-aws-user-infra) |
| **Using an internal mirror** |   |  | You can mirror the contents of your local registry and install from there. However, you still need internet access to access AWS APIs.<br />[More information](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html-single/installing/index#installing-restricted-networks-aws) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
