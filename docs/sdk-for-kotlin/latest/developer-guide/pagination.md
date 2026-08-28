---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/pagination.html
---

# Pagination
<a name="pagination"></a>

Many AWS operations return paginated results when the payload is too large to return in a single response. The AWS SDK for Kotlin includes [extensions](https://kotlinlang.org/docs/extensions.html) to the service client interface that auto paginate the results for you. You only have to write the code that processes the results.

Pagination is exposed as a [Flow<T>](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) so that you can take advantage of Kotlin’s idiomatic transforms for asynchronous collections (such as `map`, `filter`, and `take`). Exceptions are transparent, which makes error handling feel like a regular API call, and cancellation adheres to the general cooperative cancellation of coroutines. For more information, see [flows](https://kotlinlang.org/docs/flow.html) and [flow exceptions](https://kotlinlang.org/docs/flow.html#flow-exceptions) in the official guide.

**Note**
The following examples use Amazon S3. However, the concepts are the same for any service that has one or more paginated APIs. All pagination extensions are defined in the `aws.sdk.kotlin.services.<service>.paginators` package (such as `aws.sdk.kotlin.services.dynamodb.paginators`).

The following code example shows how you can process the paginated response from the [listObjectsV2Paginated](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.paginators/list-objects-v2-paginated.html) function call.

 **Imports**

```
import aws.sdk.kotlin.services.s3.S3Client
import aws.sdk.kotlin.services.s3.paginators.listObjectsV2Paginated
import kotlinx.coroutines.flow.*
```

 **Code**

```
val s3 = S3Client.fromEnvironment()
val req = ListObjectsV2Request {
    bucket = "amzn-s3-demo-bucket"
    maxKeys = 1
}

s3.listObjectsV2Paginated(req)  // Flow<ListObjectsV2Response>
    .transform { it.contents?.forEach { obj -> emit(obj) } }
    .collect { obj ->
        println("key: ${obj.key}; size: ${obj.size}")
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
