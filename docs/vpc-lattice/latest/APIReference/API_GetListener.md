---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetListener.html
---

# GetListener
<a name="API_GetListener"></a>

Retrieves information about the specified listener for the specified service.

## Request Syntax
<a name="API_GetListener_RequestSyntax"></a>

```
GET /services/{{serviceIdentifier}}/listeners/{{listenerIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetListener_RequestParameters"></a>

The request uses the following URI parameters.

 ** [listenerIdentifier](#API_GetListener_RequestSyntax) **   <a name="vpclattice-GetListener-request-uri-listenerIdentifier"></a>
The ID or ARN of the listener.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))`
Required: Yes

 ** [serviceIdentifier](#API_GetListener_RequestSyntax) **   <a name="vpclattice-GetListener-request-uri-serviceIdentifier"></a>
The ID or ARN of the service.
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))`
Required: Yes

## Request Body
<a name="API_GetListener_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetListener_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "defaultAction": { ... },
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "port": number,
   "protocol": "string",
   "serviceArn": "string",
   "serviceId": "string"
}
```

## Response Elements
<a name="API_GetListener_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-arn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}`

 ** [createdAt](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-createdAt"></a>
The date and time that the listener was created, in ISO-8601 format.
Type: Timestamp

 ** [defaultAction](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-defaultAction"></a>
The actions for the default listener rule.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [id](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-id"></a>
The ID of the listener.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `listener-[0-9a-z]{17}`

 ** [lastUpdatedAt](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-lastUpdatedAt"></a>
The date and time that the listener was last updated, in ISO-8601 format.
Type: Timestamp

 ** [name](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-name"></a>
The name of the listener.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!listener-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`

 ** [port](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-port"></a>
The listener port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.

 ** [protocol](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-protocol"></a>
The listener protocol.
Type: String
Valid Values: `HTTP | HTTPS | TLS_PASSTHROUGH`

 ** [serviceArn](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-serviceArn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`

 ** [serviceId](#API_GetListener_ResponseSyntax) **   <a name="vpclattice-GetListener-response-serviceId"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`

## Errors
<a name="API_GetListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_GetListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/GetListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/GetListener)
