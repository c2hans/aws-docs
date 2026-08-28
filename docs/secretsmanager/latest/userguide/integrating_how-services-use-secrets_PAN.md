---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_PAN.html
---

# How AWS Panorama uses Secrets Manager
<a name="integrating_how-services-use-secrets_PAN"></a>

AWS Panorama is a service that brings computer vision to your on-premises camera network. You use AWS Panorama to register an appliance, update its software, and deploy applications to it. When you register a video stream as a data source for your application, if the stream is password protected, AWS Panorama stores the credentials for it in a Secrets Manager secret. For more information, see [Managing camera streams in AWS Panorama](https://docs.aws.amazon.com/panorama/latest/dev/appliance-cameras.html) in the *AWS Panorama Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
