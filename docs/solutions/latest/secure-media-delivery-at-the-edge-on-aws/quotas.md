---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

 Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

 Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

 Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

 As you evaluate the deployment of the Secure Media Delivery at the Edge on AWS solution, one limit that should be accounted for is WCU capacity of the web ACL used with CloudFront, and when session revocation module is to be launched. The default WCU limit for AWS WAF web ACL equals to 1500 WCU which is a shared capacity for the customer defined and managed WAF Rules, as well as the rule group created in the main module of the solution. For any rule group created, its WCU limit must be declared at the time of its creation and the value you specify at this stage is what gets consumed from web ACL general WCU limit. Rule group WCU limit cannot be modified after creation, therefore you must plan in advance how much WCU you want to allocate for session revocation rule group (recall that a rule to block a single session is worth 2 WCU). The limit you plan to apply for the rule group when launching the solution cannot exceed WCU headroom left in the web ACL that the rule group will be attached to. If there is not enough headroom left for the size of the rule group you plan to create when launching the solution, request WCU limit increase for that target web ACL to increase available WCU headroom.
