---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the solution.

If these instructions don’t address your issue, [Contact AWS Support](contact-aws-support.md) provides instructions for opening an AWS Support case for this solution.

## Problem: Failed job
<a name="failed-job"></a>

If a job fails for any of the assessments, the web UI will display an error message, and the **Job History** page will show the status of the job as `FAILED`.

![Screenshot of failed job](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/image11.png)

### Resolution
<a name="failed-job-resolution"></a>

If you wish to determine the failure’s root cause, you can use [X-Ray traces](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-traces.html) to identify the resource that returned the error code. For example, if a Lambda function has failed to retrieve the list of delegated admin accounts, the X-Ray trace will direct you to the Lambda function and respective CloudWatch logs. Then you can examine the logs to determine the root cause. In addition, [X-Ray service maps](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html) identify services where errors are occurring, connections with high latency, or traces for requests that were unsuccessful. These maps can be helpful, for example, when [investigating APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-using-xray-maps.html#apigateway-using-xray-maps-active) and their downstream services.

For example, if your job failed due to the following error:

```
"Error": "Lambda.TooManyRequestsException"
"Cause": "Rate Exceeded
```

this indicates that you need to [check the Lambda function concurrent executions quota](https://console.aws.amazon.com/servicequotas/home/services/lambda/quotas) for the hub account. By default, this solution requires up to 100 Lambda concurrent executions. To request a quota increase, select **Concurrent executions** and choose **Request quota increase**. See [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide* for more information.

![Screenshot of Lambda resource quotas](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/image22.png)

## Problem: Failed Resource-Based Policies scan
<a name="failed-resource-based-policy-scan"></a>

This assessment type initiates an asynchronous Step Functions state machine execution to scan the resources in the spoke and member accounts.

### Resolution
<a name="failed-resource-based-policy-scan-resolution"></a>

If the state machine execution fails, you can view the [specific X-Ray trace](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-xray-tracing.html#xray-concept-tracing-details) for the failed state machine execution. You can either click on the state machine **FailJob** state to view the details in the **Input and Output** tab (see Figure 2) or use the [X-Ray details](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-xray-tracing.html#concepts-xray-tracing-segments) to help you identify the specific resource in the state machine where the failure occurred (see Figure 3).

![Screenshot of state machine failure details](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/image12.png)

![Screenshot of state machine failure details in X-Ray](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/image13.png)

To view the error details, click on the resource and select the **Exceptions** tab. This can help you identify the Lambda function name where the failure occurred and will display the same error from the state machine output. Note that the same exception will be logged in the CloudWatch logs.

![Screenshot of exceptions tab data](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/image14.png)

## Problem: Access denied
<a name="access-denied"></a>

You may receive an `AccessDenied` error for a specific account in ** Failed Tasks During Scan**.

### Resolution
<a name="access-denied-resolution"></a>

 [Deploy the Spoke stack](step-2-launch-the-spoke-stack.md) in the account to allow the scan to complete.

![Screenshot of AccessDenied error](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/image15.png)

## Problem: Undefined error
<a name="unidefined-error"></a>

The Web UI loads, but starting scans or viewing findings causes an `undefined error`.

### Resolution
<a name="undefined-error-resolution"></a>

The Web UI may be blocked from calling the API Gateway by AWS WAF. Check if your current IP address is within the range of valid IP addresses that you defined for the AWS WAF. Then open the AWS WAF console to investigate what reason your requests are blocked.

## Problem: Access denied after redeploying Hub Stack
<a name="access-denied-after-redeploying-hub-stack"></a>

If you delete and redeploy the Hub Stack while leaving Spoke Stacks and Org Management Stack in place, you will receive Access Denied errors. The trust policy in the spoke role and org management role references the Hub Stack. During deletion of the Hub Stack, IAM will break those references and redeploying the Hub Stack does not restore them.

### Resolution
<a name="access-denied-after-redeploying-hub-stack-resolution"></a>

Delete and redeploy the Spoke Stacks and the Org Management Stack after redeploying the Hub Stack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
