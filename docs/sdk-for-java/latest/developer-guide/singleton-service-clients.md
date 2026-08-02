---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/singleton-service-clients.html
---

# Use singleton service client instances with the AWS SDK for Java 2.x
<a name="singleton-service-clients"></a>

Service clients in the AWS SDK for Java 2.x are thread-safe. You can create one instance of each service client and reuse it throughout your application. This approach improves performance and manages resources more efficiently.

## Benefits of singleton service clients
<a name="singleton-performance-benefits"></a>

Connection pooling
Service clients maintain internal HTTP connection pools. Creating and destroying these pools is expensive. When you reuse clients, these pools are shared efficiently across requests.

Reduced initialization overhead
Creating a client involves loading configuration, establishing credentials, and initializing internal components. Singleton instances eliminate this overhead.

Better resource utilization
Singleton clients prevent resource exhaustion that can occur when you create many client instances.

## Create and use singleton service clients
<a name="singleton-best-practice-example"></a>

The following example shows how to create and use singleton service clients:

```
// Create one instance and use it throughout the application.
public class ServiceClientSource {
    private static final S3Client s3Client = S3Client.create();

    public static S3Client getS3Client() {
        return s3Client;
    }
}
```

Don't create new clients for each operation:

```
// This approach creates unnecessary overhead.
public void badExample() {
    try (S3Client s3 = S3Client.create()) {
        s3.listBuckets();
    }
}
```

## Important considerations
<a name="singleton-important-considerations"></a>
+ Service clients are thread-safe. You can safely share them across multiple threads.
+ Close clients only when your application shuts down or if you no longer need the client. Use `client.close()` or try-with-resources at the application level.
+ If you need different configurations such as regions or credentials, create separate singleton instances for each configuration.

If you use dependency injection frameworks like Spring, configure service clients as singleton beans. This ensures proper lifecycle management.
