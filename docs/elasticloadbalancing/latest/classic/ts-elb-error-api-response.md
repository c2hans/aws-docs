---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ts-elb-error-api-response.html
---

# Troubleshoot a Classic Load Balancer: API errors
<a name="ts-elb-error-api-response"></a>

The following are error messages returned by Elastic Load Balancing API, the potential causes, and the steps you can take to resolve the issues.

**Topics**
+ [CertificateNotFound: Undefined](#ts-elb-error-message-certificate)
+ [OutofService: A transient error occurred](#ts-elb-error-message-service)

## CertificateNotFound: Undefined
<a name="ts-elb-error-message-certificate"></a>

**Cause 1**: There is a delay in propagating the certificate to all Regions when it is created using the AWS Management Console. When this delay occurs, the error message is shown in the last step in the process of creating the load balancer.

**Solution 1**: Wait approximately 15 minutes and then try again. If the problem persists, go to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) for assistance.

**Cause 2**: If you are using the AWS CLI or API directly, you can receive this error if you provide an Amazon Resource Name (ARN) for a certificate that does not exist.

**Solution 2**: Use the AWS Identity and Access Management (IAM) action [GetServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServerCertificate.html) to get the certificate ARN and verify that you provided the correct value for the ARN.

## OutofService: A transient error occurred
<a name="ts-elb-error-message-service"></a>

**Cause**: There is a transient internal problem within the Elastic Load Balancing service or the underlying network. This temporary issue might also occur when Elastic Load Balancing queries the health of the load balancer and its registered instances.

**Solution**: Retry the API call. If the problem persists, go to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) for assistance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
