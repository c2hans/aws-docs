---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListInstanceProfiles.html
---

# ListInstanceProfiles
<a name="API_ListInstanceProfiles"></a>

Returns information about all the instance profiles in an AWS account.

## Request Syntax
<a name="API_ListInstanceProfiles_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInstanceProfiles_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListInstanceProfiles_RequestSyntax) **   <a name="devicefarm-ListInstanceProfiles-request-maxResults"></a>
An integer that specifies the maximum number of items you want to return in the API response.
Type: Integer
Required: No

 ** [nextToken](#API_ListInstanceProfiles_RequestSyntax) **   <a name="devicefarm-ListInstanceProfiles-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListInstanceProfiles_ResponseSyntax"></a>

```
{
   "instanceProfiles": [
      {
         "arn": "string",
         "description": "string",
         "excludeAppPackagesFromCleanup": [ "string" ],
         "name": "string",
         "packageCleanup": boolean,
         "rebootAfterUse": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInstanceProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceProfiles](#API_ListInstanceProfiles_ResponseSyntax) **   <a name="devicefarm-ListInstanceProfiles-response-instanceProfiles"></a>
An object that contains information about your instance profiles.
Type: Array of [InstanceProfile](API_InstanceProfile.md) objects

 ** [nextToken](#API_ListInstanceProfiles_ResponseSyntax) **   <a name="devicefarm-ListInstanceProfiles-response-nextToken"></a>
An identifier that can be used in the next call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListInstanceProfiles_Errors"></a>

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
<a name="API_ListInstanceProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListInstanceProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListInstanceProfiles)
