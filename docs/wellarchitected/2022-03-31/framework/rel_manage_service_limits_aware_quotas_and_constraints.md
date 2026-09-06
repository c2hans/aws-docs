---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_manage_service_limits_aware_quotas_and_constraints.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP01 Aware of service quotas and constraints
<a name="rel_manage_service_limits_aware_quotas_and_constraints"></a>

 You are aware of your default quotas and quota increase requests for your workload architecture. You additionally know which resource constraints, such as disk or network, are potentially impactful.

 Service Quotas is an AWS service that helps you manage your quotas for over 100 AWS services from one location. Along with looking up the quota values, you can also request and track quota increases from the Service Quotas console or via the AWS SDK. AWS Trusted Advisor offers a service quotas check that displays your usage and quotas for some aspects of some services. The default service quotas per service are also in the AWS documentation per respective service, for example, see [Amazon VPC Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html). Rate limits on throttled APIs are set within the API Gateway itself by configuring a usage plan. Other limits that are set as configuration on their respective services include Provisioned IOPS, RDS storage allocated, and EBS volume allocations. Amazon Elastic Compute Cloud (Amazon EC2) has its own service limits dashboard that can help you manage your instance, Amazon Elastic Block Store (Amazon EBS), and Elastic IP address limits. If you have a use case where service quotas impact your application’s performance and they are not adjustable to your needs, then contact AWS Support to see if there are mitigations.

 **Common anti-patterns:**
+  Deploying a workload with no regard of the service quotas on the AWS services used.
+  Designing a workload without investigating and accommodating for AWS services' design constraints.
+  Deploying a workload with significant use that replaces a known existing workload without configuring the necessary quotas or contacting AWS Support in advance.
+  Planning an event to drive traffic to your workload, but not configuring the necessary quotas or contacting AWS Support in advance.

 **Benefits of establishing this best practice:** Being aware of the service quotas, API throttling limits, and design constraints will allow you to account for these in your design, implementation, and operation of the workload.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Review AWS service quotas in the published documentation and Service Quotas
  +  [AWS Service Quotas (formerly referred to as limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  Determine all the services your workload requires by looking at the deployment code.
+  Use AWS Config to find all AWS resources used in your AWS accounts.
  +  [AWS Config Supported AWS Resource Types and Resource Relationships](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)
+  You can also use your AWS CloudFormation to determine your AWS resources used. Look at the resources that were created either in the AWS Management Console or via the list-stack-resources CLI command. You can also see resources configured to be deployed in the template itself.
  +  [Viewing AWS CloudFormation Stack Data and Resources on the AWS Management Console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html)
  +  [AWS CLI for CloudFormation: list-stack-resources](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-stack-resources.html)
+  Determine the service quotas that apply. Use the programmatically accessible information via Trusted Advisor and Service Quotas.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks (see the Service Limits section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
+  [AWS limit monitor on AWS answers](https://aws.amazon.com/answers/account-management/limit-monitor/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)
