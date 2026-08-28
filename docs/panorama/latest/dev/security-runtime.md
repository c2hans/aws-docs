---
source_url: https://docs.aws.amazon.com/panorama/latest/dev/security-runtime.html
---

End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

# Runtime environment software in AWS Panorama
<a name="security-runtime"></a>

AWS Panorama provides software that runs your application code in an Ubuntu Linux–based environment on the AWS Panorama Appliance. AWS Panorama is responsible for keeping software in the appliance image up to date. AWS Panorama regularly releases software updates, which you can apply by [using the AWS Panorama console](appliance-manage.md#appliance-manage-software).

You can use libraries in your application code by installing them in the application's `Dockerfile`. To ensure application stability across builds, choose a specific version of each library. Update your dependencies regularly to address security issues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
