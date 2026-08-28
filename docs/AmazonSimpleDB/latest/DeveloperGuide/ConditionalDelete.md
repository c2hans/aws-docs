---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ConditionalDelete.html
---

# Performing a Conditional Delete
<a name="ConditionalDelete"></a>

 Conditional delete enables you to delete an item or one or more attributes of an item if the existing value of an attribute matches a value that you specify. If value does not match or is not present, the insert or update is rejected with a 409 (MultiValuedAttribute, ConditionalCheckFailed ) or 404 (AttributeDoesNotExist) error code.

**Note**
 Conditional deletes can only match single-valued attributes.

 To perform a conditional delete, specify the expected name and expected value for a `DeleteAttributes` operation. If the specified attribute does not exist, Amazon SimpleDB performs the delete.

In the following example, Amazon SimpleDB deletes the `JumboFez` product from the `MyDomain` domain if the quantity of the product reaches zero.

```
https://sdb.amazonaws.com/
?Action=DeleteAttributes
&DomainName=MyDomain
&ItemName=JumboFez
&Expected.1.Name=quantity
&Expected.1.Value=0
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A05-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

If the condition is met, Amazon SimpleDB returns output similar to the following.

```
<PutAttributesResponse>
  <ResponseMetadata>
    <RequestId>490206ce-8292-456c-a00f-61b335eb202b</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
