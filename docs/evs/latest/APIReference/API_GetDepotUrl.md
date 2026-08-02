---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_GetDepotUrl.html
---

# GetDepotUrl
<a name="API_GetDepotUrl"></a>

Returns a URL and authentication token for accessing the Amazon EVS Custom Addon depot. Configure the depot URL as a download source in vSphere Lifecycle Manager (vLCM) to sync and install the Amazon EVS Custom Addon.

The depot URL remains active until you rotate the authentication token by calling this action with `rotate` set to `true`.

## Request Syntax
<a name="API_GetDepotUrl_RequestSyntax"></a>

```
{
   "environmentId": "{{string}}",
   "rotate": {{boolean}}
}
```

## Request Parameters
<a name="API_GetDepotUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [environmentId](#API_GetDepotUrl_RequestSyntax) **   <a name="evs-GetDepotUrl-request-environmentId"></a>
The unique ID of the Amazon EVS environment to get the depot URL for.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [rotate](#API_GetDepotUrl_RequestSyntax) **   <a name="evs-GetDepotUrl-request-rotate"></a>
Revokes the current authentication token and returns a new depot URL with a new token. Previously issued depot URLs will stop working within 5 minutes of rotation.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetDepotUrl_ResponseSyntax"></a>

```
{
   "depotUrl": "string",
   "token": "string"
}
```

## Response Elements
<a name="API_GetDepotUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [depotUrl](#API_GetDepotUrl_ResponseSyntax) **   <a name="evs-GetDepotUrl-response-depotUrl"></a>
The URL for accessing the Amazon EVS Custom Addon depot. This URL includes the authentication token as a path component.
Type: String

 ** [token](#API_GetDepotUrl_ResponseSyntax) **   <a name="evs-GetDepotUrl-response-token"></a>
The authentication token for depot access. This token is included in the depot URL and is used to authenticate requests.
Type: String

## Errors
<a name="API_GetDepotUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a `state` of `DELETED`.
 ** message **
Describes the error encountered.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 400

 [ThrottlingException](API_ThrottlingException.md)
The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.
 ** message **
Describes the error encountered.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetDepotUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/GetDepotUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/GetDepotUrl)
