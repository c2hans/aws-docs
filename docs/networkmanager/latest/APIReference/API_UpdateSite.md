---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateSite.html
---

# UpdateSite
<a name="API_UpdateSite"></a>

Updates the information for an existing site. To remove information for any of the parameters, specify an empty string.

## Request Syntax
<a name="API_UpdateSite_RequestSyntax"></a>

```
PATCH /global-networks/{{globalNetworkId}}/sites/{{siteId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Location": {
      "Address": "{{string}}",
      "Latitude": "{{string}}",
      "Longitude": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateSite_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalNetworkId](#API_UpdateSite_RequestSyntax) **   <a name="networkmanager-UpdateSite-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [siteId](#API_UpdateSite_RequestSyntax) **   <a name="networkmanager-UpdateSite-request-uri-SiteId"></a>
The ID of your site.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_UpdateSite_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateSite_RequestSyntax) **   <a name="networkmanager-UpdateSite-request-Description"></a>
A description of your site.
Constraints: Maximum length of 256 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Location](#API_UpdateSite_RequestSyntax) **   <a name="networkmanager-UpdateSite-request-Location"></a>
The site location:
+  `Address`: The physical address of the site.
+  `Latitude`: The latitude of the site.
+  `Longitude`: The longitude of the site.
Type: [Location](API_Location.md) object
Required: No

## Response Syntax
<a name="API_UpdateSite_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Site": {
      "CreatedAt": number,
      "Description": "string",
      "GlobalNetworkId": "string",
      "Location": {
         "Address": "string",
         "Latitude": "string",
         "Longitude": "string"
      },
      "SiteArn": "string",
      "SiteId": "string",
      "State": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateSite_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Site](#API_UpdateSite_ResponseSyntax) **   <a name="networkmanager-UpdateSite-response-Site"></a>
Information about the site.
Type: [Site](API_Site.md) object

## Errors
<a name="API_UpdateSite_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

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
<a name="API_UpdateSite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateSite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateSite)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
