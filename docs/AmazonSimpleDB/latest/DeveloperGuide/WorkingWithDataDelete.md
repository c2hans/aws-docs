---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDataDelete.html
---

# Deleting Data from a Domain
<a name="WorkingWithDataDelete"></a>

The following is an example of deleting data from an item using REST.

```
https://sdb.amazonaws.com/
?Action=DeleteAttributes
&DomainName=MyDomain
&ItemName=JumboFez
&Attribute.1.Name=color
&Attribute.1.Value=red
&Attribute.2.Name=color
&Attribute.2.Value=brick
&Attribute.3.Name=color
&Attribute.3.Value=garnet
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

Amazon SimpleDB returns output similar to the following.

```
<DeleteAttributesResponse>
  <ResponseMetadata>
    <RequestId>05ae667c-cfac-41a8-ab37-a9c897c4c3ca</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</DeleteAttributesResponse>
```

**Note**
For information on performing multiple delete operations at once, see [BatchDeleteAttributes](SDB_API_BatchDeleteAttributes.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
