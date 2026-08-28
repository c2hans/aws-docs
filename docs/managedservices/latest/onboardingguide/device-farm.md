---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/device-farm.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Use AMS SSP to provision AWS Device Farm in your AMS account
<a name="device-farm"></a>

Use AMS Self-Service Provisioning (SSP) mode to access AWS Device Farm capabilities directly in your AMS managed account. AWS Device Farm is an application testing service that lets you improve the quality of your web and mobile apps by testing them across an extensive range of desktop browsers and real mobile devices; without having to provision and manage any testing infrastructure. The service enables you to run your tests concurrently on multiple desktop browsers or real devices to speed up the execution of your test suite, and generates videos and logs to help you quickly identify issues with your app.

To learn more, see [AWS Device Farm](https://aws.amazon.com/device-farm/).

## AWS Device Farm in AWS Managed Services FAQ
<a name="device-farm-faqs"></a>

**Q: How do I request access to AWS Device Farm in my AMS account?**

Request access by submitting a Management \| AWS service \| Self-provisioned service \| Add (managed automation) (ct-3qe6io8t6jtny) change type. This RFC provisions the following IAM role to your account: `customer_devicefarm_role`.

Once provisioned in your account, you must onboard the roles in your federation solution.

**Q: What are the restrictions to using AWS Device Farm in my AMS account?**

Full access to the AWS Device Farm service is provided with the exception of using the AMS namespace in the 'Name' tag.

**Q: What are the prerequisites or dependencies to using AWS Device Farm in my AMS account?**

None.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
