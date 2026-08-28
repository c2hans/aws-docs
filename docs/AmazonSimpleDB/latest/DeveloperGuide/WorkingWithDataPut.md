---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDataPut.html
---

# Putting Data into a Domain
<a name="WorkingWithDataPut"></a>

The following is an example of putting data into a domain using REST.

**Note**
When you put attributes, notice that the `Replace` parameter is optional, and set to `false` by default. If you do not explicitly set `Replace` to `true`, a new attribute name-value pair is created each time; even if the `Name` value already exists in your Amazon SimpleDB domain.

```
https://sdb.amazonaws.com/
?Action=PutAttributes
&DomainName=MyDomain
&ItemName=JumboFez
&Attribute.1.Name=Color
&Attribute.1.Value=Blue
&Attribute.2.Name=Size
&Attribute.2.Value=Med
&Attribute.3.Name=Price
&Attribute.3.Value=0014.99
&Attribute.3.Replace=true
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A05-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

Amazon SimpleDB returns output similar to the following.

```
<PutAttributesResponse>
  <ResponseMetadata>
    <RequestId>490206ce-8292-456c-a00f-61b335eb202b</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>
```

**Note**
For information on performing multiple put operations at once, see [BatchPutAttributes](SDB_API_BatchPutAttributes.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
