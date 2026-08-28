---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetManagedView.html
---

# GetManagedView
<a name="API_GetManagedView"></a>

Retrieves details of the specified [AWS-managed view](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html).

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:GetManagedViews`

   **Resource**: The ARN of the specified view.

## Request Syntax
<a name="API_GetManagedView_RequestSyntax"></a>

```
POST /GetManagedView HTTP/1.1
Content-type: application/json

{
   "ManagedViewArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetManagedView_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetManagedView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ManagedViewArn](#API_GetManagedView_RequestSyntax) **   <a name="resourceexplorer-GetManagedView-request-ManagedViewArn"></a>
The Amazon resource name (ARN) of the managed view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_GetManagedView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ManagedView": {
      "Filters": {
         "FilterString": "string"
      },
      "IncludedProperties": [
         {
            "Name": "string"
         }
      ],
      "LastUpdatedAt": "string",
      "ManagedViewArn": "string",
      "ManagedViewName": "string",
      "Owner": "string",
      "ResourcePolicy": "string",
      "Scope": "string",
      "TrustedService": "string",
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_GetManagedView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedView](#API_GetManagedView_ResponseSyntax) **   <a name="resourceexplorer-GetManagedView-response-ManagedView"></a>
Details about the specified managed view.
Type: [ManagedView](API_ManagedView.md) object

## Errors
<a name="API_GetManagedView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** UnauthorizedException **
The principal making the request isn't permitted to perform the operation.
HTTP Status Code: 401

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_GetManagedView_Examples"></a>

### Example
<a name="API_GetManagedView_Example_1"></a>

The following example shows the call response with details about the managed view.

#### Sample Request
<a name="API_GetManagedView_Example_1_Request"></a>

```
POST /GetManagedView HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    // required field
    "ManagedViewArn": "arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ExampleManagedViewName/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_GetManagedView_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
  "ManagedView": {
    "ManagedViewArn": "arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ExampleManagedViewName/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "ManagedViewName": "ExampleManagedViewName",
    "TrustedService": "servicea.amazonaws.com",
    "LastUpdatedAt": "2024-01-01T01:01:01.100000+00:00",
    "Owner": "111111111111",
    "Scope": "arn:aws:iam::111111111111:root",
    "Filters": {
      "FilterString": ""
    },
    "IncludedProperties": [
      {
        "Name": "tags"
      }
    ],
    "ResourcePolicy": "resource_policy_string",
    "Version": "1"
  }
}
```

## See Also
<a name="API_GetManagedView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetManagedView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetManagedView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
