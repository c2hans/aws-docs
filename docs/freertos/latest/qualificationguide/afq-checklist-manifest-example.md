---
source_url: https://docs.aws.amazon.com/freertos/latest/qualificationguide/afq-checklist-manifest-example.html
---

# Example manifest.yml
<a name="afq-checklist-manifest-example"></a>

```
---
# This is an example of the manifest file that is included at the root of all FreeRTOS GitHub repositories.

name : "Project_Name"
version: "202012.00-LTS"
description: "Clear concise description of this project."

dependencies:
  - name: "dependency_1"
    version: "v1.0.0"
    repository:
      type: "git"
      url: "https://github.com/account/dependency_1"
      path: "/relative/path/from/project/root/to/dependency_1"
      branch: "1.x"
  - name: "dependency_2"
    version: "v1.0.1_LTS"
    repository:
      type: "git"
      url: "https://github.com/account/dependency_1"
      path: "/relative/path/from/project/root/to/dependency_2"

license: "MIT"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
