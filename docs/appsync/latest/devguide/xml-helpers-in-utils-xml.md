---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/xml-helpers-in-utils-xml.html
---

# XML helpers in $util.xml
<a name="xml-helpers-in-utils-xml"></a>

**Note**
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html).

`$util.xml` contains helper methods that can make it easier to translate XML responses to JSON or a Dictionary.

## $util.xml utils list
<a name="xml-helpers-in-utils-xml-list"></a>

****`$util.xml.toMap(String) : Map`****
Converts an XML string to a Dictionary.

```
Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
  <id>1</id>
  <title>Getting started with GraphQL</title>
</post>
</posts>

Output (JSON representation):

{
  "posts":{
    "post":{
      "id":1,
      "title":"Getting started with GraphQL"
    }
  }
}

Input:

<?xml version="1.0" encoding="UTF-8"?>
<posts>
<post>
  <id>1</id>
  <title>Getting started with GraphQL</title>
</post>
<post>
  <id>2</id>
  <title>Getting started with AWS AppSync</title>
</post>
</posts>

Output (JSON representation):

{
  "posts":{
    "post":[
        {
          "id":1,
          "title":"Getting started with GraphQL"
        },
        {
          "id":2,
          "title":"Getting started with AWS AppSync"
        }
    ]
  }
}
```

****`$util.xml.toJsonString(String) : String`****
Converts an XML string to a JSON string. This is similar to *toMap*, except that the output is a string. This is useful if you want to directly convert and return the XML response from an HTTP object to JSON.

****`$util.xml.toJsonString(String, Boolean) : String`****
Converts an XML string to a JSON string with an optional Boolean parameter to determine if you want to string-encode the JSON.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
