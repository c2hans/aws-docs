---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-WP-stack-elb-create.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Create an ELB Stack
<a name="gui-ex-WP-stack-elb-create"></a>

Launch a public ELB.

REQUIRED DATA:
+ `VpcId`: The VPC you are using, this should be the same as the previously used VPC.
+ `ELBSubnetIds`: An array of subnets across which the load balancer will distribute traffic. Choose either public or private subnets. Find Subnet IDs with the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-subnet-summaries) or in the AMS Console VPCs -> VPC details page.
+ `VpcId`: The VPC you are using, this should be the same as the previously used VPC.

1. On the **Create RFC** page, select the category **Deployment**, subcategory **Advanced Stack Components**, item **Load balancer (ELB) stack**, and click **Create**. Choose **Advanced** and accept all defaults (including those with no value) except those shown next.

   ```
   Subject:                          WP-ELB-RFC
   ELBSubnetIds:                     {{PUBLIC_AZ1
                                PUBLIC_AZ2}}
   ELBScheme                         true
   ELBCookieExpirationPeriod         600
   VpcId:                            {{VPC_ID}}
   Name:                             WP-Public-ELB
   ```

1. Click **Submit** when finished.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
