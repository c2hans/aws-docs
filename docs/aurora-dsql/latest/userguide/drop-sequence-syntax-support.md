---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/userguide/drop-sequence-syntax-support.html
---

# `DROP SEQUENCE`
<a name="drop-sequence-syntax-support"></a>

`DROP SEQUENCE` — remove a sequence.

## Supported syntax
<a name="drop-sequence-supported-syntax"></a>

```
DROP SEQUENCE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description
<a name="drop-sequence-description"></a>

`DROP SEQUENCE` removes sequence number generators. A sequence can only be dropped by its owner or a superuser.

## Parameters
<a name="drop-sequence-parameters"></a>

**`IF EXISTS`**
Do not throw an error if the sequence does not exist. A notice is issued in this case.

**{{name}}**
The name (optionally schema-qualified) of a sequence.

**`CASCADE`**
Automatically drop objects that depend on the sequence, and in turn all objects that depend on those objects.

**`RESTRICT`**
Refuse to drop the sequence if any objects depend on it. This is the default.

## Examples
<a name="drop-sequence-examples"></a>

To remove the sequence `seq`:

```
DROP SEQUENCE seq;
```

## Compatibility
<a name="drop-sequence-compatibility"></a>

`DROP SEQUENCE` conforms to the SQL standard, except that the standard only allows one sequence to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
