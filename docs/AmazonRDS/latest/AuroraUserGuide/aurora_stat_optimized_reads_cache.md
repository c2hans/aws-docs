---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_optimized_reads_cache.html
---

# aurora\_stat\_optimized\_reads\_cache
<a name="aurora_stat_optimized_reads_cache"></a>

This function shows tiered cache stats.

## Syntax
<a name="aurora_stat_optimized_reads_cache-syntax"></a>

```
aurora_stat_optimized_reads_cache()
```

## Arguments
<a name="aurora_stat_optimized_reads_cache-arguments"></a>

None

## Return type
<a name="aurora_stat_optimized_reads_cache-return-type"></a>

SETOF record with the following columns:
+ `total_size` – Total optimized reads cache size.
+ `used_size` – Used page size in optimized reads cache.

## Usage notes
<a name="aurora_stat_optimized_reads_cache-usage-notes"></a>

This function is available in the following Aurora PostgreSQL versions:
+ 15.4 and higher 15 versions
+ 14.9 and higher 14 versions

## Examples
<a name="aurora_stat_optimized_reads_cache-examples"></a>

The following example shows the output on a r6gd.8xlarge instance :

```
=> select pg_size_pretty(total_size) as total_size, pg_size_pretty(used_size)
                as used_size from aurora_stat_optimized_reads_cache();
total_size | used_size
-----------+-----------
1054 GB    | 975 GB
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
