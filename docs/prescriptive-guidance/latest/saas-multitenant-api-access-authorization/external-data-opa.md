---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/external-data-opa.html
---

# Retrieving external data for a PDP in OPA
<a name="external-data-opa"></a>

For OPA, if all data required for an authorization decision can be provided as input or as part of a JSON Web Token (JWT) passed as a component of the query, no additional configuration is required. (It is relatively simple to pass JWTs and SaaS context data to OPA as part of query input.) OPA can accept arbitrary JSON input in what is called the *overload input* approach. If a PDP requires data beyond what can be included as input or a JWT, OPA provides several options for retrieving this data. These include bundling, pushing data (replication), and dynamic data retrieval.

## OPA bundling
<a name="opa-bundling"></a>

The OPA bundling feature supports the following process for external data retrieval:

1. The policy enforcement point  (PEP) requests an authorization decision.

1. OPA downloads new policy bundles, including external data.

1. The bundling service replicates data from data source(s).

When you use the bundling feature, OPA periodically downloads policy and data bundles from a centralized bundle service. (OPA doesn't provide the implementation and setup of a bundle service.) All policies and external data that are pulled from the bundle service are stored in memory. This option will not work if the external data size is too large to be stored in memory, or if the data changes too frequently.

For more information about the bundling feature, see the [OPA documentation](https://www.openpolicyagent.org/docs/latest/external-data/#option-3-bundle-api).

## OPA replication (pushing data)
<a name="opa-replication"></a>

The OPA replication approach supports the following process for external data retrieval:

1. The PEP requests an authorization decision.

1. The data replicator pushes data to OPA.

1. The data replicator replicates data from data source(s).

In this alternative to the bundling approach, data is pushed to, instead of being periodically pulled by, OPA. (OPA doesn't provide the implementation and setup of a replicator.) The push approach has the same data size limitations as the bundling approach, because OPA stores all the data in memory. The primary advantage of the push option is that you can update data in OPA with deltas instead of replacing all the external data each time. This makes the push option more appropriate for datasets that change frequently.

For more information about the replication option, see the [OPA documentation](https://www.openpolicyagent.org/docs/latest/external-data/#option-4-push-data).

## OPA dynamic data retrieval
<a name="opa-dynamic-data-retrieval"></a>

If the external data to be retrieved is too large to be cached in OPA's memory, the data can be dynamically pulled from an external source during the evaluation of an authorization decision. When you use this approach, data is always up to date. This approach has two drawbacks: network latency and accessibility. Currently, OPA can retrieve data at runtime only through an HTTP request. If the calls that go to an external data source cannot return data as an HTTP response, they require a custom API or some other mechanism to provide this data to OPA. Because OPA can retrieve data only through HTTP requests, and the speed of retrieving the data is pivotal, we recommend that you use an AWS service such as Amazon DynamoDB to hold external data when possible.

For more information about the pull approach, see the [OPA documentation](https://www.openpolicyagent.org/docs/latest/external-data/#option-5-pull-data-during-evaluation).

## Using an authorization service for implementation with OPA
<a name="using-an-authorization-service-for-implementation-with-opa"></a>

When you fetch external data by using bundling, replication, or a dynamic pull approach, we recommend that the authorization service facilitate this interaction. This is because the authorization service can retrieve external data and transform it into JSON for OPA to make authorization decisions. The following diagram shows how an authorization service can function with these three external data retrieval approaches.

![Retrieving external data with OPA](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/f8c9bbba-e8dd-4f17-b509-7e9a6ae076dd.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
