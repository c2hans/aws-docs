---
source_url: https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/capture-the-deployment-uuid.html
---

# Capture the deployment UUID
<a name="capture-the-deployment-uuid"></a>

Capture and store the deployment UUIDs (Universally Unique ID) of the guidance. This is used to look for any resources not destroyed by CloudFormation after teardown completes.

```
make get-deployment-uuid
make get-cms-deployment-uuid
```

The output will be uuidv4 strings, capture and store both:

```
XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Connected Mobility on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
