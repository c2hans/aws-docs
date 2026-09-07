---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/backend-for-frontend-api-gateway/backend-for-frontend-api-gateway.html
---

# Backend for Frontend Using API Gateway
<a name="backend-for-frontend-api-gateway"></a>

Publication date: **April 27, 2022 ([Diagram history](#diagram-history))**

This architecture shows how frontend client applications apply the Backend for Frontend (BFF) pattern to load UI-ready data projections and refresh the UI with event-driven notifications. You use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) WebSockets to push real-time updates when microservices raise events about mutations in domain aggregates.

## Backend for Frontend Using API Gateway
<a name="diagram1"></a>

![Architecture diagram showing a Backend for Frontend pattern using Amazon API Gateway, AWS Lambda, Amazon DynamoDB, and Amazon Cognito for real-time UI updates.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/backend-for-frontend-api-gateway/images/backend-for-frontend-api-gateway.png)

The following steps describe the architecture:

1. Purpose-built BFF event consumers catch events from your application and update denormalized data projections in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) for frontend consumption.

1. On UI load, frontend clients authenticate with [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html), then query data by invoking the BFF API built with API Gateway. The API fetches data from DynamoDB directly or through a BFF query handler built with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

1. Frontend clients subscribe for subsequent data changes by connecting to a BFF WebSocket endpoint provided by API Gateway, which triggers an update of the connected clients table.

1. BFF event consumers continue to process all relevant events from your application and update the denormalized frontend data view in real time.

1. Amazon DynamoDB Streams captures all events from data changes in the BFF database. A Lambda trigger asynchronously invokes a BFF stream-handler function when it detects new stream records.

1. The BFF stream handler pushes notifications to clients connected to API Gateway WebSockets.

1. Frontend clients receive the change notification from API Gateway and refresh the UI content.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 27, 2022 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
