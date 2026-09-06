---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-input-data-contract-test.html
---

# Specifying input data for use in contract tests
<a name="hooks-input-data-contract-test"></a>

By default, the CloudFormation performs contract tests using input properties generated from the patterns you define in your Hook schema. However, most Hooks are complex enough that the input properties for precreating or preupdating provisioning stacks requires an understanding of the resource being provisioned. To address this, you can specify the input the CloudFormation uses when performing its contract tests.

CloudFormation offers two ways for you to specify the input data for it to use when performing contract tests:
+ Overrides file

  Using an `overrides` file provides a light-weight way of specifying input data for certain specific properties for the CloudFormation to use during `preCreate`, `preUpdate` and `preDelete` operations testing.
+ Input files

  You can also use multiple `input` files to specify contract test input data if:
  + You want or need to specify different input data for create, update, and delete operations, or invalid data with which to test.
  + You want to specify multiple different input data sets.

## Specifying input data using an override file
<a name="hook-override-inputs"></a>

The following is an example of Amazon S3 Hook's input data using the `overrides` file.

```
{
    "CREATE_PRE_PROVISION": {
        "AWS::S3::Bucket": {
            "resourceProperties": {
                "/BucketName": "encryptedbucket-us-west-2-contractor",
                "/BucketEncryption/ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            }
        },
        "AWS::SQS::Queue": {
            "resourceProperties": {
                "/QueueName": "MyQueueContract",
                "/KmsMasterKeyId": "hellocontract"
            }
        }
    },
    "UPDATE_PRE_PROVISION": {
        "AWS::S3::Bucket": {
            "resourceProperties": {
                "/BucketName": "encryptedbucket-us-west-2-contractor",
                "/BucketEncryption/ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            },
            "previousResourceProperties": {
                "/BucketName": "encryptedbucket-us-west-2-contractor",
                "/BucketEncryption/ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            }
        }
    },
    "INVALID_UPDATE_PRE_PROVISION": {
        "AWS::S3::Bucket": {
            "resourceProperties": {
                "/BucketName": "encryptedbucket-us-west-2-contractor",
                "/BucketEncryption/ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            },
            "previousResourceProperties": {
                "/BucketName": "encryptedbucket-us-west-2-contractor",
                "/BucketEncryption/ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            }
        }
    },
    "INVALID": {
        "AWS::SQS::Queue": {
            "resourceProperties": {
                "/QueueName": "MyQueueContract",
                "/KmsMasterKeyId": "KMS-KEY-ARN"
            }
        }
    }
}
```

## Specifying input data using input files
<a name="hook-test-inputs"></a>

Use `input` files to specify different kinds of input data for the CloudFormation to use: `preCreate` input, `preUpdate` input, and invalid input. Each kind of data is specified in a separate file. You can also specify multiple sets of input data for contract tests.

To specify `input` files for the CloudFormation to use in contract testing, add an `inputs` folder to the root directory of your Hooks project. Then add your input files.

Specify which kind of input data a file contains by using the following naming conventions, where *{{n}}* is an integer:
+ `inputs_{{n}}_pre_create.json`: Use files with `preCreate` handlers for specifying inputs for creating the resource.
+ `inputs_{{n}}_pre_update.json`: Use files with `preUpdate` handlers for specifying inputs for updating the resource.
+ `inputs_{{n}}_pre_delete.json`: Use files with `preDelete` handlers for specifying inputs for deleting the resource.
+ `inputs_{{n}}_invalid.json`: For specifying invalid inputs to test.

To specify multiple sets of input data for contract tests, increment the integer in the file names to order your input data sets. For example, your first set of input files should be named `inputs_1_pre_create.json`, `inputs_1_pre_update.json`, and `inputs_1_pre_invalid.json`. Your next set would be named `inputs_2_pre_create.json`, `inputs_2_pre_update.json`, and `inputs_2_pre_invalid.json`, and so on.

Each input file is a JSON file containing only the resource properties to be used in testing.

The following is an example directory for `inputs` for Amazon S3 specifying input data using input files.

`inputs_1_pre_create.json`  <a name="inputs_1_pre_create.json"></a>
The following is an example of the `inputs_1_pre_create.json` contract test.

```
{
    "AWS::S3::Bucket": {
        "resourceProperties": {
            "AccessControl": "BucketOwnerFullControl",
            "AnalyticsConfigurations": [],
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            },
            "BucketName": "encryptedbucket-us-west-2"
        }
    },
    "AWS::SQS::Queue": {
        "resourceProperties": {
            "QueueName": "MyQueue",
            "KmsMasterKeyId": "KMS-KEY-ARN"
        }
    }
}
```

`inputs_1_pre_update.json`  <a name="inputs_1_pre_update.json"></a>
The following is an example of the `inputs_1_pre_update.json` contract test.

```
{
    "AWS::S3::Bucket": {
        "resourceProperties": {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            },
            "BucketName": "encryptedbucket-us-west-2"
        },
        "previousResourceProperties": {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            },
            "BucketName": "encryptedbucket-us-west-2"
        }
    }
}
```

`inputs_1_invalid.json`  <a name="inputs_1_invalid.json"></a>
The following is an example of the `inputs_1_invalid.json` contract test.

```
{
    "AWS::S3::Bucket": {
        "resourceProperties": {
            "AccessControl": "BucketOwnerFullControl",
            "AnalyticsConfigurations": [],
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "ServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            },
            "BucketName": "encryptedbucket-us-west-2"
        }
    },
    "AWS::SQS::Queue": {
        "resourceProperties": {
            "NotValid": "The property of this resource is not valid."
        }
    }
}
```

`inputs_1_invalid_pre_update.json`  <a name="inputs_1_invalid_pre_update.json"></a>
The following is an example of the `inputs_1_invalid_pre_update.json` contract test.

```
{
    "AWS::S3::Bucket": {
        "resourceProperties": {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            },
            "BucketName": "encryptedbucket-us-west-2"
        },
        "previousResourceProperties": {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "BucketKeyEnabled": true,
                        "ServerSideEncryptionByDefault": {
                            "KMSMasterKeyID": "KMS-KEY-ARN",
                            "SSEAlgorithm": "aws:kms"
                        }
                    }
                ]
            },
            "BucketName": "encryptedbucket-us-west-2"
        }
    }
}
```
