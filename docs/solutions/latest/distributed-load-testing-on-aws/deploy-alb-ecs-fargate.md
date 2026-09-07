---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-alb-ecs-fargate.html
---

# Launch the stack (ALB \+ ECS Fargate hosted web console)
<a name="deploy-alb-ecs-fargate"></a>

## Prerequisites
<a name="alb-ecs-prerequisites"></a>

Before deploying the ALB \+ ECS Fargate template, you must complete the following:

1.  **ACM certificate** — Request or import an SSL/TLS certificate into [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) in the same Region where you will deploy the stack. The certificate must cover the domain name you plan to use for the web console.

1.  **Domain ownership** — You must own or control the domain name that you will specify in the **ConsoleDomainName** parameter. You will need the ability to create DNS records for this domain after deployment.

## Launch the stack
<a name="alb-ecs-launch-the-stack"></a>

1. Sign in to the AWS Management Console and select the button to launch the CloudFormation template.

    [![Launch solution with the ALB + ECS Fargate template](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-alb-ecs.template&redirectId=ImplementationGuide)

   Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-alb-ecs.template) as a starting point for your own implementation.

1. The template is launched in the US East (N. Virginia) Region by default. To launch in a different AWS Region, use the region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This template uses the following parameters in addition to the standard parameters from the default template.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-alb-ecs-fargate.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

## Post-deployment configuration
<a name="alb-ecs-post-deployment"></a>

After the stack creation completes, you must configure DNS to point your custom domain to the ALB.

1. Navigate to the **Outputs** tab of the CloudFormation stack and copy the **ALBDnsName** value.

1. In your DNS provider, create one of the following records:
   +  **CNAME record** — Maps your domain to the ALB DNS name. Suitable for subdomains (for example, `dlt.example.com`).
   +  **Alias record (Route 53)** — If you use Amazon Route 53, you can create an alias record pointing to the ALB. This is required for zone apex domains (for example, `example.com`) and avoids CNAME lookup charges.

     In the Route 53 console, create an A record with **Alias** enabled, select **Alias to Application and Classic Load Balancer**, choose the Region, and select the ALB.

1. Wait for DNS propagation to complete. You can verify with:

   ```
   $ dig dlt.example.com
   ```

1. Access the web console at `https://<your-domain>` (for example, `https://dlt.example.com`).

The web console URL is also available in the CloudFormation **Outputs** tab as **ConsoleURL**.

**Note**
DNS propagation can take from a few minutes to 48 hours depending on your DNS provider and TTL settings.

## WAF integration (Optional)
<a name="alb-ecs-waf-integration"></a>

The default managed rule groups (Core Rule Set, Amazon IP Reputation List, and Anonymous IP List) provide baseline protection for most deployments. You can disable WAF deployment by setting the **Deploy WAF** CloudFormation parameter to `No`. No additional WAF configuration is required unless you have specific security requirements.

If you need to customize the WAF rules, you can modify the configuration as follows:

1. Open the [AWS WAF console](https://console.aws.amazon.com/wafv2/) in the same Region as your deployment.

1. Select the web ACL created by the solution. The web ACL name can be found in the CloudFormation stack resources.

1. Choose **Rules** to view, add, remove, or modify the rules in the web ACL.

1. You can add additional AWS managed rule groups, custom rules, or rate-based rules based on your security needs.

For more information, refer to [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) in the *AWS WAF Developer Guide*.
