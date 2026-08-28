---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsList.html
---

# Verifying the Domain
<a name="WorkingWithDomainsList"></a>

The following is an example of listing domains using REST.

```
https://sdb.amazonaws.com/
?Action=ListDomains
&AWSAccessKeyId=[valid access key id]
&MaxNumberOfDomains=2
&NextToken=[valid next token]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A02%3A19-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

Amazon SimpleDB returns output similar to the following.

```
<ListDomainsResponse>
  <ListDomainsResult>
    <DomainName>MyDomain</DomainName>
    <DomainName>MyOtherDomain</DomainName>
  </ListDomainsResult>
  <ResponseMetadata>
    <RequestId>eb13162f-1b95-4511-8b12-489b86acfd28</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</ListDomainsResponse>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
