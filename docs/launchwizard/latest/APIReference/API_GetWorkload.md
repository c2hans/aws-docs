---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkload.html
---

# GetWorkload
<a name="API_GetWorkload"></a>

Returns information about a workload.

## Request Syntax
<a name="API_GetWorkload_RequestSyntax"></a>

```
POST /getWorkload HTTP/1.1
Content-type: application/json

{
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWorkload_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWorkload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [workloadName](#API_GetWorkload_RequestSyntax) **   <a name="launchwizard-GetWorkload-request-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: Yes

## Response Syntax
<a name="API_GetWorkload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workload": {
      "description": "string",
      "displayName": "string",
      "documentationUrl": "string",
      "iconUrl": "string",
      "status": "string",
      "statusMessage": "string",
      "workloadName": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workload](#API_GetWorkload_ResponseSyntax) **   <a name="launchwizard-GetWorkload-response-workload"></a>
Information about the workload.
Type: [WorkloadData](API_WorkloadData.md) object

## Errors
<a name="API_GetWorkload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified workload or deployment resource can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/GetWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/GetWorkload)
