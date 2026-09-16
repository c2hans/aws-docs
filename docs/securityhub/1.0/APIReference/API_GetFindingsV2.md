---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html
---

# GetFindingsV2
<a name="API_GetFindingsV2"></a>

Returns a list of findings that match the specified criteria.

You can use the `Scopes` parameter to define the data boundary for the query. Currently, `Scopes` supports `AwsOrganizations`, which lets you retrieve findings from your entire organization or from specific organizational units. Only the delegated administrator account can use `Scopes`.

You can use the `Filters` parameter to refine results based on finding attributes. You can use `Scopes` and `Filters` independently or together. When both are provided, `Scopes` narrows the data set first, and then `Filters` refines results within that scoped data set.

 `GetFindings` and `GetFindingsV2` both use `securityhub:GetFindings` in the `Action` element of an IAM policy statement. You must have permission to perform the `securityhub:GetFindings` action.

## Request Syntax
<a name="API_GetFindingsV2_RequestSyntax"></a>

```
POST /findingsv2 HTTP/1.1
Content-type: application/json

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
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Scopes": {
      "AwsOrganizations": [
         {
            "OrganizationalUnitId": "{{string}}",
            "OrganizationId": "{{string}}"
         }
      ]
   },
   "SortCriteria": [
      {
         "Field": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetFindingsV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFindingsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetFindingsV2_RequestSyntax) **   <a name="securityhub-GetFindingsV2-request-Filters"></a>
The finding attributes used to define a condition to filter the returned OCSF findings. You can filter up to 10 composite filters. For each filter type inside of a composite filter, you can provide up to 20 filters.
Type: [OcsfFindingFilters](API_OcsfFindingFilters.md) object
Required: No

 ** [MaxResults](#API_GetFindingsV2_RequestSyntax) **   <a name="securityhub-GetFindingsV2-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetFindingsV2_RequestSyntax) **   <a name="securityhub-GetFindingsV2-request-NextToken"></a>
 The token required for pagination. On your first call, set the value of this parameter to `NULL`. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.
Type: String
Required: No

 ** [Scopes](#API_GetFindingsV2_RequestSyntax) **   <a name="securityhub-GetFindingsV2-request-Scopes"></a>
Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an `AccessDeniedException`.
This parameter is optional. If you omit it, the delegated administrator sees findings from all accounts across the entire organization. Other accounts see only their own findings.
You can specify up to 10 entries in `Scopes.AwsOrganizations`. If multiple entries are specified, the entries are combined using OR logic.
Type: [FindingScopes](API_FindingScopes.md) object
Required: No

 ** [SortCriteria](#API_GetFindingsV2_RequestSyntax) **   <a name="securityhub-GetFindingsV2-request-SortCriteria"></a>
The finding attributes used to sort the list of returned findings.
Type: Array of [SortCriterion](API_SortCriterion.md) objects
Required: No

## Response Syntax
<a name="API_GetFindingsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Findings": [ JSON value ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetFindingsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Findings](#API_GetFindingsV2_ResponseSyntax) **   <a name="securityhub-GetFindingsV2-response-Findings"></a>
An array of security findings returned by the operation.
Type: Array of JSON values

 ** [NextToken](#API_GetFindingsV2_ResponseSyntax) **   <a name="securityhub-GetFindingsV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

## Errors
<a name="API_GetFindingsV2_Errors"></a>

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
<a name="API_GetFindingsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetFindingsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetFindingsV2)
