---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/introducing-amazon-redshift.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introducing Amazon Redshift
<a name="introducing-amazon-redshift"></a>

 In the past, when data volumes grew or an enterprise wanted to make analytics and reports available to more users, they had to choose between accepting slow query performance or investing time and effort on an expensive upgrade process. In fact, some IT teams discourage augmenting data or adding queries to protect existing service-level agreements. Many enterprises struggled with maintaining a healthy relationship with traditional database vendors. They were often forced to either upgrade hardware for a managed system, or enter a protracted negotiation cycle for an expired term license. When they hit the scaling limit on one data warehouse engine, they were forced to migrate to another engine from the same vendor with different SQL semantics.

 Cloud data warehouses like [Amazon Redshift](https://aws.amazon.com/redshift/) changed how enterprises think about data warehousing by dramatically lowering the cost and effort associated with deploying data warehouse systems, without compromising on features, scale, and performance.

 Amazon Redshift is a fast, fully managed, petabyte-scale data warehousing solution that makes it simple and cost-effective to analyze large volumes of data using existing business intelligence (BI) tools. With Amazon Redshift, you can get the performance of [columnar](https://en.wikipedia.org/wiki/Column-oriented_DBMS) data warehousing engines that perform massively parallel processing (MPP) at a tenth of the cost. You can start small for $0.25 per hour, with no commitments, and scale to petabytes for $1,000 per terabyte per year. You can grow to exabyte-scale storage by storing data in an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) data lake and taking a [lake house](https://aws.amazon.com/redshift/lake-house-architecture/) approach to data warehousing with the [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) feature. With this setup, you can query data directly from files on Amazon S3 for as low as $5 per terabyte of data scanned.

 Since launching in February 2013, Amazon Redshift has been one of the fastest growing AWS Services, with tens of thousands of customers across many industries and company sizes. Enterprises such as NTT DOCOMO, FINRA, Johnson & Johnson, McDonalds, Equinox, Fannie Mae, Hearst, Amgen, and NASDAQ have migrated to Amazon Redshift.
