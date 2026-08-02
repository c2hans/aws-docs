---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/apis.html
---

# Managing APIs
<a name="apis"></a>

Proper API management makes your microservices accessible to both internal and external consumers. AWS offers a variety of services that you can use together to securely expose your microservice APIs. These services enable you to enforce security for your APIs and implement monitoring and observability from a central location. You can also use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) to improve performance if the users of your APIs are geographically distant from the AWS Region that the services are hosted in.

## Amazon API Gateway
<a name="api-gateway"></a>

[Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) is a fully managed service that enables developers to create, publish, maintain, monitor, and secure REST and WebSocket APIs at any scale. You can use API Gateway to implement many of the patterns described in the [Communication patterns](communication-patterns.md) section of this guide.

There are two main types of REST APIs: REST and HTTP. Both types support RESTful APIs but offer different features. To determine which best fits your needs, see [Choose between REST APIs and HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html) in the API Gateway documentation. This section of the guide focuses on API Gateway REST APIs.

Using API Gateway as the entry point for your APIs provides a single place to implement common concerns, such as request validation and security. API Gateway REST APIs offer [request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html), which allows you to define the format of your requests by using [JSON Schema](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04). API Gateway validates incoming requests against your defined schema and rejects malformed requests.

### Authentication and authorization
<a name="authentication-and-authorization.dfdcaf25-c4a7-56c9-9638-68f81d08aa5d"></a>

API Gateway REST APIs support the following authentication (authN) and authorization (authZ) mechanisms:
+ **IAM** – If you use IAM, the requests to your API must be signed by using [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html).
+ **Amazon Cognito** – API Gateway will validate a presented bearer token as having been issued by an Amazon Cognito user pool. You can also configure your Amazon Cognito user pool to integrate with a third-party identity provider (IdP), if you're already using one. You can also use an Amazon Cognito user pool for machine-to-machine (M2M) authentication.
+ **AWS Lambda authorizer** – API Gateway will invoke a Lambda function that you specify to perform any checks you would like, to determine whether a request should be authorized.

For more information, see [Control and manage access to REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) in the API Gateway documentation.

### API keys and rate limits
<a name="api-keys-and-rate-limits.778847de-8814-5d08-a921-9c84fe8ef8c3"></a>

You can control who is allowed to call your APIs and at what rate by using API keys and usage plans. API keys should not be used for authentication but can be used in conjunction with the schemes mentioned earlier. Users don't always need to provide their own API key—for example, Lambda authorizers can return an API key for a user. The usage plan allows you to specify the throughput, burst limit, and monthly quota. For more information, see [Usage plans and API keys for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the API Gateway documentation.

### Public and private APIs
<a name="public-and-private-apis.4f93cd9b-e479-588b-8ff3-38b61b6c2dcc"></a>

API Gateway REST APIs that are accessible through the internet support two endpoint types:
+ Edge-optimized, which means that callers' requests are routed to a nearby CloudFront point of presence (POP). This can result in improved performance for geographically disparate clients.
+ Regional, which means that requests route to a resource within a specific AWS Region. This is a good choice when all your clients are near the Region where your API is deployed.

API Gateway REST APIs also support private API endpoints, which are accessible from a virtual private cloud (VPC) by using an interface VPC endpoint. You can also securely share private REST APIs by creating interface VPC endpoints in other VPCs and even other AWS accounts. For more information, see [API endpoint types for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html) in the API Gateway documentation.

### When to use API Gateway
<a name="when-to-use-9999999999999999abp-.0d305a6f-9f53-554c-9b2b-39cc6228f65c"></a>

API Gateway is a good choice for RESTful web services and real-time WebSocket connections. When you use WebSocket APIs in API Gateway, you can add behavior for connect and disconnect events, such as storing connection IDs in an external data store that's associated with client attributes. You can also route requests to custom behaviors by using message attributes.

Both REST and WebSocket APIs can directly integrate with many AWS services without requiring separate compute resources such as Lambda functions. This can improve performance and reduce cost.

REST APIs support both path-based and header-based routing, and you can use them separately or together. A common pattern is to provide a REST API as a front door for a number of APIs, to implement shared concerns as discussed earlier, and then behave like a reverse proxy and route authorized requests to the correct API endpoint.
