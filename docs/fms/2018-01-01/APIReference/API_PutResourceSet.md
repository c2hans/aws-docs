---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutResourceSet.html
---

# PutResourceSet
<a name="API_PutResourceSet"></a>

Creates the resource set.

An AWS Firewall Manager resource set defines the resources to import into an Firewall Manager policy from another AWS service.

## Request Syntax
<a name="API_PutResourceSet_RequestSyntax"></a>

```
{
   "ResourceSet": {
      "Description": "{{string}}",
      "Id": "{{string}}",
      "LastUpdateTime": {{number}},
      "Name": "{{string}}",
      "ResourceSetStatus": "{{string}}",
      "ResourceTypeList": [ "{{string}}" ],
      "UpdateToken": "{{string}}"
   },
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutResourceSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceSet](#API_PutResourceSet_RequestSyntax) **   <a name="fms-PutResourceSet-request-ResourceSet"></a>
Details about the resource set to be created or updated.>
Type: [ResourceSet](API_ResourceSet.md) object
Required: Yes

 ** [TagList](#API_PutResourceSet_RequestSyntax) **   <a name="fms-PutResourceSet-request-TagList"></a>
Retrieves the tags associated with the specified resource set. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_PutResourceSet_ResponseSyntax"></a>

```
{
   "ResourceSet": {
      "Description": "string",
      "Id": "string",
      "LastUpdateTime": number,
      "Name": "string",
      "ResourceSetStatus": "string",
      "ResourceTypeList": [ "string" ],
      "UpdateToken": "string"
   },
   "ResourceSetArn": "string"
}
```

## Response Elements
<a name="API_PutResourceSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceSet](#API_PutResourceSet_ResponseSyntax) **   <a name="fms-PutResourceSet-response-ResourceSet"></a>
Details about the resource set.
Type: [ResourceSet](API_ResourceSet.md) object

 ** [ResourceSetArn](#API_PutResourceSet_ResponseSyntax) **   <a name="fms-PutResourceSet-response-ResourceSetArn"></a>
The Amazon Resource Name (ARN) of the resource set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_PutResourceSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeds a resource limit, for example, the maximum number of `policy` objects that you can create for an AWS account. For more information, see [Firewall Manager Limits](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

## See Also
<a name="API_PutResourceSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/PutResourceSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PutResourceSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
