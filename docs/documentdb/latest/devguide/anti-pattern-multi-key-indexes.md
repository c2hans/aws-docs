---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/anti-pattern-multi-key-indexes.html
---

# Multi-Key Indexes with Large Arrays
<a name="anti-pattern-multi-key-indexes"></a>

## Overview
<a name="multi-key-overview"></a>

Multi-key indexes in Amazon DocumentDB let you efficiently query array fields. This indexing strategy delivers significantly lower query latencies when searching within array data, making it an attractive option for applications with complex data structures.

However, when working with large arrays or multiple array fields within a collection, it's important to understand the resource implications and performance characteristics to make informed architectural decisions. When you create an index on an array field, Amazon DocumentDB generates individual index entries for each element in the array.

## Impact on the cluster
<a name="multi-key-impact"></a>
+ **Storage and IO Overhead**: Multi-key indexes can sometimes consume storage space upto multiple times of the base table, the size is directly proportional to documents in the collection with the indexed array attribute, number of elements in the array and size of the element.
+ **Memory Usage**: As the storage footprint is relatively large, these indexes have a corresponding footprint in memory, resulting in a larger working set.
+ **Write operations**: Multi-key indexes create overhead during the write operations. Each array element generates separate index entries, multiplying the work required to complete the write operation.

## Remediation strategies
<a name="multi-key-remediation"></a>
+ Create multi-key index if it is necessary and limit the number of fields in the array.
+ Limit the number of multi key indexes on the collection
+ Consider modifying your [data model](https://skillbuilder.aws/learn/B4KABYUY33/data-modeling-for-amazon-documentdb/2E2C6J83TQ)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
