---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/arrays_overlap.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ARRAYS\_OVERLAP function
<a name="arrays_overlap"></a>

Checks whether two arrays have any common elements. Returns TRUE if the arrays share at least one element, or FALSE if no common elements exist. The function is NULL-safe, meaning it treats NULLs are treated as known objects.

## Syntax
<a name="arrays_overlap-syntax"></a>

```
ARRAYS_OVERLAP( array1, array2 )
```

## Arguments
<a name="arrays_overlap-arguments"></a>

 *array1*
A SUPER expression that specifies an array.

 *array2*
A SUPER expression that specifies an array.

## Return type
<a name="arrays_overlap-return-type"></a>

The ARRAYS\_OVERLAP function returns a Boolean type.

## Example
<a name="arrays_overlap-example"></a>

The following examples show the ARRAYS\_OVERLAP function.

```
SELECT ARRAYS_OVERLAP(ARRAY('blue', 'green'), ARRAY('red', 'green'));
 arrays_overlap
----------------
 t
(1 row)
```

The following examples show that NULLs are treated as valid elements.

```
SELECT ARRAYS_OVERLAP(ARRAY('red', NULL, 'blue'), ARRAY('green', NULL));
 arrays_overlap
----------------
 t
(1 row)

SELECT ARRAYS_OVERLAP(ARRAY('red', NULL, 'blue'), ARRAY('green'));
 arrays_overlap
----------------
 f
(1 row)

SELECT ARRAYS_OVERLAP(JSON_PARSE('[null]'), ARRAY(NULL));
 arrays_overlap
----------------
 t
(1 row)
```

## See also
<a name="arrays_overlap-see-also"></a>
+ [ARRAY\_INTERSECTION function](array_intersection.md)
+ [ARRAY\_CONTAINS function](array_contains.md)
+ [ARRAY\_EXCEPT function](array_except.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
