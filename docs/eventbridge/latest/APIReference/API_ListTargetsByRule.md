---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html
---

# ListTargetsByRule
<a name="API_ListTargetsByRule"></a>

Lists the targets assigned to the specified rule.

The maximum number of results per page for requests is 100.

## Request Syntax
<a name="API_ListTargetsByRule_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "Rule": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTargetsByRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_ListTargetsByRule_RequestSyntax) **   <a name="eventbridge-ListTargetsByRule-request-EventBusName"></a>
The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[/\.\-_A-Za-z0-9]+`
Required: No

 ** [Limit](#API_ListTargetsByRule_RequestSyntax) **   <a name="eventbridge-ListTargetsByRule-request-Limit"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTargetsByRule_RequestSyntax) **   <a name="eventbridge-ListTargetsByRule-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Rule](#API_ListTargetsByRule_RequestSyntax) **   <a name="eventbridge-ListTargetsByRule-request-Rule"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_ListTargetsByRule_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Targets": [
      {
         "AppSyncParameters": {
            "GraphQLOperation": "string"
         },
         "Arn": "string",
         "BatchParameters": {
            "ArrayProperties": {
               "Size": number
            },
            "JobDefinition": "string",
            "JobName": "string",
            "RetryStrategy": {
               "Attempts": number
            }
         },
         "DeadLetterConfig": {
            "Arn": "string"
         },
         "EcsParameters": {
            "CapacityProviderStrategy": [
               {
                  "base": number,
                  "capacityProvider": "string",
                  "weight": number
               }
            ],
            "EnableECSManagedTags": boolean,
            "EnableExecuteCommand": boolean,
            "Group": "string",
            "LaunchType": "string",
            "NetworkConfiguration": {
               "awsvpcConfiguration": {
                  "AssignPublicIp": "string",
                  "SecurityGroups": [ "string" ],
                  "Subnets": [ "string" ]
               }
            },
            "PlacementConstraints": [
               {
                  "expression": "string",
                  "type": "string"
               }
            ],
            "PlacementStrategy": [
               {
                  "field": "string",
                  "type": "string"
               }
            ],
            "PlatformVersion": "string",
            "PropagateTags": "string",
            "ReferenceId": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "TaskCount": number,
            "TaskDefinitionArn": "string"
         },
         "HttpParameters": {
            "HeaderParameters": {
               "string" : "string"
            },
            "PathParameterValues": [ "string" ],
            "QueryStringParameters": {
               "string" : "string"
            }
         },
         "Id": "string",
         "Input": "string",
         "InputPath": "string",
         "InputTransformer": {
            "InputPathsMap": {
               "string" : "string"
            },
            "InputTemplate": "string"
         },
         "KinesisParameters": {
            "PartitionKeyPath": "string"
         },
         "RedshiftDataParameters": {
            "Database": "string",
            "DbUser": "string",
            "SecretManagerArn": "string",
            "Sql": "string",
            "Sqls": [ "string" ],
            "StatementName": "string",
            "WithEvent": boolean
         },
         "RetryPolicy": {
            "MaximumEventAgeInSeconds": number,
            "MaximumRetryAttempts": number
         },
         "RoleArn": "string",
         "RunCommandParameters": {
            "RunCommandTargets": [
               {
                  "Key": "string",
                  "Values": [ "string" ]
               }
            ]
         },
         "SageMakerPipelineParameters": {
            "PipelineParameterList": [
               {
                  "Name": "string",
                  "Value": "string"
               }
            ]
         },
         "SqsParameters": {
            "MessageGroupId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListTargetsByRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTargetsByRule_ResponseSyntax) **   <a name="eventbridge-ListTargetsByRule-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Targets](#API_ListTargetsByRule_ResponseSyntax) **   <a name="eventbridge-ListTargetsByRule-response-Targets"></a>
The targets assigned to the rule.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_ListTargetsByRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ListTargetsByRule_Examples"></a>

### Lists the targets associated with a rule named "test"
<a name="API_ListTargetsByRule_Example_1"></a>

The following is an example of a ListTargetsByRule request and response.

#### Sample Request
<a name="API_ListTargetsByRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.ListTargetsByRule

{
    "Rule": "test"
}
```

#### Sample Response
<a name="API_ListTargetsByRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction"
        }
    ]
}
```

## See Also
<a name="API_ListTargetsByRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListTargetsByRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListTargetsByRule)
