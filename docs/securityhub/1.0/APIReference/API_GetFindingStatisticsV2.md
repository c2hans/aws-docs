---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingStatisticsV2.html
---

# GetFindingStatisticsV2
<a name="API_GetFindingStatisticsV2"></a>

Returns aggregated statistical data about findings.

You can use the `Scopes` parameter to define the data boundary for the query. Currently, `Scopes` supports `AwsOrganizations`, which lets you aggregate findings from your entire organization or from specific organizational units. Only the delegated administrator account can use `Scopes`.

 `GetFindingStatisticsV2` uses `securityhub:GetAdhocInsightResults` in the `Action` element of an IAM policy statement. You must have permission to perform the `securityhub:GetAdhocInsightResults` action.

## Request Syntax
<a name="API_GetFindingStatisticsV2_RequestSyntax"></a>

```
POST /findingsv2/statistics HTTP/1.1
Content-type: application/json

{
   "GroupByRules": [
      {
         "Filters": {
            "CompositeFilters": [
               {
                  "BooleanFilters": [
                     {
                        "FieldName": "{{string}}",
                        "Filter": {
                           "Value": {{boolean}}
                        }
                     }
                  ],
                  "DateFilters": [
                     {
                        "FieldName": "{{string}}",
                        "Filter": {
                           "DateRange": {
                              "Comparison": "{{string}}",
                              "Unit": "{{string}}",
                              "Value": {{number}}
                           },
                           "End": "{{string}}",
                           "Start": "{{string}}"
                        }
                     }
                  ],
                  "IpFilters": [
                     {
                        "FieldName": "{{string}}",
                        "Filter": {
                           "Cidr": "{{string}}"
                        }
                     }
                  ],
                  "MapFilters": [
                     {
                        "FieldName": "{{string}}",
                        "Filter": {
                           "Comparison": "{{string}}",
                           "Key": "{{string}}",
                           "Value": "{{string}}"
                        }
                     }
                  ],
                  "NestedCompositeFilters": [
                     "CompositeFilter"
                  ],
                  "NumberFilters": [
                     {
                        "FieldName": "{{string}}",
                        "Filter": {
                           "Eq": {{number}},
                           "Gt": {{number}},
                           "Gte": {{number}},
                           "Lt": {{number}},
                           "Lte": {{number}}
                        }
                     }
                  ],
                  "Operator": "{{string}}",
                  "StringFilters": [
                     {
                        "FieldName": "{{string}}",
                        "Filter": {
                           "Comparison": "{{string}}",
                           "Value": "{{string}}"
                        }
                     }
                  ]
               }
            ],
            "CompositeOperator": "{{string}}"
         },
         "GroupByField": "{{string}}"
      }
   ],
   "MaxStatisticResults": {{number}},
   "Scopes": {
      "AwsOrganizations": [
         {
            "OrganizationalUnitId": "{{string}}",
            "OrganizationId": "{{string}}"
         }
      ]
   },
   "SortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFindingStatisticsV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFindingStatisticsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GroupByRules](#API_GetFindingStatisticsV2_RequestSyntax) **   <a name="securityhub-GetFindingStatisticsV2-request-GroupByRules"></a>
Specifies how security findings should be aggregated and organized in the statistical analysis. It can accept up to 5 `groupBy` fields in a single call.
Type: Array of [GroupByRule](API_GroupByRule.md) objects
Required: Yes

 ** [MaxStatisticResults](#API_GetFindingStatisticsV2_RequestSyntax) **   <a name="securityhub-GetFindingStatisticsV2-request-MaxStatisticResults"></a>
The maximum number of results to be returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

 ** [Scopes](#API_GetFindingStatisticsV2_RequestSyntax) **   <a name="securityhub-GetFindingStatisticsV2-request-Scopes"></a>
Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an `AccessDeniedException`.
This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for their own findings.
You can specify up to 10 entries in `Scopes.AwsOrganizations`. If multiple entries are specified, the entries are combined using OR logic.
Type: [FindingScopes](API_FindingScopes.md) object
Required: No

 ** [SortOrder](#API_GetFindingStatisticsV2_RequestSyntax) **   <a name="securityhub-GetFindingStatisticsV2-request-SortOrder"></a>
Orders the aggregation count in descending or ascending order. Descending order is the default.
Type: String
Valid Values: `asc | desc`
Required: No

## Response Syntax
<a name="API_GetFindingStatisticsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GroupByResults": [
      {
         "GroupByField": "string",
         "GroupByValues": [
            {
               "Count": number,
               "FieldValue": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetFindingStatisticsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupByResults](#API_GetFindingStatisticsV2_ResponseSyntax) **   <a name="securityhub-GetFindingStatisticsV2-response-GroupByResults"></a>
Aggregated statistics about security findings based on specified grouping criteria.
Type: Array of [GroupByResult](API_GroupByResult.md) objects

## Errors
<a name="API_GetFindingStatisticsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** OrganizationalUnitNotFoundException **
The request failed because one or more organizational units specified in the request don't exist within the caller's organization.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.
HTTP Status Code: 400

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_GetFindingStatisticsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetFindingStatisticsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetFindingStatisticsV2)
