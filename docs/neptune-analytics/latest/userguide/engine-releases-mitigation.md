---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/engine-releases-mitigation.html
---

# Mitigation for query plan cache issue
<a name="engine-releases-mitigation"></a>

We have detected an issue in query plan cache when `skip` or `limit` is used in an inner `WITH` clause and are parameterized. For example:

```
MATCH (n:Person)
WHERE n.age > $age
WITH n skip $skip LIMIT $limit
RETURN n.name, n.age

parameters={"age": 21, "skip": 2, "limit": 3}
```

In this case, the parameter values for skip and limit from the first plan will be applied to subsequent queries, too, leading to unexpected results.

**Mitigation**

To prevent this issue, add the HTTP parameter `planCache=disabled` or SDK parameter `-\-planCache "disabled"` when submitting a query that includes a parameterized skip and/or limit sub-clause. Alternatively, you can hard-code the values into the query, or add a random comment to create a new plan for each request.

**Option 1:** Using request parameter

Curl example

```
curl -k https://<endpoint>:8182/opencypher -d 'query=MATCH (n:Person) WHERE n.age > $age WITH n skip $skip LIMIT $limit RETURN n.name, n.age' -d 'parameters={"age": 21, "skip": 2, "limit": 3}' -d planCache=disabled
```

SDK example

```
aws neptune-graph execute-query \
   -\-graph-identifier <graph-id> \
   -\-query-string "MATCH (n:Person) WHERE n.age > $age WITH n skip $skip LIMIT $limit RETURN n.name, n.age"
   -\-region <region> \
   -\-plan-cache "disabled" \
   -\-language open_cypher
```

**Option 2:** Using hard-coded values for skip and limit

```
MATCH (n:Person)
WHERE n.age > $age
WITH n skip 2 LIMIT 3
RETURN n.name, n.age

parameters={"age": 21}
```

**Option 3:** Using a random comment

```
MATCH (n:Person)
WHERE n.age > $age
WITH n skip $skip LIMIT $limit
RETURN n.name, n.age // 411357f6-00d2-4f03-92ce-060d8e037c0b

parameters={"age": 21, "skip": 2, "limit": 3}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
