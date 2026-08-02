---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-high-level.html
---

# High-level changes in mapping libraries from version 1 to version 2 of the SDK for Java
<a name="dynamodb-mapping-high-level"></a>

The names of the mapping client in each library differ in V1 and V2:
+ V1 - DynamoDBMapper
+ V2 - DynamoDB Enhanced Client

You interact with the two libraries in much the same way: you instantiate a mapper/client and then supply a Java POJO to APIs that read and write these items to DynamoDB tables. Both libraries also offer annotations for the class of the POJO to direct how the client handles the POJO.

Notable differences when you move to V2 include:
+ V2 and V1 use different method names for the low-level DynamoDB operations. For example:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-high-level.html)
+ V2 offers multiple ways to define table schemas and map POJOs to tables. You can choose from the use of annotations or a schema generated from code using a builder. V2 also offers mutable and immutable versions of schemas.
+ With V2, you specifically create the table schema as one of the first steps, whereas in V1, the table schema is inferred from the annotated class as needed.
+ V2 includes the [Document API client ](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/document/EnhancedDocument.html) in the enhanced client API, whereas V1 uses a [separate API](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/DynamoDB.html).
+ All APIs are available in synchronous and asynchronous versions in V2.

See the [DynamoDB mapping section](dynamodb-enhanced-client.md) in this guide for more detailed information on the V2 enhanced client.

## Import dependency differences
<a name="dynamodb-mapping-deps"></a>

| V1 | V2 |
| --- | --- |
|  <pre><dependencyManagement><br />  <dependencies><br />    <dependency><br />      <groupId>com.amazonaws</groupId><br />      <artifactId>aws-java-sdk-bom</artifactId><br />      <version>{{1.X.X}}</version><br />      <type>pom</type><br />      <scope>import</scope><br />    </dependency><br />  </dependencies><br /></dependencyManagement> <br /><br /><dependencies><br />  <dependency><br />    <groupId>com.amazonaws</groupId><br />    <artifactId>aws-java-sdk-dynamodb</artifactId><br />  </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />  <dependencies><br />    <dependency><br />      <groupId>software.amazon.awssdk</groupId><br />      <artifactId>bom</artifactId><br />      <version>{{2.X.X}}*</version><br />      <type>pom</type><br />      <scope>import</scope><br />    </dependency><br />  </dependencies><br /></dependencyManagement> <br /><br /><dependencies><br />  <dependency><br />    <groupId>software.amazon.awssdk</groupId><br />    <artifactId>dynamodb-enhanced</artifactId><br />  </dependency><br /></dependencies></pre>  |

\* [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

In V1, a single dependency includes both the low-level DynamoDB API and the mapping/document API, whereas in V2, you use the `dynamodb-enhanced` artifact dependency to access the mapping/document API. The `dynamodb-enhanced` module contains a transitive dependency on the low-level `dynamodb` module.
