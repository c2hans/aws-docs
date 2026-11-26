---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-security.html
---

# Security with multi-container endpoints with direct invocation

 For multi-container endpoints with direct invocation, there are multiple containers hosted in a single instance by sharing memory and a storage volume. It's your responsibility to use secure containers, maintain the correct mapping of requests to target containers, and provide users with the correct access to target containers. SageMaker AI uses IAM roles to provide IAM identity-based policies that you use to specify whether access to a resource is allowed or denied to that role, and under what conditions. For information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *AWS Identity and Access Management User Guide*. For information about identity-based policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html).

By default, an IAM principal with `InvokeEndpoint` permissions on a multi-container endpoint with direct invocation can invoke any container inside the endpoint with the endpoint name that you specify when you call `invoke_endpoint`. If you need to restrict `invoke_endpoint` access to a limited set of containers inside a multi-container endpoint, use the `sagemaker:TargetContainerHostname` IAM condition key. The following policies show how to limit calls to specific containers within an endpoint.

The following policy allows `invoke_endpoint` requests only when the value of the `TargetContainerHostname` field matches one of the specified regular expressions.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowInvokeSpecificContainers",
            "Action": [
                "sagemaker:InvokeEndpoint"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:endpoint/{{endpoint-name}}",
            "Condition": {
                "StringLike": {
                    "sagemaker:TargetContainerHostname": [
                        "{{container-hostname-1}}",
                        "{{container-hostname-prefix}}*"
                    ]
                }
            }
        }
    ]
}
```

The following policy denies `invoke_endpoint` requests when the value of the `TargetContainerHostname` field matches one of the specified regular expressions in the `Deny` statement.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowInvokeEndpoint",
            "Action": [
                "sagemaker:InvokeEndpoint"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:endpoint/{{endpoint-name}}"
        },
        {
            "Sid": "DenyInvokeSpecificContainers",
            "Action": [
                "sagemaker:InvokeEndpoint"
            ],
            "Effect": "Deny",
            "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:endpoint/{{endpoint-name}}",
            "Condition": {
                "StringLike": {
                    "sagemaker:TargetContainerHostname": [
                        "{{container-hostname-prefix}}*"
                    ]
                }
            }
        }
    ]
}
```

 For information about SageMaker AI condition keys, see [Condition Keys for SageMaker AI](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys) in the *AWS Identity and Access Management User Guide*.
