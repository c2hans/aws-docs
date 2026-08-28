---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_PutGroupingConfiguration.html
---

# PutGroupingConfiguration
<a name="API_PutGroupingConfiguration"></a>

Creates or updates the grouping configuration for this account. This operation allows you to define custom grouping attributes that determine how services are logically grouped based on telemetry attributes, AWS tags, or predefined mappings. These grouping attributes can then be used to organize and filter services in the Application Signals console and APIs.

## Request Syntax
<a name="API_PutGroupingConfiguration_RequestSyntax"></a>

```
PUT /grouping-configuration HTTP/1.1
Content-type: application/json

{
   "GroupingAttributeDefinitions": [
      {
         "DefaultGroupingValue": "{{string}}",
         "GroupingName": "{{string}}",
         "GroupingSourceKeys": [ "{{string}}" ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutGroupingConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutGroupingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GroupingAttributeDefinitions](#API_PutGroupingConfiguration_RequestSyntax) **   <a name="applicationsignals-PutGroupingConfiguration-request-GroupingAttributeDefinitions"></a>
An array of grouping attribute definitions that specify how services should be grouped. Each definition includes a friendly name, source keys to derive the grouping value from, and an optional default value.
Type: Array of [GroupingAttributeDefinition](API_GroupingAttributeDefinition.md) objects
Required: Yes

## Response Syntax
<a name="API_PutGroupingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GroupingConfiguration": {
      "GroupingAttributeDefinitions": [
         {
            "DefaultGroupingValue": "string",
            "GroupingName": "string",
            "GroupingSourceKeys": [ "string" ]
         }
      ],
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_PutGroupingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupingConfiguration](#API_PutGroupingConfiguration_ResponseSyntax) **   <a name="applicationsignals-PutGroupingConfiguration-response-GroupingConfiguration"></a>
A structure containing the updated grouping configuration, including all grouping attribute definitions and the timestamp when it was last updated.
Type: [GroupingConfiguration](API_GroupingConfiguration.md) object

## Errors
<a name="API_PutGroupingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_PutGroupingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/PutGroupingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/PutGroupingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
