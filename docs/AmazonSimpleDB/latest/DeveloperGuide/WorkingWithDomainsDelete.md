---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsDelete.html
---

# Deleting a Domain
<a name="WorkingWithDomainsDelete"></a>

The following is an example of deleting a domain using REST.

```
https://sdb.amazonaws.com/
?Action=DeleteDomain
&AWSAccessKeyId=[valid access key id]
&DomainName=MyOtherDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A02%3A20-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

Amazon SimpleDB returns output similar to the following.

```
<DeleteDomainResponse>
  <ResponseMetadata>
    <RequestId>c522638b-31a2-4d69-b376-8c5428744704</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</DeleteDomainResponse>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
