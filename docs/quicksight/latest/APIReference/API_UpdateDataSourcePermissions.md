---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSourcePermissions.html
---

# UpdateDataSourcePermissions
<a name="API_UpdateDataSourcePermissions"></a>

Updates the permissions to a data source.

## Request Syntax
<a name="API_UpdateDataSourcePermissions_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/data-sources/{{DataSourceId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokePermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateDataSourcePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDataSourcePermissions_RequestSyntax) **   <a name="QS-UpdateDataSourcePermissions-request-uri-AwsAccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DataSourceId](#API_UpdateDataSourcePermissions_RequestSyntax) **   <a name="QS-UpdateDataSourcePermissions-request-uri-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.
Required: Yes

## Request Body
<a name="API_UpdateDataSourcePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateDataSourcePermissions_RequestSyntax) **   <a name="QS-UpdateDataSourcePermissions-request-GrantPermissions"></a>
A list of resource permissions that you want to grant on the data source.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [RevokePermissions](#API_UpdateDataSourcePermissions_RequestSyntax) **   <a name="QS-UpdateDataSourcePermissions-request-RevokePermissions"></a>
A list of resource permissions that you want to revoke on the data source.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

## Response Syntax
<a name="API_UpdateDataSourcePermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSourceArn": "string",
   "DataSourceId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDataSourcePermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDataSourcePermissions_ResponseSyntax) **   <a name="QS-UpdateDataSourcePermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSourceArn](#API_UpdateDataSourcePermissions_ResponseSyntax) **   <a name="QS-UpdateDataSourcePermissions-response-DataSourceArn"></a>
The Amazon Resource Name (ARN) of the data source.
Type: String

 ** [DataSourceId](#API_UpdateDataSourcePermissions_ResponseSyntax) **   <a name="QS-UpdateDataSourcePermissions-response-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.
Type: String

 ** [RequestId](#API_UpdateDataSourcePermissions_ResponseSyntax) **   <a name="QS-UpdateDataSourcePermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDataSourcePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_UpdateDataSourcePermissions_Examples"></a>

### Example
<a name="API_UpdateDataSourcePermissions_Example_1"></a>

This example illustrates one usage of UpdateDataSourcePermissions.

#### Sample Request
<a name="API_UpdateDataSourcePermissions_Example_1_Request"></a>

```
POST /accounts/{AwsAccountId}/data-sources/{DataSourceId}/permissions HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_UpdateDataSourcePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDataSourcePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDataSourcePermissions)
