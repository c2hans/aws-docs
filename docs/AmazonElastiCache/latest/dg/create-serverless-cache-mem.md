---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/create-serverless-cache-mem.html
---

# Create a Memcached serverless cache
<a name="create-serverless-cache-mem"></a>

**AWS Management Console**

To create a new Memcached serverless cache using the ElastiCache console:

1. Sign in to the AWS Management Console and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In the navigation pane on the left side of the console, choose **Memcached Caches**.

1. On the right side of the console, choose **Create Memcached cache**.

1. In the **Cache settings** enter a **Name**. You can optionally enter a **description** for the cache.

1. Leave the default settings selected.

1. Click **Create** to create the cache.

1. Once the cache is in "ACTIVE" status, you can begin writing and reading data to the cache.

To create a new cache using the AWS CLI

The following AWS CLI example creates a new cache using create-serverless-cache.

**Linux**

```
aws elasticache create-serverless-cache \
		--serverless-cache-name CacheName \
		--engine memcached
```

**Windows**

```
aws elasticache create-serverless-cache ^
		--serverless-cache-name CacheName ^
		--engine memcached
```

Note that the value of the Status field is set to `CREATING`.

To verify that ElastiCache has finished creating the cache, use the `describe-serverless-caches` command.

**Linux**

```
aws elasticache describe-serverless-caches --serverless-cache-name CacheName
```

**Windows**

```
aws elasticache describe-serverless-caches --serverless-cache-name CacheName
```

After creating the new cache, proceed to [Read and write data to the cache](read-write-cache-mem.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
