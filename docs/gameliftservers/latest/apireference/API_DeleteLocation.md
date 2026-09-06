---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteLocation.html
---

# DeleteLocation
<a name="API_DeleteLocation"></a>

 **This API works with the following fleet types:** Anywhere

Deletes a custom location.

Before deleting a custom location, review any fleets currently using the custom location and deregister the location if it is in use. For more information, see [DeregisterCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeregisterCompute.html).

## Request Syntax
<a name="API_DeleteLocation_RequestSyntax"></a>

```
{
   "LocationName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteLocation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [LocationName](#API_DeleteLocation_RequestSyntax) **   <a name="gameliftservers-DeleteLocation-request-LocationName"></a>
The location name of the custom location to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^custom-[A-Za-z0-9\-]+|^arn:.*:location\/custom-\S+`
Required: Yes

## Response Elements
<a name="API_DeleteLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteLocation)
