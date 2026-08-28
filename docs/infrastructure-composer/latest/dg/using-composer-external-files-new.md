---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-new.html
---

# Create an external file reference in Infrastructure Composer
<a name="using-composer-external-files-new"></a>

You can create an external file reference from the **resource properties** panel of supported resources.

**To create an external file reference**

1. From an **API Gateway** or **Step Functions** enhanced component card, select **Details** to bring up the **resource properties ** panel.

1. Locate and select the **Use external file** option.

1. Specify the relative path to the external file. This is the path from your `template.yaml` file to the external file.

   For example, to reference the `api-spec.yaml` external file from the following project’s structure, specify `./api-spec.yaml` as your relative path.

   ```
   demo
   ├── api-spec.yaml
   ├── src
   │ └── Function
   │ ├── index.js
   │ └── package.json
   └── template.yaml
   ```
**Note**
If the external file and its specified path does not exist, Infrastructure Composer will create it.

1. **Save** your changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
