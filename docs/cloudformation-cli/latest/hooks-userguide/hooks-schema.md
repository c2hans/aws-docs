---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-schema.html
---

# Schema syntax reference for CloudFormation Hooks
<a name="hooks-schema"></a>

This section describes the syntax of the schema that you use to develop CloudFormation Hooks.

A Hook includes a Hook specification represented by a JSON schema and Hook handlers. The first step in creating a custom Hook is modeling a schema that defines the Hook, its properties, and their attributes. When you initialize a custom Hook project using the CloudFormation CLI [init](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-init.html) command, a Hook schema file is created for you. Use this schema file as a starting point for defining the shape and semantics of your custom Hook.

## Schema syntax
<a name="schema-syntax"></a>

The following schema is the structure for a Hook.

```
{
"typeName": "string",
    "description": "string",
    "sourceUrl": "string",
    "documentationUrl": "string",
    "definitions": {
        "definitionName": {
          . . .
        }
    },
    "typeConfiguration": {
        "properties": {
             "propertyName": {
                "description": "string",
                "type": "string",
                 . . .
            },
        },
    "required": [
        "propertyName"
         . . .
            ],
    "additionalProperties": false
    },
    "handlers": {
        "preCreate": {
            "targetNames": [
            ],
            "permissions": [
            ]
        },
        "preUpdate": {
            "targetNames": [
            ],
            "permissions": [
            ]
        },
        "preDelete": {
            "targetNames": [
            ],
            "permissions": [
            ]
        }
   },
   "additionalProperties": false
}
```

`typeName`  <a name="hooks-properties-typeName"></a>
The unique name for your Hook. Specifies a three-part namespace for your Hook, with a recommended pattern of `Organization::Service::Hook`.
The following organization namespaces are reserved and can't be used in your Hook type names:
+ `Alexa`
+ `AMZN`
+ `Amazon`
+ `ASK`
+ `AWS`
+ `Custom`
+ `Dev`
*Required*: Yes
 *Pattern*: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$`
*Minimum*: `10`
*Maximum*: `196`

`description`  <a name="hooks-properties-description"></a>
A short description of the Hook that's displayed in the CloudFormation console.
*Required*: Yes

`sourceUrl`  <a name="hooks-properties-sourceUrl"></a>
The URL of the source code for the Hook, if public.
*Required*: No
*Maximum*: `4096`

`documentationUrl`  <a name="hooks-properties-documentationurl"></a>
The URL of a page providing detailed documentation for the Hook.
*Required*: Yes
*Pattern*: `^https\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])(\:[0-9]*)*([\?/#].*)?$`
*Maximum*: `4096`
Although the Hook schema should include complete and accurate property descriptions, you can use the `documentationURL` property to provide users with more details, including examples, use cases, and other detailed information.

`definitions`  <a name="hooks-properties-definitions"></a>
Use the `definitions` block to provide shared Hook property schemas.
It's considered a best practice to use the `definitions` section to define schema elements that can be used at multiple points in your Hook type schema. You can then use a JSON pointer to reference that element at the appropriate places in your Hook type schema.
*Required*: No

`typeConfiguration`  <a name="hooks-properties-typeconfiguration"></a>
The definition of a Hook’s configuration data.
*Required*: Yes

`properties`  <a name="hooks-properties-properties"></a>
The properties of the Hook. All properties of a Hook must be expressed in the schema. Align the Hook schema properties with the Hook type configuration properties.
Nested properties aren't allowed. Instead, define any nested properties in the `definitions` element, and use a `$ref` pointer to reference them in the desired property.
The following properties are currently supported:
+ `default` – The default value of the property.
+ `description` – A description of the property.
+ `pattern` – A regex pattern used for validating the input.
+ `type` – The accepted type of the property.

`additionalProperties`  <a name="hooks-properties-additionalproperties"></a>
`additionalProperties` must be set to `false`. All properties of a Hook must be expressed in the schema: arbitrary inputs aren't allowed.
*Required*: Yes
*Valid values*: `false`

`handlers`  <a name="hooks-properties-handlers"></a>
Handlers specify the operations which can initiate the Hook defined in the schema, such as Hook invocation points. For example, a `preUpdate` handler is invoked before the update operations for all specified targets in the handler.
*Valid values*: `preCreate` \| `preUpdate` \| `preDelete`
At least one value must be specified for the handler.
Stack operations that result in the status of `UpdateCleanup` do not invoke a Hook. For example, during the following two scenarios, the Hook's `preDelete` handler is not invoked:
+ the stack is updated after removing one resource from the template.
+ a resource with the update type of [replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement) is deleted.

`targetNames`  <a name="hooks-properties-targetNames"></a>
A string array of type names that Hook targets. For example, if a `preCreate` handler has an `AWS::S3::Bucket` target, the Hook runs for Amazon S3 buckets during the preprovisioning phase.
+ `TargetName`

  Specify at least one target name for each implemented handler.

  *Pattern*: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$`

  *Minimum*: `1`

  *Required*: Yes
**Warning**
SSM SecureString and Secrets Manager dynamic references are not resolved before they are passed to Hooks.

`permissions`  <a name="hooks-properties-permissions"></a>
A string array that specifies the AWS permissions needed to invoke the handler.
*Required*: Yes

`additionalProperties`  <a name="hooks-additional-properties"></a>
`additionalProperties` must be set to `false`. All properties of a Hook must be expressed in the schema: arbitrary inputs aren't allowed.
*Required*: Yes
*Valid values*: `false`

## Example Hooks schemas
<a name="example-hooks"></a>

 **Example 1**

The Java and the Python walkthroughs use the following code example. The following is an example structure for a Hook called `mycompany-testing-mytesthook.json`.

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
                "type":"string",
                "pattern": "[a-zA-Z]*[1-9]"
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

 **Example 2**

The following example is a schema that uses the `STACK` and `CHANGE_SET` for `targetNames` to target a stack template and a change set operation.

```
{
    "typeName":"MyCompany::Testing::MyTestHook",
    "description":"Verifies Stack and Change Set properties before create and update",
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
                "type":"string",
                "pattern": "[a-zA-Z]*[1-9]"
            }
        },
        "required":[
        ],
        "additionalProperties":false
    },
    "handlers":{
        "preCreate":{
            "targetNames":[
                "STACK",
                "CHANGE_SET"
            ],
            "permissions":[
            ]
        },
        "preUpdate":{
            "targetNames":[
                "STACK"
            ],
            "permissions":[
            ]
        },
        "preDelete":{
            "targetNames":[
                "STACK"
            ],
            "permissions":[

            ]
        }
    },
    "additionalProperties":false
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
