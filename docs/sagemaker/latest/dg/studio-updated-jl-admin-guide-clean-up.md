---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-clean-up.html
---

# Delete unused resources
<a name="studio-updated-jl-admin-guide-clean-up"></a>

To avoid incurring additional costs running JupyterLab, we recommend deleting unused resources in the following order:

1. JupyterLab applications

1. Spaces

1. User profiles

1. domains

Use the following AWS Command Line Interface (AWS CLI) commands to delete resources within a domain:

------
#### [ Delete a JupyterLab application ]

```
aws --region {{AWS Region}} sagemaker delete-app --domain-id {{example-domain-id}} --app-name default --app-type JupyterLab --space-name {{example-space-name}}
```

------
#### [ Delete a space ]

**Important**
If you delete a space, you delete the Amazon EBS volume associated with it. We recommend backing up any valuable data before you delete your space.

```
aws --region {{AWS Region}} sagemaker delete-space --domain-id {{example-domain-id}}  --space-name {{example-space-name}}
```

------
#### [ Delete a user profile ]

```
aws --region {{AWS Region}} sagemaker delete-user-profile --domain-id {{example-domain-id}} --user-profile {{example-user-profile}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
