---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/getting-started-store-retrieve-data.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Store and Retrieve Data with DynamoDB
<a name="getting-started-store-retrieve-data"></a>

 [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fast, highly scalable, highly available, cost-effective, non-relational database service. DynamoDB removes traditional scalability limitations on data storage while maintaining low latency and predictable performance.

The tutorial below explains how to integrate the DynamoDB Object Persistence Model with your app, which stores objects in DynamoDB.

## Project Setup
<a name="project-setup"></a>

### Prerequisites
<a name="prerequisites"></a>

You must complete all of the instructions on the [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) before beginning this tutorial.

### Create a DynamoDB Table
<a name="create-a-dynamodb-table"></a>

Before you can read and write data to a DynamoDB database, you must create a table. When creating a table you must specify the primary key. The primary key is composed of a hash attribute and an optional range attribute. For more information on how primary and range attributes are used, see [Working With Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html).

1. Go to the [DynamoDB Console](https://console.aws.amazon.com/dynamodb/home) and click **Create Table**. The Create Table wizard appears.

1. Specify your table name, primary key type (Hash), and hash attribute name (“Id”) as shown below, and then click **Continue**:
![](https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/images/create-table.png)

1. Leave the edit fields in the next screen empty and click **Continue**.

1. Accept the default values for **Read Capacity Units** and **Write Capacity Units** and click **Continue**.

1. On the next screen enter your email address in the **Send notification to:** text box and click **Continue**. The review screen appears.

1. Click **Create**. It may take a few minutes for your table to be created.

### Set Permissions for DynamoDB
<a name="set-permissions-for-dynamodb"></a>

In order for your identity pool to access Amazon DynamoDB, you must modify the identity pool’s roles.

1. Navigate to the [Identity and Access Management Console](https://console.aws.amazon.com/iam/home) and click **Roles** in the left-hand pane. Search for your identity pool name - two roles will be listed one for unauthenticated users and one for authenticated users.

1. Click the role for unauthenticated users (it will have “unauth” appended to your identity pool name) and click **Create Role Policy**.

1. Select **Policy Generator** and click **Select**.

1. On the **Edit Permissions** page, enter the settings shown in the following image. The Amazon Resource Name (ARN) of a DynamoDB table looks like `arn:aws:dynamodb:us-west-2:123456789012:table/Books` and is composed of the region in which the table is located, the owner’s AWS account number, and the name of the table in the format `table/Books`. For more information about specifying ARNs, see [Amazon Resource Names for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/UsingIAMWithDDB.html#ARN_Format).
![](https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/images/edit-permissions-dynamodb.png)

1. Click **Add Statement**, and then click **Next Step**. The Wizard will show you the configuration generated.

1. Click **Apply Policy**.

### Add NuGet package for DynamoDB to Your Project
<a name="add-nuget-package-for-dynamodb-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the DynamoDB NuGet package to your project.

## Initialize AmazonDynamoDBClient
<a name="initialize-amazondynamodbclient"></a>

Pass your initialized Amazon Cognito credentials provider and your region to the `AmazonDynamoDB` constructor, then pass the client to the DynamoDBContext:

```
var client = new AmazonDynamoDBClient(credentials,region);
DynamoDBContext context = new DynamoDBContext(client);
```

## Create a Class
<a name="create-a-class"></a>

To write a row to the table, define a class to hold your row data. The class should also contain properties that hold the attribute data for the row and will be mapped to the DynamoDB Table created in the console. The following class declaration illustrates such a class:

```
[DynamoDBTable("Books")]
public class Book
{
    [DynamoDBHashKey]    // Hash key.
    public int Id { get; set; }
    public string Title { get; set; }
    public string ISBN { get; set; }
    public int Price { get; set; }
    public string PageCount { get; set; }
    public string Author{ get; set; }
}
```

## Save an Item
<a name="save-an-item"></a>

To save an item, first create an object:

```
Book songOfIceAndFire = new Book()
{
    Id=1,
    Title="Game Of Thrones",
    ISBN="978-0553593716",
    Price=4,
    PageCount="819",
    Author="GRRM"
};
```

Then save it:

```
context.Save(songOfIceAndFire);
```

To update a row, modify the instance of the `DDTableRow` class and call `AWSDynamoObjectMapper.save()` as shown above.

## Retrieve an Item
<a name="retrieve-an-item"></a>

Retrieve an item using a primary key:

```
Book retrievedBook = context.Load<Book>(1);
```

## Update an Item
<a name="update-an-item"></a>

To update an item:

```
Book retrievedBook = context.Load<Book>(1);
retrievedBook.ISBN = "978-0553593716";
context.Save(retrievedBook);
```

## Delete an Item
<a name="delete-an-item"></a>

To delete an item:

```
Book retrievedBook = context.Load<Book>(1);
context.Delete(retrievedBook);
```

For more information on accessing DynamoDB from a Xamarin application, see [Amazon DynamoDB](dynamodb.md).
