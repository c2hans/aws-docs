---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListAntennas.html
---

# ListAntennas
<a name="API_ListAntennas"></a>

Returns a list of antennas at a specified ground station.

## Request Syntax
<a name="API_ListAntennas_RequestSyntax"></a>

```
GET /groundstation/{{groundStationId}}/antenna?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAntennas_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groundStationId](#API_ListAntennas_RequestSyntax) **   <a name="groundstation-ListAntennas-request-uri-groundStationId"></a>
ID of a ground station.
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: Yes

 ** [maxResults](#API_ListAntennas_RequestSyntax) **   <a name="groundstation-ListAntennas-request-uri-maxResults"></a>
Maximum number of antennas returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAntennas_RequestSyntax) **   <a name="groundstation-ListAntennas-request-uri-nextToken"></a>
Next token returned in the request of a previous `ListAntennas` call. Used to get the next page of results.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Request Body
<a name="API_ListAntennas_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAntennas_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "antennaList": [
      {
         "antennaName": "string",
         "groundStationName": "string",
         "region": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAntennas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [antennaList](#API_ListAntennas_ResponseSyntax) **   <a name="groundstation-ListAntennas-response-antennaList"></a>
List of antennas.
Type: Array of [AntennaListItem](API_AntennaListItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListAntennas_ResponseSyntax) **   <a name="groundstation-ListAntennas-response-nextToken"></a>
Next token to be used in a subsequent `ListAntennas` call to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Errors
<a name="API_ListAntennas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

## See Also
<a name="API_ListAntennas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListAntennas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListAntennas)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
