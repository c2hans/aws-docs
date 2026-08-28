---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/making-requests.html
---

# Make requests
<a name="making-requests"></a>

Use a service client to make requests to an AWS service. The AWS SDK for Kotlin provides Domain Specific Languages (DSLs) following a [type-safe builder](https://kotlinlang.org/docs/type-safe-builders.html) pattern to create requests. Nested structures of requests are also accessible through their DSLs.

The following example shows how to create an Amazon DynamoDB [createTable](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/create-table.html) operation input:

```
val ddb = DynamoDbClient.fromEnvironment()

val req = CreateTableRequest {
    tableName = name
    keySchema = listOf(
        KeySchemaElement {
            attributeName = "year"
            keyType = KeyType.Hash
        },
        KeySchemaElement {
            attributeName = "title"
            keyType = KeyType.Range
        }
    )

    attributeDefinitions = listOf(
        AttributeDefinition {
            attributeName = "year"
            attributeType = ScalarAttributeType.N
        },
        AttributeDefinition {
            attributeName = "title"
            attributeType = ScalarAttributeType.S
        }
    )

    // You can configure the `provisionedThroughput` member
    // by using the `ProvisionedThroughput.Builder` directly:
    provisionedThroughput {
        readCapacityUnits = 10
        writeCapacityUnits = 10
    }
}

val resp = ddb.createTable(req)
```

## Service interface DSL overloads
<a name="service-interface-dsl-overloads"></a>

Each non-streaming operation on the service client interface has a DSL overload so that you don’t have to create a separate request.

Example of creating an Amazon Simple Storage Service (Amazon S3) bucket with the overloaded function:

```
s3Client.createBucket {    // this: CreateBucketRequest.Builder
    bucket = newBucketName
}
```

This is equivalent to:

```
val request = CreateBucketRequest {    // this: CreateBucketRequest.Builder
    bucket = newBucketName
}

s3client.createBucket(request)
```

## Requests with no required inputs
<a name="requests-no-required-inputs"></a>

Operations that don’t have required inputs can be called without having to pass a request object. This is often possible with list-type operations, such as the Amazon S3 [`listBuckets`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/list-buckets.html) API operation.

For example, the following three statements are equivalent:

```
s3Client.listBuckets(ListBucketsRequest {
  // Construct the request object directly.
})
s3Client.listBuckets {
  // DSL builder without explicitly setting any arguments.
}
s3Client.listBuckets()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
