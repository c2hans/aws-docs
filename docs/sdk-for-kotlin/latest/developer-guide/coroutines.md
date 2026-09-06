---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/coroutines.html
---

# Coroutines
<a name="coroutines"></a>

The AWS SDK for Kotlin is asynchronous by default. The SDK for Kotlin uses `suspend` functions for all operations, which are meant to be called from a coroutine.

For a more in-depth guide to coroutines, see the [official Kotlin documentation](https://kotlinlang.org/docs/coroutines-overview.html).

## Making concurrent requests
<a name="making-concurrent-requests"></a>

The [async](https://kotlinlang.org/docs/composing-suspending-functions.html#concurrent-using-async) coroutine builder can be used to launch concurrent requests where you care about the results. `async` returns a [Deferred](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-deferred/index.html), which represents a light-weight, non-blocking future that represents a promise to provide a result later.

If you don’t care about the results (only that an operation completed), you can use the [launch](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/launch.html) coroutine builder. `launch` is conceptually similar to `async`. The difference is that launch returns a [Job](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/index.html) and does not carry any resulting value, while `async` returns a `Deferred`.

The following is an example of making concurrent requests to Amazon S3 using the [headObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/head-object.html) operation to get the content size of two keys:

```
import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import kotlin.system.measureTimeMillis
import aws.sdk.kotlin.services.s3.S3Client

fun main(): Unit = runBlocking {

    val s3 = S3Client { region = "us-east-2" }

    val myBucket = "<your-bucket-name-here>"
    val key1 = "<your-object-key-here>"
    val key2 = "<your-second-object-key-here>"

    val resp1 = async {
        s3.headObject{
            bucket = myBucket
            key = key1
        }
    }

    val resp2 = async {
        s3.headObject{
            bucket = myBucket
            key = key2
        }
    }

    val elapsed = measureTimeMillis {
        val totalContentSize = resp1.await().contentLength + resp2.await().contentLength
        println("content length of $key1 + $key2 = $totalContentSize")
    }

    println("requests completed in $elapsed ms")

}
```

## Making blocking requests
<a name="making-clocking-requests"></a>

To make service calls from existing code that doesn’t use coroutines and implements a different threading model, you can use the [runBlocking](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html) coroutine builder. An example of a different threading model is using Java’s traditional executors/futures approach. You might need to use this approach if you’re blending Java and Kotlin code or libraries.

As its name suggests, this `runBlocking` builder launches a new coroutine and blocks the current thread until it completes.

**Warning**
 `runBlocking` should not generally be used from a coroutine. It is designed to bridge regular blocking code to libraries that are written in suspending style (such as in main functions and tests).
