---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ListServerNeighbors.html
---

# ListServerNeighbors
<a name="API_ListServerNeighbors"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Retrieves a list of servers that are one network hop away from a specified server.

## Request Syntax
<a name="API_ListServerNeighbors_RequestSyntax"></a>

```
{
   "configurationId": "{{string}}",
   "maxResults": {{number}},
   "neighborConfigurationIds": [ "{{string}}" ],
   "nextToken": "{{string}}",
   "portInformationNeeded": {{boolean}}
}
```

## Request Parameters
<a name="API_ListServerNeighbors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [configurationId](#API_ListServerNeighbors_RequestSyntax) **   <a name="DiscServ-ListServerNeighbors-request-configurationId"></a>
Configuration ID of the server for which neighbors are being listed.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

 ** [maxResults](#API_ListServerNeighbors_RequestSyntax) **   <a name="DiscServ-ListServerNeighbors-request-maxResults"></a>
Maximum number of results to return in a single page of output.
Type: Integer
Required: No

 ** [neighborConfigurationIds](#API_ListServerNeighbors_RequestSyntax) **   <a name="DiscServ-ListServerNeighbors-request-neighborConfigurationIds"></a>
List of configuration IDs to test for one-hop-away.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** [nextToken](#API_ListServerNeighbors_RequestSyntax) **   <a name="DiscServ-ListServerNeighbors-request-nextToken"></a>
Token to retrieve the next set of results. For example, if you previously specified 100 IDs for `ListServerNeighborsRequest$neighborConfigurationIds` but set `ListServerNeighborsRequest$maxResults` to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** [portInformationNeeded](#API_ListServerNeighbors_RequestSyntax) **   <a name="DiscServ-ListServerNeighbors-request-portInformationNeeded"></a>
Flag to indicate if port and protocol information is needed as part of the response.
Type: Boolean
Required: No

## Response Syntax
<a name="API_ListServerNeighbors_ResponseSyntax"></a>

```
{
   "knownDependencyCount": number,
   "neighbors": [
      {
         "connectionsCount": number,
         "destinationPort": number,
         "destinationServerId": "string",
         "sourceServerId": "string",
         "transportProtocol": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListServerNeighbors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [knownDependencyCount](#API_ListServerNeighbors_ResponseSyntax) **   <a name="DiscServ-ListServerNeighbors-response-knownDependencyCount"></a>
Count of distinct servers that are one hop away from the given server.
Type: Long

 ** [neighbors](#API_ListServerNeighbors_ResponseSyntax) **   <a name="DiscServ-ListServerNeighbors-response-neighbors"></a>
List of distinct servers that are one hop away from the given server.
Type: Array of [NeighborConnectionDetail](API_NeighborConnectionDetail.md) objects

 ** [nextToken](#API_ListServerNeighbors_ResponseSyntax) **   <a name="DiscServ-ListServerNeighbors-response-nextToken"></a>
Token to retrieve the next set of results. For example, if you specified 100 IDs for `ListServerNeighborsRequest$neighborConfigurationIds` but set `ListServerNeighborsRequest$maxResults` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListServerNeighbors_Errors"></a>

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

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_ListServerNeighbors_Examples"></a>

### List server neighbors
<a name="API_ListServerNeighbors_Example_1"></a>

The following example requests to find out if there are any server neighbors that are one network hop away from the server specified in the required parameter `configurationId`. Port information is also requested by passing "true" to the boolean parameter `portInformationNeeded` (note that boolean parameters must be passed as all lowercase without any quotes). It this particular example, no server neighbors are found that are one network hop away.

#### Sample Request
<a name="API_ListServerNeighbors_Example_1_Request"></a>

```
{
   "configurationId": "d-server-0974b967a76335589",
   "neighborConfigurationIds": [ "d-server-0c269e353e6d1fb4c","d-server-01440c9c5df26ae50" ],
   "portInformationNeeded": true
}
```

#### Sample Response
<a name="API_ListServerNeighbors_Example_1_Response"></a>

```
{
    "neighbors": [],
    "knownDependencyCount": 0
}
```

## See Also
<a name="API_ListServerNeighbors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/ListServerNeighbors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ListServerNeighbors)
