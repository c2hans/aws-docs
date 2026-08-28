---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteContainerGroupDefinition.html
---

# DeleteContainerGroupDefinition
<a name="API_DeleteContainerGroupDefinition"></a>

 **This API works with the following fleet types:** Container

 **Request options:**

Deletes a container group definition.
+ Delete an entire container group definition, including all versions. Specify the container group definition name, or use an ARN value without the version number.
+ Delete a particular version. Specify the container group definition name and a version number, or use an ARN value that includes the version number.
+ Keep the newest versions and delete all older versions. Specify the container group definition name and the number of versions to retain. For example, set `VersionCountToRetain` to 5 to delete all but the five most recent versions.

 **Result**

If successful, Amazon GameLift Servers removes the container group definition versions that you request deletion for. This request will fail for any requested versions if the following is true:
+ If the version is being used in an active fleet
+ If the version is being deployed to a fleet in a deployment that's currently in progress.
+ If the version is designated as a rollback definition in a fleet deployment that's currently in progress.

 **Learn more**
+  [Manage a container group definition](https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html)

## Request Syntax
<a name="API_DeleteContainerGroupDefinition_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "VersionCountToRetain": {{number}},
   "VersionNumber": {{number}}
}
```

## Request Parameters
<a name="API_DeleteContainerGroupDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_DeleteContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-DeleteContainerGroupDefinition-request-Name"></a>
The unique identifier for the container group definition to delete. You can use either the `Name` or `ARN` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: Yes

 ** [VersionCountToRetain](#API_DeleteContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-DeleteContainerGroupDefinition-request-VersionCountToRetain"></a>
The number of most recent versions to keep while deleting all older versions.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [VersionNumber](#API_DeleteContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-DeleteContainerGroupDefinition-request-VersionNumber"></a>
The specific version to delete.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Elements
<a name="API_DeleteContainerGroupDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteContainerGroupDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_DeleteContainerGroupDefinition_Examples"></a>

### Delete a container group definition version
<a name="API_DeleteContainerGroupDefinition_Example_1"></a>

This example deletes the 8th version of a container group definition. It assumes we're working in the same AWS Region as the container group we want to delete. To delete a container group definition in a different region, we could make the request using the definition's ARN value or we could specify the other region.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DeleteContainerGroupDefinition_Example_1_Request"></a>

```
{
  "Name": "MyAdventureGameContainerGroup",
  "Version": 8
}
```

#### Sample Response
<a name="API_DeleteContainerGroupDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Date: Thu, 14 Apr 2024 00:48:07 GMT
```

## See Also
<a name="API_DeleteContainerGroupDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteContainerGroupDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteContainerGroupDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
