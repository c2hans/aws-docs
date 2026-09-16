---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListEntitySecurityProfiles.html
---

# ListEntitySecurityProfiles
<a name="API_ListEntitySecurityProfiles"></a>

 Lists all security profiles attached to a Q in Connect AIAgent Entity in an Amazon Connect instance.

## Request Syntax
<a name="API_ListEntitySecurityProfiles_RequestSyntax"></a>

```
POST /entity-security-profiles-summary/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "EntityArn": "{{string}}",
   "EntityType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEntitySecurityProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListEntitySecurityProfiles_RequestSyntax) **   <a name="connect-ListEntitySecurityProfiles-request-uri-InstanceId"></a>
 The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_ListEntitySecurityProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EntityArn](#API_ListEntitySecurityProfiles_RequestSyntax) **   <a name="connect-ListEntitySecurityProfiles-request-EntityArn"></a>
 ARN of a Q in Connect AI Agent.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [EntityType](#API_ListEntitySecurityProfiles_RequestSyntax) **   <a name="connect-ListEntitySecurityProfiles-request-EntityType"></a>
 Only supported type is AI\_AGENT.
Type: String
Valid Values: `USER | AI_AGENT`
Required: Yes

 ** [MaxResults](#API_ListEntitySecurityProfiles_RequestSyntax) **   <a name="connect-ListEntitySecurityProfiles-request-MaxResults"></a>
 The maximum number of results to return per page. The default MaxResult size is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListEntitySecurityProfiles_RequestSyntax) **   <a name="connect-ListEntitySecurityProfiles-request-NextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

## Response Syntax
<a name="API_ListEntitySecurityProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SecurityProfiles": [
      {
         "Id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListEntitySecurityProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListEntitySecurityProfiles_ResponseSyntax) **   <a name="connect-ListEntitySecurityProfiles-response-NextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [SecurityProfiles](#API_ListEntitySecurityProfiles_ResponseSyntax) **   <a name="connect-ListEntitySecurityProfiles-response-SecurityProfiles"></a>
 List of Security Profile Object.
Type: Array of [SecurityProfileItem](API_SecurityProfileItem.md) objects
Array Members: Maximum number of 100 items.

## Errors
<a name="API_ListEntitySecurityProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListEntitySecurityProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListEntitySecurityProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListEntitySecurityProfiles)
