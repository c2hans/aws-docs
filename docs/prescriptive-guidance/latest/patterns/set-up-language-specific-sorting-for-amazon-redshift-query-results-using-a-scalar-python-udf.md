---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf.html
---

# Set up language-specific sorting for Amazon Redshift query results using a scalar Python UDF
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf"></a>

*Ethan Stark, Amazon Web Services*

## Summary
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf-summary"></a>

This pattern provides steps and sample code for using a scalar Python UDF (user-defined function) to set up case insensitive linguistic sorting for Amazon Redshift query results. It’s necessary to use a scalar Python UDF because Amazon Redshift returns results based on binary UTF-8 ordering and doesn’t support language-specific sorting. A Python UDF is non-SQL processing code that’s based on a Python program and runs in a data warehouse. You can run Python UDF code with a SQL statement in a single query. For more information, see the [Introduction to Python UDFs in Amazon Redshift](https://aws.amazon.com/blogs/big-data/introduction-to-python-udfs-in-amazon-redshift/) AWS Big Data Blog post.

The sample data in this pattern is based on the Turkish alphabet for demonstration purposes. The scalar Python UDF in this pattern is built to make the default query results of Amazon Redshift conform to the linguistic ordering of characters in the Turkish language. For more information, see *Turkish language example* in the *Additional information* section of this pattern. You can modify the scalar Python UDF in this pattern for other languages.

## Prerequisites and limitations
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf-prereqs"></a>

**Prerequisites**
+ [Amazon Redshift cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) with a database, schema, and tables
+ [Amazon Redshift user](https://docs.aws.amazon.com/redshift/latest/dg/r_Users.html) with `CREATE TABLE` and `CREATE FUNCTION` permissions
+ [Python 2.7](https://www.python.org/download/releases/2.7/) or later

**Limitations**

The linguistic sorting used by the queries in this pattern is case insensitive.

## Tools
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf-tools"></a>

**AWS services**
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) is a managed petabyte-scale data warehouse service in the AWS Cloud. Amazon Redshift is integrated with your data lake, which enables you to use your data to acquire new insights for your business and customers.

**Other tools**
+ [Python (UDFs) user-defined functions](https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-introduction.html) are functions that you can write in Python and then call in SQL statements.

## Epics
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf-epics"></a>

### Develop code to sort query results in linguistic order
<a name="develop-code-to-sort-query-results-in-linguistic-order"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a table for your sample data. | To create a table in Amazon Redshift and insert your sample data into the table, use the following SQL statements:<pre>CREATE TABLE my_table (first_name varchar(30));<br /><br />INSERT INTO my_table (first_name)<br />VALUES<br />    ('ali'),<br />    ('Ali'),<br />    ('ırmak'),<br />    ('IRMAK'),<br />    ('irem'),<br />    ('İREM'),<br />    ('oğuz'),<br />    ('OĞUZ'),<br />    ('ömer'),<br />    ('ÖMER'),<br />    ('sedat'),<br />    ('SEDAT'),<br />    ('şule'),</pre>The first names in the sample data include special characters from the Turkish alphabet. For more information about Turkish language considerations for this example, see *Turkish language example* in the *Additional information* section of this pattern. | Data engineer |
| Check the default sorting of the sample data. | To see the default sorting of your sample data in Amazon Redshift, run the following query:<pre>SELECT first_name FROM my_table ORDER BY first_name;</pre><br />The query returns the list of first names from the table that you created earlier:<pre>first_name<br />---------------<br />Ali<br />IRMAK<br />OĞUZ<br />SEDAT<br />ali<br />irem<br />oğuz<br />sedat<br />ÖMER<br />ömer<br />İREM<br />ırmak<br />ŞULE<br />şule</pre><br />The query results aren’t in the correct order because the default binary UTF-8 ordering doesn’t accommodate the linguistic ordering of the Turkish special characters. | Data engineer |
| Create a scalar Python UDF. | To create a scalar Python UDF, use the following SQL code: <pre>CREATE OR REPLACE FUNCTION collate_sort (value varchar) <br />RETURNS varchar <br />IMMUTABLE <br />AS <br />$$    <br />    def sort_str(val):<br />        import string<br />        <br />        dictionary = {<br />            'I': 'ı', <br />            'ı': 'h~', <br />            'İ': 'i', <br />            'Ş': 's~', <br />            'ş': 's~', <br />            'Ğ': 'g~', <br />            'ğ': 'g~', <br />            'Ü': 'u~', <br />            'ü': 'u~', <br />            'Ö': 'o~', <br />            'ö': 'o~', <br />            'Ç': 'c~', <br />            'ç': 'c~'<br />        }<br />        <br />        for key, value in dictionary.items():<br />            val = val.replace(key, value)<br />        <br />        return val.lower()<br /> <br />    return sort_str(value)<br />    <br />$$ LANGUAGE plpythonu;</pre> | Data engineer |
| Query the sample data. | To query the sample data by using the Python UDF, run the following SQL query:<pre>SELECT first_name FROM my_table ORDER BY collate_sort(first_name);</pre><br />The query now returns the sample data in Turkish linguistic order:<pre>first_name<br />---------------<br />ali<br />Ali<br />ırmak<br />IRMAK<br />irem<br />İREM<br />oğuz<br />OĞUZ<br />ömer<br />Ömer<br />sedat<br />SEDAT<br />şule<br />ŞULE</pre> | Data engineer |

## Related resources
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf-resources"></a>
+ [ORDER BY clause](https://docs.aws.amazon.com/redshift/latest/dg/r_ORDER_BY_clause.html) (Amazon Redshift documentation)
+ [Creating a scalar Python UDF](https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-scalar-udf.html) (Amazon Redshift documentation)

## Additional information
<a name="set-up-language-specific-sorting-for-amazon-redshift-query-results-using-a-scalar-python-udf-additional"></a>

**Turkish language example**

Amazon Redshift returns query results based on binary UTF-8 sort ordering, not language-specific sort ordering. This means that if you query an Amazon Redshift table containing Turkish characters, then the query results aren’t sorted according to the linguistic ordering of the Turkish language. The Turkish language contains six special characters (ç, ı, ğ, ö, ş, and ü) that don’t appear in the Latin alphabet. These special characters are placed at the end of a sorted result set based on binary UTF-8 ordering, as the following table shows.

|
|
| Binary UTF-8 ordering | Turkish linguistic ordering |
| --- |--- |
| a | a |
| b | b |
| c | c |
| d | **ç (\*)** |
| e | d |
| f | e |
| g | f |
| h | g |
| i | **ğ (\*)** |
| j | h |
| k | **ı (\*)** |
| l | i |
| m | j |
| n | k |
| o | l |
| p | m |
| r | n |
| s | o |
| t | **ö (\*)** |
| u | p |
| v | r |
| y | s |
| z | **ş (\*)** |
| **ç (\*)** | t |
| **ğ (\*)** | u |
| **ı (\*)** | **ü (\*)** |
| **ö (\*)** | v |
| **ş (\*)** | y |
| **ü (\*)** | z |

**Note**
The asterisk (\*) indicates a special character in the Turkish language.

As the table above illustrates, special character **ç** is between **c** and **d** in Turkish linguistic ordering, but appears after **z** in binary UTF-8 ordering. The scalar Python UDF in this pattern uses the following character replacement dictionary to replace the Turkish special characters with corresponding Latin-equivalent characters.

|
|
| Turkish special character | Latin-equivalent character |
| --- |--- |
| ç | c\~ |
| ı | h\~ |
| ğ | g\~ |
| ö | o\~ |
| ş | s\~ |
| ü | u\~ |

**Note**
A tilde (\~) character is appended to the end of the Latin characters that replace their corresponding Turkish special characters.

**Modify a scalar Python UDF function**

To modify the scalar Python UDF function from this pattern so that the function accepts a locate parameter and supports a multiple transaction dictionary, use the following SQL code:

```
CREATE OR REPLACE FUNCTION collate_sort (value varchar, locale varchar)
RETURNS varchar
IMMUTABLE
AS
$$
    def sort_str(val):
       import string
       # Turkish Dictionary
       if locale == 'tr-TR':
            dictionary = {
               'I': 'ı',
               'ı': 'h~',
               'İ': 'i',
               'Ş': 's~',
               'ş': 's~',
               'Ğ': 'g~',
               'ğ': 'g~',
               'Ü': 'u~',
               'ü': 'u~',
               'Ö': 'o~',
               'ö': 'o~',
               'Ç': 'c~',
               'ç': 'c~'
        }
        # German Dictionary
        if locale == 'de-DE':
            dictionary = {
               ....
               ....
        }

        for key, value in dictionary.items():
            val = val.replace(key, value)

        return val.lower()

    return sort_str(value)

$$ LANGUAGE plpythonu;
```

The following example code shows how to query the modified Python UDF:

```
SELECT first_name FROM my_table ORDER BY collate_order(first_name, 'tr-TR');
```
