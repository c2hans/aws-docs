---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteAssetType.html
---

# DeleteAssetType
<a name="API_DeleteAssetType"></a>

Deletes an asset type in Amazon DataZone.

Prerequisites:
+ The asset type must exist in the domain.
+ You must have DeleteAssetType permission.
+ The asset type must not be in use (e.g., assigned to any asset). If used, deletion will fail.
+ You should retrieve the asset type using get-asset-type to confirm its presence before deletion.

## Request Syntax
<a name="API_DeleteAssetType_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/asset-types/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAssetType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteAssetType_RequestSyntax) **   <a name="datazone-DeleteAssetType-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the asset type is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteAssetType_RequestSyntax) **   <a name="datazone-DeleteAssetType-request-uri-identifier"></a>
The identifier of the asset type that is deleted.
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

## Request Body
<a name="API_DeleteAssetType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAssetType_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAssetType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAssetType_Errors"></a>

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
<a name="API_DeleteAssetType_Examples"></a>

### Example
<a name="API_DeleteAssetType_Example_1"></a>

This example illustrates one usage of DeleteAssetType.

#### Sample Request
<a name="API_DeleteAssetType_Example_1_Request"></a>

```
aws datazone delete-asset-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "CustomerDataAssetType"
```

### Example
<a name="API_DeleteAssetType_Example_2"></a>

Failure case - already deleted or non-existent type:

#### Sample Request
<a name="API_DeleteAssetType_Example_2_Request"></a>

```
aws datazone get-asset-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "NonExistentAssetType"
```

#### Sample Response
<a name="API_DeleteAssetType_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetAssetType operation: The given AssetType doesn't exist. Try creating AssetType before accessing it.
```

### Example
<a name="API_DeleteAssetType_Example_3"></a>

Failure case - missing `--identifier`

#### Sample Request
<a name="API_DeleteAssetType_Example_3_Request"></a>

```
aws datazone delete-asset-type \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_DeleteAssetType_Example_3_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

## See Also
<a name="API_DeleteAssetType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteAssetType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteAssetType)
