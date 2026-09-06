---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-create-lambda-function.html
---

# Create Lambda functions to evaluate resources for Lambda Hooks
<a name="lambda-hooks-create-lambda-function"></a>

CloudFormation Lambda Hooks allows you to evaluate CloudFormation and AWS Cloud Control API operations against your own custom code. Your Hook can block an operation from proceeding, or issue a warning to the caller and allow the operation to proceed. When you create a Lambda Hook, you can configure it to intercept and evaluate the following CloudFormation operations:
+ Resource operations
+ Stack operations
+ Change set operations

**Topics**
+ [Developing a Lambda Hook](#lambda-hooks-create-lambda-function-develop)
+ [Evaluating resource operations with Lambda Hooks](#lambda-hooks-create-lambda-function-resource)
+ [Evaluating stack operations with Lambda Hooks](#lambda-hooks-create-lambda-function-stack)
+ [Evaluating change set operations with Lambda Hooks](#lambda-hooks-create-lambda-function-change-set)

## Developing a Lambda Hook
<a name="lambda-hooks-create-lambda-function-develop"></a>

When Hooks invoke your Lambda it will wait up to 30 seconds for the Lambda to evaluate the input. The Lambda will return a JSON response that indicates whether the Hook succeeded or failed.

**Topics**
+ [Request input](#lambda-hooks-create-lambda-function-request-input)
+ [Response input](#lambda-hooks-create-lambda-function-request-response)
+ [Examples](#lambda-hooks-create-lambda-function-request-example)

### Request input
<a name="lambda-hooks-create-lambda-function-request-input"></a>

The input passed to your Lambda function depends on the Hook target operation (examples: stack, resource, or change set).

### Response input
<a name="lambda-hooks-create-lambda-function-request-response"></a>

In order to communicate to Hooks if your request succeeded or failed, your Lambda function needs to return a JSON response.

The following is an example shape of the response Hooks expects:

```
{
  "hookStatus": "SUCCESS" or "FAILED" or "IN_PROGRESS",
  "errorCode": "NonCompliant" or "InternalFailure"
  "message": String,
  "clientRequestToken": String,
  "callbackContext": None,
  "callbackDelaySeconds": Integer,
  "annotations": [
    {
      "annotationName": String,
      "status": "PASSED" or "FAILED" or "SKIPPED",
      "statusMessage": String,
      "remediationMessage": String,
      "remediationLink": String,
      "severityLevel": "INFORMATIONAL" or "LOW" or "MEDIUM" or "HIGH" or "CRITICAL"
    }
  ]
}
```

hookStatus  <a name="lambda-hook-response-hookstatus"></a>
The status of the Hook. This is a required field.
*Valid values*: (`SUCCESS` \| `FAILED` \| `IN_PROGRESS`)
A Hook can return `IN_PROGRESS` 3 times. If no result is returned, the Hook will fail. For a Lambda Hook, this means your Lambda function can be invoked up to 3 times.

errorCode  <a name="lambda-hook-response-errorcode"></a>
Shows whether the operation was evaluated and determined to be invalid, or if errors occurred within the Hook, preventing the evaluation. This field is required if the Hook fails.
*Valid values*: (`NonCompliant` \| `InternalFailure`)

message  <a name="lambda-hook-response-message"></a>
The message to the caller that states why the Hook succeeded or failed.
When evaluating CloudFormation operations, this field is truncated to 4096 characters.
When evaluating Cloud Control API operations, this field is truncated to 1024 characters.

clientRequestToken  <a name="lambda-hook-response-clientrequesttoken"></a>
The request token that was provided as an input to the Hook request. This is a required field.

callbackContext  <a name="lambda-hook-response-callbackcontext"></a>
If you indicate that the `hookStatus` is `IN_PROGRESS` you pass an additional context that's provided as input when the Lambda function is reinvoked.

callbackDelaySeconds  <a name="lambda-hook-response-callbackdelayseconds"></a>
How long Hooks should wait to invoke this Hook again.

annotations  <a name="lambda-hook-response-annotations"></a>
An array of annotation objects that provide further details and remediation guidance.
annotationName
An identifier for the annotation.
status
The Hook invocation status. This is helpful when annotations represent logic with pass/fail evaluation similar to a Guard rule.
*Valid values*: (`PASSED` \| `FAILED` \| `SKIPPED`)
statusMessage
Explanation for the specific status.
remediationMessage
Suggestion for fixing a `FAILED` status. For example, if a resource is missing encryption, you can state how to add encryption to the resource configuration.
remediationLink
An HTTP URL for additional remediation guidance.
severityLevel
Defines the relative risk associated with any violations of this type. When assigning severity levels to your Hook invocation results, you can reference the AWS Security Hub CSPM [severity framework](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-required-attributes.html#Severity) as an example of how to structure meaningful severity categories.
*Valid values*: (`INFORMATIONAL` \| `LOW` \| `MEDIUM` \| `HIGH` \| `CRITICAL`)

### Examples
<a name="lambda-hooks-create-lambda-function-request-example"></a>

The following is an example of a successful response:

```
{
  "hookStatus": "SUCCESS",
  "message": "compliant",
  "clientRequestToken": "123avjdjk31"
}
```

The following is an example of a failed response:

```
{
  "hookStatus": "FAILED",
  "errorCode": "NonCompliant",
  "message": "S3 Bucket Versioning must be enabled.",
  "clientRequestToken": "123avjdjk31"
 }
```

## Evaluating resource operations with Lambda Hooks
<a name="lambda-hooks-create-lambda-function-resource"></a>

Any time you create, update, or delete a resource, that's considered a resource operation. As an example, if you run update a CloudFormation stack that creates a new resource, you have completed a resource operation. When you create, update or delete a resource using Cloud Control API, that is also considered a resource operation. You can configure your CloudFormation Lambda Hook to target `RESOURCE` and `CLOUD_CONTROL` operations in the Hook `TargetOperations` configuration.

**Note**
The `delete` Hook handler is only invoked when a resource is deleted using an operation trigger from Cloud Control API `delete-resource` or CloudFormation `delete-stack`.

**Topics**
+ [Lambda Hook resource input syntax](#lambda-hooks-create-lambda-function-resource-input)
+ [Example Lambda Hook resource change input](#lambda-hooks-create-lambda-function-resource-example)
+ [Example Lambda function for resource operations](#lambda-hooks-create-lambda-function-resource-example-function)

### Lambda Hook resource input syntax
<a name="lambda-hooks-create-lambda-function-resource-input"></a>

When your Lambda is invoked for a resource operation, you'll receive a JSON input containing the resource properties, proposed properties, and the context around the Hook invocation.

The following is an example shape of the JSON input:

```
{
    "awsAccountId": String,
    "stackId": String,
    "changeSetId": String,
    "hookTypeName": String,
    "hookTypeVersion": String,
    "hookModel": {
        "LambdaFunction": String
    },
    "actionInvocationPoint": "CREATE_PRE_PROVISION" or "UPDATE_PRE_PROVISION" or "DELETE_PRE_PROVISION"
    "requestData": {
        "targetName": String,
        "targetType": String,
        "targetLogicalId": String,
        "targetModel": {
            "resourceProperties": {...},
            "previousResourceProperties": {...}
        }
    },
    "requestContext": {
        "invocation": 1,
        "callbackContext": null
    }
}
```

`awsAccountId`  <a name="lambda-hook-resource-awsaccountid"></a>
The ID of the AWS account containing the resource being evaluated.

`stackId`  <a name="lambda-hook-resource-stackid"></a>
The stack ID of the CloudFormation stack this operation is a part of. This field is empty if the caller is Cloud Control API.

`changeSetId`  <a name="lambda-hook-resource-changesetid"></a>
The ID of the change set that initiated the Hook invocation. This value is empty if the resource change was initiated by Cloud Control API, or the `create-stack`, `update-stack`, or `delete-stack` operations.

`hookTypeName`  <a name="lambda-hook-resource-hooktypename"></a>
The name of the Hook that's running.

`hookTypeVersion`  <a name="lambda-hook-resource-hooktypeversion"></a>
The version of the Hook that's running.

`hookModel`  <a name="lambda-hook-resource-hookmodel"></a>
`LambdaFunction`  <a name="lambda-hook-resource-hookmodel-lambdafunction"></a>
The current Lambda ARN invoked by the Hook.

`actionInvocationPoint`  <a name="lambda-hook-resource-actioninvocationpoint"></a>
The exact point in the provisioning logic where the Hook runs.
*Valid values*: (`CREATE_PRE_PROVISION` \| `UPDATE_PRE_PROVISION` \| `DELETE_PRE_PROVISION`)

`requestData`  <a name="lambda-hook-resource-requestdata"></a>
`targetName`  <a name="lambda-hook-resource-requestdata-targetname"></a>
The target type being evaluated, for example, `AWS::S3::Bucket`.
`targetType`  <a name="lambda-hook-resource-requestdata-targettype"></a>
The target type being evaluated, for example `AWS::S3::Bucket`. For resources provisioned with Cloud Control API, this value will be `RESOURCE`.
`targetLogicalId`  <a name="lambda-hook-resource-requestdata-targetlogicalid"></a>
The logical ID of the resource being evaluated. If the origin of the Hook invocation is CloudFormation, this will be the logical resource ID defined in your CloudFormation template. If the origin of this Hook invocation is Cloud Control API, this will be a constructed value.
`targetModel`  <a name="lambda-hook-resource-requestdata-targetmodel"></a>
`resourceProperties`  <a name="lambda-hook-resource-requestdata-targetmodel-resourceproperties"></a>
The proposed properties of the resource being modified. If the resource is being deleted, this value will be empty.
`previousResourceProperties`  <a name="lambda-hook-resource-requestdata-targetmodel-previousresourceproperties"></a>
The properties that are currently associated with the resource being modified. If the resource is being created, this value will be empty.

`requestContext`  <a name="lambda-hook-resource-requestcontext"></a>
invocation  <a name="lambda-hook-resource-requestcontext-invocation"></a>
The current attempt at executing the Hook.
callbackContext  <a name="lambda-hook-resource-requestcontext-callbackcontext"></a>
If the Hookwas set to `IN_PROGRESS`, and `callbackContext` was returned, it will be here after reinvocation.

### Example Lambda Hook resource change input
<a name="lambda-hooks-create-lambda-function-resource-example"></a>

The following example input shows a Lambda Hook that will receive the definition of the `AWS::DynamoDB::Table` resource to update, where the `ReadCapacityUnits` of `ProvisionedThroughput` is changed from 3 to 10. This is the data available to Lambda for evaluation.

```
{
    "awsAccountId": "123456789012",
    "stackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
    "hookTypeName": "my::lambda::resourcehookfunction",
    "hookTypeVersion": "00000008",
    "hookModel": {
        "LambdaFunction": "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
    },
    "actionInvocationPoint": "UPDATE_PRE_PROVISION",
    "requestData": {
        "targetName": "AWS::DynamoDB::Table",
        "targetType": "AWS::DynamoDB::Table",
        "targetLogicalId": "DDBTable",
        "targetModel": {
            "resourceProperties": {
                "AttributeDefinitions": [
                    {
                        "AttributeType": "S",
                        "AttributeName": "Album"
                    },
                    {
                        "AttributeType": "S",
                        "AttributeName": "Artist"
                    }
                ],
                "ProvisionedThroughput": {
                    "WriteCapacityUnits": 5,
                    "ReadCapacityUnits": 10
                },
                "KeySchema": [
                    {
                        "KeyType": "HASH",
                        "AttributeName": "Album"
                    },
                    {
                        "KeyType": "RANGE",
                        "AttributeName": "Artist"
                    }
                ]
            },
            "previousResourceProperties": {
                "AttributeDefinitions": [
                    {
                        "AttributeType": "S",
                        "AttributeName": "Album"
                    },
                    {
                        "AttributeType": "S",
                        "AttributeName": "Artist"
                    }
                ],
                "ProvisionedThroughput": {
                    "WriteCapacityUnits": 5,
                    "ReadCapacityUnits": 5
                },
                "KeySchema": [
                    {
                        "KeyType": "HASH",
                        "AttributeName": "Album"
                    },
                    {
                        "KeyType": "RANGE",
                        "AttributeName": "Artist"
                    }
                ]
            }
        }
    },
    "requestContext": {
        "invocation": 1,
        "callbackContext": null
    }
}
```

To see all of the properties available for the resource type, see [AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html).

### Example Lambda function for resource operations
<a name="lambda-hooks-create-lambda-function-resource-example-function"></a>

The following is a simple function that fails any resource update to DynamoDB, which tries to set the `ReadCapacity` of `ProvisionedThroughput` to something larger than 10. If the Hook succeeds, the message, "ReadCapacity is correctly configured," will display to the caller. If the request fails validation, the Hook will fail with the status, "ReadCapacity cannot be more than 10."

------
#### [ Node.js ]

```
export const handler = async (event, context) => {
    var targetModel = event?.requestData?.targetModel;
    var targetName = event?.requestData?.targetName;
    var response = {
        "hookStatus": "SUCCESS",
        "message": "ReadCapacity is correctly configured.",
        "clientRequestToken": event.clientRequestToken
    };

    if (targetName == "AWS::DynamoDB::Table") {
        var readCapacity = targetModel?.resourceProperties?.ProvisionedThroughput?.ReadCapacityUnits;
        if (readCapacity > 10) {
            response.hookStatus = "FAILED";
            response.errorCode = "NonCompliant";
            response.message = "ReadCapacity must be cannot be more than 10.";
        }
    }
    return response;
};
```

------
#### [ Python ]

```
import json

def lambda_handler(event, context):
    # Using dict.get() for safe access to nested dictionary values
    request_data = event.get('requestData', {})
    target_model = request_data.get('targetModel', {})
    target_name = request_data.get('targetName', '')

    response = {
        "hookStatus": "SUCCESS",
        "message": "ReadCapacity is correctly configured.",
        "clientRequestToken": event.get('clientRequestToken')
    }

    if target_name == "AWS::DynamoDB::Table":
        # Safely navigate nested dictionary
        resource_properties = target_model.get('resourceProperties', {})
        provisioned_throughput = resource_properties.get('ProvisionedThroughput', {})
        read_capacity = provisioned_throughput.get('ReadCapacityUnits')

        if read_capacity and read_capacity > 10:
            response['hookStatus'] = "FAILED"
            response['errorCode'] = "NonCompliant"
            response['message'] = "ReadCapacity must be cannot be more than 10."

    return response
```

------

## Evaluating stack operations with Lambda Hooks
<a name="lambda-hooks-create-lambda-function-stack"></a>

Any time you create, update, or delete a stack with a new template, you can configure your CloudFormation Lambda Hook to start by evaluating the new template and potentially block the stack operation from proceeding. You can configure your CloudFormation Lambda Hook to target `STACK` operations in the Hook `TargetOperations` configuration.

**Topics**
+ [Lambda Hook stack input syntax](#lambda-hooks-create-lambda-function-stack-input)
+ [Example Lambda Hook stack change input](#lambda-hooks-create-lambda-function-stack-example)
+ [Example Lambda function for stack operations](#lambda-hooks-create-lambda-function-stack-example-function)

### Lambda Hook stack input syntax
<a name="lambda-hooks-create-lambda-function-stack-input"></a>

When your Lambda is invoked for a stack operation, you'll receive a JSON request containing the Hook invocation context, `actionInvocationPoint`, and request context. Due to the size of CloudFormation templates, and the limited input size accepted by Lambda functions, the actual templates are stored in an Amazon S3 object. The input of the `requestData` includes an Amazon S3 resigned URL to another object, which contains the current and previous template version.

The following is an example shape of the JSON input:

```
{
    "clientRequesttoken": String,
    "awsAccountId": String,
    "stackID": String,
    "changeSetId": String,
    "hookTypeName": String,
    "hookTypeVersion": String,
    "hookModel": {
        "LambdaFunction":String
    },
    "actionInvocationPoint": "CREATE_PRE_PROVISION" or "UPDATE_PRE_PROVISION" or "DELETE_PRE_PROVISION"
    "requestData": {
        "targetName": "STACK",
        "targetType": "STACK",
        "targetLogicalId": String,
        "payload": String (S3 Presigned URL)
    },
    "requestContext": {
        "invocation": Integer,
        "callbackContext": String
    }
}
```

`clientRequesttoken`  <a name="lambda-hook-stack-clientrequesttoken"></a>
The request token that was provided as an input to the Hook request. This is a required field.

`awsAccountId`  <a name="lambda-hook-stack-awsaccountid"></a>
The ID of the AWS account containing the stack being evaluated.

`stackID`  <a name="lambda-hook-stack-stackid"></a>
The stack ID of the CloudFormation stack.

`changeSetId`  <a name="lambda-hook-stack-changesetid"></a>
The ID of the change set that initiated the Hook invocation. This value is empty if the stack change was initiated by Cloud Control API, or the `create-stack`, `update-stack`, or `delete-stack` operations.

`hookTypeName`  <a name="lambda-hook-stack-hooktypename"></a>
The name of the Hook that's running.

`hookTypeVersion`  <a name="lambda-hook-stack-hooktypeversion"></a>
The version of the Hook that's running.

`hookModel`  <a name="lambda-hook-stack-hookmodel"></a>
`LambdaFunction`  <a name="lambda-hook-stack-hookmodel-lambdafunction"></a>
The current Lambda ARN invoked by the Hook.

`actionInvocationPoint`  <a name="lambda-hook-stack-actioninvocationpoint"></a>
The exact point in the provisioning logic where the Hook runs.
*Valid values*: (`CREATE_PRE_PROVISION` \| `UPDATE_PRE_PROVISION` \| `DELETE_PRE_PROVISION`)

`requestData`  <a name="lambda-hook-stack-requestdata"></a>
`targetName`  <a name="lambda-hook-stack-requestdata-targetname"></a>
This value will be `STACK`.
`targetType`  <a name="lambda-hook-stack-requestdata-targettype"></a>
This value will be `STACK`.
`targetLogicalId`  <a name="lambda-hook-stack-requestdata-targetlogicalid"></a>
The stack name.
`payload`  <a name="lambda-hook-stack-requestdata-payload"></a>
The Amazon S3 presigned URL containing a JSON object with the current and previous template definitions.

`requestContext`  <a name="lambda-hook-stack-requestcontext"></a>
If the Hook is being reinvoked, this object will be set.
`invocation`  <a name="lambda-hook-stack-requestcontext-invocation"></a>
The current attempt at executing the Hook.
`callbackContext`  <a name="lambda-hook-stack-requestcontext-callbackcontext"></a>
If the Hook was set to `IN_PROGRESS` and `callbackContext` was returned, it will be here upon reinvocation.

The `payload` property in the request data is a URL that your code needs to fetch. Once it has received the URL, you get an object with the following schema:

```
{
    "template": String,
    "previousTemplate": String
}
```

`template`  <a name="lambda-hook-stack-payload-template"></a>
The full CloudFormation template that was provided to `create-stack` or `update-stack`. It can be a JSON or YAML string depending on what was provided to CloudFormation.
In `delete-stack` operations, this value will be empty.

`previousTemplate`  <a name="lambda-hook-stack-payload-previoustemplate"></a>
The previous CloudFormation template. It can be a JSON or YAML string depending on what was provided to CloudFormation.
In `delete-stack` operations, this value will be empty.

### Example Lambda Hook stack change input
<a name="lambda-hooks-create-lambda-function-stack-example"></a>

The following is an example stack change input. The Hook is evaluating a change which updates the `ObjectLockEnabled` to true, and adds an Amazon SQS queue:

```
{
    "clientRequestToken": "f8da6d11-b23f-48f4-814c-0fb6a667f50e",
    "awsAccountId": "123456789012",
    "stackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
    "changeSetId": null,
    "hookTypeName": "my::lambda::stackhook",
    "hookTypeVersion": "00000008",
    "hookModel": {
        "LambdaFunction": "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
    },
    "actionInvocationPoint": "UPDATE_PRE_PROVISION",
    "requestData": {
        "targetName": "STACK",
        "targetType": "STACK",
        "targetLogicalId": "my-cloudformation-stack",
        "payload": "https://s3......"
    },
    "requestContext": {
        "invocation": 1,
        "callbackContext": null
    }
}
```

This is an example `payload` of the `requestData`:

```
{
    "template": "{\"Resources\":{\"S3Bucket\":{\"Type\":\"AWS::S3::Bucket\",\"Properties\":{\"ObjectLockEnabled\":true}},\"SQSQueue\":{\"Type\":\"AWS::SQS::Queue\",\"Properties\":{\"QueueName\":\"NewQueue\"}}}}",
    "previousTemplate": "{\"Resources\":{\"S3Bucket\":{\"Type\":\"AWS::S3::Bucket\",\"Properties\":{\"ObjectLockEnabled\":false}}}}"
}
```

### Example Lambda function for stack operations
<a name="lambda-hooks-create-lambda-function-stack-example-function"></a>

The following example is a simple function that downloads the stack operation payload, parses the template JSON, and returns `SUCCESS`.

------
#### [ Node.js ]

```
export const handler = async (event, context) => {
    var targetType = event?.requestData?.targetType;
    var payloadUrl = event?.requestData?.payload;

    var response = {
        "hookStatus": "SUCCESS",
        "message": "Stack update is compliant",
        "clientRequestToken": event.clientRequestToken
    };
    try {
        const templateHookPayloadRequest = await fetch(payloadUrl);
        const templateHookPayload = await templateHookPayloadRequest.json()
        if (templateHookPayload.template)  {
            // Do something with the template templateHookPayload.template
            // JSON or YAML
        }
        if (templateHookPayload.previousTemplate) {
            // Do something with the template templateHookPayload.previousTemplate
            // JSON or YAML
        }
    } catch (error) {
        console.log(error);
        response.hookStatus = "FAILED";
        response.message = "Failed to evaluate stack operation.";
        response.errorCode = "InternalFailure";
    }
    return response;
};
```

------
#### [ Python ]

To use Python, you'll need to import the `requests` library. To do this, you'll need to include the library in your deployment package when creating your Lambda function. For more information, see [Creating a .zip deployment package with dependencies](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-dependencies) in the *AWS Lambda Developer Guide*.

```
import json
import requests

def lamnbda_handler(event, context):
    # Safely access nested dictionary values
    request_data = event.get('requestData', {})
    target_type = request_data.get('targetType')
    payload_url = request_data.get('payload')

    response = {
        "hookStatus": "SUCCESS",
        "message": "Stack update is compliant",
        "clientRequestToken": event.get('clientRequestToken')
    }

    try:
        # Fetch the payload
        template_hook_payload_request = requests.get(payload_url)
        template_hook_payload_request.raise_for_status()  # Raise an exception for bad responses
        template_hook_payload = template_hook_payload_request.json()

        if 'template' in template_hook_payload:
            # Do something with the template template_hook_payload['template']
            # JSON or YAML
            pass

        if 'previousTemplate' in template_hook_payload:
            # Do something with the template template_hook_payload['previousTemplate']
            # JSON or YAML
            pass

    except Exception as error:
        print(error)
        response['hookStatus'] = "FAILED"
        response['message'] = "Failed to evaluate stack operation."
        response['errorCode'] = "InternalFailure"

    return response
```

------

## Evaluating change set operations with Lambda Hooks
<a name="lambda-hooks-create-lambda-function-change-set"></a>

Any time you create a change set, you can configure your CloudFormation Lambda Hook to first evaluate the new change set and potentially block its execution. You can configure your CloudFormation Lambda Hook to target `CHANGE_SET` operations in the Hook `TargetOperations` configuration.

**Topics**
+ [Lambda Hook change set input syntax](#lambda-hooks-create-lambda-function-change-set-input)
+ [Example Lambda Hook change set change input](#lambda-hooks-create-lambda-function-change-set-example)
+ [Example Lambda function for change set operations](#lambda-hooks-create-lambda-function-change-set-example-function)

### Lambda Hook change set input syntax
<a name="lambda-hooks-create-lambda-function-change-set-input"></a>

The input for change set operations is similar to stack operations, but the payload of the `requestData` also includes a list of resource changes introduced by the change set.

The following is an example shape of the JSON input:

```
{
    "clientRequesttoken": String,
    "awsAccountId": String,
    "stackID": String,
    "changeSetId": String,
    "hookTypeName": String,
    "hookTypeVersion": String,
    "hookModel": {
        "LambdaFunction":String
    },
    "requestData": {
        "targetName": "CHANGE_SET",
        "targetType": "CHANGE_SET",
        "targetLogicalId": String,
        "payload": String (S3 Presigned URL)
    },
    "requestContext": {
        "invocation": Integer,
        "callbackContext": String
    }
}
```

`clientRequesttoken`  <a name="lambda-hook-change-set-clientrequesttoken"></a>
The request token that was provided as an input to the Hook request. This is a required field.

`awsAccountId`  <a name="lambda-hook-change-set-awsaccountid"></a>
The ID of the AWS account containing the stack being evaluated.

`stackID`  <a name="lambda-hook-change-set-stackid"></a>
The stack ID of the CloudFormation stack.

`changeSetId`  <a name="lambda-hook-change-set-changesetid"></a>
The ID of the change set that initiated the Hook invocation.

`hookTypeName`  <a name="lambda-hook-change-set-hooktypename"></a>
The name of the Hook that's running.

`hookTypeVersion`  <a name="lambda-hook-change-set-hooktypeversion"></a>
The version of the Hook that's running.

`hookModel`  <a name="lambda-hook-change-set-hookmodel"></a>
`LambdaFunction`  <a name="lambda-hook-change-set-hookmodel-lambdafunction"></a>
The current Lambda ARN invoked by the Hook.

`requestData`  <a name="lambda-hook-change-set-requestdata"></a>
`targetName`  <a name="lambda-hook-change-set-requestdata-targetname"></a>
This value will be `CHANGE_SET`.
`targetType`  <a name="lambda-hook-change-set-requestdata-targettype"></a>
This value will be `CHANGE_SET`.
`targetLogicalId`  <a name="lambda-hook-change-set-requestdata-targetlogicalid"></a>
The change set ARN..
`payload`  <a name="lambda-hook-change-set-requestdata-payload"></a>
The Amazon S3 presigned URL containing a JSON object with the current template, as well as a list of changes introduced by this change set.

`requestContext`  <a name="lambda-hook-change-set-requestcontext"></a>
If the Hook is being reinvoked, this object will be set.
`invocation`  <a name="lambda-hook-change-set-requestcontext-invocation"></a>
The current attempt at executing the Hook.
`callbackContext`  <a name="lambda-hook-change-set-requestcontext-callbackcontext"></a>
If the Hook was set to `IN_PROGRESS` and `callbackContext` was returned, it will be here upon reinvocation.

The `payload` property in the request data is a URL that your code needs to fetch. Once it has received the URL, you get an object with the following schema:

```
{
    "template": String,
    "changedResources": [
        {
            "action": String,
            "beforeContext": JSON String,
            "afterContext": JSON String,
            "lineNumber": Integer,
            "logicalResourceId": String,
            "resourceType": String
        }
    ]
}
```

`template`  <a name="lambda-hook-change-set-payload-template"></a>
The full CloudFormation template that was provided to `create-stack` or `update-stack`. It can be a JSON or YAML string depending on what was provided to CloudFormation.

`changedResources`  <a name="lambda-hook-change-set-payload-changed-resources"></a>
A list of changed resources.
`action`  <a name="lambda-hook-change-set-payload-changed-resources-action"></a>
The type of change applied to the resource.
*Valid values*: (`CREATE` \| `UPDATE` \| `DELETE`)
`beforeContext`  <a name="lambda-hook-change-set-payload-changed-resources-beforecontext"></a>
A JSON string of the resource properties before the change. This value is null when the resource is being created. All boolean and number values in this JSON string are STRINGS.
`afterContext`  <a name="lambda-hook-change-set-payload-changed-resources-aftercontext"></a>
A JSON string of the resources properties if this change set is executed. This value is null when the resource is being deleted. All boolean and number values in this JSON string are STRINGS.
`lineNumber`  <a name="lambda-hook-change-set-payload-changed-resources-linenumber"></a>
The line number in the template that caused this change. If the action is `DELETE` this value will be null.
`logicalResourceId`  <a name="lambda-hook-change-set-payload-changed-resources-logicalresourceid"></a>
The logical resource ID of the resource being changed.
`resourceType`  <a name="lambda-hook-change-set-payload-changed-resources-resourcetype"></a>
The resource type that’s being changed.

### Example Lambda Hook change set change input
<a name="lambda-hooks-create-lambda-function-change-set-example"></a>

The following is an example change set change input. In the following example, you can see the changes introduced by the change set. The first change is deleting a queue called `CoolQueue`. The second change is adding a new queue called `NewCoolQueue`. The last change is an update to the `DynamoDBTable`.

```
{
    "clientRequestToken": "f8da6d11-b23f-48f4-814c-0fb6a667f50e",
    "awsAccountId": "123456789012",
    "stackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
    "changeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000",
    "hookTypeName": "my::lambda::changesethook",
    "hookTypeVersion": "00000008",
    "hookModel": {
        "LambdaFunction": "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
    },
    "actionInvocationPoint": "CREATE_PRE_PROVISION",
    "requestData": {
        "targetName": "CHANGE_SET",
        "targetType": "CHANGE_SET",
        "targetLogicalId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000",
        "payload": "https://s3......"
    },
    "requestContext": {
        "invocation": 1,
        "callbackContext": null
    }
}
```

This is an example `payload` of the `requestData.payload`:

```
{
  template: 'Resources:\n' +
    '  DynamoDBTable:\n' +
    '    Type: AWS::DynamoDB::Table\n' +
    '    Properties:\n' +
    '      AttributeDefinitions:\n' +
    '        - AttributeName: "PK"\n' +
    '          AttributeType: "S"\n' +
    '      BillingMode: "PAY_PER_REQUEST"\n' +
    '      KeySchema:\n' +
    '        - AttributeName: "PK"\n' +
    '          KeyType: "HASH"\n' +
    '      PointInTimeRecoverySpecification:\n' +
    '        PointInTimeRecoveryEnabled: false\n' +
    '  NewSQSQueue:\n' +
    '    Type: AWS::SQS::Queue\n' +
    '    Properties:\n' +
    '      QueueName: "NewCoolQueue"',
  changedResources: [
    {
      logicalResourceId: 'SQSQueue',
      resourceType: 'AWS::SQS::Queue',
      action: 'DELETE',
      lineNumber: null,
      beforeContext: '{"Properties":{"QueueName":"CoolQueue"}}',
      afterContext: null
    },
    {
      logicalResourceId: 'NewSQSQueue',
      resourceType: 'AWS::SQS::Queue',
      action: 'CREATE',
      lineNumber: 14,
      beforeContext: null,
      afterContext: '{"Properties":{"QueueName":"NewCoolQueue"}}'
    },
    {
      logicalResourceId: 'DynamoDBTable',
      resourceType: 'AWS::DynamoDB::Table',
      action: 'UPDATE',
      lineNumber: 2,
      beforeContext: '{"Properties":{"BillingMode":"PAY_PER_REQUEST","AttributeDefinitions":[{"AttributeType":"S","AttributeName":"PK"}],"KeySchema":[{"KeyType":"HASH","AttributeName":"PK"}]}}',
      afterContext: '{"Properties":{"BillingMode":"PAY_PER_REQUEST","PointInTimeRecoverySpecification":{"PointInTimeRecoveryEnabled":"false"},"AttributeDefinitions":[{"AttributeType":"S","AttributeName":"PK"}],"KeySchema":[{"KeyType":"HASH","AttributeName":"PK"}]}}'
    }
  ]
}
```

### Example Lambda function for change set operations
<a name="lambda-hooks-create-lambda-function-change-set-example-function"></a>

The following example is a simple function that downloads the change set operation payload, loops through each change, and then prints out the before and after properties before it returns a `SUCCESS`.

------
#### [ Node.js ]

```
export const handler = async (event, context) => {
    var payloadUrl = event?.requestData?.payload;
    var response = {
        "hookStatus": "SUCCESS",
        "message": "Change set changes are compliant",
        "clientRequestToken": event.clientRequestToken
    };
    try {
        const changeSetHookPayloadRequest = await fetch(payloadUrl);
        const changeSetHookPayload = await changeSetHookPayloadRequest.json();
        const changes = changeSetHookPayload.changedResources || [];
        for(const change of changes) {
            var beforeContext = {};
            var afterContext = {};
            if(change.beforeContext) {
                beforeContext = JSON.parse(change.beforeContext);
            }
            if(change.afterContext) {
                afterContext = JSON.parse(change.afterContext);
            }
            console.log(beforeContext)
            console.log(afterContext)
            // Evaluate Change here
        }
    } catch (error) {
        console.log(error);
        response.hookStatus = "FAILED";
        response.message = "Failed to evaluate change set operation.";
        response.errorCode = "InternalFailure";
    }
    return response;
};
```

------
#### [ Python ]

To use Python, you'll need to import the `requests` library. To do this, you'll need to include the library in your deployment package when creating your Lambda function. For more information, see [Creating a .zip deployment package with dependencies](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-dependencies) in the *AWS Lambda Developer Guide*.

```
import json
import requests

def lambda_handler(event, context):
    payload_url = event.get('requestData', {}).get('payload')
    response = {
        "hookStatus": "SUCCESS",
        "message": "Change set changes are compliant",
        "clientRequestToken": event.get('clientRequestToken')
    }

    try:
        change_set_hook_payload_request = requests.get(payload_url)
        change_set_hook_payload_request.raise_for_status()  # Raises an HTTPError for bad responses
        change_set_hook_payload = change_set_hook_payload_request.json()

        changes = change_set_hook_payload.get('changedResources', [])

        for change in changes:
            before_context = {}
            after_context = {}

            if change.get('beforeContext'):
                before_context = json.loads(change['beforeContext'])

            if change.get('afterContext'):
                after_context = json.loads(change['afterContext'])

            print(before_context)
            print(after_context)
            # Evaluate Change here

    except requests.RequestException as error:
        print(error)
        response['hookStatus'] = "FAILED"
        response['message'] = "Failed to evaluate change set operation."
        response['errorCode'] = "InternalFailure"
    except json.JSONDecodeError as error:
        print(error)
        response['hookStatus'] = "FAILED"
        response['message'] = "Failed to parse JSON payload."
        response['errorCode'] = "InternalFailure"

    return response
```

------
