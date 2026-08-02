---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteAsset.html
---

# DeleteAsset
<a name="API_DeleteAsset"></a>

Deletes an asset in Amazon DataZone.
+ --domain-identifier must refer to a valid and existing domain.
+ --identifier must refer to an existing asset in the specified domain.
+ Asset must not be referenced in any existing asset filters.
+ Asset must not be linked to any draft or published data product.
+ User must have delete permissions for the domain and project.

## Request Syntax
<a name="API_DeleteAsset_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/assets/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteAsset_RequestSyntax) **   <a name="datazone-DeleteAsset-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the asset is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteAsset_RequestSyntax) **   <a name="datazone-DeleteAsset-request-uri-identifier"></a>
The identifier of the asset that is deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_DeleteAsset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAsset_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAsset_Errors"></a>

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
<a name="API_DeleteAsset_Examples"></a>

### Example
<a name="API_DeleteAsset_Example_1"></a>

This example illustrates one usage of DeleteAsset.

#### Sample Request
<a name="API_DeleteAsset_Example_1_Request"></a>

```
aws datazone delete-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4"
```

#### Sample Response
<a name="API_DeleteAsset_Example_1_Response"></a>

```
aws datazone delete-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4"
```

### Example
<a name="API_DeleteAsset_Example_2"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_DeleteAsset_Example_2_Request"></a>

```
aws datazone delete-asset \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "ast7k9mpq2xvn4"
```

#### Sample Response
<a name="API_DeleteAsset_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the DeleteAsset operation:
 The given Asset doesn't exist. Try creating Asset before accessing it.
```

### Example
<a name="API_DeleteAsset_Example_3"></a>

Failure case - a required parameter is missing:

#### Sample Request
<a name="API_DeleteAsset_Example_3_Request"></a>

```
aws datazone delete-asset \
--domain-identifier "dzd_53ielnpxktdilj"
```

```
aws: error: the following arguments are required: —identifier
```

## See Also
<a name="API_DeleteAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteAsset)
