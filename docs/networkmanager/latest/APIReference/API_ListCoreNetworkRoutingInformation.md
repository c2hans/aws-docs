---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListCoreNetworkRoutingInformation.html
---

# ListCoreNetworkRoutingInformation
<a name="API_ListCoreNetworkRoutingInformation"></a>

Lists routing information for a core network, including routes and their attributes.

## Request Syntax
<a name="API_ListCoreNetworkRoutingInformation_RequestSyntax"></a>

```
POST /core-networks/{{coreNetworkId}}/core-network-routing-information?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "CommunityMatches": [ "{{string}}" ],
   "EdgeLocation": "{{string}}",
   "ExactAsPathMatches": [ "{{string}}" ],
   "LocalPreferenceMatches": [ "{{string}}" ],
   "MedMatches": [ "{{string}}" ],
   "NextHopFilters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "SegmentName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCoreNetworkRoutingInformation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreNetworkId](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-uri-CoreNetworkId"></a>
The ID of the core network to retrieve routing information for.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [MaxResults](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-uri-MaxResults"></a>
The maximum number of routing information entries to return in a single page.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Request Body
<a name="API_ListCoreNetworkRoutingInformation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CommunityMatches](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-CommunityMatches"></a>
BGP community values to match when filtering routing information.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [EdgeLocation](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-EdgeLocation"></a>
The edge location to filter routing information by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: Yes

 ** [ExactAsPathMatches](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-ExactAsPathMatches"></a>
Exact AS path values to match when filtering routing information.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [LocalPreferenceMatches](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-LocalPreferenceMatches"></a>
Local preference values to match when filtering routing information.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [MedMatches](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-MedMatches"></a>
Multi-Exit Discriminator (MED) values to match when filtering routing information.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [NextHopFilters](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-NextHopFilters"></a>
Filters to apply based on next hop information.
Type: String to array of strings map
Key Length Constraints: Maximum length of 128.
Key Pattern: `^[0-9a-zA-Z\.-]*$`
Length Constraints: Maximum length of 255.
Pattern: `^[0-9a-zA-Z\*\.\\/\?-]*$`
Required: No

 ** [SegmentName](#API_ListCoreNetworkRoutingInformation_RequestSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-request-SegmentName"></a>
The name of the segment to filter routing information by.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_ListCoreNetworkRoutingInformation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetworkRoutingInformation": [
      {
         "AsPath": [ "string" ],
         "Communities": [ "string" ],
         "LocalPreference": "string",
         "Med": "string",
         "NextHop": {
            "CoreNetworkAttachmentId": "string",
            "EdgeLocation": "string",
            "IpAddress": "string",
            "ResourceId": "string",
            "ResourceType": "string",
            "SegmentName": "string"
         },
         "Prefix": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCoreNetworkRoutingInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetworkRoutingInformation](#API_ListCoreNetworkRoutingInformation_ResponseSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-response-CoreNetworkRoutingInformation"></a>
The list of routing information for the core network.
Type: Array of [CoreNetworkRoutingInformation](API_CoreNetworkRoutingInformation.md) objects

 ** [NextToken](#API_ListCoreNetworkRoutingInformation_ResponseSyntax) **   <a name="networkmanager-ListCoreNetworkRoutingInformation-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListCoreNetworkRoutingInformation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_ListCoreNetworkRoutingInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListCoreNetworkRoutingInformation)
