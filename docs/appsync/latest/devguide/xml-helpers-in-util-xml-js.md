---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/xml-helpers-in-util-xml-js.html
---

# XML helpers in util.xml
<a name="xml-helpers-in-util-xml-js"></a>

 `util.xml` contains methods to help with XML string conversion.

## util.xml utils list
<a name="xml-helpers-in-util-xml-list-js"></a>

 **`util.xml.toMap(String) : Object`**
Converts a XML string to a dictionary.
**Example 1:**

```
Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
    <id>1</id>
    <title>Getting started with GraphQL</title>
</post>
</posts>

Output (object):

{
    "posts":{
      "post":{
        "id":1,
        "title":"Getting started with GraphQL"
      }
    }
}
```
**Example 2:**

```
Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
  <id>1</id>
  <title>Getting started with GraphQL</title>
</post>
<post>
  <id>2</id>
  <title>Getting started with AppSync</title>
</post>
</posts>

Output (JavaScript object):

{
    "posts":{
    "post":[
        {
            "id":1,
            "title":"Getting started with GraphQL"
        },
        {
            "id":2,
            "title":"Getting started with AppSync"
        }
    ]
    }
}
```

**`util.xml.toJsonString(String, Boolean?) : String`**
Converts a XML string to a JSON string. This is similar to `toMap`, except that the output is a string. This is useful if you want to directly convert and return the XML response from an HTTP object to JSON. You can set an optional boolean parameter to determine if you want to string-encode the JSON.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
