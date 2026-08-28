---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-query-hints.html
---

# openCypher query hints
<a name="opencypher-query-hints"></a>

**Important**
 openCypher query hint is only available from engine release [1.3.2.0](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.2.0.html) and later.

 In Amazon Neptune, you can use the `USING` clause to specify query hints for openCypher queries. These hints allow you to control optimization and evaluation strategies.

 The syntax for query hints is:

```
USING {scope}:{hint} {value}
```

1.  `{scope}` defines the scope in which the hint applies to: `Query` or `Clause`.

    A scope value of `Query` means that the query hint applies to the whole query (query-level).

    A scope value of `Clause` means that the query hint applies to the clause the hint precedes (clause-level).

1.  `{hint}` is the name of the query hint being applied.

1.  `{value}` is the argument for the `{hint}`.

 The values can be case-insensitive.

 For example, to enable the query plan cache for a query:

```
Using QUERY:PLANCACHE "enabled"
MATCH (a:Person {firstName: "Erin", lastName: $lastName})
 RETURN a
```

**Note**
 Currently, the **Query** scope query hints **PLANCACHE**, **TIMEOUTMILLISECONDS**, and **assumeConsistentDataTypes** are supported. Supported query hints are listed below.

**Topics**
+ [openCypher query plan cache hint](opencypher-query-hints-qpc-hint.md)
+ [AssumeConsistentDataTypes hint](opencypher-query-hints-AssumeConsistentDataTypes.md)
+ [openCypher query timeout hint](opencypher-query-hints-timeout-hint.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
