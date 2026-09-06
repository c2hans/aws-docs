---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/tune-the-solution.html
---

# Tune the solution
<a name="tune-the-solution"></a>

## CloudFront distribution domain name
<a name="cloudfront-distribution-domain-name"></a>

The CloudFront distribution in this solution uses the default CloudFront domain name (`xxxxxxxxxxxxxx.cloudfront.net`) and certificate (`\*.cloudfront.net`). To use a custom domain name and HTTPS between viewers and CloudFront, see [Configuring alternate domain names and HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.html) in the *Amazon CloudFront Developer Guide* after stack deployment.

## Guidance on how to implement/enable TLS between CloudFront and ALB
<a name="tls-guidance"></a>

You can configure your CloudFront distribution to always use HTTPS when sending requests to your Application Load Balancer. Remember, this only works if you keep the custom header name and value secret. Using HTTPS can help prevent an eavesdropper from discovering the header name and value. We also recommend rotating the header name and value periodically.

 **Use HTTPS for origin requests**

To configure CloudFront to use HTTPS for origin requests, set the origin protocol policy setting to HTTPS Only. This setting is available in the CloudFront console, AWS CloudFormation, and the CloudFront API. For more information, see [Protocol (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginProtocolPolicy) in the *Amazon CloudFront Developer Guide*.

The following also applies when you configure CloudFront to use HTTPS for origin requests:
+ You must configure CloudFront to forward the host header to the origin with the managed origin request policy. For details, see [AllViewer managed origin request policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html#managed-origin-request-policy-all-viewer).
+ Make sure that your Application Load Balancer has an [HTTPS listener](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html#restrict-alb-route-based-on-header). For more information, see [Create an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) in *Elastic Load Balancing*. Using an HTTPS listener requires you to have an SSL/TLS certificate that matches the domain name that’s routed to your ALB.
+ SSL/TLS certificates for CloudFront can only be requested (or imported) in the us-east-1 Region in AWS Certificate Manager (ACM). Because CloudFront is a global service, it automatically distributes the certificate from the us-east-1 Region to all Regions associated with your CloudFront distribution.
  + For example, if you have an ALB in the ap-southeast-2 Region, you must configure SSL/TLS certificates in both the ap-southeast-2 Region (for using HTTPS between CloudFront and ALB origin) and the us-east-1 Region (for using HTTPS between viewers and CloudFront). Both certificates should match the domain name that is routed to your Application Load Balancer. For more information, see [AWS Region for AWS Certificate Manager](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html#https-requirements-aws-region) in the *Amazon CloudFront Developer Guide*.
+ If the end users of your web application can use HTTPS, you can also configure CloudFront to prefer (or even require) HTTPS connections from the end users. To do this, use the **Viewer Protocol Policy** setting. You can set it to redirect end users from HTTP to HTTPS, or to reject requests that use HTTP. This setting is available in the CloudFront console, AWS CloudFormation, and the CloudFront API. For more information, see [Viewer protocol policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesViewerProtocolPolicy) in the *Amazon CloudFront Developer Guide*.

## Firewall rules
<a name="firewall-rules"></a>

This solution uses AWS WAF as a protection mechanism from DDoS attacks against the Prebid Server cluster. The web access control list (web ACL) gives customers fine-grained control over the web requests that the Amazon CloudFront distribution responds to. This solution adds AWS Managed Rules in the web ACL but users must add more web ACLs according to their own environment, such as a referrer rule to reject requests when referrer headers don’t match supported websites. For more information, see [AWS WAF rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html) in the *AWS WAF, Firewall Manager, and AWS Shield Advanced Developer Guide*.

To add new rules, open the web ACL corresponding to the `PrebidWAFWebACL` resource listed in the CloudFormation stack outputs. For more information, see [Web access control lists (web ACLs)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html) in the *AWS WAF, Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Container tuning
<a name="container-tuning"></a>

The performance and cost of running this solution are dominated by utilization of the ECS cluster. The largest user-configurable factors that users can customize to affect performance, cost, and efficiency are ECS Service Auto Scaling, min and max container size, and Fargate / Fargate Spot capacity providers. For the effect of ECS service configuration on performance and cost, refer to the [Cost](cost1.md) and [Configurations for Elastic Container Service (ECS) Auto Scaling](configurations-for-elastic.md) sections in this guide.

This solution has Service Auto Scaling in place to add or remove service tasks based on metric and target value. For more information about automatic scaling in ECS, refer to [Automatically scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/userguide/service-auto-scaling.html) and [Scale your Amazon ECS service using a target metric value](https://docs.aws.amazon.com/AmazonECS/latest/userguide/service-autoscaling-targettracking.html) in the *Amazon ECS Developer Guide*.

This solution uses a weighted combination of Fargate and Fargate Spot instances with defaults to 50/50. For information about Fargate Spot tasks. see [AWS Fargate capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html) in the *Amazon ECS Developer Guide* and [Deep dive into Fargate Spot to run your ECS Tasks for up to 70% less](https://aws.amazon.com/blogs/compute/deep-dive-into-fargate-spot-to-run-your-ecs-tasks-for-up-to-70-less/) on the *AWS Blog*. You can perform the procedures in [Updating a service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon ECS Developer Guide*, to edit Service Auto Scaling policies, Fargate Spot instances ratio. To adjust how much CPU and memory to use with each task, see [Updating the task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/userguide/update-task-definition-console-v2.html) in the *Amazon ECS Developer Guide*. Also, see [Amazon ECS task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html).
