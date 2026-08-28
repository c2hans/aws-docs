---
source_url: https://docs.aws.amazon.com/sap/latest/general/application-integration.html
---

# Application integration
<a name="application-integration"></a>

Deploy [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to extract data out of SAP S/4HANA via `HTTP` API. API Gateway can consume data from IDOC, BAPI, and RFC. These need to be translated to a web service call. For more information, see [AWS blogs](https://aws.amazon.com/blogs/awsforsap/category/application-services/amazon-api-gateway-application-services/). The following image shows this scenario.

![Data flow with Amazon API Gateway.](http://docs.aws.amazon.com/sap/latest/general/images/data-integration.png)

Data flow

1. RISE with SAP VPC is connected to your AWS account not managed by SAP, via AWS Transit Gateway.

1. Amazon API Gateway is configured to route the authentication to AWS Lambda and Amazon Cognito

1. Amazon Cognito authenticates the session.

1. Once authenticated, Amazon API Gateway routes the package to AWS Lambda.

1.  AWS Lambda stores the data in an Amazon S3 bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
