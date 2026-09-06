---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CancelMetadataGenerationRun.html
---

# CancelMetadataGenerationRun
<a name="API_CancelMetadataGenerationRun"></a>

Cancels the metadata generation run.

Prerequisites:
+ The run must exist and be in a cancelable status (e.g., SUBMITTED, IN\_PROGRESS).
+ Runs in SUCCEEDED status cannot be cancelled.
+ User must have access to the run and cancel permissions.

## Request Syntax
<a name="API_CancelMetadataGenerationRun_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/metadata-generation-runs/{{identifier}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelMetadataGenerationRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CancelMetadataGenerationRun_RequestSyntax) **   <a name="datazone-CancelMetadataGenerationRun-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_CancelMetadataGenerationRun_RequestSyntax) **   <a name="datazone-CancelMetadataGenerationRun-request-uri-identifier"></a>
The ID of the metadata generation run.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CancelMetadataGenerationRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelMetadataGenerationRun_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelMetadataGenerationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelMetadataGenerationRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_CancelMetadataGenerationRun_Examples"></a>

### Example
<a name="API_CancelMetadataGenerationRun_Example_1"></a>

This example illustrates one usage of CancelMetadataGenerationRun.

#### Sample Request
<a name="API_CancelMetadataGenerationRun_Example_1_Request"></a>

```
aws datazone cancel-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "mgr5g0fy285m1q"
```

### Example
<a name="API_CancelMetadataGenerationRun_Example_2"></a>

Failure case - validation error - succeeded cannot be cancelled:

#### Sample Request
<a name="API_CancelMetadataGenerationRun_Example_2_Request"></a>

```
aws datazone cancel-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "mgr3tlpxo4mg5q"
```

#### Sample Response
<a name="API_CancelMetadataGenerationRun_Example_2_Response"></a>

```
An error occurred (ValidationException) when calling the CancelMetadataGenerationRun operation: The MetadataGenerationRun in SUCCEEDED status cannot be canceled.
```

### Example
<a name="API_CancelMetadataGenerationRun_Example_3"></a>

Failure case - validation error - succeeded cannot be cancelled:

#### Sample Request
<a name="API_CancelMetadataGenerationRun_Example_3_Request"></a>

```
aws datazone cancel-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "mgr_nonexistent"
```

#### Sample Response
<a name="API_CancelMetadataGenerationRun_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the CancelMetadataGenerationRun operation: Requested prediction cannot be found in domain
```

### Example
<a name="API_CancelMetadataGenerationRun_Example_4"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_CancelMetadataGenerationRun_Example_4_Request"></a>

```
aws datazone cancel-metadata-generation-run
```

#### Sample Response
<a name="API_CancelMetadataGenerationRun_Example_4_Response"></a>

```
aws: error: the following arguments are required: —domain-identifier, —identifier
```

## See Also
<a name="API_CancelMetadataGenerationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CancelMetadataGenerationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CancelMetadataGenerationRun)
