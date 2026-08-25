---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/sdk-warmup.html
---

# Warm up SDK clients in the AWS SDK for Java 2.x
<a name="sdk-warmup"></a>

Use the `SdkWarmUp` utility in the AWS SDK for Java 2.x to warm up your SDK clients during application initialization. This reduces the latency of the first request that your application handles after startup or restore.

A warm-up exercises the SDK request path (building a client and invoking an operation) before your application handles real traffic. You use it with checkpoint-and-restore features such as [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html). These features take a snapshot of your initialized application, then restore from that snapshot to reduce cold-start latency.

Without `SdkWarmUp`, you must write your own warm-up code before each checkpoint, which is cumbersome. With `SdkWarmUp`, you make a single call to warm all your clients. You can warm all SDK clients on your classpath, or only the specific clients that your application uses.

In this topic, you learn how to configure and use `SdkWarmUp` with CRaC and AWS Lambda SnapStart. For more information about other techniques that reduce startup time on Lambda, see [Reduce SDK startup time for AWS Lambda](lambda-optimize-starttime.md).

## The SdkWarmUp API
<a name="sdk-warmup-api"></a>

`SdkWarmUp` is part of the `sdk-core` module, so it is available to every service client without an additional dependency. Configure your project to use version 2.54.0 or later of the AWS SDK for Java 2.x. Then call one of the two static methods described in the following sections. When you call either method, `SdkWarmUp` makes one network call to warm the HTTP client. To warm the service client, it uses a local, canned response. It needs no AWS credentials or IAM permissions, and does not incur AWS charges.

### Warm up all SDK clients on the classpath
<a name="sdk-warmup-api-noarg"></a>

The `warmUp()` method discovers every SDK service client on the classpath and warms each one, along with the HTTP clients that they use. Use this method when you depend on a small number of service modules and call most of the clients that they provide. The following Java code example calls `warmUp()` with no arguments:

```
import software.amazon.awssdk.core.warmup.SdkWarmUp;

SdkWarmUp.warmUp();
```

This method runs at most once per JVM. After a successful call, subsequent calls return immediately.

### Warm up specific SDK clients
<a name="sdk-warmup-api-targeted"></a>

The `warmUp(Class<? extends SdkClient>... clients)` method warms only the clients that you name. Pass a synchronous client class to warm the synchronous path, or an asynchronous client class to warm the asynchronous path.

Use this method when your classpath contains more service clients than your application calls. For example, this happens when a dependency brings in service modules that you don't use. Naming only the clients you need keeps warm-up time proportional to your application's actual usage rather than to your full classpath. The following Java code example warms only the `S3Client` and `DynamoDbClient` classes:

```
import software.amazon.awssdk.core.warmup.SdkWarmUp;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

SdkWarmUp.warmUp(S3Client.class, DynamoDbClient.class);
```

## Use SdkWarmUp with Lambda SnapStart
<a name="sdk-warmup-lambda-snapstart"></a>

[AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) improves startup performance for Java functions. When you publish a new version of a function, Lambda SnapStart initializes it and takes a snapshot of the memory and disk state. It then caches the snapshot for reuse. For information about supported runtimes and how to activate SnapStart for your function, see the *AWS Lambda Developer Guide*.

Because Lambda takes the snapshot after your handler's constructor runs, call `SdkWarmUp.warmUp()` in the constructor. The snapshot then includes your warmed clients, and each invocation that restores from the snapshot benefits from the warm-up. The following Java code example calls `SdkWarmUp.warmUp()` in a Lambda handler constructor:

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import software.amazon.awssdk.core.warmup.SdkWarmUp;

public class MyHandler implements RequestHandler<String, String> {

    public MyHandler() {
        SdkWarmUp.warmUp();
        // Your other initialization here.
    }

    @Override
    public String handleRequest(String input, Context context) {
        // Your handler logic here.
    }
}
```

If your function needs to run custom code before Lambda takes the snapshot or after it restores, implement SnapStart runtime hooks. For more information, see [SnapStart runtime hooks for Java](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks-java.html) in the *AWS Lambda Developer Guide*.

## Use SdkWarmUp with standalone CRaC
<a name="sdk-warmup-standalone-crac"></a>

You can also use `SdkWarmUp` with CRaC directly, in an application that manages its own checkpoints. This section shows where the warm-up call belongs in an application that is already configured for CRaC. To configure an application for CRaC, see [Step-by-step CRaC support](https://github.com/CRaC/docs/blob/master/STEP-BY-STEP.md) on GitHub. That walkthrough covers the supported JDK distributions, the platform prerequisites, and the `org.crac:crac` dependency that the lifecycle interfaces require.

### Warm up before the checkpoint
<a name="sdk-warmup-crac-step1"></a>

Call `SdkWarmUp.warmUp()` during initialization, before you take the checkpoint. Your application already registers itself as a CRaC `Resource` to close and reopen connections around the checkpoint. Add the warm-up call to the same constructor, as shown in the following Java code example:

```
import org.crac.Context;
import org.crac.Core;
import org.crac.Resource;
import software.amazon.awssdk.core.warmup.SdkWarmUp;

public class MyApp implements Resource {

    public MyApp() {
        SdkWarmUp.warmUp();
        // Your other initialization here.
        Core.getGlobalContext().register(this);
    }

    @Override
    public void beforeCheckpoint(Context<? extends Resource> context) throws Exception {
        // Close your service clients here.
    }

    @Override
    public void afterRestore(Context<? extends Resource> context) throws Exception {
        // Create your service clients again here.
    }
}
```

**Note**
CRaC does not take a checkpoint while any file descriptor is open. If you use the AWS CRT-based HTTP client, closing your service clients alone is not enough, because the client keeps a shared event loop open. Release it in `beforeCheckpoint` as shown in the following Java code example:

```
import org.crac.Context;
import org.crac.Resource;
import software.amazon.awssdk.crt.CrtResource;
import software.amazon.awssdk.crt.io.EventLoopGroup;

@Override
public void beforeCheckpoint(Context<? extends Resource> context) {
    EventLoopGroup.closeStaticDefault();
    CrtResource.waitForNoResources();
}
```
The Netty-based and Apache-based HTTP clients release their resources when you close the service client, so they need no additional teardown.

Take the checkpoint as you normally would.

## Additional resources
<a name="sdk-warmup-additional-resources"></a>

The following resources provide more information about the topics covered in this section:
+ [CRaC documentation](https://github.com/CRaC/docs) on GitHub
