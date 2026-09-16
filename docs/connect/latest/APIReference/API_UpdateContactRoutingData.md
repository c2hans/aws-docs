---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactRoutingData.html
---

# UpdateContactRoutingData
<a name="API_UpdateContactRoutingData"></a>

Updates routing priority and age on the contact (**QueuePriority** and **QueueTimeAdjustmentInSeconds**). These properties can be used to change a customer's position in the queue. For example, you can move a contact to the back of the queue by setting a lower routing priority relative to other contacts in queue; or you can move a contact to the front of the queue by increasing the routing age which will make the contact look artificially older and therefore higher up in the first-in-first-out routing order. Note that adjusting the routing age of a contact affects only its position in queue, and not its actual queue wait time as reported through metrics. These properties can also be updated by using [the Set routing priority / age flow block](https://docs.aws.amazon.com/connect/latest/adminguide/change-routing-priority.html).

**Note**
Either **QueuePriority** or **QueueTimeAdjustmentInSeconds** should be provided within the request body, but not both.

## Request Syntax
<a name="API_UpdateContactRoutingData_RequestSyntax"></a>

```
POST /contacts/{{InstanceId}}/{{ContactId}}/routing-data HTTP/1.1
Content-type: application/json

{
   "QueuePriority": {{number}},
   "QueueTimeAdjustmentSeconds": {{number}},
   "RoutingCriteria": {
      "Steps": [
         {
            "Expiry": {
               "DurationInSeconds": {{number}}
            },
            "Expression": {
               "AndExpression": [
                  "Expression"
               ],
               "AttributeCondition": {
                  "ComparisonOperator": "{{string}}",
                  "MatchCriteria": {
                     "AgentsCriteria": {
                        "AgentIds": [ "{{string}}" ]
                     }
                  },
                  "Name": "{{string}}",
                  "ProficiencyLevel": {{number}},
                  "Range": {
                     "MaxProficiencyLevel": {{number}},
                     "MinProficiencyLevel": {{number}}
                  },
                  "Value": "{{string}}"
               },
               "NotAttributeCondition": {
                  "ComparisonOperator": "{{string}}",
                  "MatchCriteria": {
                     "AgentsCriteria": {
                        "AgentIds": [ "{{string}}" ]
                     }
                  },
                  "Name": "{{string}}",
                  "ProficiencyLevel": {{number}},
                  "Range": {
                     "MaxProficiencyLevel": {{number}},
                     "MinProficiencyLevel": {{number}}
                  },
                  "Value": "{{string}}"
               },
               "OrExpression": [
                  "Expression"
               ]
            }
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateContactRoutingData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_UpdateContactRoutingData_RequestSyntax) **   <a name="connect-UpdateContactRoutingData-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateContactRoutingData_RequestSyntax) **   <a name="connect-UpdateContactRoutingData-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateContactRoutingData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueuePriority](#API_UpdateContactRoutingData_RequestSyntax) **   <a name="connect-UpdateContactRoutingData-request-QueuePriority"></a>
Priority of the contact in the queue. The default priority for new contacts is 5. You can raise the priority of a contact compared to other contacts in the queue by assigning them a higher priority, such as 1 or 2.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 9223372036854775807.
Required: No

 ** [QueueTimeAdjustmentSeconds](#API_UpdateContactRoutingData_RequestSyntax) **   <a name="connect-UpdateContactRoutingData-request-QueueTimeAdjustmentSeconds"></a>
The number of seconds to add or subtract from the contact's routing age. Contacts are routed to agents on a first-come, first-serve basis. This means that changing their amount of time in queue compared to others also changes their position in queue.
Type: Integer
Required: No

 ** [RoutingCriteria](#API_UpdateContactRoutingData_RequestSyntax) **   <a name="connect-UpdateContactRoutingData-request-RoutingCriteria"></a>
Updates the routing criteria on the contact. These properties can be used to change how a contact is routed within the queue.
Type: [RoutingCriteriaInput](API_RoutingCriteriaInput.md) object
Required: No

## Response Syntax
<a name="API_UpdateContactRoutingData_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateContactRoutingData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateContactRoutingData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidActiveRegionException **
This exception occurs when an API request is made to a non-active region in an Amazon Connect instance configured with Amazon Connect Global Resiliency. For example, if the active region is US West (Oregon) and a request is made to US East (N. Virginia), the exception will be returned.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_UpdateContactRoutingData_Examples"></a>

### Preferred Agent Routing, without Expiry timer
<a name="API_UpdateContactRoutingData_Example_1"></a>

In this example, we are setting a single-step routing criteria on a contact, to specify that this contact can be targeted only to this particular agent. Note that in order to route, the contact must still first be placed into a queue; in order to be offered the contact in their Contact Control Panel, the agent must have that queue in their routing profile and be in an available state for routing.

Note that in this specific example, there is no expiration timer set for this step. This means that so long as this routing criteria is set on the contact, this contact will not be offered to any other agent. In most scenarios, we would recommend to set an Expiry timer, so that if the agent is not available within some amount of time, you can fallback the contact to any agent in queue, or any agent matching some other condition. See Example 3 for an example showing the Expiry timer.

```
{
    "InstanceId": "5d463351-d515-4241-b8f3-bf78da37770d",
    "ContactId": "44c84896-243d-43bc-ad8c-76fc8baadced",
    "QueueTimeAdjustmentSeconds": 60,
    "RoutingCriteria": {
        "Steps": [{
            "Expression": {
                "AttributeCondition": {
                    "ComparisonOperator": "Match",
                    "MatchCriteria": {
                        "AgentsCriteria": {
                            "AgentIds": ["39bc9666-4d3c-4558-b2ad-9bab4bd48568"]
                        }
                    }
                }
            }
        }
        ]
    }
}
```

### Route only to agents with a specific predefined attribute, without Expiry timer
<a name="API_UpdateContactRoutingData_Example_2"></a>

In this example, we are setting a single-step routing criteria on a contact, to specify that this contact can only be targeted to agents in this queue who have >= 1/5 proficiency level in `Technology:Cloudwatch`.

Note that in this specific example, there is no expiration timer set for this step. This means that so long as this routing criteria is set on the contact, this contact will not be offered to any agent in queue unless they have >= 1/5 proficiency level in `Technology:Cloudwatch`.

Additionally, in this specific example, QueueTimeAdjustmentSeconds was set to 60 for this contact, meaning that this contact will look 60 seconds older than its true age to the routing engine, which may put it closer to the head of the queue relative to other contacts.

```
{
    "InstanceId": "5d463351-d515-4241-b8f3-bf78da37770d",
    "ContactId": "90422764-7f29-4359-943d-d84be5e53642",
    "QueueTimeAdjustmentSeconds": 60,
    "RoutingCriteria": {
        "Steps": [
            {
                "Expression": {
                    "AndExpression": [
                        {
                            "AttributeCondition": {
                                "Name": "Technology",
                                "Value": "Cloudwatch",
                                "ProficiencyLevel": 1,
                                "ComparisonOperator": "NumberGreaterOrEqualTo"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

### Route using an OrExpression, with Expiry timer
<a name="API_UpdateContactRoutingData_Example_3"></a>

In this example, we are setting a single-step routing criteria on a contact with an expiry timer and an OR condition. During this step, the contact can target only agents in queue who either have( >= 1/5 proficiency level in `Technology:Cloudwatch`), OR have both (>= 3/5 proficiency level in `Technology:S3` AND >= 1/5 proficiency level in `Technology:DynamoDB`).

Since in this example there is an Expiry set with a DurationInSeconds of 60, if no agents matching the expressions become available to take the contact within 60 seconds, then the step will expire off, and the contact could be offered to any longest available agent in queue.

Additionally, in this specific example, QueueTimeAdjustmentSeconds was set to 60 for this contact, meaning that this contact will look 60 seconds older than its true age to the routing engine, which may put it closer to the head of the queue relative to other contacts.

```
{
    "InstanceId": "5d463351-d515-4241-b8f3-bf78da37770d",
    "ContactId": "90422764-7f29-4359-943d-d84be5e53642",
    "QueueTimeAdjustmentSeconds": 60,
    "RoutingCriteria": {
        "Steps": [
            {   "Expiry" : {
                "DurationInSeconds": 60
            },
                "Expression": {
                    "OrExpression": [
                        {
                            "AndExpression": [
                                {
                                    "AttributeCondition": {
                                        "Name": "Technology",
                                        "Value": "Cloudwatch",
                                        "ProficiencyLevel": 1,
                                        "ComparisonOperator": "NumberGreaterOrEqualTo"
                                    }
                                }
                            ]
                        },
                        {
                            "AndExpression": [
                                {
                                    "AttributeCondition": {
                                        "Name": "Technology",
                                        "Value": "S3",
                                        "ProficiencyLevel": 3,
                                        "ComparisonOperator": "NumberGreaterOrEqualTo"
                                    }
                                },
                                {
                                    "AttributeCondition": {
                                        "Name": "Technology",
                                        "Value": "DynamoDB",
                                        "ProficiencyLevel": 1,
                                        "ComparisonOperator": "NumberGreaterOrEqualTo"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```

### Two-step routing criteria
<a name="API_UpdateContactRoutingData_Example_4"></a>

In this example, we are setting a two-step routing criteria. Step 1 restricts this contact so that only the agent matching the specified user ID can be offered the contact, with an expiry of 30 seconds. Note that this agent must be in Available status with the queue the contact is in their Routing Profile in order to be offered the contact. If this agent does not accept the contact within 30 seconds, then the contact will instead be offered to an agent within the queue with at least 5/5 proficiency level in language English.

```
{
    "InstanceId": "5d463351-d515-4241-b8f3-bf78da37770d",
    "ContactId": "90422764-7f29-4359-943d-d84be5e53642",
    "RoutingCriteria": {
        "Steps": [
            {
                "Expression": {
                    "AttributeCondition": {
                        "ComparisonOperator": "Match",
                        "MatchCriteria": {
                            "AgentsCriteria": {
                                "AgentIds": ["39bc9666-4d3c-4558-b2ad-9bab4bd48568"]
                            }
                        }
                    }
                },
                "Expiry": {
                    "DurationInSeconds": 30
                }
            },
            {
                "Expression": {
                    "AttributeCondition": {
                        "Name": "Language",
                        "Value": "English",
                        "ProficiencyLevel": 5,
                        "ComparisonOperator": "NumberGreaterOrEqualTo"
                    }
                }
            }
        ]
    }
}
```

## See Also
<a name="API_UpdateContactRoutingData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateContactRoutingData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateContactRoutingData)
