---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExtensionAssociations.html
---

# ListExtensionAssociations
<a name="API_ListExtensionAssociations"></a>

Lists all AWS AppConfig extension associations in the account. For more information about extensions and associations, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the * AWS AppConfig User Guide*.

## Request Syntax
<a name="API_ListExtensionAssociations_RequestSyntax"></a>

```
GET /extensionassociations?extension_identifier={{ExtensionIdentifier}}&extension_version_number={{ExtensionVersionNumber}}&max_results={{MaxResults}}&next_token={{NextToken}}&resource_identifier={{ResourceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExtensionAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExtensionIdentifier](#API_ListExtensionAssociations_RequestSyntax) **   <a name="appconfig-ListExtensionAssociations-request-uri-ExtensionIdentifier"></a>
The name, the ID, or the Amazon Resource Name (ARN) of the extension.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [ExtensionVersionNumber](#API_ListExtensionAssociations_RequestSyntax) **   <a name="appconfig-ListExtensionAssociations-request-uri-ExtensionVersionNumber"></a>
The version number for the extension defined in the association.

 ** [MaxResults](#API_ListExtensionAssociations_RequestSyntax) **   <a name="appconfig-ListExtensionAssociations-request-uri-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListExtensionAssociations_RequestSyntax) **   <a name="appconfig-ListExtensionAssociations-request-uri-NextToken"></a>
A token to start the list. Use this token to get the next set of results or pass null to get the first set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [ResourceIdentifier](#API_ListExtensionAssociations_RequestSyntax) **   <a name="appconfig-ListExtensionAssociations-request-uri-ResourceIdentifier"></a>
The ARN of an application, configuration profile, or environment.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

## Request Body
<a name="API_ListExtensionAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExtensionAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ExtensionArn": "string",
         "Id": "string",
         "ResourceArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExtensionAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListExtensionAssociations_ResponseSyntax) **   <a name="appconfig-ListExtensionAssociations-response-Items"></a>
The list of extension associations. Each item represents an extension association to an application, environment, or configuration profile.
Type: Array of [ExtensionAssociationSummary](API_ExtensionAssociationSummary.md) objects

 ** [NextToken](#API_ListExtensionAssociations_ResponseSyntax) **   <a name="appconfig-ListExtensionAssociations-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListExtensionAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

## Examples
<a name="API_ListExtensionAssociations_Examples"></a>

### Example
<a name="API_ListExtensionAssociations_Example_1"></a>

This example illustrates one usage of ListExtensionAssociations.

#### Sample Request
<a name="API_ListExtensionAssociations_Example_1_Request"></a>

```
GET /extensionassociations HTTP/1.1
Host: appconfig.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.7.19 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/appconfig.list-extension-associations
X-Amz-Date: 20220803T215900Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220803/us-west-2/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListExtensionAssociations_Example_1_Response"></a>

```
{
	"Items": [{
		"ExtensionArn": "arn:aws:appconfig:us-west-2:111122223333:extension/6czExample/1",
		"Id": "rnekru4",
		"ResourceArn": "arn:aws:appconfig:us-west-2:111122223333:application/xlmtnms"
	}],
	"NextToken": null
}
```

## See Also
<a name="API_ListExtensionAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/ListExtensionAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ListExtensionAssociations)
