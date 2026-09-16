---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListActivityTypes.html
---

# ListActivityTypes
<a name="API_ListActivityTypes"></a>

Returns information about all activities registered in the specified domain that match the specified name and registration status. The result includes information like creation date, current status of the activity, etc. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the `nextPageToken` returned by the initial call.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_ListActivityTypes_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "maximumPageSize": {{number}},
   "name": "{{string}}",
   "nextPageToken": "{{string}}",
   "registrationStatus": "{{string}}",
   "reverseOrder": {{boolean}}
}
```

## Request Parameters
<a name="API_ListActivityTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_ListActivityTypes_RequestSyntax) **   <a name="SWF-ListActivityTypes-request-domain"></a>
The name of the domain in which the activity types have been registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [maximumPageSize](#API_ListActivityTypes_RequestSyntax) **   <a name="SWF-ListActivityTypes-request-maximumPageSize"></a>
The maximum number of results that are returned per call. Use `nextPageToken` to obtain further pages of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [name](#API_ListActivityTypes_RequestSyntax) **   <a name="SWF-ListActivityTypes-request-name"></a>
If specified, only lists the activity types that have this name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [nextPageToken](#API_ListActivityTypes_RequestSyntax) **   <a name="SWF-ListActivityTypes-request-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a `400` error: "`Specified token has exceeded its maximum lifetime`".
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [registrationStatus](#API_ListActivityTypes_RequestSyntax) **   <a name="SWF-ListActivityTypes-request-registrationStatus"></a>
Specifies the registration status of the activity types to list.
Type: String
Valid Values: `REGISTERED | DEPRECATED`
Required: Yes

 ** [reverseOrder](#API_ListActivityTypes_RequestSyntax) **   <a name="SWF-ListActivityTypes-request-reverseOrder"></a>
When set to `true`, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by `name` of the activity types.
Type: Boolean
Required: No

## Response Syntax
<a name="API_ListActivityTypes_ResponseSyntax"></a>

```
{
   "nextPageToken": "string",
   "typeInfos": [
      {
         "activityType": {
            "name": "string",
            "version": "string"
         },
         "creationDate": number,
         "deprecationDate": number,
         "description": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListActivityTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextPageToken](#API_ListActivityTypes_ResponseSyntax) **   <a name="SWF-ListActivityTypes-response-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.

 ** [typeInfos](#API_ListActivityTypes_ResponseSyntax) **   <a name="SWF-ListActivityTypes-response-typeInfos"></a>
List of activity type information.
Type: Array of [ActivityTypeInfo](API_ActivityTypeInfo.md) objects

## Errors
<a name="API_ListActivityTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_ListActivityTypes_Examples"></a>

### ListActivityTypes Example
<a name="API_ListActivityTypes_Example_1"></a>

This example illustrates one usage of ListActivityTypes.

#### Sample Request
<a name="API_ListActivityTypes_Example_1_Request"></a>

```
{"domain": "867530901",
"registrationStatus": "REGISTERED",
"maximumPageSize": 50,
"reverseOrder": false}
```

#### Sample Response
<a name="API_ListActivityTypes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 171
Content-Type: application/json
x-amzn-RequestId: 11b6fbeb-3f25-11e1-9e8f-57bb03e21482

{"typeInfos":
[
{"activityType":
{"name": "activityVerify",
"version": "1.0"},
"creationDate": 1326586446.471,
"description": "Verify the customer credit",
"status": "REGISTERED"}
]
}
```

## See Also
<a name="API_ListActivityTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/ListActivityTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ListActivityTypes)
