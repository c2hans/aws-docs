---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTopic.html
---

# UpdateTopic
<a name="API_UpdateTopic"></a>

Updates a topic.

## Request Syntax
<a name="API_UpdateTopic_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/topics/{{TopicId}} HTTP/1.1
Content-type: application/json

{
   "CustomInstructions": {
      "CustomInstructionsString": "{{string}}"
   },
   "Topic": {
      "ConfigOptions": {
         "QBusinessInsightsEnabled": {{boolean}}
      },
      "DataSets": [
         {
            "CalculatedFields": [
               {
                  "Aggregation": "{{string}}",
                  "AllowedAggregations": [ "{{string}}" ],
                  "CalculatedFieldDescription": "{{string}}",
                  "CalculatedFieldName": "{{string}}",
                  "CalculatedFieldSynonyms": [ "{{string}}" ],
                  "CellValueSynonyms": [
                     {
                        "CellValue": "{{string}}",
                        "Synonyms": [ "{{string}}" ]
                     }
                  ],
                  "ColumnDataRole": "{{string}}",
                  "ComparativeOrder": {
                     "SpecifedOrder": [ "{{string}}" ],
                     "TreatUndefinedSpecifiedValues": "{{string}}",
                     "UseOrdering": "{{string}}"
                  },
                  "DefaultFormatting": {
                     "DisplayFormat": "{{string}}",
                     "DisplayFormatOptions": {
                        "BlankCellFormat": "{{string}}",
                        "CurrencySymbol": "{{string}}",
                        "DateFormat": "{{string}}",
                        "DecimalSeparator": "{{string}}",
                        "FractionDigits": {{number}},
                        "GroupingSeparator": "{{string}}",
                        "NegativeFormat": {
                           "Prefix": "{{string}}",
                           "Suffix": "{{string}}"
                        },
                        "Prefix": "{{string}}",
                        "Suffix": "{{string}}",
                        "UnitScaler": "{{string}}",
                        "UseBlankCellFormat": {{boolean}},
                        "UseGrouping": {{boolean}}
                     }
                  },
                  "DisableIndexing": {{boolean}},
                  "Expression": "{{string}}",
                  "IsIncludedInTopic": {{boolean}},
                  "NeverAggregateInFilter": {{boolean}},
                  "NonAdditive": {{boolean}},
                  "NotAllowedAggregations": [ "{{string}}" ],
                  "SemanticType": {
                     "FalseyCellValue": "{{string}}",
                     "FalseyCellValueSynonyms": [ "{{string}}" ],
                     "SubTypeName": "{{string}}",
                     "TruthyCellValue": "{{string}}",
                     "TruthyCellValueSynonyms": [ "{{string}}" ],
                     "TypeName": "{{string}}",
                     "TypeParameters": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "TimeGranularity": "{{string}}"
               }
            ],
            "Columns": [
               {
                  "Aggregation": "{{string}}",
                  "AllowedAggregations": [ "{{string}}" ],
                  "CellValueSynonyms": [
                     {
                        "CellValue": "{{string}}",
                        "Synonyms": [ "{{string}}" ]
                     }
                  ],
                  "ColumnDataRole": "{{string}}",
                  "ColumnDescription": "{{string}}",
                  "ColumnFriendlyName": "{{string}}",
                  "ColumnName": "{{string}}",
                  "ColumnSynonyms": [ "{{string}}" ],
                  "ComparativeOrder": {
                     "SpecifedOrder": [ "{{string}}" ],
                     "TreatUndefinedSpecifiedValues": "{{string}}",
                     "UseOrdering": "{{string}}"
                  },
                  "DefaultFormatting": {
                     "DisplayFormat": "{{string}}",
                     "DisplayFormatOptions": {
                        "BlankCellFormat": "{{string}}",
                        "CurrencySymbol": "{{string}}",
                        "DateFormat": "{{string}}",
                        "DecimalSeparator": "{{string}}",
                        "FractionDigits": {{number}},
                        "GroupingSeparator": "{{string}}",
                        "NegativeFormat": {
                           "Prefix": "{{string}}",
                           "Suffix": "{{string}}"
                        },
                        "Prefix": "{{string}}",
                        "Suffix": "{{string}}",
                        "UnitScaler": "{{string}}",
                        "UseBlankCellFormat": {{boolean}},
                        "UseGrouping": {{boolean}}
                     }
                  },
                  "DisableIndexing": {{boolean}},
                  "IsIncludedInTopic": {{boolean}},
                  "NeverAggregateInFilter": {{boolean}},
                  "NonAdditive": {{boolean}},
                  "NotAllowedAggregations": [ "{{string}}" ],
                  "SemanticType": {
                     "FalseyCellValue": "{{string}}",
                     "FalseyCellValueSynonyms": [ "{{string}}" ],
                     "SubTypeName": "{{string}}",
                     "TruthyCellValue": "{{string}}",
                     "TruthyCellValueSynonyms": [ "{{string}}" ],
                     "TypeName": "{{string}}",
                     "TypeParameters": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "TimeGranularity": "{{string}}"
               }
            ],
            "DataAggregation": {
               "DatasetRowDateGranularity": "{{string}}",
               "DefaultDateColumnName": "{{string}}"
            },
            "DatasetArn": "{{string}}",
            "DatasetDescription": "{{string}}",
            "DatasetName": "{{string}}",
            "Filters": [
               {
                  "CategoryFilter": {
                     "CategoryFilterFunction": "{{string}}",
                     "CategoryFilterType": "{{string}}",
                     "Constant": {
                        "CollectiveConstant": {
                           "ValueList": [ "{{string}}" ]
                        },
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "Inverse": {{boolean}},
                     "NullFilter": "{{string}}"
                  },
                  "DateRangeFilter": {
                     "Constant": {
                        "ConstantType": "{{string}}",
                        "RangeConstant": {
                           "Maximum": "{{string}}",
                           "Minimum": "{{string}}"
                        }
                     },
                     "Inclusive": {{boolean}},
                     "NullFilter": "{{string}}"
                  },
                  "FilterClass": "{{string}}",
                  "FilterDescription": "{{string}}",
                  "FilterName": "{{string}}",
                  "FilterSynonyms": [ "{{string}}" ],
                  "FilterType": "{{string}}",
                  "NullFilter": {
                     "Constant": {
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "Inverse": {{boolean}},
                     "NullFilterType": "{{string}}"
                  },
                  "NumericEqualityFilter": {
                     "Aggregation": "{{string}}",
                     "Constant": {
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "Inverse": {{boolean}},
                     "NullFilter": "{{string}}"
                  },
                  "NumericRangeFilter": {
                     "Aggregation": "{{string}}",
                     "Constant": {
                        "ConstantType": "{{string}}",
                        "RangeConstant": {
                           "Maximum": "{{string}}",
                           "Minimum": "{{string}}"
                        }
                     },
                     "Inclusive": {{boolean}},
                     "Inverse": {{boolean}},
                     "NullFilter": "{{string}}"
                  },
                  "OperandFieldName": "{{string}}",
                  "RelativeDateFilter": {
                     "Constant": {
                        "ConstantType": "{{string}}",
                        "SingularConstant": "{{string}}"
                     },
                     "NullFilter": "{{string}}",
                     "RelativeDateFilterFunction": "{{string}}",
                     "TimeGranularity": "{{string}}"
                  }
               }
            ],
            "NamedEntities": [
               {
                  "Definition": [
                     {
                        "FieldName": "{{string}}",
                        "IsHidden": {{boolean}},
                        "Metric": {
                           "Aggregation": "{{string}}",
                           "AggregationFunctionParameters": {
                              "{{string}}" : "{{string}}"
                           }
                        },
                        "PresentationOrder": {{number}},
                        "PropertyName": "{{string}}",
                        "PropertyRole": "{{string}}",
                        "PropertyUsage": "{{string}}",
                        "RankOrder": {{number}}
                     }
                  ],
                  "EntityDescription": "{{string}}",
                  "EntityName": "{{string}}",
                  "EntitySynonyms": [ "{{string}}" ],
                  "PresentationOrder": {{number}},
                  "RankOrder": {{number}},
                  "SemanticEntityType": {
                     "SubTypeName": "{{string}}",
                     "TypeName": "{{string}}",
                     "TypeParameters": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "Sort": [
                     {
                        "Direction": "{{string}}",
                        "FieldName": "{{string}}"
                     }
                  ]
               }
            ]
         }
      ],
      "Description": "{{string}}",
      "Name": "{{string}}",
      "UserExperienceVersion": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateTopic_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateTopic_RequestSyntax) **   <a name="QS-UpdateTopic-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the topic that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [TopicId](#API_UpdateTopic_RequestSyntax) **   <a name="QS-UpdateTopic-request-uri-TopicId"></a>
The ID of the topic that you want to modify. This ID is unique per AWS Region for each AWS account.
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: Yes

## Request Body
<a name="API_UpdateTopic_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Topic](#API_UpdateTopic_RequestSyntax) **   <a name="QS-UpdateTopic-request-Topic"></a>
The definition of the topic that you want to update.
Type: [TopicDetails](API_TopicDetails.md) object
Required: Yes

 ** [CustomInstructions](#API_UpdateTopic_RequestSyntax) **   <a name="QS-UpdateTopic-request-CustomInstructions"></a>
Custom instructions for the topic.
Type: [CustomInstructions](API_CustomInstructions.md) object
Required: No

## Response Syntax
<a name="API_UpdateTopic_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RefreshArn": "string",
   "RequestId": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_UpdateTopic_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateTopic_ResponseSyntax) **   <a name="QS-UpdateTopic-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateTopic_ResponseSyntax) **   <a name="QS-UpdateTopic-response-Arn"></a>
The Amazon Resource Name (ARN) of the topic.
Type: String

 ** [RefreshArn](#API_UpdateTopic_ResponseSyntax) **   <a name="QS-UpdateTopic-response-RefreshArn"></a>
The Amazon Resource Name (ARN) of the topic refresh.
Type: String

 ** [RequestId](#API_UpdateTopic_ResponseSyntax) **   <a name="QS-UpdateTopic-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TopicId](#API_UpdateTopic_ResponseSyntax) **   <a name="QS-UpdateTopic-response-TopicId"></a>
The ID of the topic that you want to modify. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`

## Errors
<a name="API_UpdateTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_UpdateTopic_Examples"></a>

### Example
<a name="API_UpdateTopic_Example_1"></a>

This example illustrates one usage of UpdateTopic.

#### Sample Request
<a name="API_UpdateTopic_Example_1_Request"></a>

```
PUT /accounts/{AwsAccountId}/topics/{TopicId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_UpdateTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateTopic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateTopic)
