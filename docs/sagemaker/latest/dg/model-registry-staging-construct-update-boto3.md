---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct-update-boto3.html
---

# Update a model package stage and status example (boto3)
<a name="model-registry-staging-construct-update-boto3"></a>

To update a model package stage and status, you will need to assume an execution role with the relevant permissions. The following provides an example on how you can update the stage status using the [`UpdateModelPackage`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelPackage.html) API using AWS SDK for Python (Boto3).

In this example, the `ModelLifeCycle` stage `"Development"` and stage status `"Approved"` condition keys for the [`UpdateModelPackage`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelPackage.html) API action has been granted to the your execution role. You can include a description in `{{stage-description}}`. See [Set up Staging Construct Examples](model-registry-staging-construct-set-up.md) for more information.

```
from sagemaker.core.helper.session_helper import get_execution_role, session
import boto3

region = boto3.Session().region_name role = get_execution_role()
sm_client = boto3.client('sagemaker', region_name=region)

model_package_update_input_dict = {
    "ModelLifeCycle" : {
        "stage" : "Development",
        "stageStatus" : "Approved",
        "stageDescription" : "{{stage-description}}"
    }
}
model_package_update_response = sm_client.update_model_package(**model_package_update_input_dict)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
