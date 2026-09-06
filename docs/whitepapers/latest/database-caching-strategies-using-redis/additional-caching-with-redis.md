---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/additional-caching-with-redis.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Additional Caching with Redis
<a name="additional-caching-with-redis"></a>

 Redis is traditionally used in a database cache setting. However, it can also be used to cache output from other services, or full objects from storage services such as [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3).

 The low latency and high throughput of Amazon ElastiCache (Redis OSS), coupled with the large item storage availability, make it a great choice for further optimizing throughput and scalability to new and existing applications.

## Object Caching with Amazon S3
<a name="object-caching-with-amazon-s3"></a>

 Amazon S3 is the persistent store for applications such as data lakes, media catalogs, and website-related content. These applications often have latency requirements of 10 ms or less, with frequent object requests on 1–10% of the total stored S3 data. Many customers achieve this by directly writing to S3. Some applications, such as media catalog updates, require high frequency reads and consistent throughput. For such applications, customers often complement S3 with Redis, to reduce the S3 retrieval cost and to improve performance.

 By using Amazon ElastiCache (Redis OSS), applications can maintain a consistent and low-latency throughput, sustained at less than 5 ms, when serving this content outside of S3 at scale. Serving heavily-requested objects via Amazon ElastiCache (Redis OSS) in this manner can enable you to meet performance goals, while also reducing retrieval and transfer costs.

 A blog post on how to [Turbocharge Amazon S3 with Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/blogs/storage/turbocharge-amazon-s3-with-amazon-elasticache-for-redis/) covers how to set up, deploy, and organize data for this purpose.
