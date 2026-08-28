---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDataGet.html
---

# Getting Data from a Domain
<a name="WorkingWithDataGet"></a>

The following is an example of getting data from an item using REST.

```
https://sdb.amazonaws.com/
?Action=GetAttributes
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&ItemName=JumboFez
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

Amazon SimpleDB returns output similar to the following.

```
<GetAttributesResponse>
  <GetAttributesResult>
    <Attribute><Name>Color</Name><Value>Blue</Value></Attribute>
    <Attribute><Name>Size</Name><Value>Med</Value></Attribute>
    <Attribute><Name>Price</Name><Value>0014.99</Value></Attribute>
  </GetAttributesResult>
  <ResponseMetadata>
    <RequestId>b1e8f1f7-42e9-494c-ad09-2674e557526d</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</GetAttributesResponse>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
