---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/language-runtimes.html
---

# Getting started with programming runtimes on AL2027
<a name="language-runtimes"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The following table lists the language runtimes available in AL2027 and the versions removed from AL2023.

**Topics**
+ [Databases](#languages-databases)
+ [Python in AL2027](python.md)
+ [Java in AL2027](language-runtimes-java.md)
+ [Node.js in AL2027](nodejs.md)
+ [TypeScript in AL2027](typescript.md)
+ [Go in AL2027](go.md)
+ [Rust in AL2027](rust.md)
+ [.NET in AL2027](dotnet.md)
+ [PHP in AL2027](language-runtimes-php.md)
+ [Ruby in AL2027](language-runtimes-ruby.md)
+ [Swift in AL2027](swift.md)
+ [C, C\+\+, and Fortran in AL2027](c-cplusplus.md)
+ [Perl in AL2027](perl.md)

**Language runtimes in AL2027**

| Language | Available in AL2027 | Removed from AL2023 |
| --- | --- | --- |
| Python | 3.14 (system python), 3.15 (beta) | 3.9, 3.11, 3.12, 3.13 |
| PHP | 8.5 | 8.1, 8.2, 8.3, 8.4 |
| Node.js | 24 | 18, 20, 22 |
| Ruby | 3.4 | 3.2 |
| Java (Corretto) | 8, 11, 17, 21, 25 | 22, 23, 24, 26 |
| .NET | 10.0 | 6.0, 8.0, 9.0 |
| Rust | 1.97 or later | — |
| Go | 1.25 | — |
| Swift | 6.3 (new) | — |
| Perl | 5.42 | 5.32 |

**Important**
If you are using Python 3.9, PHP 8.1–8.4, Node.js 18–22, or .NET 6, 8, or 9, you must upgrade to the versions available in AL2027 before migrating.

## Databases
<a name="languages-databases"></a>

The following databases are available in the AL2027 preview:

**Databases in AL2027**

| Database | Version | Notes |
| --- | --- | --- |
| MariaDB | 10.11.18 |  |
| MariaDB | 11.4.12 |  |
| MariaDB | 11.8.8 | New in AL2027. |
| PostgreSQL | 16.14 |  |
| PostgreSQL | 17.10 |  |
| PostgreSQL | 18.4 | New in AL2027. |
| Memcached | 1.6.42 | New in AL2027. |
