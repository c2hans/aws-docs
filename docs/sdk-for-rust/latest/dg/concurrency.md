---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/concurrency.html
---

# Concurrency in the AWS SDK for Rust
<a name="concurrency"></a>

The AWS SDK for Rust doesn't provide concurrency control but users have many options for implementing their own.

## Terms
<a name="conc-terms"></a>

Terms related to this subject are easy to confuse and some terms have become synonyms even though they originally represented separate concepts. In this guide, we'll define the following:
+  **Task**: Some "unit of work" that your program will run to completion, or attempt to run to completion.
+  **Sequential Computing**: When several tasks are executed one after another.
+  **Concurrent Computing**: When several tasks are executed in overlapping time periods.
+  **Concurrency**: The ability of a computer to complete multiple tasks in an arbitrary order.
+  **Multitasking**: The ability of a computer to run several tasks concurrently.
+  **Race Condition**: When the behavior of your program changes based on when a task is started or how long it takes to process a task.
+  **Contention**: Conflict over access to a shared resource. When two or more tasks want to access a resource at the same time, that resource is "in contention".
+  **Deadlock**: A state in which no more progress can be made. This typically happens because two tasks want to acquire each other's resources but neither task will release their resource until the other's resource becomes available. Deadlocks lead to a program becoming partly or completely unresponsive.

## A simple example
<a name="conc-simple"></a>

Our first example is a sequential program. In later examples, we'll change this code using concurrency techniques. Later examples reuse the same `build_client_and_list_objects_to_download()` method and make changes within `main()`. Run the following commands to add dependencies to your project:
+ `cargo add aws-sdk-s3`
+ `cargo add aws-config tokio --features tokio/full`

The following example task is to download all the files in an Amazon Simple Storage Service bucket:

1.  Start by listing all the files. Save the keys in a list.

1.  Iterate over the list, downloading each file in turn

```
use aws_sdk_s3::{Client, Error};
const EXAMPLE_BUCKET: &str = "amzn-s3-demo-bucket";  // Update to name of bucket you own.

// This initialization function won't be reproduced in
// examples following this one, in order to save space.
async fn build_client_and_list_objects_to_download() -> (Client, Vec<String>) {
    let cfg = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
    let client = Client::new(&cfg);
    let objects_to_download: Vec<_> = client
        .list_objects_v2()
        .bucket(EXAMPLE_BUCKET)
        .send()
        .await
        .expect("listing objects succeeds")
        .contents()
        .into_iter()
        .flat_map(aws_sdk_s3::types::Object::key)
        .map(ToString::to_string)
        .collect();

    (client, objects_to_download)
}
```

```
#[tokio::main]
async fn main() {
    let (client, objects_to_download) =
        build_client_and_list_objects_to_download().await;

    for object in objects_to_download {
        let res = client
            .get_object()
            .key(&object)
            .bucket(EXAMPLE_BUCKET)
            .send()
            .await
            .expect("get_object succeeds");
        let body = res.body.collect().await.expect("reading body succeeds").into_bytes();
        std::fs::write(object, body).expect("write succeeds");
    }
}
```

**Note**
 In these examples, we won't be handling errors, and we assume that the example bucket has no objects with keys that look like file paths. Thus, we won't cover creating nested directories.

Because of the architecture of modern computers, we can rewrite this program to be much more efficient. We'll do that in a later example, but first, let's learn a few more concepts.

## Ownership and mutability
<a name="conc-ownership"></a>

Each value in Rust has a single owner. When an owner goes out of scope, all values it owns will also be dropped. The owner can provide either one or more immutable references to a value **or** a single mutable reference. The Rust compiler is responsible for ensuring that no reference outlives its owner.

Additional planning and design is needed when multiple tasks need to mutably access the same resource. In sequential computing, each task can mutably access the same resource without contention because they run one after another in a sequence. However, in concurrent computing, tasks can run in any order, and at the same time. Therefore, we must do more to prove to the compiler that multiple mutable references are impossible (or at least to crash if they do occur).

The Rust standard library provides many tools to help us accomplish this. For more information on these topics, see [Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html) and [Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html) in The Rust Programming Language book.

## More terms\!
<a name="conc-moreTerms"></a>

The following are lists of "synchronization objects". Altogether, they are the tools necessary to convince the compiler that our concurrent program won't break ownership rules.

 [https://doc.rust-lang.org/std/sync/index.html](https://doc.rust-lang.org/std/sync/index.html):
+ [https://doc.rust-lang.org/std/sync/struct.Arc.html](https://doc.rust-lang.org/std/sync/struct.Arc.html): An ***A**tomically **R**eference-**C**ounted* pointer. When data is wrapped in an `Arc`, it can be shared freely, without worrying about any specific owner dropping the value early. In this sense, the ownership of the value becomes "shared". Values within an `Arc` cannot be mutable, but might have [interior mutability](https://doc.rust-lang.org/reference/interior-mutability.html).
+ [https://doc.rust-lang.org/std/sync/struct.Barrier.html](https://doc.rust-lang.org/std/sync/struct.Barrier.html): Ensures multiple threads will wait for each other to reach a point in the program, before continuing execution all together.
+ [https://doc.rust-lang.org/std/sync/struct.Condvar.html](https://doc.rust-lang.org/std/sync/struct.Condvar.html): a ***Cond**ition **Var**iable* providing the ability to block a thread while waiting for an event to occur.
+ [https://doc.rust-lang.org/std/sync/struct.Mutex.html](https://doc.rust-lang.org/std/sync/struct.Mutex.html): a ***Mut**ual **Ex**clusion* mechanism that ensures that at most one thread at a time is able to access some data. Generally speaking, a `Mutex` lock should never be held across an `.await` point in the code.

 [https://docs.rs/tokio/latest/tokio/sync/index.html](https://docs.rs/tokio/latest/tokio/sync/index.html):

While the AWS SDKs are intended to be `async`-runtime-agnostic, we recommend the use of `tokio` synchronization objects for specific cases.
+ [https://docs.rs/tokio/latest/tokio/sync/struct.Mutex.html](https://docs.rs/tokio/latest/tokio/sync/struct.Mutex.html): Similar to the standard library's `Mutex`, but with a slightly higher cost. Unlike the standard `Mutex`, this one can be held across an `.await` point in the code.
+ [https://docs.rs/tokio/latest/tokio/sync/struct.Semaphore.html](https://docs.rs/tokio/latest/tokio/sync/struct.Semaphore.html): A variable used to control access to a common resource by multiple tasks.

## Rewriting our example to be more efficient (single-threaded concurrency)
<a name="conc_singleThread"></a>

In the following modified example, we use [https://docs.rs/futures-util/latest/futures_util/future/fn.join_all.html](https://docs.rs/futures-util/latest/futures_util/future/fn.join_all.html) to run **ALL** `get_object` requests concurrently. Run the following command to add a new dependency to your project:
+ `cargo add futures-util`

```
#[tokio::main]
async fn main() {
    let (client, objects_to_download) =
        build_client_and_list_objects_to_download().await;

    let get_object_futures = objects_to_download.into_iter().map(|object| {
        let req = client
            .get_object()
            .key(&object)
            .bucket(EXAMPLE_BUCKET);

        async {
            let res = req
                .send()
                .await
                .expect("get_object succeeds");
            let body = res.body.collect().await.expect("body succeeds").into_bytes();
           // Note that we MUST use the async runtime's preferred way
           // of writing files. Otherwise, this call would block,
           // potentially causing a deadlock.
            tokio::fs::write(object, body).await.expect("write succeeds");
        }
    });

    futures_util::future::join_all(get_object_futures).await;
}
```

 This is the simplest way to benefit from concurrency, but it also has a few issues that might not be obvious at first glance:

1.  We create all the request inputs at the same time. If we don't have enough memory to hold all the `get_object` request inputs then we'll run into an "out-of-memory" allocation error.

1.  We create and await all the futures at the same time. Amazon S3 throttles requests if we try to download too much at once.

To fix both of these issues, we must limit the amount of requests that we're sending at any one time. We'll do this with a `tokio` [semaphore](https://docs.rs/tokio/latest/tokio/sync/struct.Semaphore.html):

```
use std::sync::Arc;
use tokio::sync::Semaphore;
const CONCURRENCY_LIMIT: usize = 50;

#[tokio::main(flavor = "current_thread")]
async fn main() {
    let (client, objects_to_download) =
        build_client_and_list_objects_to_download().await;
    let concurrency_semaphore = Arc::new(Semaphore::new(CONCURRENCY_LIMIT));

    let get_object_futures = objects_to_download.into_iter().map(|object| {
        // Since each future needs to acquire a permit, we need to clone
        // the Arc'd semaphore before passing it in.
        let semaphore = concurrency_semaphore.clone();
        // We also need to clone the client so each task has its own handle.
        let client = client.clone();
        async move {
            let permit = semaphore
                .acquire()
                .await
                .expect("we'll get a permit if we wait long enough");
            let res = client
                .get_object()
                .key(&object)
                .bucket(EXAMPLE_BUCKET)
                .send()
                .await
                .expect("get_object succeeds");
            let body = res.body.collect().await.expect("body succeeds").into_bytes();
            tokio::fs::write(object, body).await.expect("write succeeds");
            std::mem::drop(permit);
        }
    });

    futures_util::future::join_all(get_object_futures).await;
}
```

We've fixed the potential memory usage issue by moving the request creation into the `async` block. This way, requests won't be created until it's time to send them.

**Note**
 If you have the memory for it, it might be more efficient to create all your request inputs at once and hold them in memory until they're ready to be sent. To try this, move request input creation outside of the `async` block.

 We've also fixed the issue of sending too many requests at once by limiting requests in flight to `CONCURRENCY_LIMIT`.

**Note**
 The right value for `CONCURRENCY_LIMIT` is different for every project. When constructing and sending your own requests, try to set it as high as you can without running into throttling errors. While it's possible to dynamically update your concurrency limit based on the ratio of successful to throttled responses that a service sends back, that's outside the scope of this guide due to its complexity.

## Rewriting our example to be more efficient (multi-threaded concurrency)
<a name="conc-multiThread"></a>

 In the previous two examples, we performed our requests concurrently. While this is more efficient than running them synchronously, we can make things even more efficient by using multi-threading. To do this with `tokio`, we'll need to spawn them as separate tasks.

**Note**
 This example requires that you use the multi-threaded `tokio` runtime. This runtime is gated behind the `rt-multi-thread` feature. And, of course, you'll need to run your program on a multi-core machine.

Run the following command to add a new dependency to your project:
+ `cargo add tokio --features=rt-multi-thread`

```
// Set this based on the amount of cores your target machine has.
const THREADS: usize = 8;

#[tokio::main(flavor = "multi_thread")]
async fn main() {
    let (client, objects_to_download) =
        build_client_and_list_objects_to_download().await;
    let concurrency_semaphore = Arc::new(Semaphore::new(THREADS));

    let get_object_task_handles = objects_to_download.into_iter().map(|object| {
        // Since each future needs to acquire a permit, we need to clone
        // the Arc'd semaphore before passing it in.
        let semaphore = concurrency_semaphore.clone();
        // We also need to clone the client so each task has its own handle.
        let client = client.clone();

        // Note this difference! We're using `tokio::task::spawn` to
        // immediately begin running these requests.
        tokio::task::spawn(async move {
            let permit = semaphore
                .acquire()
                .await
                .expect("we'll get a permit if we wait long enough");
            let res = client
                .get_object()
                .key(&object)
                .bucket(EXAMPLE_BUCKET)
                .send()
                .await
                .expect("get_object succeeds");
            let body = res.body.collect().await.expect("body succeeds").into_bytes();
            tokio::fs::write(object, body).await.expect("write succeeds");
            std::mem::drop(permit);
        })
    });

    futures_util::future::join_all(get_object_task_handles).await;
}
```

Dividing work into tasks can be complex. Doing I/O (*input/output*) is typically blocking. Runtimes might struggle to balance the needs of long-running tasks with those of short-running tasks. Whatever runtime you choose, be sure to read their recommendations for the most efficient way to divide your work into tasks. For the `tokio` runtime recommendations, see [Module `tokio::task`](https://docs.rs/tokio/latest/tokio/task/index.html).

## Debugging multi-threaded apps
<a name="conc-debug"></a>

Tasks running concurrently can be run in any order. As such, the logs of concurrent programs can very difficult to read. In the SDK for Rust, we recommend using the `tracing` logging system. It can group logs with their specific tasks, no matter when they're running. For guidance, see [Configuring and using logging in the AWS SDK for Rust](logging.md).

A very useful tool for identifying tasks that have locked up is [https://github.com/tokio-rs/console](https://github.com/tokio-rs/console), which is a diagnostic and debugging tool for asynchronous Rust programs. By instrumenting and running your program, and then running the `tokio-console` app, you can see a live view of the tasks your program is running. This view includes helpful information like the amount of time a task has spent waiting to acquire shared resources or the amount of times it has been polled.
