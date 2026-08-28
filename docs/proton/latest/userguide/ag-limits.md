---
source_url: https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html
---

End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October 7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure will remain intact. For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# AWS Proton quotas
<a name="ag-limits"></a>

The following table lists AWS Proton quotas. All values are per AWS account, per supported AWS Region.

| Resource quota | Default limit | Adjustable? |
| --- | --- | --- |
| Maximum size of template bundle | 10 MB |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum size of template manifest file | 2 MB |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum size of template schema file | 2 MB |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum size of each template file | 2 MB |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum length of each template name | 100 characters |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum number of CloudFormation template files per bundle | 1 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum number of registered templates per account, service and environment templates combined | 1000 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |
| Maximum number of template versions registered per template | 1000 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |
| Maximum number of files per CodeBuild Provisioning bundle | 500 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-no.png) No |
| Maximum number of environments per account | 1000 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |
| Maximum number of services per account | 1000 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |
| Maximum number of service instances per service | 20 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |
| Maximum number of components per account | 1000 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |
| Maximum number of environment account connections per environment account | 1000 |  ![](http://docs.aws.amazon.com/proton/latest/userguide/images/icon-yes.png) Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
