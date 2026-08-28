---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model.html
---

# Modeling custom CloudFormation Hooks
<a name="hooks-model"></a>

Modeling custom CloudFormation Hooks involves creating a schema that defines the Hook, its properties, and their attributes. When you create your custom Hook project using the `cfn init` command, an example Hook schema is created as a JSON-formatted text file, `{{hook-name}}.json`.

Target invocation points and target actions specify the exact point where the Hook is invoked. *Hook handlers* host executable custom logic for these points. For example, a target action of the `CREATE` operation uses a `preCreate` handler. Your code written in the handler will invoke when Hook targets and services perform a matching action. *Hook targets* are the destination where hooks are invoked. You can specify targets such as, CloudFormation public resources, private resources, or custom resources. Hooks support an unlimited number of Hook targets.

The schema contains permissions required for the Hook. Authoring the Hook requires you to specify permissions for each Hook handler. CloudFormation encourages authors to write policies that follow the standard security advice of granting *least privilege*, or granting only the permissions required to perform a task. Determine what users (and roles) need to do, and then craft policies that allow them to perform *only* those tasks for Hook operations. CloudFormation uses these permissions to scope-down Hook users provided permissions. These permissions are passed down to the Hook. Hook handlers use these permissions to access AWS resources.

You can use the following schema file as a starting point to define your Hook. Use the Hook schema to specify which handlers you want to implement. If you choose not to implement a specific handler, remove it from the handlers' section of the Hook schema. For more details on the schema, see [Schema syntax](hooks-schema.md).

```
{
    "typeName":"MyCompany::Testing::MyTestHook",
    "description":"Verifies S3 bucket and SQS queues properties before create and update",
    "sourceUrl":"https://mycorp.com/my-repo.git",
    "documentationUrl":"https://mycorp.com/documentation",
    "typeConfiguration":{
        "properties":{
            "minBuckets":{
                "description":"Minimum number of compliant buckets",
                "type":"string"
            },
            "minQueues":{
                "description":"Minimum number of compliant queues",
                "type":"string"
            },
            "encryptionAlgorithm":{
                "description":"Encryption algorithm for SSE",
                "default":"AES256",
                "type":"string"
            }
        },
        "required":[

        ],
        "additionalProperties":false
    },
    "handlers":{
        "preCreate":{
            "targetNames":[
                "AWS::S3::Bucket",
                "AWS::SQS::Queue"
            ],
            "permissions":[

            ]
        },
        "preUpdate":{
            "targetNames":[
                "AWS::S3::Bucket",
                "AWS::SQS::Queue"
            ],
            "permissions":[

            ]
        },
        "preDelete":{
            "targetNames":[
                "AWS::S3::Bucket",
                "AWS::SQS::Queue"
            ],
            "permissions":[
                "s3:ListBucket",
                "s3:ListAllMyBuckets",
                "s3:GetEncryptionConfiguration",
                "sqs:ListQueues",
                "sqs:GetQueueAttributes",
                "sqs:GetQueueUrl"
            ]
        }
    },
    "additionalProperties":false
}
```

**Topics**
+ [Modeling custom CloudFormation Hooks using Java](hooks-model-java.md)
+ [Modeling custom CloudFormation Hooks using Python](hooks-model-python.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
