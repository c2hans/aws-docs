---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridProjects.html
---

# ListTestGridProjects
<a name="API_ListTestGridProjects"></a>

Gets a list of all Selenium testing projects in your account.

## Request Syntax
<a name="API_ListTestGridProjects_RequestSyntax"></a>

```
{
   "maxResult": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTestGridProjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResult](#API_ListTestGridProjects_RequestSyntax) **   <a name="devicefarm-ListTestGridProjects-request-maxResult"></a>
Return no more than this number of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListTestGridProjects_RequestSyntax) **   <a name="devicefarm-ListTestGridProjects-request-nextToken"></a>
From a response, used to continue a paginated listing.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListTestGridProjects_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "testGridProjects": [
      {
         "arn": "string",
         "created": number,
         "description": "string",
         "name": "string",
         "vpcConfig": {
            "securityGroupIds": [ "string" ],
            "subnetIds": [ "string" ],
            "vpcId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListTestGridProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTestGridProjects_ResponseSyntax) **   <a name="devicefarm-ListTestGridProjects-response-nextToken"></a>
Used for pagination. Pass into [ListTestGridProjects](#API_ListTestGridProjects) to get more results in a paginated request.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [testGridProjects](#API_ListTestGridProjects_ResponseSyntax) **   <a name="devicefarm-ListTestGridProjects-response-testGridProjects"></a>
The list of TestGridProjects, based on a [ListTestGridProjectsRequest](API_ListTestGridProjectsRequest.md).
Type: Array of [TestGridProject](API_TestGridProject.md) objects

## Errors
<a name="API_ListTestGridProjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** InternalServiceException **
An internal exception was raised in the service. Contact [aws-devicefarm-support@amazon.com](mailto:aws-devicefarm-support@amazon.com) if you see this error.
HTTP Status Code: 500

## See Also
<a name="API_ListTestGridProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListTestGridProjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListTestGridProjects)
