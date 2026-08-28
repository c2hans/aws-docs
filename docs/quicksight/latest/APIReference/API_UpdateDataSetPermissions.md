---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSetPermissions.html
---

# UpdateDataSetPermissions
<a name="API_UpdateDataSetPermissions"></a>

Updates the permissions on a dataset.

The permissions resource is `arn:aws:quicksight:region:aws-account-id:dataset/data-set-id`.

## Request Syntax
<a name="API_UpdateDataSetPermissions_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}}/permissions HTTP/1.1
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
<a name="API_UpdateDataSetPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDataSetPermissions_RequestSyntax) **   <a name="QS-UpdateDataSetPermissions-request-uri-AwsAccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DataSetId](#API_UpdateDataSetPermissions_RequestSyntax) **   <a name="QS-UpdateDataSetPermissions-request-uri-DataSetId"></a>
The ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.
Required: Yes

## Request Body
<a name="API_UpdateDataSetPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateDataSetPermissions_RequestSyntax) **   <a name="QS-UpdateDataSetPermissions-request-GrantPermissions"></a>
The resource permissions that you want to grant to the dataset.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [RevokePermissions](#API_UpdateDataSetPermissions_RequestSyntax) **   <a name="QS-UpdateDataSetPermissions-request-RevokePermissions"></a>
The resource permissions that you want to revoke from the dataset.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

## Response Syntax
<a name="API_UpdateDataSetPermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DataSetArn": "string",
   "DataSetId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDataSetPermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDataSetPermissions_ResponseSyntax) **   <a name="QS-UpdateDataSetPermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DataSetArn](#API_UpdateDataSetPermissions_ResponseSyntax) **   <a name="QS-UpdateDataSetPermissions-response-DataSetArn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String

 ** [DataSetId](#API_UpdateDataSetPermissions_ResponseSyntax) **   <a name="QS-UpdateDataSetPermissions-response-DataSetId"></a>
The ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.
Type: String

 ** [RequestId](#API_UpdateDataSetPermissions_ResponseSyntax) **   <a name="QS-UpdateDataSetPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDataSetPermissions_Errors"></a>

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
<a name="API_UpdateDataSetPermissions_Examples"></a>

### Example
<a name="API_UpdateDataSetPermissions_Example_1"></a>

This example illustrates one usage of UpdateDataSetPermissions.

#### Sample Request
<a name="API_UpdateDataSetPermissions_Example_1_Request"></a>

```
POST /accounts/{AwsAccountId}/data-sets/{DataSetId}/permissions HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_UpdateDataSetPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDataSetPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDataSetPermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
