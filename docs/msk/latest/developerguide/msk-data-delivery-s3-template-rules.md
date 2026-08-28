---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-template-rules.html
---

# Rules
<a name="msk-data-delivery-s3-template-rules"></a>

If you provide a template, it must satisfy all of the following.

## Structure
<a name="msk-data-delivery-s3-template-rules-structure"></a>
+ **Length** — at most 1024 characters. In addition, the output prefix length plus the template length must be at most 1024 characters (they are concatenated into the final key).
+ **No path traversal** — must not contain `..` or `./`, and must not start with `/`.
+ **Must not end with `/`** — the key must resolve to an object, not a directory boundary.
+ **Balanced variables** — every `!{` must have a matching `}`.
+ **Allowed literals** — characters outside `!{...}` must match `[a-zA-Z0-9/_\-.+=]` (alphanumerics, `/`, `_`, `-`, `.`, `+`, `=`). Spaces are not allowed.

## Variables
<a name="msk-data-delivery-s3-template-rules-variables"></a>
+ **Known names only** — only the supported variables are valid; any other variable is rejected.
+ **At least one variable** — a template of only literals is rejected.
+ **Exactly one uniqueness token** — must contain either `!{sequence-number}` or `!{kafka-offset}`, but not both (they are mutually exclusive).
+ **`kafka-offset` requires `partition-id`** — if you use `!{kafka-offset}`, the template must also contain `!{partition-id}`.
+ **Uniqueness token placement** — the chosen token (`!{sequence-number}` or `!{kafka-offset}`) must appear in the last `/`-separated segment, so each delivered object gets a distinct key.

**Note**
**Why a uniqueness token is required:** The Channel writes multiple records into each S3 object (a batch), so the token identifies the object, not an individual record. `!{sequence-number}` is a monotonic per-object batch number; `!{kafka-offset}` is the Kafka offset of the first record in the object. The template requires exactly one of these tokens in the final path segment so that every delivered object gets a distinct key and objects aren't overwritten.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
