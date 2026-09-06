---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-document-api.html
---

# Document API differences between version 1 and version 2 of the AWS SDK for Java
<a name="dynamodb-mapping-document-api"></a>

The Document API supports working with JSON-style documents as single items in a DynamoDB table. The V1 Document API has a corresponding API in V2, but instead of using a separate client for the document API as in V1, V2 incorporates document API features in the DynamoDB enhanced client.

In V1, the [`Item`](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Item.html) class represents an unstructured record from a DynamoDB table. In V2, an unstructured record is represented by an instance of the [`EnhancedDocument`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/document/EnhancedDocument.html) class. Note that primary keys are defined in the table schema for V2, and on the item itself in V1.

The table below compares the differences between the Document APIs in V1 and V2.

| Use case | V1 | V2 |
| --- |--- |--- |
| Create a document client |  <pre>AmazonDynamoDB client = ... //Create a client.<br />DynamoDB documentClient = new DynamoDB(client);</pre>  |  <pre>// The V2 Document API uses the same DynamoDbEnhancedClient<br />// that is used for mapping POJOs.<br />DynamoDbClient standardClient = ... //Create a standard client.<br />DynamoDbEnhancedClient enhancedClient = ... // Create an enhanced client.<br /></pre>  |
| Reference a table |  <pre>Table documentTable = docClient.documentClient("Person");</pre>  |  <pre>DynamoDbTable<EnhancedDocument> documentTable = enhancedClient.table("Person",  <br />        TableSchema.documentSchemaBuilder()<br />              .addIndexPartitionKey(TableMetadata.primaryIndexName(),"id", AttributeValueType.S)<br />              .attributeConverterProviders(AttributeConverterProvider.defaultProvider())<br />              .build());</pre>  |
| **Work with semi-structured data** |
| --- |
| Put item |  <pre>Item item = new Item()<br />      .withPrimaryKey("id", 50)<br />      .withString("firstName", "Shirley");<br />PutItemOutcome outcome = documentTable.putItem(item);</pre>  |  <pre>EnhancedDocument personDocument = EnhancedDocument.builder()<br />        .putNumber("id", 50)<br />        .putString("firstName", "Shirley")<br />        .build();<br />documentTable.putItem(personDocument);</pre>  |
| Get item |  <pre>GetItemOutcome outcome = documentTable.getItemOutcome( "id", 50);<br />Item personDocFromDb = outcome.getItem();<br />String firstName = personDocFromDb.getString("firstName");<br /></pre>  |  <pre>EnhancedDocument personDocFromDb = documentTable<br />        .getItem(Key.builder()<br />            .partitionValue(50)<br />            .build()); <br />String firstName = personDocFromDb.getString("firstName");<br /></pre>  |
| **Work with JSON items** |
| --- |
| Convert a JSON structure to use it with the Document API |  <pre>// The 'jsonPerson' identifier is a JSON string. <br />Item item = new Item().fromJSON(jsonPerson);</pre>  |  <pre>// The 'jsonPerson' identifier is a JSON string.<br />EnhancedDocument document = EnhancedDocument.builder()<br />        .json(jsonPerson).build());</pre>  |
| Put JSON |  <pre>documentTable.putItem(item)</pre>  |  <pre>documentTable.putItem(document);</pre>  |
| Read JSON |  <pre>GetItemOutcome outcome = //Get item.<br />String jsonPerson = outcome.getItem().toJSON();</pre>  |  <pre>String jsonPerson = documentTable.getItem(Key.builder()<br />        .partitionValue(50).build())<br />        .fromJson();</pre>  |

## API reference and guides for document APIs
<a name="dynamodb-mapping-document-api-ref"></a>

|  | V1 | V2 |
| --- | --- | --- |
| API reference | [API reference](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/package-summary.html) | [API reference](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/document/package-summary.html) |
| Documentation guide | [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/JavaDocumentAPIItemCRUD.html) | [Enhanced Document API](ddb-en-client-doc-api.md) (this guide) |
