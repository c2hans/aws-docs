---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-caching.html
---

# Use caching to reduce database demand
<a name="net-caching"></a>

## Overview
<a name="net-caching-overview"></a>

You can use caching as an effective strategy to help reduce costs for your .NET applications. Many applications use backend databases, such as Microsoft SQL Server, when they require frequent access to data. The cost of maintaining these backend services to cope with demand can be high, but a caching strategy can reduce the load on backend databases by lowering sizing and scaling requirements. This can help you reduce costs and improve the performance of your applications.

Caching is a useful technique to save on costs for read-heavy workloads that use more expensive resources such as SQL Server. Choose a caching technique that suits your workload. For instance, local caching doesn't scale well and requires you to maintain a local cache for each instance of an application. Weigh the performance benefits against the potential costs, so that the savings from the underlying data source offset any added costs of the caching mechanism.

## Cost impact
<a name="cost-impact"></a>

SQL Server requires you to factor in read requests when sizing your database. This might affect costs, because you may need to add read replicas to accommodate the load. Read replicas are available only on SQL Server Enterprise edition, which requires a more expensive license than SQL Server Standard edition.

The following diagram helps you understand caching effectiveness. It shows Amazon RDS for SQL Server with four db.m4.2xlarge nodes running SQL Server Enterprise edition. You deploy it in a Multi-AZ configuration with one read replica. The configuration directs exclusive read traffic (for example, SELECT queries) to the read replicas. In comparison, Amazon DynamoDB uses an r4.2xlarge two-node DynamoDB Accelerator (DAX) cluster.

The following chart shows the results of removing the need for dedicated read replicas that handle high read traffic.

![Chart showsing results of removing dedicated read replicas](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/e8ef2317-aa29-4054-bace-cba365ee4cc8.png)

You can achieve cost savings by using local caching with no read replicas or by introducing DAX side by side with SQL Server on Amazon RDS as a caching layer. This layer offloads read traffic from SQL Server and reduces the size of the SQL Server instance required to run the database.

## Cost optimization recommendations
<a name="net-caching-rec"></a>

### Local caching
<a name="local-caching.95a4a816-c2ee-5019-aad1-d11db7cc6750"></a>

Local caching is one of the most commonly used ways to cache content for applications hosted both in on-premises environments and in the cloud. This is because it's relatively easy and intuitive to implement. Local caching involves taking content from a database or other source and caching it locally, either in memory or on disk, for quicker access. Although this approach is easy to implement, it isn't ideal for some use cases. Examples include when cached content needs to persist over time, such as to preserve application state or user state, or when other application instances need to access the cached content.

The diagram below illustrates a highly available SQL Server cluster with four nodes and two read replicas.

![Highly available SQL Server cluster with 4 nodes and 2 read replicas](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/74ef05a7-f1e5-4560-87f7-f585be611dc8.png)

With local caching, you might need to load balance traffic across multiple EC2 instances. Each instance must maintain its own local cache. If the cache stores stateful information, you must regularly commit that information to the database, and you might need to route users to the same instance for each subsequent request (sticky session). This presents a challenge when you scale applications because some instances could be overutilized while others are underutilized because of the uneven distribution of traffic.

You can use local caching, either in-memory or using local storage, for .NET applications. To do so, you can add functionality to either store objects on disk and retrieve them when required, or query data from the database and persist it in memory. To perform local caching in-memory and on local storage of data from a SQL Server in C\#, for example, you can use a combination of `MemoryCache` and `LiteDB` libraries. `MemoryCache` provides in-memory caching, while `LiteDB` is an embedded NoSQL disk-based database that's fast and lightweight.

To perform in-memory caching, use the .NET library `System.Runtime.Caching.MemoryCache`. The following code example shows how to use the `System.Runtime.Caching.MemoryCache` class to cache data in memory. This class provides a way to temporarily store data in the application's memory. This can help improve the performance of an application by reducing the need to fetch data from a more expensive resource, such as a database or an API.

Here's how the code works:

1. A private static instance of `MemoryCache` named `_memoryCache` is created. The cache is given a name (`dataCache`) to identify it. Then, the cache stores and retrieves the data.

1. The `GetData` method is a generic method that takes two arguments: a `string` key and a `Func<T>` delegate called `getData`. The key is used to identify the cached data, while the `getData` delegate represents the data retrieval logic that gets executed when the data isn't present in the cache.

1. The method first checks if the data is present in the cache using the `_memoryCache.Contains(key)` method. If the data is in the cache, the method retrieves the data by using `_memoryCache.Get(key)` and casts it to the expected type T.

1. If the data isn't in the cache, the method calls the `getData` delegate to fetch the data. Then, it adds the data to the cache by using `_memoryCache.Add(key, data, DateTimeOffset.Now.AddMinutes(10))`. This call specifies that the cache entry should expire after 10 minutes, at which point the data is removed from the cache automatically.

1. The `ClearCache` method takes a `string` key as an argument and removes the data associated with that key from the cache by using `_memoryCache.Remove(key)`.

```
using System;
using System.Runtime.Caching;

public class InMemoryCache
{
    private static MemoryCache _memoryCache = new MemoryCache("dataCache");

    public static T GetData<T>(string key, Func<T> getData)
    {
        if (_memoryCache.Contains(key))
        {
            return (T)_memoryCache.Get(key);
        }

        T data = getData();
        _memoryCache.Add(key, data, DateTimeOffset.Now.AddMinutes(10));

        return data;
    }

    public static void ClearCache(string key)
    {
        _memoryCache.Remove(key);
    }
}
```

You can use the following code:

```
public class Program
{
    public static void Main()
    {
        string cacheKey = "sample_data";

        Func<string> getSampleData = () =>
        {
            // Replace this with your data retrieval logic
            return "Sample data";
        };

        string data = InMemoryCache.GetData(cacheKey, getSampleData);
        Console.WriteLine("Data: " + data);
    }
}
```

The following example shows you how to use [LiteDB](https://www.litedb.org/) to cache data in local storage. You can use LiteDB as an alternative or complement to in-memory caching. The following code demonstrates how to use the LiteDB library to cache data in local storage. The `LocalStorageCache` class contains the main functions for managing the cache.

```
using System;
using LiteDB;

public class LocalStorageCache
{
    private static string _liteDbPath = @"Filename=LocalCache.db";

    public static T GetData<T>(string key, Func<T> getData)
    {
        using (var db = new LiteDatabase(_liteDbPath))
        {
            var collection = db.GetCollection<T>("cache");
            var item = collection.FindOne(Query.EQ("_id", key));

            if (item != null)
            {
                return item;
            }
        }

        T data = getData();

        using (var db = new LiteDatabase(_liteDbPath))
        {
            var collection = db.GetCollection<T>("cache");
            collection.Upsert(new BsonValue(key), data);
        }

        return data;
    }

    public static void ClearCache(string key)
    {
        using (var db = new LiteDatabase(_liteDbPath))
        {
            var collection = db.GetCollection("cache");
            collection.Delete(key);
        }
    }
}

public class Program
{
    public static void Main()
    {
        string cacheKey = "sample_data";

        Func<string> getSampleData = () =>
        {
            // Replace this with your data retrieval logic
            return "Sample data";
        };

        string data = LocalStorageCache.GetData(cacheKey, getSampleData);
        Console.WriteLine("Data: " + data);
    }
}
```

If you have a static cache or static files that don't change frequently, you can also store these files in Amazon Simple Storage Service (Amazon S3) object storage. The application can retrieve the static cache file on startup to use locally. For more details on how to retrieve files from Amazon S3 by using .NET, see [Downloading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the Amazon S3 documentation.

### Caching with DAX
<a name="caching-with-dax.d8c73d30-2427-5e4d-aac5-0b055e4d0dec"></a>

You can use a caching layer that you share across all application instances. [DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html) is a fully managed, highly available in-memory cache for DynamoDB that can deliver up to a 10 times performance improvement. You can use DAX to help reduce costs by reducing the need to overprovision read capacity units in DynamoDB tables. This is especially useful for read-heavy workloads that require repeated reads for individual keys.

DynamoDB is priced on demand or with provisioned capacity, so the number of reads and writes per month contributes to the cost. If you have read-heavy workloads, DAX clusters can help lower costs by reducing the number of reads on your DynamoDB tables. For instructions on how to set up DAX, see [In-memory acceleration with DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) in the DynamoDB documentation. For information about .NET application integration, watch [Integrating Amazon DynamoDB DAX into Your ASP.NET Application](https://www.youtube.com/watch?v=ZMkLhD8OxYQ) on YouTube.

## Additional resources
<a name="net-caching-resources"></a>
+ [In-memory acceleration with DynamoDB Accelerator (DAX) - Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) (DynamoDB documentation)
+ [Integrating Amazon DynamoDB DAX into Your ASP.NET Application](https://www.youtube.com/watch?v=ZMkLhD8OxYQ) (YouTube)
+ [Downloading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) (Amazon S3 documentation)
