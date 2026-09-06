---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDeviceInstances.html
---

# ListDeviceInstances
<a name="API_ListDeviceInstances"></a>

Returns information about the private device instances associated with one or more AWS accounts.

## Request Syntax
<a name="API_ListDeviceInstances_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeviceInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDeviceInstances_RequestSyntax) **   <a name="devicefarm-ListDeviceInstances-request-maxResults"></a>
An integer that specifies the maximum number of items you want to return in the API response.
Type: Integer
Required: No

 ** [nextToken](#API_ListDeviceInstances_RequestSyntax) **   <a name="devicefarm-ListDeviceInstances-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListDeviceInstances_ResponseSyntax"></a>

```
{
   "deviceInstances": [
      {
         "arn": "string",
         "deviceArn": "string",
         "instanceProfile": {
            "arn": "string",
            "description": "string",
            "excludeAppPackagesFromCleanup": [ "string" ],
            "name": "string",
            "packageCleanup": boolean,
            "rebootAfterUse": boolean
         },
         "labels": [ "string" ],
         "status": "string",
         "udid": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeviceInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deviceInstances](#API_ListDeviceInstances_ResponseSyntax) **   <a name="devicefarm-ListDeviceInstances-response-deviceInstances"></a>
An object that contains information about your device instances.
Type: Array of [DeviceInstance](API_DeviceInstance.md) objects

 ** [nextToken](#API_ListDeviceInstances_ResponseSyntax) **   <a name="devicefarm-ListDeviceInstances-response-nextToken"></a>
An identifier that can be used in the next call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListDeviceInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListDeviceInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListDeviceInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListDeviceInstances)
