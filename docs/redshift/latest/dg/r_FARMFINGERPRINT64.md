---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_FARMFINGERPRINT64.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# farmFingerprint64 function
<a name="r_FARMFINGERPRINT64"></a>

Computes the farmhash value of the input argument using the `Fingerprint64` function.

## Syntax
<a name="r_FARMFINGERPRINT64-synopsis"></a>

```
farmFingerprint64(expression)
```

## Argument
<a name="r_FARMFINGERPRINT64-argument"></a>

 *expression*
The input expression must be a `VARCHAR` or `VARBYTE` data type.

## Return type
<a name="r_FARMFINGERPRINT64-return-type"></a>

The `farmFingerprint64` function returns a `BIGINT`.

## Example
<a name="r_FARMFINGERPRINT64-example"></a>

The following example returns the `farmFingerprint64` value of `Amazon Redshift` that is input as a `VARCHAR` data type.

```
SELECT farmFingerprint64('Amazon Redshift');
```

```

  farmfingerprint64
---------------------
 8085098817162212970
```

The following example returns the `farmFingerprint64` value of `Amazon Redshift` that is input as a `VARBYTE` data type.

```
SELECT farmFingerprint64('Amazon Redshift'::varbyte);
```

```

  farmfingerprint64
---------------------
 8085098817162212970
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
