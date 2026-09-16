---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetScheduleGroup.html
---

# GetScheduleGroup
<a name="API_GetScheduleGroup"></a>

Retrieves the specified schedule group.

## Request Syntax
<a name="API_GetScheduleGroup_RequestSyntax"></a>

```
GET /schedule-groups/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetScheduleGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetScheduleGroup_RequestSyntax) **   <a name="scheduler-GetScheduleGroup-request-uri-Name"></a>
The name of the schedule group to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: Yes

## Request Body
<a name="API_GetScheduleGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetScheduleGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationDate": number,
   "LastModificationDate": number,
   "Name": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_GetScheduleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetScheduleGroup_ResponseSyntax) **   <a name="scheduler-GetScheduleGroup-response-Arn"></a>
The Amazon Resource Name (ARN) of the schedule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule-group\/[0-9a-zA-Z-_.]+`

 ** [CreationDate](#API_GetScheduleGroup_ResponseSyntax) **   <a name="scheduler-GetScheduleGroup-response-CreationDate"></a>
The time at which the schedule group was created.
Type: Timestamp

 ** [LastModificationDate](#API_GetScheduleGroup_ResponseSyntax) **   <a name="scheduler-GetScheduleGroup-response-LastModificationDate"></a>
The time at which the schedule group was last modified.
Type: Timestamp

 ** [Name](#API_GetScheduleGroup_ResponseSyntax) **   <a name="scheduler-GetScheduleGroup-response-Name"></a>
The name of the schedule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [State](#API_GetScheduleGroup_ResponseSyntax) **   <a name="scheduler-GetScheduleGroup-response-State"></a>
Specifies the state of the schedule group.
Type: String
Valid Values: `ACTIVE | DELETING`

## Errors
<a name="API_GetScheduleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetScheduleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/GetScheduleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/GetScheduleGroup)
