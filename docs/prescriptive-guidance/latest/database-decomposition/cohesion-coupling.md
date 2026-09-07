---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/cohesion-coupling.html
---

# Analyzing cohesion and coupling for database decomposition
<a name="cohesion-coupling"></a>

This section helps you analyze coupling and cohesion patterns in your monolithic database to guide its decomposition. Understanding how database components interact and depend on each other is crucial for identifying natural break points, assessing complexity, and planning a phased migration approach. This analysis reveals hidden dependencies, highlights areas that are suitable for immediate separation, and helps you prioritize decomposition efforts while minimizing transformation risks. By examining both coupling and cohesion, you can make informed decisions about the component separation sequence in order to maintain system stability throughout the transformation process.

**This section contains the following topics:**
+ [About cohesion and coupling](#cohesion-coupling-about)
+ [Common coupling patterns in monolithic databases](#coupling-patterns)
+ [Common cohesion patterns in monolithic databases](#cohesion-patterns)
+ [Implementing low coupling and high cohesion](#cohesion-coupling-implementation)

## About cohesion and coupling
<a name="cohesion-coupling-about"></a>

*Coupling* measures the degree of interdependence between database components. In a well-designed system, you want to achieve loose coupling, where changes to one component have minimal impact on others. *Cohesion* measures how well the elements within a database component work together to serve a single, well-defined purpose. High cohesion indicates that a component's elements are strongly related and focused on a specific function. When decomposing a monolithic database, you must analyze both the cohesion within individual components and the coupling between them. This analysis helps you make informed decisions about how to break down the database while maintaining system integrity and performance.

The following image shows loose coupling with high cohesion. The components in the database work together to perform a specific function, and you minimize the impact of change on a single component. This is the ideal state.

![Components have loose coupling and high cohesion.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/d8340f09-3dfe-4427-98a4-3ef8d100d644.png)

The following image shows high coupling with low cohesion. The database components are disconnected, and changes are highly likely to impact other components.

![Components have high coupling and low cohesion.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/1ea05b97-30f1-4a19-a241-301655845a14.png)

## Common coupling patterns in monolithic databases
<a name="coupling-patterns"></a>

There are several coupling patterns that are commonly found when decomposing a monolithic database into microservice-specific databases. Understanding these patterns is crucial for successful database modernization initiatives. This section describes each pattern, its challenges, and best practices for reducing coupling.

### Implementation coupling pattern
<a name="implementation-coupling-pattern.4be458d0-04ad-5c8c-9bc1-8794adc9f2db"></a>

**Definition**: Components are tightly interconnected at the code and schema level. For example, modifying the structure of a `customer` table impacts `order`, `inventory`, and `billing` services.

**Modernization impact**: Each microservice requires its own dedicated database schema and data access layer.

**Challenges**:
+ Changes to shared tables affect multiple services
+ High risk of unintended side effects
+ Increased testing complexity
+ Difficult to modify individual components

**Best practices to reduce coupling**:
+ Define clear interfaces between components
+ Use abstraction layers to hide implementation details
+ Implement domain-specific schemas

### Temporal coupling pattern
<a name="temporal-coupling-pattern.0cc6ca82-6fbf-5ee1-a32d-5248aed14c73"></a>

**Definition**: Operations must run in a specific sequence. For example, order processing cannot proceed until inventory updates are complete.

**Modernization impact**: Each microservice needs autonomous data control.

**Challenges**:
+ Breaking synchronous dependencies between services
+ Performance bottlenecks
+ Difficult to optimize
+ Limited parallel processing

**Best practices to reduce coupling**:
+ Implement asynchronous processing where possible
+ Use event-driven architectures
+ Design for eventual consistency when appropriate

### Deployment coupling pattern
<a name="deployment-coupling-pattern.bb137e32-53b6-5f4b-be20-476f7352bbed"></a>

**Definition**: System components must be deployed as a single unit. For example, a minor change to the payment processing logic requires redeploying the entire database.

**Modernization impact**: Independent database deployments per service

**Challenges**:
+ High-risk deployments
+ Limited deployment frequency
+ Complex rollback procedures

**Best practices to reduce coupling**:
+ Break down into independently deployable components
+ Implement database sharding strategies
+ Use blue-green deployment patterns

### Domain coupling pattern
<a name="domain-coupling-pattern.f8fc9c7d-e94c-5afd-9f5d-8e68e7cf810c"></a>

**Definition**: Business domains share database structures and logic. For example, the `customer`, `order`, and `inventory` domains share tables and stored procedures.

**Modernization impact**: Domain-specific data isolation

**Challenges**:
+ Complex domain boundaries
+ Difficult to scale individual domains
+ Tangled business rules

**Best practices to reduce coupling**:
+ Identify clear domain boundaries
+ Separate data by domain context
+ Implement domain-specific services

## Common cohesion patterns in monolithic databases
<a name="cohesion-patterns"></a>

There are several cohesion patterns that are commonly found when evaluating database components for decomposition. Understanding these patterns is crucial for identifying well-structured database components. This section describes each pattern, its characteristics, and best practices for strengthening cohesion.

### Functional cohesion pattern
<a name="functional-cohesion-pattern.586b8d65-227a-50d5-a038-90fdc33a19d4"></a>

**Definition**: All elements directly support and contribute to performing a single, well-defined function. For example, all stored procedures and tables in a payment-processing module handle only payment-related operations.

**Modernization impact**: Ideal pattern for microservice database design

**Challenges**:
+ Identifying clear functional boundaries
+ Separating mixed-purpose components
+ Maintaining single responsibility

**Best practices to strengthen cohesion:**
+ Group related functions together
+ Remove unrelated functionality
+ Define clear component boundaries

### Sequential cohesion pattern
<a name="sequential-cohesion-pattern.ff193df4-4dbb-5978-8806-676175316bd6"></a>

**Definition**: Output from one element becomes input for another. For example, validation results for an order feed into order processing.

**Modernization impact**: Requires careful workflow analysis and data flow mapping

**Challenges**:
+ Managing dependencies between steps
+ Handling failure scenarios
+ Maintaining process order

**Best practices to strengthen cohesion:**
+ Document clear data flows
+ Implement proper error handling
+ Design clear interfaces between steps

### Communicational cohesion pattern
<a name="communicational-cohesion-pattern.94d7021f-aa47-5a4a-b366-ef843e4eccb9"></a>

**Definition**: Elements operate on the same data. For example, customer-profile management functions all work with customer data.

**Modernization impact**: Helps identify data boundaries for service separation to decrease coupling between modules

**Challenges**:
+ Determining data ownership
+ Managing shared data access
+ Maintaining data consistency

**Best practices to strengthen cohesion:**
+ Define clear data ownership
+ Implement proper data access patterns
+ Design effective data partitioning

### Procedural cohesion pattern
<a name="procedural-cohesion-pattern.7715ad2a-9343-5064-b1ae-f50bbc427071"></a>

**Definition**: Elements are grouped together because they must be executed in a specific order, but they may not be functionally related. For example, in order processing, a stored procedure that handles both order validation and user notification is grouped together simply because they happen in sequence, even though they serve different purposes and could be handled by separate services.

**Modernization impact**: Requires careful separation of procedures while maintaining process flow

**Challenges**:
+ Maintaining correct process flow after decomposition
+ Identifying true functional boundaries compared to procedural dependencies

**Best practices to strengthen cohesion:**
+ Separate procedures based on their functional purpose rather than execution order
+ Use orchestration patterns to manage process flow
+ Implement workflow management systems for complex sequences
+ Design event-driven architectures to handle process steps independently

### Temporal cohesion pattern
<a name="temporal-cohesion-pattern.a198384f-3966-5d2b-a493-d195de3a7939"></a>

**Definition**: Elements are related by timing requirements. For example, when an order is placed, several operations must execute together: inventory check, payment processing, order confirmation, and shipping notification must all occur within a specific time window to maintain a consistent order state.

**Modernization impact**: Might require special handling in distributed systems

**Challenges**:
+ Coordinating timing dependencies across distributed services
+ Managing distributed transactions
+ Confirming process completion across multiple components

**Best practices to strengthen cohesion:**
+ Implement proper scheduling mechanisms and timeouts
+ Use event-driven architectures with clear sequence handling
+ Design for eventual consistency with compensation patterns
+ Implement saga patterns for distributed transactions

### Logical or coincidental cohesion pattern
<a name="logical-or-coincidental-cohesion-pattern.d89288d1-5d33-5a8b-9942-553015341bc9"></a>

**Definition**: Elements are logically categorized to do the same things, even though they have weak or no meaningful relationships. An example is storing customer order data, warehouse inventory counts, and marketing email templates in the same database schema because they all relate to sales operations, despite having different access patterns, lifecycle management, and scaling requirements. Another example is combining order payment processing and product catalog management within the same database component because they're both part of the e-commerce system, even though they serve distinct business functions with different operational needs.

**Modernization impact**: Should be refactored or reorganized

**Challenges**:
+ Identifying better organization patterns
+ Breaking unnecessary dependencies
+ Restructuring components that were arbitrarily grouped

**Best practices to strengthen cohesion:**
+ Reorganize based on true functional boundaries and business domains
+ Remove arbitrary groupings based on superficial relationships
+ Implement proper separation of elements based on business capabilities
+ Align database components with their specific operational requirements

## Implementing low coupling and high cohesion
<a name="cohesion-coupling-implementation"></a>

### Best practices
<a name="best-practices.38b7a4eb-45a3-5da3-b7a2-1ea2b4ced18c"></a>

The following best practices can help you achieve low coupling:
+ Minimize dependencies between database components
+ Use well-defined interfaces for component interaction
+ Avoid shared state and global data structures

The following best practices can help you achieve high cohesion:
+ Group related data and operations together
+ Make sure that each component has a single, clear responsibility
+ Maintain clear boundaries between different business domains

### Phase 1: Map data dependencies
<a name="phase-1--map-data-dependencies.f0e7940a-2d18-5bfa-9bfa-bdc9a9b08474"></a>

Map data relationships and identify natural boundaries. You can use tools, such as [SchemaSpy](https://schemaspy.org/), to visualize the database by showing the tables in entity-relationship (ER) diagram. This provides a static analysis of the database and indicates some of the clear boundaries and dependencies within the database.

You can also export your database schemas in a graph database or in a Jupiter notebook. Then, you can apply clustering or interconnected components algorithms to identify natural boundaries and dependencies. Other AWS Partner tools, such as [CAST Imaging](https://www.castsoftware.com/imaging), can help to understand your database dependencies.

### Phase 2: Analyze transaction boundaries and access patterns
<a name="phase-2--analyze-transaction-boundaries-and-access-patterns.fc649980-5933-5940-8aab-b0ed6fe27fa4"></a>

Analyze transaction patterns to maintain atomicity, consistency, isolation, durability (ACID) properties and understand how data is accessed and modified. You can use database analysis and diagnosis tools, such as [Oracle Automatic Workload Repository (AWR)](https://docs.oracle.com/en-us/iaas/performance-hub/doc/awr-report-ui.html) or [PostgreSQL pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html). This analysis helps you understand who is accessing the database and what the transaction boundaries are. It can also help you understand the cohesion and coupling between tables at runtime. You can also use monitoring and profiling tools that can link code and database execution profiles, such as [Dynatrace AppEngine](https://www.dynatrace.com/platform/appengine/).

AI tools, such as [vFunction](https://vfunction.com/), can help you identify domain boundaries by analyzing the application's functional and domain boundaries. Although vFunction primarily analyzes the application layer, its insights can guide the decomposition of both the application and the database, supporting alignment with business domains.

### Phase 3: Identify self-contained tables
<a name="phase-3--identify-self-contained-tables.73168f97-7c70-5b92-abb8-1e5f6a516f99"></a>

Look for tables that demonstrate two key characteristics:
+ High cohesion – The table's contents are strongly related to each other
+ Low coupling – They have minimal dependencies on other tables.

The following coupling-cohesion matrix can help you identify the difficulty of decoupling each table. Tables that appear in the upper-right quadrant of this matrix are ideal candidates for initial decoupling efforts because they're the easiest to separate. In an ER diagram, these tables have few foreign key relationships or other dependencies. After you have decoupled these tables, progress toward tables with more complex relationships.

![Upper-right quadrant is easy, and lower-left quadrant is hard.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/40a152be-d75b-4a39-b9b0-56dbf1f8e265.png)

**Note**
Database structure often mirrors application architecture. Tables that are easier to decouple at the database level typically correspond to components that are easier to convert into microservices at the application level.
