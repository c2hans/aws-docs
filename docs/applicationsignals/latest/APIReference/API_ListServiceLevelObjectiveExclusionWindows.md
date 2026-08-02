---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectiveExclusionWindows.html
---

# ListServiceLevelObjectiveExclusionWindows
<a name="API_ListServiceLevelObjectiveExclusionWindows"></a>

Retrieves all exclusion windows configured for a specific SLO.

## Request Syntax
<a name="API_ListServiceLevelObjectiveExclusionWindows_RequestSyntax"></a>

```
GET /slo/{{Id}}/exclusion-windows?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServiceLevelObjectiveExclusionWindows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListServiceLevelObjectiveExclusionWindows_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectiveExclusionWindows-request-uri-Id"></a>
The ID of the SLO to list exclusion windows for.
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]$|^arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** [MaxResults](#API_ListServiceLevelObjectiveExclusionWindows_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectiveExclusionWindows-request-uri-MaxResults"></a>
The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListServiceLevelObjectiveExclusionWindows_RequestSyntax) **   <a name="applicationsignals-ListServiceLevelObjectiveExclusionWindows-request-uri-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of service level objectives.

## Request Body
<a name="API_ListServiceLevelObjectiveExclusionWindows_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServiceLevelObjectiveExclusionWindows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExclusionWindows": [
      {
         "Reason": "string",
         "RecurrenceRule": {
            "Expression": "string"
         },
         "StartTime": number,
         "Window": {
            "Duration": number,
            "DurationUnit": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListServiceLevelObjectiveExclusionWindows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExclusionWindows](#API_ListServiceLevelObjectiveExclusionWindows_ResponseSyntax) **   <a name="applicationsignals-ListServiceLevelObjectiveExclusionWindows-response-ExclusionWindows"></a>
A list of exclusion windows configured for the SLO.
Type: Array of [ExclusionWindow](API_ExclusionWindow.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [NextToken](#API_ListServiceLevelObjectiveExclusionWindows_ResponseSyntax) **   <a name="applicationsignals-ListServiceLevelObjectiveExclusionWindows-response-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of service level objectives.
Type: String

## Errors
<a name="API_ListServiceLevelObjectiveExclusionWindows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceLevelObjectiveExclusionWindows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListServiceLevelObjectiveExclusionWindows)
