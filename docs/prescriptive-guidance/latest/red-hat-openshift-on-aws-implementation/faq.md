---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/faq.html
---

# FAQ
<a name="faq"></a>

1. What happens if cluster provisioning fails?

   The installer provides logs that can provide guidance for fixing the error.

1. Can I use IPI and UPI interchangeably?

   You should use one of these methods depending on your use case. For a comparison, see the section [Advantages and disadvantages of each approach](installation-options.md#adv-disadv). IPI is the easier method for most standard scenarios.

1. Where can I get AWS CloudFormation templates for provisioning the underlying infrastructure on AWS, if I decide to go with UPI?

   For details and example templates, see the [OpenShift documentation](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.6/html-single/installing/index#installing-aws-user-infra). You can use these templates as a base and modify them to meet your requirements.
