---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

 [Known issue resolution](#known-issue-resolution) provides instructions to mitigate known errors. If these instructions don’t address your issue, [Contact AWS Support](contact-aws-support.md) provides instructions for opening an AWS Support case for this solution.

## Known issue resolution
<a name="known-issue-resolution"></a>

 **Issue: You are using an existing VPC and your tests fail with a status of Failed, resulting in the following error message:**

 `Test might have failed to run.`
+ Resolution:

Ensure that the subnets exist in the VPC specified and that they have a route to the internet with either an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) or a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html). AWS Fargate needs access to pull the container image from the public repository to successfully run tests.

 **Issue: Tests are taking too long to run or are stuck indefinitely running**
+ Resolution:

Cancel the test and check AWS Fargate to ensure that all tasks have stopped. If they have not stopped, manually stop all Fargate tasks. Check the on-demand Fargate task limits on your account to ensure that you can launch the number of tasks desired. You can also check the CloudWatch logs for the Lambda task-runner function for more insight into failures when launching Fargate tasks. Check the CloudWatch ECS logs for details of what is happening in Fargate containers that are running.

 **Issue: Tests are starting but failing to complete or the state of the ECS tasks is unknown**
+ Resolution:

If you selected the option to provide an existing VPC in the account where the solution has been deployed, ensure that the VPC being used by the ECS Tasks has enough free IP addresses to start the number of tasks provided in the test input. The ECS task definition uses the ECR image that needs an internet gateway or a route to the internet so that the ECS service can provision the tasks by downloading the solution ECR image from [aws-solutions/distributed-load-testing-on-aws-load-tester](https://gallery.ecr.aws/aws-solutions/distributed-load-testing-on-aws-load-tester). If you cannot provide a route to the internet since all subnets in the VPC are private, you can host the ECR image in your account using [ECR pull through cache](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html). Update the task definition with the new ECR image URI and create a new revision. Once the task definition is updated, the solution configuration in the DynamoDB table needs to be updated to use the new revision. The DynamoDB table name can be found in the CloudFormation stack outputs tab under the key ScenariosTable. Update the attribute taskDefinition for the item with the key testId and value region-[SOLUTION-DEPLOYED-REGION].

 **Issue: Tests need to use an endpoint which is private or not available through the internet gateway**
+ Resolution:

When testing private API endpoints that aren’t accessible through the internet gateway, consider the following approaches:

1.  **Network Configuration**: Ensure the subnet route tables used by the ECS tasks are updated with a route to the IP address range of the private endpoint being tested. This allows the test traffic to reach the private endpoint within your VPC.

1.  **DNS Resolution**: For custom domains, configure the DNS settings in your VPC to resolve the private endpoint’s domain name. Refer to [VPC DNS](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) documentation for detailed instructions.

1.  **VPC Endpoints**: If testing AWS services, consider using VPC endpoints (AWS PrivateLink) to establish private connectivity. For example, to test a private API Gateway, you can create a VPC endpoint for API Gateway. See [Private API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html) documentation.

1.  **VPC Peering**: If the private endpoint is in a different VPC, establish VPC peering between the VPC where the solution is deployed and the VPC containing the private endpoint. Configure appropriate route tables in both VPCs. See [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) documentation.

1.  **Transit Gateway**: For more complex networking scenarios involving multiple VPCs, consider using AWS Transit Gateway to route traffic between the solution’s VPC and the VPC containing the private endpoint. See [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) documentation.

1.  **Security Groups**: Ensure that the security groups associated with your ECS tasks allow outbound traffic to the private endpoint, and the security groups of the private endpoint allow inbound traffic from the ECS tasks.

For testing internal Application Load Balancers or EC2 instances, ensure that the VPC CIDR ranges don’t overlap and that the necessary routes are configured in the route tables.

 **Issue: Tests are completing but the results are not available on the UI**
+ Resolution:

If the test has completed but the results are not available in the UI, the result files should still be available in the S3 Bucket from the ECS tasks which ran the tests. This is a known limitation in the solution. In the current architecture, the solution uses a result parsing Lambda function to summarize the results from multiple ECS tasks, which are then stored as an item in the DynamoDB table. The DynamoDB table has a limit of 400 KB maximum item size. This limitation is reached depending on the complexity of the test script, the concurrency, and the number of tasks being used. The error does not mean the test is failing; it indicates that the process to summarize the results and store them in the DynamoDB table for CRUD operations has failed. The results are still available in the S3 bucket for the test scenario.

 **Issue: A Native mode test ends earlier than the script intended, and the run is recorded as complete**
+ Resolution:

The test reached its safety duration. In Native mode, your script decides when the run finishes, so the solution requires a safety duration and stops the testing framework when it elapses. The solution records the run as complete rather than failed and keeps the results for the portion that ran. Raise the safety duration above the longest run the script needs, up to the 24-hour maximum. For more information, refer to [Traffic shape modes](create-test-scenario.md#traffic-shape-modes).

 **Issue: A Native mode Locust test reports far fewer requests than the script generated**
+ Resolution:

Check whether your Locust script sets `processes`. The solution counts requests only when Locust runs as a single process, so a script that spawns worker processes under-reports its results. Remove the `processes` setting and scale the load with the task count instead, because each task already runs a full copy of the script. For more information, refer to [Locust tests](design-considerations.md#locust-script-support).

### ALB \+ ECS Fargate deployment issues
<a name="alb-ecs-troubleshooting"></a>

 **Issue: ACM certificate validation is stuck in "Pending validation" status**
+ Resolution:

If you requested a public ACM certificate using DNS validation, you must add the CNAME record provided by ACM to your DNS configuration. Navigate to the [ACM console](https://console.aws.amazon.com/acm/), expand the certificate details, and add the DNS validation record to your domain’s DNS provider. If you used email validation, check the email address associated with the domain for the validation email from AWS. For more information, refer to [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) in the *AWS Certificate Manager User Guide*.

 **Issue: Web console returns a "502 Bad Gateway" or "503 Service Temporarily Unavailable" error after deployment**
+ Resolution:

Check the ALB target group health checks in the [EC2 console](https://console.aws.amazon.com/ec2/home#TargetGroups). If the ECS Fargate tasks are showing as unhealthy, verify that the tasks are running in the [ECS console](https://console.aws.amazon.com/ecs/) and check the task logs in CloudWatch for errors. Ensure the security group attached to the ECS tasks allows inbound traffic from the ALB security group.

 **Issue: DNS is configured but the custom domain does not resolve to the web console**
+ Resolution:

Verify that the CNAME record is correctly configured in your DNS provider, mapping your custom domain (for example, `console.example.com`) to the ALB DNS name from the CloudFormation outputs. DNS propagation can take up to 48 hours depending on your DNS provider and TTL settings. You can verify the DNS record using `dig console.example.com CNAME` or `nslookup console.example.com`.

 **Issue: Web console returns a "403 Forbidden" error after deployment**
+ Resolution:

The AWS WAF web ACL deployed in front of the ALB may be blocking legitimate requests. Open the [AWS WAF console](https://console.aws.amazon.com/wafv2/), select the web ACL associated with the ALB, and check the **Sampled requests** tab to identify which rule is blocking the traffic. You can modify the WAF rules to allow the blocked requests. For example, if a managed rule group is producing false positives, you can set the specific rule action to **Count** instead of **Block** to allow the traffic while still logging it. For more information, refer to [Testing and tuning your AWS WAF protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html) in the *AWS WAF Developer Guide*.

### Headless (bring your own web server) deployment issues
<a name="self-hosted-troubleshooting"></a>

 **Issue: Web console displays CORS errors when connecting to the API**
+ Resolution:

Cross-Origin Resource Sharing (CORS) errors occur when the web console hosted on your domain attempts to call the solution’s API Gateway endpoints. Ensure that your web server is serving the console over HTTPS, as the API Gateway endpoints require HTTPS. Verify that the origin domain of your web server matches the allowed origins configured in the API Gateway CORS settings. If you are using a custom domain, you may need to update the API Gateway CORS configuration to include your domain.

 **Issue: Web console loads but authentication fails or redirects incorrectly**
+ Resolution:

The web console assets include a configuration file with the Cognito user pool settings and API endpoint URL. Verify that this configuration file was not modified during extraction. Ensure your web server is serving the console over HTTPS, as Cognito requires HTTPS for callback URLs. Check that the Cognito app client callback URL includes your web server’s domain.
