---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions-kvs.html
---

# Work with key value store
<a name="kvs-with-functions-kvs"></a>

You must create a key value store to hold the key-value pairs that you want to use in CloudFront Functions.

After you create the key value stores and added key-value pairs, you can use the key values in your CloudFront function code.

To get started, see the following topics:

**Topics**
+ [Create a key value store](kvs-with-functions-create.md)
+ [Associate a key value store with a function](kvs-with-functions-associate.md)
+ [Update a key value store](kvs-with-functions-edit.md)
+ [Get a reference to a key value store](kvs-with-functions-get-reference.md)
+ [Delete a key value store](kvs-with-functions-delete.md)
+ [File format for key-value pairs](kvs-with-functions-create-s3-kvp.md)

**Note**
The JavaScript runtime 2.0 includes some helper methods for working with key values in the function code. For more information, see [Helper methods for key value stores](functions-custom-methods.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
