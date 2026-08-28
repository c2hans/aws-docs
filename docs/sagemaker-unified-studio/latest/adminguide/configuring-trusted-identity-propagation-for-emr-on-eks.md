---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-trusted-identity-propagation-for-emr-on-eks.html
---

# Configuring trusted identity propagation for Amazon EMR on EKS
<a name="configuring-trusted-identity-propagation-for-emr-on-eks"></a>

 Amazon EMR on EKS requires additional IAM permissions to enable trusted identity propagation. You must attach the following inline IAM role policy to the IAM role created as the Amazon EMR on EKS system namespace role.

**Note**
 The Amazon EMR on EKS system namespace role for an Amazon SageMaker Unified Studio project is named `datazone_emr_containers_system_namespace_role_{{{project_id}}}`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TrustedIdentityPropagation",
            "Effect": "Allow",
            "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
            ],
            "Resource": "*"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
