---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-xml-results.html
---

# Getting Results as XML in Amazon CloudSearch
<a name="getting-xml-results"></a>

By default, Amazon CloudSearch search responses are formatted in JSON. To get results as XML, specify the query parameter `format=xml` in your search request:

```
search?q=star wars&return=_no_fields&format=xml
```

Search responses formatted in XML contain exactly the same information as a JSON response:

```
<results>
    <status rid="3abhhs8oEAqMHnk=" time-ms="2"/>
    <hits found="9" start="0">
        <hit id="tt0076759"/>
        <hit id="tt0086190"/>
        <hit id="tt0121766"/>
        <hit id="tt2488496"/>
        <hit id="tt1408101"/>
        <hit id="tt0489049"/>
        <hit id="tt0120915"/>
        <hit id="tt0080684"/>
        <hit id="tt0121765"/>
    </hits>
</results>
```

For detailed information about the JSON and XML response formats for search requests, see [Search Response](search-api.md#search-response).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
