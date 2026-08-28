---
source_url: https://docs.aws.amazon.com/translate/latest/dg/tagging-newtags.html
---

# Tagging a new resource
<a name="tagging-newtags"></a>

You can add tags to a **ParallelData** or **Custom Terminology** resource when you create it.

**To add tags to a new resource (console)**

1. Sign in to the [Amazon Translate console](https://console.aws.amazon.com/translate/).

1. From the left navigation pane, select the resource (`Parallel data` or `Custom terminology`) that you want to create.

1. Chose **Create parallel data** or **Create terminology**. The console displays the main 'create' page for your resource. At the end of this page, you see a '**Tags -** *optional*' panel.
![Screen shot showing the empty tags panel.](http://docs.aws.amazon.com/translate/latest/dg/images/add-tags-1.png)

1. Choose **Add new tag** to add a tag for the resource. Enter a tag key and, optionally, a tag value.
![Screen shot showing the tags panel with one tag defined.](http://docs.aws.amazon.com/translate/latest/dg/images/add-tags-2.png)

1. Repeat step 4 until you have added all your tags. Each key must be unique for this resource.
![Screen shot showing the the empty fields for adding a new tag.](http://docs.aws.amazon.com/translate/latest/dg/images/add-tags-3.png)

1. Choose **Create parallel data** or **Create terminology** to create the resource.

You can also add tags using the Amazon Translate [CreateParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_CreateParallelData.html) API operation. The following example shows how to add tags with the create-parallel-data CLI command.

```
aws translate create-parallel-data \
--name "{{myTest}}" \
--parallel-data-config "{\"format\": \"{{CSV}}\",  \
             "S3Uri\": \"s3://{{test-input/TEST.csv}}\"}" \
--tags "[{\"Key\": \"{{color}}\",\"Value\": \"{{orange}}\"}]"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
