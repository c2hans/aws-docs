---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/api-composition.html
---

# API composition pattern
<a name="api-composition"></a>

This pattern uses an API composer, or aggregator, to implement a query by invoking individual microservices that own the data. It then combines the results by performing an in-memory join.

The following diagram illustrates how this pattern is implemented.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/a2d3fb7d-3374-4e19-9050-0e554d4d6cd4.png)

The diagram shows the following workflow:

1. An API gateway serves the "/customer" API, which has an "Orders" microservice that tracks customer orders in an Amazon Aurora database.

1. The "Support" microservice tracks customer support issues and stores them in an Amazon OpenSearch Service database.

1. The "CustomerDetails" microservice maintains customer attributes (for example, address, phone number, or payment details) in an Amazon DynamoDB table.

1. The "GetCustomer" AWS Lambda function runs the APIs for these microservices, and performs an inmemory join on the data before returning it to the requester. This helps easily retrieve customer information in one network call to the user-facing API, and keeps the interface very simple.

The API composition pattern offers the simplest way to gather data from multiple microservices. However, there are the following disadvantages to using the API composition pattern:
+ It might not be suitable for complex queries and large datasets that require in-memory joins.
+ Your overall system becomes less available if you increase the number of microservices connected to the API composer.
+ Increased database requests create more network traffic, which increases your operational costs.
