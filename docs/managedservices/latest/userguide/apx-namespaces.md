---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/apx-namespaces.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# AMS protected namespaces
<a name="apx-namespaces"></a>

The list of protected namespaces for AWS Managed Services (AMS). When you work with AWS resources, prevent conflict with AMS by not using these namespaces. For details on other AWS service namespaces, see [ Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces).
+ `ams-*` (this is the preferred naming standard for new resources)
+ `/ams/*` (this is the preferred naming standard for path-based resources)
+ `AWSManagedServices*` (this is the preferred naming standard for resources where CamelCase is appropriate)
+ `ams*` and `AMS*` and `Ams*`
+ `AWS_*` and `aws*`
+ `*/aws_reserved/*`
+ `CloudTrail*` and `Cloudtrail*`
+ `codedeploy_service_role`
+ `customer-mc-*`
+ `eps` and `EPS`
+ `EPSMarketplaceSubscriptionRole`
+ `EPSDB*`
+ `IAMPolicy*`
+ `INGEST*`
+ `LandingZone*`
+ `Managed_Services*`
+ `managementhost`
+ `mc*` and `MC*` and `Mc*`
+ `MMS*`
+ `ms-`
+ `NewAMS*`
+ `Root*`
+ `sentinel*` and `Sentinel*`
+ `sentinel.int.`
+ `StateMachine*`
+ `StackSet-ams*`
+ `StackSet-AWS-Landing-Zone`
+ `TemplateId*`
+ `UnhealthyInServiceBastion`
+ `VPC_*`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
