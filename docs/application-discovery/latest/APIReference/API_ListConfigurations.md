---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ListConfigurations.html
---

# ListConfigurations
<a name="API_ListConfigurations"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Retrieves a list of configuration items as specified by the value passed to the required parameter `configurationType`. Optional filtering may be applied to refine search results.

## Request Syntax
<a name="API_ListConfigurations_RequestSyntax"></a>

```
{
   "configurationType": "{{string}}",
   "filters": [
      {
         "condition": "{{string}}",
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "orderBy": [
      {
         "fieldName": "{{string}}",
         "sortOrder": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ListConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [configurationType](#API_ListConfigurations_RequestSyntax) **   <a name="DiscServ-ListConfigurations-request-configurationType"></a>
A valid configuration identified by Application Discovery Service.
Type: String
Valid Values: `SERVER | PROCESS | CONNECTION | APPLICATION`
Required: Yes

 ** [filters](#API_ListConfigurations_RequestSyntax) **   <a name="DiscServ-ListConfigurations-request-filters"></a>
You can filter the request using various logical operators and a *key*-*value* format. For example:
 `{"key": "serverType", "value": "webServer"}`
For a complete list of filter options and guidance about using them with this action, see [Using the ListConfigurations Action](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations) in the * AWS Application Discovery Service User Guide*.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [maxResults](#API_ListConfigurations_RequestSyntax) **   <a name="DiscServ-ListConfigurations-request-maxResults"></a>
The total number of items to return. The maximum value is 100.
Type: Integer
Required: No

 ** [nextToken](#API_ListConfigurations_RequestSyntax) **   <a name="DiscServ-ListConfigurations-request-nextToken"></a>
Token to retrieve the next set of results. For example, if a previous call to ListConfigurations returned 100 items, but you set `ListConfigurationsRequest$maxResults` to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.
Type: String
Required: No

 ** [orderBy](#API_ListConfigurations_RequestSyntax) **   <a name="DiscServ-ListConfigurations-request-orderBy"></a>
Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see [Using the ListConfigurations Action](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations) in the * AWS Application Discovery Service User Guide*.
Type: Array of [OrderByElement](API_OrderByElement.md) objects
Required: No

## Response Syntax
<a name="API_ListConfigurations_ResponseSyntax"></a>

```
{
   "configurations": [
      {
         "string" : "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurations](#API_ListConfigurations_ResponseSyntax) **   <a name="DiscServ-ListConfigurations-response-configurations"></a>
Returns configuration details, including the configuration ID, attribute names, and attribute values.
Type: Array of string to string maps
Key Length Constraints: Maximum length of 10000.
Key Pattern: `[\s\S]*`
Value Length Constraints: Maximum length of 10000.
Value Pattern: `[\s\S]*`

 ** [nextToken](#API_ListConfigurations_ResponseSyntax) **   <a name="DiscServ-ListConfigurations-response-nextToken"></a>
Token to retrieve the next set of results. For example, if your call to ListConfigurations returned 100 items, but you set `ListConfigurationsRequest$maxResults` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.
Type: String

## Errors
<a name="API_ListConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified configuration ID was not located. Verify the configuration ID and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_ListConfigurations_Examples"></a>

### List configurations based on server type
<a name="API_ListConfigurations_Example_1"></a>

The following example lists server configurations where the server type is an EC2 instance. This is done by passing the value "SERVER" to the required parameter `configurationType`. Then, to limit the results to just EC2 servers, object array values are passed to the parameter `filters` where `condition` is "EQUALS, `name` is "server.type", and `values` is "EC2". A sorting refinement is also used in this example by passing values to the parameter `orderBy` that sorts the results by the server's OS name in reverse alphabetical order.

#### Sample Request
<a name="API_ListConfigurations_Example_1_Request"></a>

```
{
   "configurationType": "SERVER",
   "filters": [
      {
         "condition": "EQUALS",
         "name": "server.type",
         "values": [ "EC2" ]
      }
   ],
   "orderBy": [
      {
         "fieldName": "server.osName",
         "sortOrder": "DESC"
      }
   ]
}
```

#### Sample Response
<a name="API_ListConfigurations_Example_1_Response"></a>

```
{
    "configurations": [
        {
            "server.agentId": "i-0adf772ed9f61445a",
            "server.configurationId": "d-server-062d1f42166d190a4",
            "server.hostName": "WIN-7O92JH2AKNB",
            "server.osName": "WindowsOS - Windows Server 2012 R2 x64",
            "server.osVersion": "6.2.9200",
            "server.source": "Agent",
            "server.timeOfCreation": "2017-10-09 20:42:25.0",
            "server.type": "EC2"
        },
        {
            "server.agentId": "i-0243426187d59c9c3",
            "server.configurationId": "d-server-0fc7f9126ed1c2be7",
            "server.hostName": "ip-10-0-0-22.us-west-2.compute.internal",
            "server.osName": "Linux - Red Hat Enterprise Linux Server release 7.3 (Maipo)",
            "server.osVersion": "3.10.0-514.el7.x86_64",
            "server.source": "Agent",
            "server.timeOfCreation": "2017-04-06 19:58:15.0",
            "server.type": "EC2"
        }
}
```

## See Also
<a name="API_ListConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/ListConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ListConfigurations)
