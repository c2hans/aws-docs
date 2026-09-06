---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/supported-datasources.html
---

# Supported data sources
<a name="supported-datasources"></a>

**AWS Lambda**

Lambda functions are ideal for event processing in AWS AppSync Events. They execute in response to triggers and process events (JSON documents containing event data). Lambda functions can transform event data, perform business logic, or integrate with other AWS services. Lambda is particularly useful when you need custom event processing logic or integration with external services. In your channel namespace integrations, you can write code in your onPublish or onSubscribe handlers to invoke your Lambda function. Alternately, you can configure a direct integration without writing any code. AWS AppSync Events will directly call your Lambda function with the request context.

**Amazon DynamoDB**

DynamoDB provides scalable storage for event-driven applications. The core component is the table, which stores collections of data. Tables can store event data, application state, or any other structured information. Each entry in a table is stored as an item, containing multiple attributes (fields). For example, an item might include attributes like eventId, timestamp, and payload.

DynamoDB is particularly effective for event storage and processing due to its high throughput and low latency. AWS AppSync Events can interact with DynamoDB tables to store, retrieve, and modify event data as needed.

**Amazon RDS**

Amazon RDS provides managed relational databases that can be used to store structured event data or application state. You can use a database instance with your preferred DB engine, such as PostgreSQL or MySQL, to maintain relational data that is relevant to your event processing workflow.

Amazon RDS is particularly useful when you need to maintain relationships between different types of events or when you need ACID compliance for your event data.

**Amazon EventBridge**

EventBridge complements AWS AppSync Events by providing event buses that can route events between different services. An event bus receives events from event sources and processes them based on rules. Each rule follows an event pattern that determines which events get routed to which targets.

EventBridge integration allows AWS AppSync Events to participate in broader event-driven architectures, either as a source or target of events.

**Amazon OpenSearch Service**

OpenSearch Service enables full-text search and analytics on your event data. You can create nodes containing indices to store and search event information. Data is stored as JSON documents within shards, enabling efficient searching and analysis of event data.

**HTTP endpoints**

HTTP endpoints can be used as data sources to integrate with external services or APIs. AWS AppSync Events can send HTTP requests with event data and process the responses as part of your event handling workflow. Each data source type has its own strengths and use cases in event-driven architectures. You can combine multiple data sources within a single AWS AppSync Events API to create sophisticated event processing workflows. You can also use an HTTP endpoint data source to interact with any AWS service API.

**Amazon Bedrock**

Amazon Bedrock enables AWS AppSync to integrate directly with foundation models for AI/ML capabilities. Through this data source, you can incorporate generative AI features into your event processing workflows without managing complex ML infrastructure. Amazon Bedrock provides access to various foundation models from leading AI companies, including Anthropic, AI21 Labs, Cohere, Meta, Stability AI, and Amazon.
