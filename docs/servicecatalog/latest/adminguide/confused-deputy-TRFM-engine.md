---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/confused-deputy-TRFM-engine.html
---

# Adding Confused Deputy to your Terraform provisioning engine
<a name="confused-deputy-TRFM-engine"></a>

## Confused Deputy context keys on the endpoints to restrict access for `lambda:Invoke` operations
<a name="confused-deputy-TRFM-lambda"></a>

The parameter parser Lambda function created by AWS Service Catalog-provided engines has an access policy that grants cross-account `lambda:Invoke` permission only to the AWS Service Catalog service principal:

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
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-1:{{111122223333}}:function:ServiceCatalogTerraformOSParameterParser"
        }
    ]
}
```

------

This should be the only permission necessary in order for the integration with AWS Service Catalog to function properly. However, you can constrain this further using the `aws:SourceAccount` [ Confused Deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy) context key. When AWS Service Catalog sends messages to these queues, AWS Service Catalog populates the key with the provisioning account's ID. This is helpful when you intend to distribute products via portfolio sharing and want to ensure that only specific accounts are using your engine.

For example, you can restrict your engine to only allow requests that originate from 000000000000 and 111111111111 using the condition shown below:

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
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-1:{{111122223333}}:function:ServiceCatalogTerraformOSParameterParser",
            "Condition": {
                "StringLike": {
                    "aws:SourceAccount": [
                        "000000000000",
                        "111111111111"
                    ]
                }
            }
        }
    ]
}
```

------

## Confused Deputy context keys on the endpoints to restrict access for `sqs:SendMessage` operations
<a name="confused-deputy-TRFM-sqs"></a>

The provisioning operation intake Amazon SQS queues created by AWS Service Catalog-provided engines have an access policy that grants cross-account `sqs:SendMessage` (and associated KMS) permissions only to the AWS Service Catalog service principal:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Enable AWS Service Catalog to send messages to the queue",
            "Effect": "Allow",
            "Principal": {
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": "sqs:SendMessage",
            "Resource": [
                "arn:aws:sqs:us-east-1:{{111122223333}}:ServiceCatalogTerraformOSProvisionOperationQueue"
            ]
        },
        {
            "Sid": "Enable AWS Service Catalog encryption/decryption permissions when sending message to queue",
            "Effect": "Allow",
            "Principal": {
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:Decrypt",
                "kms:ReEncryptFrom",
                "kms:ReEncryptTo",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:{{111122223333}}:key/key_id"
        }
    ]
}
```

------

This should be the only permission necessary in order for the integration with AWS Service Catalog to function properly. However, you can constrain this further using the `aws:SourceAccount` [ Confused Deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy) context key. When AWS Service Catalog sends messages to these queues, AWS Service Catalog populates the keys with the provisioning account's ID. This is helpful when you intend to distribute products via portfolio sharing and want to ensure that only specific accounts are using your engine.

For example, you can restrict your engine to only allow requests that originate from 000000000000 and 111111111111 using the condition shown below:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Enable AWS Service Catalog to send messages to the queue",
            "Effect": "Allow",
            "Principal": {
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": "sqs:SendMessage",
            "Resource": [
                "arn:aws:sqs:us-east-1:{{111122223333}}:ServiceCatalogTerraformOSProvisionOperationQueue"
            ],
            "Condition": {
                "StringLike": {
                    "aws:SourceAccount": [
                        "000000000000",
                        "111111111111"
                    ]
                }
            }
        },
        {
            "Sid": "Enable AWS Service Catalog encryption/decryption permissions when sending message to queue",
            "Effect": "Allow",
            "Principal": {
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:Decrypt",
                "kms:ReEncryptFrom",
                "kms:ReEncryptTo",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:{{111122223333}}:key/key_id"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
