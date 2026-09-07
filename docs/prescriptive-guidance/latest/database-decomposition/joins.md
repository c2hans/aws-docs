---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/joins.html
---

# Decoupling table relationships during database decomposition
<a name="joins"></a>

This section provides guidance on breaking down complex table relationships and JOIN operations during monolithic database decomposition. A table *join* combines rows from two or more tables based on a related column between them. The goal of separating these relationships is to reduce high coupling between tables while maintaining data integrity across microservices.

**This section contains the following topics:**
+ [Denormalization strategy](#joins-denormalization)
+ [Reference-by-key strategy](#joins-reference-by-key)
+ [CQRS pattern](#joins-cqrs)
+ [Event-based data synchronization](#joins-event-based-synchronization)
+ [Implementing alternatives to table joins](#joins-implementing-alternatives)
+ [Scenario-based example](#joins-example)

## Denormalization strategy
<a name="joins-denormalization"></a>

*Denormalization* is a database design strategy that involves intentionally introducing redundancy by combining or duplicating data across tables. When breaking apart a large database into small databases, it might make sense to duplicate some data across services. For example, storing basic customer details, such as name and email addresses, in both a marketing service and an order service eliminates the need for constant cross-service lookups. The marketing service might need customer preferences and contact information for campaign targeting, while the order service requires the same data for order processing and notifications. While this creates some data redundancy, it can significantly improve service performance and independence, allowing the marketing team to operate their campaigns without depending on real-time customer service lookups.

When implementing denormalization, focus on frequently accessed fields that you identify through careful analysis of data access patterns. You can use tools, such Oracle AWR reports or pg\_stat\_statements, to understand which data is commonly retrieved together. Domain experts can also provide valuable insights into natural data groupings. Remember that denormalization isn't an all-or-nothing approach—only duplicate data that demonstrably improves system performance or reduces complex dependencies.

## Reference-by-key strategy
<a name="joins-reference-by-key"></a>

A *reference-by-key strategy* is a database design pattern where relationships between entities are maintained through unique keys rather than storing the actual related data. Instead of traditional foreign key relationships, modern microservices often store just the unique identifiers of related data. For example, rather than keeping all customer details in the order table, the order service only stores the customer ID and retrieves additional customer information through an API call when needed. This approach maintains service independence while ensuring access to related data.

## CQRS pattern
<a name="joins-cqrs"></a>

The *Command Query Responsibility Segregation (CQRS)* pattern separates the read and write operations of a data store. This pattern is particularly useful in complex systems with high-performance requirements, especially those with asymmetric read/write loads. If your application frequently needs data combined from multiple sources, you can create a dedicated CQRS model instead of complex joins. For example, rather than joining `Product`, `Pricing`, and `Inventory` tables on every request, maintain a consolidated `Product Catalog` table that contains the necessary data. The benefits of this approach can outweigh the costs of the additional table.

Consider a scenario where `Product`, `Price`, and `Inventory` services frequently need product information. Instead of configuring these services to directly access shared tables, create a dedicated `Product Catalog` service. This service maintains its own database that contains the consolidated product information. It acts as a single source of truth for product-related queries. When product details, prices, or inventory levels change, respective services can publish events to update the `Product Catalog` service. This provides data consistency while maintaining service independence. The following image shows this configuration, where [Amazon EventBridge](https://aws.amazon.com/eventbridge/) serves as an event bus.

![An event bus updates the Product Catalog service.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/d0700b6a-cd9b-4aaa-98fd-7044413e4fc7.png)

As discussed in [Event-based data synchronization](#joins-event-based-synchronization), the next section, keep the CQRS model updated through events. When product details, prices, or inventory levels change, the respective services publish events. The `Product Catalog` service subscribes to these events and updates its consolidated view. This provides fast reads without complex joins, and it maintains service independence.

## Event-based data synchronization
<a name="joins-event-based-synchronization"></a>

*Event-based data synchronization* is a pattern where changes to data are captured and propagated as events, which enables different systems or components to maintain synchronized data states. When data changes, instead of updating all related databases immediately, publish an event to notify subscribed services. For example, when a customer changes their shipping address in the `Customer` service, a `CustomerUpdated` event initiates updates to the `Order` service and `Delivery` service on each service's schedule. This approach replaces rigid table joins with flexible, scalable event-driven updates. Some services might briefly have outdated data, but the trade-off is improved system scalability and service independence.

## Implementing alternatives to table joins
<a name="joins-implementing-alternatives"></a>

Begin your database decomposition with read operations because they're typically simpler to migrate and validate. After read paths are stable, tackle the more complex write operations. For critical, high-performance requirements, consider implementing the [CQRS pattern](#joins-cqrs). Use a separate, optimized database for reads while maintaining another for writes.

Build resilient systems by adding retry logic for cross-service calls and implementing appropriate caching layers. Monitor service interactions closely, and set up alerts for data consistency issues. The end goal isn't perfect consistency everywhere—it's creating independent services that perform well while maintaining acceptable data accuracy for your business needs.

The decoupled nature of microservices introduces the following new complexities in data management:
+ Data is distributed. Data now resides in separate databases, which are managed by independent services.
+ Real-time synchronization across services is often impractical, necessitating an eventual consistency model.
+ Operations that previously occurred within a single database transaction now span multiple services.

To address these challenges, do the following:
+ **Implement an event-driven architecture** – Use message queues and event publishing to propagate data changes across services. For more information, see [Building Event Driven Architectures](https://serverlessland.com/event-driven-architecture/intro) on Serverless Land.
+ **Adopt the saga orchestration pattern** – This pattern helps you manage distributed transactions and maintain data integrity across services. For more information, see [Building a serverless distributed application using a saga orchestration pattern](https://aws.amazon.com/blogs/compute/building-a-serverless-distributed-application-using-a-saga-orchestration-pattern/) on AWS Blogs.
+ **Design for failure** – Incorporate retry mechanisms, circuit breakers, and compensating transactions to handle network issues or service failures.
+ **Use version stamping** – Track data versions to manage conflicts and make sure that the most recent updates are applied.
+ **Regular reconciliation** – Implement periodic data synchronization processes to catch and correct any inconsistencies.

## Scenario-based example
<a name="joins-example"></a>

The following schema example has two tables, a `Customer` table and an `Order` table:

```
-- Customer table
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP
);

-- Order table
CREATE TABLE order (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

The following is an example of how you could use a denormalized approach:

```
CREATE TABLE order (
    order_id INT PRIMARY KEY,
    customer_id INT,                  -- Reference only
    customer_first_name VARCHAR(100), -- Denormalized
    customer_last_name VARCHAR(100),  -- Denormalized
    customer_email VARCHAR(255),      -- Denormalized
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(50)
);
```

The new `Order` table has customer name and email addresses that are denormalized. The `customer_id` is referenced, and there is no foreign key constraint with the `Customer` table. The following are the benefits of this denormalized approach:
+ The `Order` service can display order history with customer details, and it doesn't require API calls to the `Customer` microservice.
+ If the `Customer` service is down, the `Order` service remains fully functional.
+ Queries for order processing and reporting run faster.

The following diagram shows a monolithic application that retrieves order data using `getOrder(customer_id)`, `getOrder(order_id)`, `getCustomerOders(customer_id)`, and `createOrder(Order order)` API calls to the `Order` microservice.

![A monolithic application retrieving data from a microservice with a dedicated database.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/e1be89e3-4260-4d51-bfa4-054a815be799.png)

During the microservices migration, you can maintain the `Order` table in the monolithic database as a transitional safety measure, ensuring that the legacy application remains functional. However, it's crucial that all new order-related operations are routed through the `Order` microservice API, which maintains its own database while simultaneously writing to the legacy database as a backup. This dual-write pattern provides a safety net. It allows for gradual migration while maintaining system stability. After all customers have successfully migrated to the new microservice, you can deprecate the legacy `Order` table in the monolithic database. After decomposing the monolithic application and its database into separate `Customer` and `Order` microservices, maintaining data consistency becomes the primary challenge.
