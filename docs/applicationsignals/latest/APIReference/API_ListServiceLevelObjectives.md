---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html
---

# ListServiceLevelObjectives
<a name="API_ListServiceLevelObjectives"></a>

Returns a list of SLOs created in this account.

## Request Syntax
<a name="API_ListServiceLevelObjectives_RequestSyntax"></a>

```
POST /slos?IncludeLinkedAccounts={{IncludeLinkedAccounts}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&OperationName={{OperationName}}&SloOwnerAwsAccountId={{SloOwnerAwsAccountId}} HTTP/1.1
Content-type: application/json

{
   "DependencyConfig": {
      "DependencyKeyAttributes": {
         "{{string}}" : "{{string}}"
      },
      "DependencyOperationName": "{{string}}"
   },
   "KeyAttributes": {
      "{{string}}" : "{{string}}"
   },
   "MetricSource": {
      "MetricSourceAttributes": {
         "{{string}}" : "{{string}}"
      },
      "MetricSourceKeyAttributes": {
         "{{string}}" : "{{string}}"
      }
   },
   "MetricSourceTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListServiceLevelObjectives_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IncludeLinkedAccounts](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-uri-IncludeLinkedAccounts"></a>
If you are using this operation in a monitoring account, specify `true` to include SLO from source accounts in the returned data.
When you are monitoring an account, you can use AWS account ID in `KeyAttribute` filter for service source account and `SloOwnerawsaccountID` for SLO source account with `IncludeLinkedAccounts` to filter the returned data to only a single source account.

 ** [MaxResults](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-uri-MaxResults"></a>
The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-uri-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of service level objectives.

 ** [OperationName](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-uri-OperationName"></a>
The name of the operation that this SLO is associated with.
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SloOwnerAwsAccountId](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-uri-SloOwnerAwsAccountId"></a>
SLO's AWS account ID.
Pattern: `[0-9]{12}`

## Request Body
<a name="API_ListServiceLevelObjectives_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DependencyConfig](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-DependencyConfig"></a>
Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.
Type: [DependencyConfig](API_DependencyConfig.md) object
Required: No

 ** [KeyAttributes](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-KeyAttributes"></a>
You can use this optional field to specify which services you want to retrieve SLO information for.
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this is.
+  `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+  `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Environment` specifies the location where this object is hosted, or what it belongs to.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: No

 ** [MetricSource](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-MetricSource"></a>
Identifies the metric source to filter SLOs by.
Type: [MetricSource](API_MetricSource.md) object
Required: No

 ** [MetricSourceTypes](#API_ListServiceLevelObjectives_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-request-MetricSourceTypes"></a>
Use this optional field to only include SLOs with the specified metric source types in the output. Supported types are:
+ Service operation
+ Service dependency
+ Service
+ CloudWatch metric
+ AppMonitor
+ Canary
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `ServiceOperation | CloudWatchMetric | ServiceDependency | AppMonitor | Canary | Service`
Required: No

## Response Syntax
<a name="API_ListServiceLevelObjectives_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SloSummaries": [
      {
         "Arn": "string",
         "CompositeSliConfig": {
            "Components": [
               { ... }
            ],
            "SelectionConfig": {
               "Pattern": "string",
               "Type": "string"
            }
         },
         "CreatedTime": number,
         "DependencyConfig": {
            "DependencyKeyAttributes": {
               "string" : "string"
            },
            "DependencyOperationName": "string"
         },
         "EvaluationType": "string",
         "KeyAttributes": {
            "string" : "string"
         },
         "MetricSource": {
            "MetricSourceAttributes": {
               "string" : "string"
            },
            "MetricSourceKeyAttributes": {
               "string" : "string"
            }
         },
         "MetricSourceType": "string",
         "Name": "string",
         "OperationName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServiceLevelObjectives_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListServiceLevelObjectives_ResponseSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-response-NextToken"></a>
Include this value in your next use of this API to get next set of service level objectives.
Type: String

 ** [SloSummaries](#API_ListServiceLevelObjectives_ResponseSyntax) **   <a name="applicationsignals-ListServiceLevelObjectives-response-SloSummaries"></a>
An array of structures, where each structure contains information about one SLO.
Type: Array of [ServiceLevelObjectiveSummary](API_ServiceLevelObjectiveSummary.md) objects

## Errors
<a name="API_ListServiceLevelObjectives_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceLevelObjectives_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListServiceLevelObjectives)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListServiceLevelObjectives)
