---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step3.html
---

# Step 3. Identify your data access patterns
<a name="step3"></a>

## Objective
<a name="obj3"></a>
+ Document the data access patterns.

## Process
<a name="proc3"></a>
+ Database engineer and business analyst interview the end users to identify how data will be queried using the data-access patterns matrix template.
  + For new applications, they review user stories about activities and objectives. They document the use cases and analyze the access patterns that the use cases require.
  + For existing applications, they analyze query logs to find out how people are currently using the system and to identify the key access patterns.
+ Database engineer identifies the following properties of the access patterns:
  + Data size: Knowing how much data will be stored and requested at one time helps determine the most effective way to partition the data (see [blog post](https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/)).
  + Data shape: Instead of reshaping data when a query is processed (as an RDBMS system does), a NoSQL database organizes data so that its shape in the database corresponds with what will be queried. This is a key factor in increasing speed and scalability.
  + Data velocity: DynamoDB scales by increasing the number of physical partitions that are available to process queries, and by efficiently distributing data across those partitions. Knowing the peak query loads in advance might help determine how to partition data to best use I/O capacity.
+ Business user prioritizes the access or query patterns.
  + Priority queries usually are the most used or most relevant queries. It is also important to identify queries that require lower response latency.

## Tools and resources
<a name="tools3"></a>
+ Access patterns matrix (see [template](template-access-patterns.md))
+ [Choosing the Right DynamoDBPartition Key](https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/) (AWS Database blog)
+ [NoSQL design for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html) (DynamoDB documentation)

## RACI
<a name="raci3"></a>

|
|
| Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |
| C | A | I | R |   |   |

## Outputs
<a name="outputs3"></a>
+ Data-access patterns matrix

## Example
<a name="sample3"></a>

|
|
| Access pattern | Priority | Read or write | Description | Type (single item, multiple items, or all) | Key attribute | Filters | Result ordering |
| --- |--- |--- |--- |--- |--- |--- |--- |
| Create user profile | High | Write | User creates a new profile | Single item | Username | N/A | N/A |
| Update user profile | Medium | Write | User updates their profile | Single item | Username | Username = current user | N/A |
