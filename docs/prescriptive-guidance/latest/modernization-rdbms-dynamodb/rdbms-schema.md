---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/rdbms-schema.html
---

# RDBMS table schema and mapping

The following diagram shows the tables and relationships in the source RDBMS schema.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/images/guide-img/bb14de26-e912-4fbe-b307-0ec4123e45b0/images/d28b5f81-663f-4a10-a860-2823d57cc12e.png)

As shown in the previous diagram, the production\_apps table has id and version columns, which have a one-to-many relationship with the production\_app\_properties and production\_app\_configs tables. Therefore, in the DynamoDB design, the production\_app\_properties and production\_app\_configs tables are embedded within the production\_app item, as shown in the following  JSON code. Because production\_app\_properties and production\_app\_configs can have multiple values, these tables are added as arrays in the JSON code. The changed\_apps and test\_apps tables are mapped similarly.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/images/guide-img/bb14de26-e912-4fbe-b307-0ec4123e45b0/images/95d80a30-5d0c-464d-9a9a-89e51c77facf.png)

## Single table design
<a name="single-tables"></a>

DynamoDB doesn't maintain relationships; it supports a fixed table schema. As a result, you can store different types of items (such as SQL tables) in a single DynamoDB table, with an attribute (ItemType) that identifies the type of item.

In DynamoDB, the combination of partition keys (PK) and sort keys (SK) must be unique, so these keys vary based on the item type.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/images/guide-img/bb14de26-e912-4fbe-b307-0ec4123e45b0/images/c433cb2c-5257-4160-b983-80b625d338c4.png)

## Global secondary indexes
<a name="gsi"></a>

Indexes help retrieve data faster and improve application performance. For the sample application, the following indexes were created. The PKs and SKs were chosen based on how distinct items could be identified.

|
|
|  Index name | Description |  PK |  SK |  Projected\_Attributes |
| --- |--- |--- |--- |--- |
|  Version-index | Gets all production applications for a given version. |  version |   |   id, name |
|  Release-index | Gets all test applications for a given release-id.  |  release-id |   |   id, name |
|  Change-index | Gets all (changed) applications associated with a change-id. |  change-id |   | id, modified-by, date |
