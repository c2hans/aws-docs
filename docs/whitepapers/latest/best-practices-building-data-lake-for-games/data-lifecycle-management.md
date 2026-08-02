---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/data-lifecycle-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data lifecycle management
<a name="data-lifecycle-management"></a>

 Most game developers choose to use Amazon S3 as its primary storage platform when they design and build a data lake on AWS. Amazon S3 is designed for 99.999999999% (11 nines) of data durability and offers industry-leading scalability, data availability, security, and performance. Amazon S3 also delivers strong read-after-write consistency automatically, at no cost, and without changes to performance or availability. Using Amazon S3 as your data lake reduces over-provisioning, tears down data silos, and provides unlimited scale.

 [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/) are designed for different use cases, and offer the flexibility and automation to manage your costs. They include:
+  S3 Standard for general-purpose storage of frequently accessed data
+  S3 Intelligent-Tiering for data with unknown or changing access patterns
+  S3 Standard-Infrequent Access and S3 One Zone-Infrequent Access for long-lived, but less frequently accessed data
+  Amazon Glacier and S3 Glacier Deep Archive for long-term archive and digital preservation
+  S3 on Outposts for storing S3 data on-premises if you have data residency requirements that can’t be met by an existing AWS Region

 This wide range of cost-effective storage classes allows game developers to take advantage of the cost savings without sacrificing performance or making changes to their applications. You can use [S3 Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html) to analyze storage access patterns to help you decide when to transition the right data to the right storage class to lower cost, and configure an [S3 Lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to complete transitions and expirations.

 If your data has changing or unknown access patterns, you can use S3 Intelligent-Tiering to tier objects based on changing access patterns, and automatically deliver cost savings without operational overhead. You pay a small monthly monitoring and auto-tiering fee. There are no lifecycle fees and retrieval fees. S3 Intelligent-Tiering works by monitoring access patterns, and then moving the objects that have not been accessed in 30 consecutive days to the Infrequent Access tier. Once you have activated one or both of the archive access tiers, S3 Intelligent-Tiering will automatically move objects that haven’t been accessed for 90 consecutive days to the Archive Access tier, and then after 180 consecutive days of no access to the Deep Archive Access tier.

 You can configure Amazon S3 Lifecycle to manage and optimize your S3 storage cost effectively at scale. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. There are two types of actions:
+  Transition actions
+  Expiration actions

 As the number of objects grow, multi-tenant buckets are created, and the size of the workloads increase, it can become a very complex task to create and manage the many needed lifecycle configuration rules. The use of object tagging can help simplify this process by reducing the number of rules that you need to manage. The purpose of object tagging is to categorize storage, and each tag is a key-value pair. You can add tags to new objects when you upload them, or you can add them to existing objects.

 S3 Lifecycle rules contain filters for object tags to specify the objects eligible for the specific lifecycle action, whether it is moving the objects to a more cost-effective storage class, or deleting them after a predefined retention period. Each rule can contain one or a set of object tags. The rule then applies to the subset of objects with the specific tag. You can specify a filter based on multiple tags. For more implementation details, refer to [Simplify your data lifecycle by using object tags with Amazon S3 Lifecycle](https://aws.amazon.com/blogs/storage/simplify-your-data-lifecycle-by-using-object-tags-with-amazon-s3-lifecycle/).

 Amazon S3 Storage Lens provides a single view of usage and activity across your Amazon S3 storage. It analyzes storage metrics to deliver contextual recommendations to help you optimize storage costs and apply best practices for protecting your data. You can use S3 Storage Lens to generate summary insights and identify potential cost savings opportunities. For example, you can find objects that could be transitioned to a lower-cost storage class and better utilize S3 storage classes; you can identify and reduce incomplete multipart upload bytes; and you can reduce the number of noncurrent versions retained.
