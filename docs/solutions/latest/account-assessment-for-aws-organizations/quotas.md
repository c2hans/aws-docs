---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this guidance
<a name="quotas-for-aws-services-in-this-guidance"></a>

Make sure you have sufficient quota for each of the [services implemented in this guidance](aws-services.md). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Select one of the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.
+  [Lambda](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)
+  [Step Functions](https://docs.aws.amazon.com/general/latest/gr/step-functions.html)
+  [DynamoDB](https://docs.aws.amazon.com/general/latest/gr/ddb.html)
+  [API Gateway](https://docs.aws.amazon.com/general/latest/gr/apigateway.html)
+  [Amazon S3](https://docs.aws.amazon.com/general/latest/gr/s3.html)
+  [Amazon CloudFront](https://docs.aws.amazon.com/general/latest/gr/cf_region.html)
+  [Cognito](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html)
+  [AWS WAF](https://docs.aws.amazon.com/general/latest/gr/waf.html)
+  [AWS X-Ray](https://docs.aws.amazon.com/general/latest/gr/xray.html)

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has [AWS CloudFormation](https://aws.amazon.com/cloudformation/) quotas that you should be aware of when [deploying the stack](step-3-launch-the-spoke-stack.md) in this guidance. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this guidance successfully. For more information, refer to [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*.

## AWS Lambda quotas
<a name="aws-lambda-quotas"></a>

In the hub account, the Step Function invokes up to 100 Lambda functions to run the scan in parallel across multiple accounts and services. [Review](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) and [increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) your Lambda funtion’s concurrency limit to avoid throttling.

## AWS Step Functions quotas
<a name="aws-step-functions-quotas"></a>

A Step Function execution failure can occur due to maximum input or output size for a task, state, or execution quota of 262,144 bytes of data as a UTF-8 encoded string, or maximum execution history size of 25,000 events in a single state machine execution history. For example:
+  **Scenario 1** - You scan resources in 25 supported services with a maximum of 100 accounts in a job. If you increase the number of accounts, you will reach maximum execution history size of 25,000 events.
+  **Scenario 2** - You scan 8,000 accounts with a maximum of 3 services in a job. If you add more accounts, you will reach maximum input or output size for a task, state, or execution quota of 262,144 bytes of data.

To avoid reaching the quota for large-scale scans, we recommend that you define your batch size (number of accounts • number of services) per scan.
