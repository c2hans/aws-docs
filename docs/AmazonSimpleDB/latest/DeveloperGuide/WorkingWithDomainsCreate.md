---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsCreate.html
---

# Creating a Domain
<a name="WorkingWithDomainsCreate"></a>

The following is an example of creating a domain using REST.

```
https://sdb.amazonaws.com/
?Action=CreateDomain
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A01%3A28-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

Amazon SimpleDB returns output similar to the following.

```
<CreateDomainResponse>
  <ResponseMetadata>
    <RequestId>2a1305a2-ed1c-43fc-b7c4-e6966b5e2727</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</CreateDomainResponse>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
