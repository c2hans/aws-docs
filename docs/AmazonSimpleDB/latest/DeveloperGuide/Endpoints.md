---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Endpoints.html
---

# Region Endpoints
<a name="Endpoints"></a>

 To improve latency and to store data in a location that meets your requirements, Amazon SimpleDB enables you to select different Region endpoints.

For information about the Amazon SimpleDB Regions and endpoints, go to [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#sdb_region) in the Amazon Web Services General Reference.

For example, to create a SimpleDB domain in Europe, you would generate a REST request similar to the following:

```
https://sdb.eu-west-1.amazonaws.com/?Action=CreateDomain
&DomainName=MyDomain
&<authentication parameters>
```

Each Amazon SimpleDB endpoint is entirely independent. For example, if you have two domains called "MyDomain," one in sdb.amazonaws.com and one in sdb.eu-west-1.amazonaws.com, they are completely independent and do not share any data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
