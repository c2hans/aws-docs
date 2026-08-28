---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/external-data-avp.html
---

# Retrieving external data for a PDP in Amazon Verified Permissions
<a name="external-data-avp"></a>

Amazon Verified Permissions doesn't support retrieving external data for a PDP, but it can store user-provided data as part of its schema. As in OPA, if all data for an authorization decision can be provided as part of an authorization request or as part of a JSON Web Token (JWT) that is passed as part of the request, no additional configuration is required. However, you can provide additional data from external sources to Verified Permissions through the authorization request as part of an application's authorizer service that calls Verified Permissions. For example, an application's authorizer service can query an external source such as DynamoDB or Amazon RDS for data, and these services can then include the externally provided data as part of an authorization request.

The following diagram shows an example of how additional data can be retrieved and incorporated into a Verified Permissions authorization request. It might be necessary to use this method to retrieve data such as RBAC role mappings, to retrieve additional attributes that are relevant to resources or principals, or in cases where data resides in different parts of an application and cannot be provided through an identity provider (IdP) token.

![Retrieving external data with Amazon Verified Permissions](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/e17aad23-26ba-4de7-9272-2914afb421ec.png)

The diagram includes a feature of Amazon API Gateway called a[ Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html). Although this feature might not be available for APIs that are provided by other services or applications, you can replicate the general model of using an authorizer to fetch additional data to incorporate into a Verified Permissions authorization request across a multitude of use cases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
