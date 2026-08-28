---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-geospatial-roles-pass-role.html
---

# Adding the SageMaker geospatial service principal to an existing SageMaker AI execution role
<a name="sagemaker-geospatial-roles-pass-role"></a>

To use the SageMaker geospatial specific API operations your SageMaker AI execution role must include the SageMaker geospatial service principal, `sagemaker-geospatial.amazonaws.com` in the execution role's trust policy. This allows the SageMaker AI execution role to perform actions in your AWS account on your behalf.

Actions like passing a role between services are common within SageMaker AI. For more details,

To add the SageMaker geospatial service principal to an existing SageMaker AI execution role update the existing policy to include the SageMaker geospatial service principal as shown in the following trust policy. By attaching the service principal to the trust policy a SageMaker AI execution role can now run the SageMaker geospatial specific APIs on your behalf.

To learn more about SageMaker geospatial specific IAM actions, resources, and conditions, see [Actions, Resources, and Condition Keys for SageMaker AI](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-actions-as-permissions) in the *IAM User Guide*.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "{{sagemaker-geospatial.amazonaws.com}}",
                    "sagemaker.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
