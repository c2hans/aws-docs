---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListDataflowEndpointGroups.html
---

# ListDataflowEndpointGroups
<a name="API_ListDataflowEndpointGroups"></a>

Returns a list of `DataflowEndpoint` groups.

## Request Syntax
<a name="API_ListDataflowEndpointGroups_RequestSyntax"></a>

```
GET /dataflowEndpointGroup?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataflowEndpointGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDataflowEndpointGroups_RequestSyntax) **   <a name="groundstation-ListDataflowEndpointGroups-request-uri-maxResults"></a>
Maximum number of dataflow endpoint groups returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDataflowEndpointGroups_RequestSyntax) **   <a name="groundstation-ListDataflowEndpointGroups-request-uri-nextToken"></a>
Next token returned in the request of a previous `ListDataflowEndpointGroups` call. Used to get the next page of results.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Request Body
<a name="API_ListDataflowEndpointGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataflowEndpointGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataflowEndpointGroupList": [
      {
         "dataflowEndpointGroupArn": "string",
         "dataflowEndpointGroupId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataflowEndpointGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataflowEndpointGroupList](#API_ListDataflowEndpointGroups_ResponseSyntax) **   <a name="groundstation-ListDataflowEndpointGroups-response-dataflowEndpointGroupList"></a>
A list of dataflow endpoint groups.
Type: Array of [DataflowEndpointListItem](API_DataflowEndpointListItem.md) objects

 ** [nextToken](#API_ListDataflowEndpointGroups_ResponseSyntax) **   <a name="groundstation-ListDataflowEndpointGroups-response-nextToken"></a>
Next token returned in the response of a previous `ListDataflowEndpointGroups` call. Used to get the next page of results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Errors
<a name="API_ListDataflowEndpointGroups_Errors"></a>

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

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_ListDataflowEndpointGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListDataflowEndpointGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListDataflowEndpointGroups)
