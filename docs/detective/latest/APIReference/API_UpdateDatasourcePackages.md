---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateDatasourcePackages.html
---

# UpdateDatasourcePackages
<a name="API_UpdateDatasourcePackages"></a>

Starts a data source package for the Detective behavior graph.

## Request Syntax
<a name="API_UpdateDatasourcePackages_RequestSyntax"></a>

```
POST /graph/datasources/update HTTP/1.1
Content-type: application/json

{
   "DatasourcePackages": [ "{{string}}" ],
   "GraphArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDatasourcePackages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateDatasourcePackages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DatasourcePackages](#API_UpdateDatasourcePackages_RequestSyntax) **   <a name="detective-UpdateDatasourcePackages-request-DatasourcePackages"></a>
The data source package to start for the behavior graph.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Valid Values: `DETECTIVE_CORE | EKS_AUDIT | ASFF_SECURITYHUB_FINDING`
Required: Yes

 ** [GraphArn](#API_UpdateDatasourcePackages_RequestSyntax) **   <a name="detective-UpdateDatasourcePackages-request-GraphArn"></a>
The ARN of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

## Response Syntax
<a name="API_UpdateDatasourcePackages_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateDatasourcePackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDatasourcePackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
This request cannot be completed for one of the following reasons.
+ This request cannot be completed if it would cause the number of member accounts in the behavior graph to exceed the maximum allowed. A behavior graph cannot have more than 1,200 member accounts.
+ This request cannot be completed if the current volume ingested is above the limit of 10 TB per day. Detective will not allow you to add additional member accounts.
 ** Resources **
The type of resource that has exceeded the service quota.
HTTP Status Code: 402

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDatasourcePackages_Examples"></a>

### Example
<a name="API_UpdateDatasourcePackages_Example_1"></a>

This example illustrates one usage of UpdateDatasourcePackages.

#### Sample Request
<a name="API_UpdateDatasourcePackages_Example_1_Request"></a>

```
POST /graph/datasources/set HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: gzip, deflate, br
Content-Length: 167
Authorization: AUTHPARAMS
X-Amz-Date: 20220511T171741Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
   "GraphArn":"arn:aws:detective:us-east-1:111122223333:graph:1a8ef4ba50e74440b4b3c0d4a32ef48b",
   "DatasourcePackages":[
      "DETECTIVE_CORE",
      "EKS_AUDIT",
      "ASFF_SECURITYHUB_FINDING"
   ]
}
```

### Example
<a name="API_UpdateDatasourcePackages_Example_2"></a>

This example illustrates one usage of UpdateDatasourcePackages.

#### Sample Response
<a name="API_UpdateDatasourcePackages_Example_2_Response"></a>

```
Sample Response
HTTP/1.1 200 OK
Content-Length: 0
Date: Wed, 11 May 2022 17:17:41 GMT
x-amzn-RequestId: ddce670a-02cf-4993-9bb7-72e05c2d08f1
Connection: Keep-alive
```

## See Also
<a name="API_UpdateDatasourcePackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/UpdateDatasourcePackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/UpdateDatasourcePackages)
