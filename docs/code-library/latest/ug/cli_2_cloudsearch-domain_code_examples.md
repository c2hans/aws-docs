---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_cloudsearch-domain_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon CloudSearch examples using AWS CLI
<a name="cli_2_cloudsearch-domain_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon CloudSearch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `upload-documents`
<a name="cloudsearch-domain_UploadDocuments_cli_2_topic"></a>

The following code example shows how to use `upload-documents`.

**AWS CLI**
The following `upload-documents` command uploads a batch of JSON documents to an Amazon CloudSearch domain:

```
aws cloudsearchdomain upload-documents --endpoint-url {{https://doc-my-domain.us-west-1.cloudsearch.amazonaws.com}} --content-type {{application/json}} --documents {{document-batch.json}}
```
Output:

```
{
  "status": "success",
  "adds": 5000,
  "deletes": 0
}
```
+  For API details, see [UploadDocuments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/upload-documents.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
