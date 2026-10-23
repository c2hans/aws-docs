---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCollectorDataAccessAuthorization.html
---

# GetCollectorDataAccessAuthorization
<a name="API_GetCollectorDataAccessAuthorization"></a>

Authorizes an Environment's access to a Collector's data. Continuum calls this operation with the Environment's Collector data-access role before it reads the Collector's inventory, so grant continuum:GetCollectorDataAccessAuthorization to that role and, for a Collector in another account, in the Collector's resource policy. The operation evaluates the action against the exact Collector ARN and the Collector's current resource policy using IAM and the caller's authenticated request context, with environmentArn as the continuum:EnvironmentArn condition key. A successful request returns HTTP 200 with no response members. If access is not granted, the operation returns AccessDeniedException without disclosing Collector existence, ownership, or the policy layer that denied access. The service does not reinterpret the policy using only an account ID.

## Request Syntax
<a name="API_GetCollectorDataAccessAuthorization_RequestSyntax"></a>

```
GET /collectors/{{collectorId}}/data-access-authorization?accountId={{accountId}}&environmentArn={{environmentArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollectorDataAccessAuthorization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_GetCollectorDataAccessAuthorization_RequestSyntax) **   <a name="continuum-GetCollectorDataAccessAuthorization-request-uri-accountId"></a>
The identifier of the account.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** [collectorId](#API_GetCollectorDataAccessAuthorization_RequestSyntax) **   <a name="continuum-GetCollectorDataAccessAuthorization-request-uri-collectorId"></a>
The identifier of the collector.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [environmentArn](#API_GetCollectorDataAccessAuthorization_RequestSyntax) **   <a name="continuum-GetCollectorDataAccessAuthorization-request-uri-environmentArn"></a>
The Amazon Resource Name (ARN) of the environment.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+`

## Request Body
<a name="API_GetCollectorDataAccessAuthorization_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollectorDataAccessAuthorization_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_GetCollectorDataAccessAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_GetCollectorDataAccessAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetCollectorDataAccessAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetCollectorDataAccessAuthorization)
